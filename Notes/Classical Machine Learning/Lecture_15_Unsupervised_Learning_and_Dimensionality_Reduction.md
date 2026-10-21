# Lecture 15: Unsupervised Learning, Clustering & Dimensionality Reduction
## Student Notes — SST Classical Machine Learning

---

## 🎯 Learning Objectives

By the end of this lecture, you should be able to:
- Formulate the **Unsupervised Learning Paradigm**, contrasting exploratory latent structure discovery against supervised inductive loss minimization.
- Dissect **K-Means Clustering**:
  - Derive the objective function (Sum of Squared Errors / Inertia: $J(\mathbf{C}, \boldsymbol{\mu})$).
  - Prove convergence of **Lloyd's Algorithm** via coordinate descent on assignment and centroid steps.
  - Implement **K-Means++ initialization** using $D(\mathbf{x})^2$ sampling to achieve $\mathcal{O}(\log k)$ approximation bounds.
  - Determine optimal cluster count $K$ using the **Elbow Method** and **Silhouette Analysis** ($s(i) \in [-1, 1]$).
- Formulate **Hierarchical Agglomerative Clustering (HAC)**:
  - Differentiate linkage criteria: **Single**, **Complete**, **Average**, and **Ward's Minimum Variance**.
  - Interpret hierarchical **Dendrograms** and cophenetic correlation cuts.
- Master **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**:
  - Formulate $\epsilon$-neighborhoods, Core points, Border points, and Noise points.
  - Understand density-reachability and density-connectivity to cluster arbitrary non-convex geometries without specifying $K$.
- Explain the **Curse of Dimensionality** and its impact on distance metrics ($L_2$ norm concentration).
- Derive **Principal Component Analysis (PCA)**:
  - Formulate PCA via **Maximum Variance Projection** and **Minimum Reconstruction Error**.
  - Solve the constrained optimization problem via **Lagrangian multipliers** and the **Covariance Matrix Eigendecomposition** ($\mathbf{\Sigma}\mathbf{v} = \lambda \mathbf{v}$).
  - Connect PCA to **Singular Value Decomposition (SVD)** of centered data: $\mathbf{X}_c = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$.
  - Interpret **Explained Variance Ratio (EVR)** and Scree plots for rank selection.
- Implement vectorized K-Means and PCA completely from scratch in pure NumPy.

---

## 1. The Unsupervised Learning Paradigm

In supervised learning, algorithms optimize a parameter vector $\mathbf{w}$ to minimize empirical risk $\frac{1}{n} \sum_{i=1}^n \mathcal{L}(f(\mathbf{x}_i; \mathbf{w}), y_i)$ guided by ground-truth supervisory labels $y_i \in \mathcal{Y}$.

In **Unsupervised Learning**, we are given only an unlabelled feature matrix $\mathbf{X} \in \mathbb{R}^{n \times d}$:
$$\mathcal{D} = \{\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_n\}, \quad \mathbf{x}_i \in \mathbb{R}^d$$

There is no target signal $y$. The objective is to discover **latent structure, low-dimensional manifolds, probability densities, or natural clusterings** hidden within $\mathbf{X}$.

```
  Supervised Classification:                    Unsupervised Clustering:
  Known labels define boundaries                Natural density groupings discovered
  
        x₂ ▲                                          x₂ ▲
           │    o   o    /    +   +                      │     o o o           * * *
           │   o   o    /    +   +                       │    o o o o         * * * *
           │  o   o    /    +   +                        │     o o o           * * *
           │          /                                  │
           │         / Decision                          │           Δ Δ Δ
           │        /  Boundary                          │          Δ Δ Δ Δ
           └───────────────────────►                     └───────────────────────►
                                   x₁                                            x₁
```

### Major Families of Unsupervised Learning:
1. **Partitioning Methods (K-Means, K-Medoids)**: Hard disjoint partition of space into $K$ Voronoi regions.
2. **Hierarchical Methods (Agglomerative, Divisive)**: Nested tree structures of multiscale clusters.
3. **Density-Based Methods (DBSCAN, OPTICS, HDBSCAN)**: Discovery of arbitrary contiguous high-density regions separated by low-density noise.
4. **Subspace & Manifold Learning (PCA, SVD, t-SNE, UMAP)**: Projecting high-dimensional observations onto low-dimensional informative subspaces.

---

## 2. Partitioning Clustering: K-Means

K-Means partitions $n$ observations into $K$ disjoint clusters $\mathcal{C} = \{C_1, C_2, \dots, C_K\}$ such that each point belongs to the cluster with the nearest centroid $\boldsymbol{\mu}_k \in \mathbb{R}^d$.

```
                        Voronoi Partitioning (K=3)
                 x₂ ▲
                    │         \      *   * (C₂)
                    │   (C₁)   \   *   μ₂ *
                    │  o   o    \    *   *
                    │ o  μ₁  o   \---------
                    │  o   o     /   Δ   Δ
                    │           /  Δ   μ₃  Δ (C₃)
                    └──────────/─────────────► x₁
```

### 2.1 The Objective Function (Inertia / WCSS)
K-Means minimizes the **Within-Cluster Sum of Squares (WCSS)**, also termed **Inertia**:

$$J(\mathbf{C}, \boldsymbol{\mu}) = \sum_{k=1}^K \sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2$$

Equivalently, using binary indicator variables $r_{ik} \in \{0, 1\}$ where $r_{ik} = 1 \iff \mathbf{x}_i \in C_k$:

$$J(\mathbf{R}, \boldsymbol{\mu}) = \sum_{i=1}^n \sum_{k=1}^K r_{ik} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2 \quad \text{s.t.} \quad \sum_{k=1}^K r_{ik} = 1 \quad \forall i$$

Finding the global minimum of $J$ is an **NP-hard** problem in general Euclidean space $\mathbb{R}^d$ even for $K=2$. Lloyd's algorithm provides a local greedy heuristic via alternating coordinate descent.

---

### 2.2 Lloyd's Algorithm (Expectation-Maximization Dynamics)

Lloyd's algorithm alternates between two steps until the cluster assignments no longer change:

#### Step 1: Cluster Assignment (Expectation / Coordinate step over $\mathbf{R}$)
Holding cluster centroids $\boldsymbol{\mu}_k$ fixed, minimize $J$ with respect to assignments $r_{ik}$:
$$r_{ik}^{(t)} = \begin{cases} 1 & \text{if } k = \arg\min_j \|\mathbf{x}_i - \boldsymbol{\mu}_j^{(t)}\|_2^2 \\ 0 & \text{otherwise} \end{cases}$$
Each point is assigned to its geometrically closest centroid.

#### Step 2: Centroid Update (Maximization / Coordinate step over $\boldsymbol{\mu}$)
Holding assignments $r_{ik}$ fixed, minimize $J$ with respect to $\boldsymbol{\mu}_k$. We compute the gradient and set it to zero:
$$\frac{\partial J}{\partial \boldsymbol{\mu}_k} = -2 \sum_{i=1}^n r_{ik} (\mathbf{x}_i - \boldsymbol{\mu}_k) = \mathbf{0}$$
$$\sum_{i=1}^n r_{ik} \boldsymbol{\mu}_k = \sum_{i=1}^n r_{ik} \mathbf{x}_i \implies \boldsymbol{\mu}_k^{(t+1)} = \frac{\sum_{i=1}^n r_{ik} \mathbf{x}_i}{\sum_{i=1}^n r_{ik}} = \frac{1}{|C_k|} \sum_{\mathbf{x}_i \in C_k} \mathbf{x}_i$$
The optimal centroid is the **arithmetic mean (center of mass)** of all data points currently assigned to cluster $k$.

#### Convergence Guarantee:
Because each step monotonically decreases or maintains the non-negative objective $J$ ($J^{(t+1)} \le J^{(t)}$), and there exist only a finite number of possible partitions ($K^n$), **Lloyd's algorithm is guaranteed to converge to a local minimum** in a finite number of iterations. However, it does not guarantee reaching the global minimum.

---

### 2.3 The Initialization Problem & K-Means++

Standard K-Means randomly selects $K$ initial points uniformly from $\mathcal{D}$. If two centroids initialize near the same physical cluster, Lloyd's algorithm easily traps in severe sub-optimal local minima.

**K-Means++** solves this by probabilistically spreading out the initial centroids:

```
 Algorithm: K-Means++ Initialization
 ─────────────────────────────────────────────────────────────────────────────
 1. Choose the first centroid μ₁ uniformly at random from dataset D.
 2. For each remaining centroid k = 2, 3, ..., K:
    a. For each data point xᵢ, compute D(xᵢ) = min_{j < k} ||xᵢ - μⱼ||₂
       (distance to the closest already chosen centroid).
    b. Select the next centroid μₖ from D with probability proportional to D(xᵢ)²:
                          P(xᵢ) = D(xᵢ)² / ∑_{j=1}^n D(xⱼ)²
 3. Run standard Lloyd's algorithm using these K initial seeds.
 ─────────────────────────────────────────────────────────────────────────────
```

> **Theoretical Guarantee (Arthur & Vassilvitskii, 2007)**:  
> K-Means++ achieves an expected approximation ratio:
> $$\mathbb{E}[J_{\text{kmeans++}}] \le 8(\ln K + 2) \cdot J_{\text{optimal}}$$
> It is $\mathcal{O}(\log K)$-competitive with the globally optimal clustering, dramatically reducing convergence time and inertia.

---

### 2.4 Determining the Optimal Number of Clusters $K$

Because $J$ strictly decreases as $K$ increases (reaching $J = 0$ when $K = n$), we cannot simply minimize $J$ to pick $K$.

#### 1. The Elbow Method
Plot Inertia $J(K)$ against candidate values of $K \in \{1, 2, \dots, 10\}$.
Identify the inflection point ("elbow") where the marginal rate of variance explained drops sharply:

```
  Inertia J ▲
            │  ●
            │   \
            │    \
            │     ●
            │      \
            │       \
            │        ● ◄─── "Elbow" Point (Optimal K=3)
            │         \________●_______●_______●
            └────────────────────────────────────► Number of Clusters K
                 1    2        3       4       5
```

#### 2. The Silhouette Analysis
The **Silhouette Coefficient** evaluates both **cohesion** (compactness within the same cluster) and **separation** (isolation from neighboring clusters).

For each sample $\mathbf{x}_i \in C_I$:
1. **Intra-cluster distance $a(i)$ (Cohesion)**: Mean distance from $\mathbf{x}_i$ to all other points in its own cluster $C_I$:
   $$a(i) = \frac{1}{|C_I| - 1} \sum_{\mathbf{x}_j \in C_I, j \ne i} \|\mathbf{x}_i - \mathbf{x}_j\|_2$$
2. **Nearest-cluster distance $b(i)$ (Separation)**: Mean distance from $\mathbf{x}_i$ to points in the closest neighboring cluster $C_J \ne C_I$:
   $$b(i) = \min_{J \ne I} \frac{1}{|C_J|} \sum_{\mathbf{x}_j \in C_J} \|\mathbf{x}_i - \mathbf{x}_j\|_2$$
3. **Silhouette Coefficient $s(i)$**:
   $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, +1]$$

| Silhouette Score $s(i)$ | Geometric Interpretation |
| :--- | :--- |
| **$s(i) \approx +1$** | Point is deeply embedded within its own cluster and far from neighboring clusters ($a(i) \ll b(i)$). Optimal assignment. |
| **$s(i) \approx 0$** | Point lies right on the decision boundary between two clusters ($a(i) \approx b(i)$). Ambiguous assignment. |
| **$s(i) \approx -1$** | Point is closer to a neighboring cluster than to its assigned cluster ($b(i) \ll a(i)$). Misclustered sample. |

The **Global Silhouette Score** is the mean across all $n$ samples: $\bar{s} = \frac{1}{n}\sum_{i=1}^n s(i)$. The optimal $K$ is chosen to maximize $\bar{s}$.

---

### 2.5 Assumptions and Limitations of K-Means

| Assumption | Manifestation / Failure Case | Better Alternative |
| :--- | :--- | :--- |
| **Spherical Clusters** | Fails on elongated, ring-shaped, or moon-shaped manifolds | DBSCAN, Spectral Clustering |
| **Equal Variance** | Assigns points from spread-out clusters to denser neighboring clusters | Gaussian Mixture Models (GMM) |
| **Equal Cluster Sizes** | Distorts boundaries when one cluster has $100\times$ more points than another | GMM with unconstrained priors |
| **Euclidean Metric Sensitivity** | Highly vulnerable to unstandardized feature scales and outliers | Standard Scaler, K-Medoids / PAM |

---

## 3. Hierarchical Agglomerative Clustering (HAC)

Hierarchical clustering constructs a nested tree of partitions without requiring a predefined cluster count $K$.

```
  Dendrogram Construction:
  Height (Distance)
     ▲
     │              ┌───────────────┐
  1.8│              │               │
     │      ┌───────┴───────┐       │
  1.0│      │               │       │
     │   ┌──┴──┐         ┌──┴──┐    │       Cut at h=0.8 yields 3 clusters!
  0.5│───│─────│─────────│─────│────│───────◄ [Cluster Cut Threshold]
     │   │     │         │     │    │
  0.0┴───┴─────┴─────────┴─────┴────┴────►
        x₁    x₂        x₃    x₄   x₅
```

### 3.1 Agglomerative (Bottom-Up) Algorithm
1. Start with $n$ individual clusters: $\mathcal{C} = \{\{\mathbf{x}_1\}, \{\mathbf{x}_2\}, \dots, \{\mathbf{x}_n\}\}$.
2. Compute the pairwise distance matrix $D \in \mathbb{R}^{n \times n}$.
3. At each step, identify the two clusters $A, B$ with the minimum linkage distance $d(A, B)$.
4. Merge $A$ and $B$ into a composite cluster $A \cup B$.
5. Update the distance matrix.
6. Repeat until all observations merge into a single root cluster of size $n$.

---

### 3.2 Linkage Criteria

The distance between two clusters $A$ and $B$ depends on the chosen **Linkage Metric**:

```
 Single Linkage (Min)         Complete Linkage (Max)       Average Linkage (Mean)
     o   o───*   *                o───o       *───*             o   o  ╲ ╱  *   *
    o     o   *     *            o     o     *     *           o     o  ╳  *     *
     o   o     *   *              o   o       *   *             o   o  ╱ ╲  *   *
     d(A, B) = min                d(A, B) = max               d(A, B) = mean
```

#### 1. Single Linkage (Minimum Distance):
$$d_{\text{single}}(A, B) = \min_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$$
- **Property**: Can extract non-elliptical concentric rings and curves.
- **Pathology**: Extremely vulnerable to the **chaining effect**, where single stray noise points form bridges connecting distinct clusters.

#### 2. Complete Linkage (Maximum Distance):
$$d_{\text{complete}}(A, B) = \max_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$$
- **Property**: Favors compact, tightly bounded spherical clusters of approximately equal diameter.
- **Pathology**: Highly sensitive to peripheral outliers, which inflate maximum distances.

#### 3. Average Linkage (UPGMA):
$$d_{\text{avg}}(A, B) = \frac{1}{|A| |B|} \sum_{\mathbf{a} \in A} \sum_{\mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$$
- **Property**: Robust balance between single and complete linkage; less sensitive to outliers.

#### 4. Ward's Minimum Variance Linkage:
Merges the pair of clusters that minimizes the increase in total within-cluster sum of squares ($\Delta \text{WCSS}$):
$$\Delta J(A, B) = \frac{|A| |B|}{|A| + |B|} \|\boldsymbol{\mu}_A - \boldsymbol{\mu}_B\|_2^2$$
- **Property**: Most effective linkage for Euclidean data; produces balanced, cohesive clusters matching K-Means dynamics.

---

## 4. Density-Based Clustering: DBSCAN

DBSCAN (**Density-Based Spatial Clustering of Applications with Noise**) groups points based on spatial density connectivity rather than distance to centroids.

### 4.1 Hyperparameters:
1. **$\epsilon$ (Epsilon / Radius)**: The maximum Euclidean distance defining a local neighborhood.
2. **$\text{MinPts}$**: The minimum number of points required within the $\epsilon$-neighborhood to form a dense region.

---

### 4.2 Point Classification Taxonomy

For each point $\mathbf{p} \in \mathcal{D}$, evaluate its $\epsilon$-neighborhood:
$$N_\epsilon(\mathbf{p}) = \{\mathbf{q} \in \mathcal{D} \mid \|\mathbf{p} - \mathbf{q}\|_2 \le \epsilon\}$$

```
                   DBSCAN Point Classification (MinPts = 4)

             Core Point (p)            Border Point (b)          Noise Point (n)
            |N_ε(p)| = 5 ≥ 4           |N_ε(b)| = 2 < 4          |N_ε(n)| = 1 < 4
                                       (Inside ε of Core p)      (Isolated)
                   ●                         ●
                 /   \                         \
                ●── p ──●                        b ─── p                n
                 \   /                                 │
                   ●                                   ●
```

1. **Core Point**: Point $\mathbf{p}$ is a Core point if $|N_\epsilon(\mathbf{p})| \ge \text{MinPts}$.
2. **Border Point**: Point $\mathbf{b}$ has $|N_\epsilon(\mathbf{b})| < \text{MinPts}$, but lies within the $\epsilon$-neighborhood of a Core point $\mathbf{p}$ ($\mathbf{b} \in N_\epsilon(\mathbf{p})$).
3. **Noise / Outlier Point**: Point $\mathbf{n}$ is neither a Core point nor a Border point ($|N_\epsilon(\mathbf{n})| < \text{MinPts}$ and $\mathbf{n} \notin N_\epsilon(\mathbf{p})$ for all Core points $\mathbf{p}$). Labeled as $-1$.

---

### 4.3 Connectivity Definitions
- **Directly Density-Reachable**: $\mathbf{q}$ is directly density-reachable from $\mathbf{p}$ if $\mathbf{p}$ is a Core point and $\mathbf{q} \in N_\epsilon(\mathbf{p})$.
- **Density-Reachable**: $\mathbf{q}$ is density-reachable from $\mathbf{p}$ if there exists a chain of points $\mathbf{p}_1, \mathbf{p}_2, \dots, \mathbf{p}_k$ such that $\mathbf{p}_1 = \mathbf{p}$, $\mathbf{p}_k = \mathbf{q}$, and $\mathbf{p}_{i+1}$ is directly density-reachable from $\mathbf{p}_i$.
- **Density-Connected**: $\mathbf{p}$ and $\mathbf{q}$ are density-connected if there exists an intermediate point $\mathbf{o}$ such that both $\mathbf{p}$ and $\mathbf{q}$ are density-reachable from $\mathbf{o}$.

A **DBSCAN Cluster** is defined as a maximal set of density-connected points.

---

### 4.4 DBSCAN vs K-Means Comparison

| Dimension | K-Means | DBSCAN |
| :--- | :--- | :--- |
| **Number of Clusters $K$** | Must be predefined in advance | Discovered automatically from density topology |
| **Cluster Geometry** | Restricted to convex / spherical Voronoi partitions | Arbitrary complex non-convex geometries (rings, spirals) |
| **Noise & Outliers** | Forced into the nearest centroid, distorting clusters | Explicitly identified and isolated as Noise (label $-1$) |
| **Density Variations** | Handles varying densities gracefully | Struggles when clusters exhibit substantially different local densities |
| **Computational Complexity** | $\mathcal{O}(n \cdot K \cdot d \cdot \text{iters})$ — highly scalable | $\mathcal{O}(n^2)$ naive, $\mathcal{O}(n \log n)$ with $k$-d trees / ball trees |

---

## 5. The Curse of Dimensionality & Dimensionality Reduction

As the feature dimension $d$ grows:
1. **Exponential Volume Expansion**: The volume of the feature space expands exponentially ($\mathbb{R}^d \propto V^d$). Data becomes extremely sparse, requiring exponentially more samples ($n \propto \mathcal{O}(e^d)$) to maintain sample density.
2. **Distance Concentration Phenomenon**: The relative contrast between the distance to the nearest neighbor and the distance to the furthest neighbor vanishes:
   $$\lim_{d \to \infty} \frac{d_{\max} - d_{\min}}{d_{\min}} \to 0$$
   Every point becomes equidistant from every other point, rendering distance-based algorithms ($L_2$ norm in K-Means, KNN, DBSCAN) ineffective.
3. **Multicollinearity & Overfitting**: Redundant correlated features inflate model variance and computational storage.

**Dimensionality Reduction** resolves this by mapping $\mathbf{X} \in \mathbb{R}^{n \times d} \to \mathbf{Z} \in \mathbb{R}^{n \times k}$ where $k \ll d$ while preserving maximal variance and intrinsic information.

---

## 6. Principal Component Analysis (PCA)

PCA is the canonical linear dimensionality reduction technique. It performs an orthogonal linear transformation to project correlated features into a set of linearly uncorrelated variables called **Principal Components (PCs)**.

```
                         PCA Geometric Projection
                 x₂ ▲               PC 1 (Direction of Max Variance v₁)
                    │             ╱
                    │           ●╱
                    │         ●╱  ●
                    │       ●╱ ●
                    │     ●╱●
                    │   ●╱─────────────── PC 2 (Orthogonal v₂)
                    │  ╱●
                    └────────────────────────► x₁
```

### 6.1 Derivation 1: Maximizing Projection Variance

Let $\mathbf{X}_c \in \mathbb{R}^{n \times d}$ be the zero-centered data matrix where each column mean is 0:
$$\bar{\mathbf{x}} = \frac{1}{n}\sum_{i=1}^n \mathbf{x}_i, \quad \mathbf{X}_c = \mathbf{X} - \mathbf{1}\bar{\mathbf{x}}^T$$

The sample covariance matrix $\mathbf{\Sigma} \in \mathbb{R}^{d \times d}$ is:
$$\mathbf{\Sigma} = \frac{1}{n-1}\mathbf{X}_c^T \mathbf{X}_c$$

We seek a unit projection vector $\mathbf{v}_1 \in \mathbb{R}^d$ ($\|\mathbf{v}_1\|_2 = 1 \implies \mathbf{v}_1^T \mathbf{v}_1 = 1$) such that the variance of the projected data $\mathbf{z}_1 = \mathbf{X}_c \mathbf{v}_1$ is maximized:

$$\text{Var}(\mathbf{z}_1) = \frac{1}{n-1} \mathbf{z}_1^T \mathbf{z}_1 = \frac{1}{n-1} (\mathbf{X}_c \mathbf{v}_1)^T (\mathbf{X}_c \mathbf{v}_1) = \mathbf{v}_1^T \left(\frac{1}{n-1}\mathbf{X}_c^T \mathbf{X}_c\right) \mathbf{v}_1 = \mathbf{v}_1^T \mathbf{\Sigma} \mathbf{v}_1$$

#### Formulating the Constrained Optimization Problem:
$$\max_{\mathbf{v}_1} \mathbf{v}_1^T \mathbf{\Sigma} \mathbf{v}_1 \quad \text{subject to} \quad \mathbf{v}_1^T \mathbf{v}_1 = 1$$

Construct the Lagrangian:
$$\mathcal{L}(\mathbf{v}_1, \lambda_1) = \mathbf{v}_1^T \mathbf{\Sigma} \mathbf{v}_1 - \lambda_1 (\mathbf{v}_1^T \mathbf{v}_1 - 1)$$

Take the derivative with respect to $\mathbf{v}_1$ and set to zero:
$$\nabla_{\mathbf{v}_1}\mathcal{L} = 2\mathbf{\Sigma} \mathbf{v}_1 - 2\lambda_1 \mathbf{v}_1 = \mathbf{0}$$
$$\mathbf{\Sigma} \mathbf{v}_1 = \lambda_1 \mathbf{v}_1$$

> **Fundamental Result**:  
> The optimal projection vector $\mathbf{v}_1$ is an **eigenvector** of the sample covariance matrix $\mathbf{\Sigma}$, and the projection variance equals the corresponding **eigenvalue** $\lambda_1$:
> $$\text{Var}(\mathbf{z}_1) = \mathbf{v}_1^T \mathbf{\Sigma} \mathbf{v}_1 = \mathbf{v}_1^T (\lambda_1 \mathbf{v}_1) = \lambda_1 (\mathbf{v}_1^T \mathbf{v}_1) = \lambda_1$$
> 
> To maximize variance, $\mathbf{v}_1$ must be the eigenvector corresponding to the **largest eigenvalue** $\lambda_1$.  
> Subsequent orthogonal components $\mathbf{v}_2, \dots, \mathbf{v}_k$ correspond to the 2nd, 3rd, ..., $k$-th largest eigenvalues of $\mathbf{\Sigma}$.

---

### 6.2 Connection to Singular Value Decomposition (SVD)

In practice, forming the covariance matrix $\mathbf{\Sigma} = \frac{1}{n-1}\mathbf{X}_c^T \mathbf{X}_c$ incurs numerical loss of precision and $\mathcal{O}(n d^2)$ computational overhead. Production implementations (like scikit-learn) compute PCA directly via **Singular Value Decomposition (SVD)** of centered $\mathbf{X}_c$:

$$\mathbf{X}_c = \mathbf{U} \mathbf{S} \mathbf{V}^T$$
Where:
- $\mathbf{U} \in \mathbb{R}^{n \times n}$ is an orthogonal matrix of left-singular vectors (eigenvectors of $\mathbf{X}_c \mathbf{X}_c^T$).
- $\mathbf{S} \in \mathbb{R}^{n \times d}$ is a diagonal matrix of non-negative singular values $s_1 \ge s_2 \ge \dots \ge s_d \ge 0$.
- $\mathbf{V} \in \mathbb{R}^{d \times d}$ is an orthogonal matrix of right-singular vectors (eigenvectors of $\mathbf{X}_c^T \mathbf{X}_c$).

Notice:
$$\mathbf{\Sigma} = \frac{1}{n-1}\mathbf{X}_c^T \mathbf{X}_c = \frac{1}{n-1}(\mathbf{U} \mathbf{S} \mathbf{V}^T)^T (\mathbf{U} \mathbf{S} \mathbf{V}^T) = \frac{1}{n-1}\mathbf{V} \mathbf{S}^T \mathbf{U}^T \mathbf{U} \mathbf{S} \mathbf{V}^T = \mathbf{V} \left(\frac{\mathbf{S}^2}{n-1}\right) \mathbf{V}^T$$

Therefore:
1. The **Principal Directions** $\mathbf{v}_j$ are exactly the columns of right-singular matrix $\mathbf{V}$.
2. The **Eigenvalues** $\lambda_j$ relate directly to the singular values:
   $$\lambda_j = \frac{s_j^2}{n-1}$$
3. The **Projected Subspace Coordinates** (Principal Component scores $\mathbf{Z}$) are computed directly as:
   $$\mathbf{Z} = \mathbf{X}_c \mathbf{V}_k = \mathbf{U}_k \mathbf{S}_k$$

---

### 6.3 Explained Variance Ratio & Scree Plot

The proportion of total dataset variance explained by the $j$-th principal component is:

$$\text{EVR}_j = \frac{\lambda_j}{\sum_{m=1}^d \lambda_m} = \frac{s_j^2}{\sum_{m=1}^d s_m^2}$$

The **Cumulative Explained Variance** for $k$ components is:
$$\text{Cumulative EVR}(k) = \frac{\sum_{j=1}^k \lambda_j}{\sum_{m=1}^d \lambda_m}$$

```
  Cumulative Variance ▲
               100% ┼ - - - - - - - - - - - - - - - - - - ●────● 98%
                    │                               ●────┘
                90% ┼ - - - - - - - - - - - - - ●──┘ (Threshold: 90%)
                    │                      ●───┘
                60% ┼                 ●───┘
                    │            ●───┘
                30% ┼       ●───┘
                    │  ●───┘
                 0% ┴──┴─────┴─────┴─────┴─────┴─────┴─────┴───► Number of PCs
                       1     2     3     4     5     6     7
```
Standard engineering heuristics select the minimal $k$ that retains $90\%$ to $95\%$ of total cumulative variance.

---

## 7. Complete Implementations from Scratch in Pure NumPy

### 7.1 Vectorized K-Means with K-Means++ Initialization

```python
import numpy as np

class ScratchKMeans:
    def __init__(self, k=3, max_iter=300, tol=1e-4, random_state=42):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        self.centroids = None
        self.inertia_ = None

    def _init_kmeans_plus_plus(self, X):
        """K-Means++ initialization algorithm."""
        np.random.seed(self.random_state)
        n_samples, n_features = X.shape
        
        # 1. Randomly pick first centroid
        centroids = [X[np.random.choice(n_samples)]]
        
        for _ in range(1, self.k):
            # Compute distance from each point to nearest existing centroid
            dists = np.min([np.sum((X - c) ** 2, axis=1) for c in centroids], axis=0)
            
            # Probability proportional to D(x)^2
            probs = dists / np.sum(dists)
            next_idx = np.random.choice(n_samples, p=probs)
            centroids.append(X[next_idx])
            
        return np.array(centroids)

    def fit(self, X):
        X = np.asarray(X, dtype=np.float64)
        n_samples = X.shape[0]
        
        # Initialize centroids via K-Means++
        self.centroids = self._init_kmeans_plus_plus(X)
        
        for iteration in range(self.max_iter):
            # E-step: Compute pairwise Euclidean distances (n_samples, k)
            # Using broadcast: (X[:, None, :] - centroids[None, :, :])^2
            dists = np.sum((X[:, np.newaxis, :] - self.centroids[np.newaxis, :, :]) ** 2, axis=2)
            labels = np.argmin(dists, axis=1)
            
            # M-step: Update centroids to arithmetic mean
            new_centroids = np.zeros_like(self.centroids)
            for j in range(self.k):
                cluster_pts = X[labels == j]
                if len(cluster_pts) > 0:
                    new_centroids[j] = np.mean(cluster_pts, axis=0)
                else:
                    # Handle empty cluster: reinitialize to random sample
                    new_centroids[j] = X[np.random.choice(n_samples)]
            
            # Check convergence
            shift = np.sum((new_centroids - self.centroids) ** 2)
            self.centroids = new_centroids
            if shift < self.tol:
                break
                
        # Final inertia computation
        final_dists = np.sum((X[:, np.newaxis, :] - self.centroids[np.newaxis, :, :]) ** 2, axis=2)
        self.inertia_ = np.sum(np.min(final_dists, axis=1))
        return self

    def predict(self, X):
        X = np.asarray(X, dtype=np.float64)
        dists = np.sum((X[:, np.newaxis, :] - self.centroids[np.newaxis, :, :]) ** 2, axis=2)
        return np.argmin(dists, axis=1)
```

---

### 7.2 Vectorized Principal Component Analysis (PCA) via SVD

```python
import numpy as np

class ScratchPCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.components_ = None          # V_k^T (n_components, d)
        self.explained_variance_ = None  # Eigenvalues lambda_j
        self.explained_variance_ratio_ = None
        self.mean_ = None

    def fit(self, X):
        X = np.asarray(X, dtype=np.float64)
        n_samples, n_features = X.shape
        
        # 1. Zero-center the feature matrix
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        
        # 2. Compute Singular Value Decomposition (SVD): X_c = U * S * Vt
        # U: (n, n), S: (min(n,d),), Vt: (d, d)
        U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
        
        # 3. Eigenvalues equal s_j^2 / (n - 1)
        eigenvalues = (S ** 2) / (n_samples - 1)
        total_variance = np.sum(eigenvalues)
        
        # 4. Store top k components (rows of Vt)
        self.components_ = Vt[:self.n_components]
        self.explained_variance_ = eigenvalues[:self.n_components]
        self.explained_variance_ratio_ = self.explained_variance_ / total_variance
        
        return self

    def transform(self, X):
        """Project centered data onto principal eigenvectors."""
        X_centered = X - self.mean_
        return np.dot(X_centered, self.components_.T)

    def inverse_transform(self, Z):
        """Reconstruct original space from reduced latent projection."""
        return np.dot(Z, self.components_) + self.mean_
```

---

## 8. Common Pitfalls & Practical Anti-Patterns

### 1. Failing to Standardize Before PCA or K-Means
- **Pathology**: PCA and K-Means both rely directly on variance and Euclidean $L_2$ distance. If feature $A$ has range $[0, 100000]$ (e.g., Annual Income) and feature $B$ has range $[1, 5]$ (e.g., Household Size), the variance of feature $A$ is $10^8\times$ larger. PCA will blindly align the 1st Principal Component almost completely along feature $A$, treating feature $B$ as noise.
- **Rule**: Always apply `StandardScaler` (zero mean, unit variance) prior to PCA and distance-based clustering.

### 2. Information Leakage via Unsupervised Preprocessing
- **Pathology**: Running PCA or `StandardScaler` across the entire dataset before executing `train_test_split`. The test set distribution contaminates the mean vector $\bar{\mathbf{x}}$, variance $\mathbf{s}$, and projection eigenvectors $\mathbf{V}$.
- **Rule**: Always fit PCA exclusively on `X_train` and transform `X_test` using the fitted transformation:
  ```python
  from sklearn.pipeline import Pipeline
  from sklearn.decomposition import PCA
  from sklearn.linear_model import LogisticRegression

  pipe = Pipeline([
      ('scaler', StandardScaler()),
      ('pca', PCA(n_components=0.95)),
      ('clf', LogisticRegression())
  ])
  pipe.fit(X_train, y_train)  # Strict containment!
  ```

### 3. Misinterpreting PCA as Feature Selection
- **Pathology**: Expecting PCA to identify "which 3 original features are best".
- **Reality**: PCA is **Feature Extraction**, not Feature Selection. Each principal component $\mathbf{z}_j$ is a linear combination of *all* $d$ original input features ($\mathbf{z}_j = v_{1j}x_1 + v_{2j}x_2 + \dots + v_{dj}x_d$). Original feature interpretability is lost unless inspecting eigenvector loadings.

### 4. Relying Exclusively on PCA for Manifold Visualization
- **Pathology**: Expecting PCA to untangle highly non-linear topological manifolds (e.g., concentric circles, Swiss roll).
- **Reality**: PCA is strictly linear. For complex non-linear high-dimensional manifold exploration, use **t-SNE** (t-Distributed Stochastic Neighbor Embedding) or **UMAP** (Uniform Manifold Approximation and Projection).

---

## 9. Self-Assessment Practice Problems

1. **Inertia Minimization Proof**:  
   Prove analytically that given a fixed cluster assignment $C_k$, the centroid $\boldsymbol{\mu}_k$ that minimizes the within-cluster sum of squares $\sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2$ is strictly the arithmetic mean $\boldsymbol{\mu}_k = \frac{1}{|C_k|}\sum_{\mathbf{x}_i \in C_k} \mathbf{x}_i$. What happens if the loss uses $L_1$ norm instead of squared $L_2$ norm? *(Hint: Medoid/Median).*
2. **K-Means++ Probability**:  
   Given 3 points on a line $x_1 = 0, x_2 = 3, x_3 = 10$. If $x_1$ is randomly chosen as the first centroid $\mu_1 = 0$, calculate the exact probability that $x_3$ is chosen as the second centroid under K-Means++.
3. **DBSCAN Density Paradox**:  
   Suppose you have two clusters: Cluster 1 has 1000 points packed within a unit sphere of radius 1, while Cluster 2 has 1000 points uniformly distributed within a sphere of radius 10. Why will any fixed choice of $(\epsilon, \text{MinPts})$ in DBSCAN fail to separate both clusters simultaneously? How does HDBSCAN resolve this?
4. **PCA Covariance vs Correlation**:  
   Under what mathematical condition will PCA on the raw covariance matrix $\mathbf{\Sigma}$ yield the exact same eigenvectors as PCA on the correlation matrix $\mathbf{R}$?
5. **Reconstruction Loss**:  
   If the eigenvalues of a $5$-dimensional dataset are $\lambda = [12.0, 5.0, 2.0, 0.8, 0.2]$, what is the exact percentage of total variance retained if we compress the data to $k = 2$ principal components? What is the mean squared reconstruction error?
