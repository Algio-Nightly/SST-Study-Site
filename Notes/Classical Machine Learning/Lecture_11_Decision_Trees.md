# Lecture 11: Decision Trees & Recursive Partitioning
## Student Notes — SST Classical Machine Learning

---

## 🎯 Learning Objectives

By the end of this lecture, you should be able to:
- Formulate Decision Trees as **non-parametric recursive binary space partitioners** that divide $\mathbb{R}^d$ into axis-aligned hyper-rectangles.
- Mathematically derive and compare the core impurity criteria: **Shannon Entropy & Information Gain** (ID3), **Gain Ratio** (C4.5), and **Gini Impurity** (CART).
- Implement efficient continuous feature splitting via candidate midpoint evaluation in $\mathcal{O}(d \cdot n \log n)$ time.
- Formulate **Regression Trees**, deriving variance reduction as the splitting criterion and proving that leaf predictions minimize squared error by computing the local conditional mean $\bar{y}_{R_m}$.
- Analyze the inductive bias and high-variance pathology of unconstrained decision trees (orthogonal decision boundaries, instability to small data perturbations).
- Implement regularization through **Pre-pruning** hyperparameters and derive **Minimal Cost-Complexity Post-pruning** using the complexity penalty $\alpha |T|$.
- Calculate **Feature Importance** via Mean Decrease in Impurity (MDI).
- Construct a production-grade Decision Tree from scratch in pure NumPy.

---

## 1. High-Level Philosophy: Space Partitioning

Unlike linear models that attempt to separate classes using a global $(d-1)$-dimensional hyperplane:

$$\mathbf{w}^T \mathbf{x} + b = 0$$

A **Decision Tree** is a non-parametric, hierarchical model that recursively partitions the feature space into a set of mutually exclusive, axis-aligned hyper-rectangles $R_1, R_2, \dots, R_M$. 

```
 Feature Space Partitioning:               Tree Topology:
       x₂ ▲                                        [ x₁ ≤ 5.0 ]
          │      R₁        │    R₂                /            \
          │                │                   Yes              No
          ├────────────────┼──────────        /                    \
          │      R₃        │    R₄       [ x₂ ≤ 3.0 ]          [ Class B ]
          │                │               /       \
          └────────────────┴────────►    Yes        No
          0               5.0     x₁    /            \
                                  [ Class A ]    [ Class C ]
```

### Mathematical Formulation
For any query point $\mathbf{x}$, the decision tree maps it to exactly one leaf region $R_m$:

$$\hat{f}(\mathbf{x}) = \sum_{m=1}^M c_m \cdot \mathbb{I}(\mathbf{x} \in R_m)$$

Where:
- $\mathbb{I}(\cdot)$ is the indicator function ($1$ if $\mathbf{x} \in R_m$, else $0$).
- For **Classification**: $c_m = \operatorname{argmax}_k \hat{p}_{mk}$ (the majority class in region $R_m$).
- For **Regression**: $c_m = \frac{1}{N_m} \sum_{\mathbf{x}_i \in R_m} y_i$ (the arithmetic mean of target values in region $R_m$).

---

## 2. Mathematical Splitting Criteria (Classification)

At each internal node, the tree must select a feature $j$ and a threshold $t$ to split the local dataset $D$ into two subsets:

$$D_L(j, t) = \{(\mathbf{x}, y) \in D \mid x_j \le t\}, \quad D_R(j, t) = \{(\mathbf{x}, y) \in D \mid x_j > t\}$$

The optimal split $(j^*, t^*)$ maximizes the **reduction in impurity**:

$$\Delta I(D, j, t) = I(D) - \left( \frac{|D_L|}{|D|} I(D_L) + \frac{|D_R|}{|D|} I(D_R) \right)$$

Where $I(D)$ is an impurity function measured over the class probability distribution $p_k = \frac{1}{|D|} \sum_{i \in D} \mathbb{I}(y_i = k)$ for $k \in \{1, \dots, K\}$.

```
 Impurity Functions vs Class Probability p:
     Impurity ▲
          1.0 ┼               ┌─── Entropy / 2: -0.5 [p log₂ p + (1-p) log₂ (1-p)]
              │             ╱   ╲
          0.5 ┼───────────╭───────╮── Gini Impurity: 2p(1 - p)
              │          ╱│       │╲
              │         ╱ │       │ ╲── Misclassification Error: 1 - max(p, 1-p)
          0.0 ┼────────┴──┼───────┼──┴─────►
              0          0.5     1.0      p
```

### 2.1 Shannon Entropy & Information Gain (ID3)
Rooted in Claude Shannon's Information Theory, **Entropy** measures the expected information content (in bits) required to describe the state of an outcome:

$$H(D) = -\sum_{k=1}^K p_k \log_2(p_k) \quad (\text{with } 0 \log_2 0 \triangleq 0)$$

- **Minimum ($H = 0$)**: Complete purity; every instance belongs to a single class.
- **Maximum ($H = \log_2 K$)**: Uniform distribution; maximal uncertainty. For binary classification ($K=2$), $H_{\max} = \log_2 2 = 1.0\text{ bit}$.

**Information Gain (IG)** is the decrease in entropy after the split:

$$IG(D, j, t) = H(D) - \sum_{v \in \{L, R\}} \frac{|D_v|}{|D|} H(D_v)$$

> [!WARNING]
> **The High-Cardinality Pathology of ID3**:  
> If an attribute has unique values for every instance (e.g., `Customer_ID` or `Credit_Card_Number`), splitting on it creates leaves with $|D_v| = 1$.  
> The resulting entropy is $H(D_v) = 0$ everywhere, giving an artificially astronomical Information Gain! The model memorizes IDs and fails to generalize.

### 2.2 Gain Ratio (C4.5)
Ross Quinlan introduced **C4.5** to penalize features with excessively high cardinality by dividing Information Gain by the **Split Information** (the entropy of the split itself):

$$\text{SplitInfo}(D, A) = -\sum_{v=1}^V \frac{|D_v|}{|D|} \log_2 \left(\frac{|D_v|}{|D|}\right)$$

$$\text{Gain Ratio}(D, A) = \frac{IG(D, A)}{\text{SplitInfo}(D, A)}$$

If an attribute partitions data into hundreds of microscopic subsets, $\text{SplitInfo}$ becomes large, driving the Gain Ratio down.

### 2.3 Gini Impurity (CART)
Leo Breiman's **Classification and Regression Trees (CART)** replaces logarithms with polynomial arithmetic, dramatically accelerating training:

$$G(D) = 1 - \sum_{k=1}^K p_k^2 = \sum_{k=1}^K p_k (1 - p_k)$$

- **Intuition**: $G(D)$ is the probability that a randomly chosen element from the set would be incorrectly labeled if it were randomly labeled according to the distribution of labels in the subset.
- For binary classification with probability $p$:
  $$G(p) = 1 - [p^2 + (1-p)^2] = 2p(1 - p)$$
  - Pure node ($p = 0$ or $p = 1$): $G = 0$.
  - Maximally mixed node ($p = 0.5$): $G = 0.5$.

> [!TIP]
> **Gini vs. Entropy**:  
> In practice, Gini Impurity and Entropy yield identical tree structures $>98\%$ of the time. However, Gini avoids computing transcendental functions ($\log_2$), making it $2\times$ to $3\times$ faster during feature selection.

---

## 3. Splitting Continuous Features

Unlike discrete categories, continuous numerical features have infinite possible thresholds. CART optimizes continuous thresholds efficiently:

```
 Continuous Feature Evaluation:
 1. Sort values:           [ 1.2,  1.8,  2.9,  3.5,  4.1,  5.8 ]
 2. Class labels:          [  0 ,   0 ,   1 ,   1 ,   0 ,   1  ]
 3. Candidate thresholds:        1.5   2.35  3.2   3.8   4.95
                                  ▲     ▲     ▲     ▲     ▲
                        Evaluate Gini at each boundary midpoint!
```

### The Algorithm:
1. For feature $j$, sort the $N$ observations in ascending order: $x_{(1), j} \le x_{(2), j} \le \dots \le x_{(N), j}$.
2. Candidate split thresholds are the midpoints between adjacent distinct values:
   $$t_i = \frac{x_{(i), j} + x_{(i+1), j}}{2}$$
3. To achieve $\mathcal{O}(N \log N)$ complexity, maintain running label count histograms. As the threshold moves from left to right, shift counts from $D_R$ to $D_L$ in $\mathcal{O}(1)$ time, computing impurity incrementally without scanning all instances.

---

## 4. Regression Trees

When the target $y \in \mathbb{R}$ is continuous, CART builds **Regression Trees**.

### 4.1 Splitting Criterion: Variance Reduction
The impurity of a continuous region $R_m$ is its **Mean Squared Error (Variance)**:

$$\text{MSE}(R_m) = \frac{1}{N_m} \sum_{i \in R_m} (y_i - \bar{y}_{R_m})^2, \quad \text{where } \bar{y}_{R_m} = \frac{1}{N_m} \sum_{i \in R_m} y_i$$

The optimal split $(j^*, t^*)$ minimizes the weighted sum of squared errors:

$$\min_{j, t} \left[ \sum_{i \in D_L(j, t)} (y_i - \bar{y}_L)^2 + \sum_{i \in D_R(j, t)} (y_i - \bar{y}_R)^2 \right]$$

### 4.2 Prediction
At inference, any query falling into region $R_m$ is predicted as the constant leaf mean $\bar{y}_{R_m}$.

```
 Regression Tree Step Function Approximation:
    y ▲                     ┌─────── Leaf 3 Mean
      │                 ┌───┘
      │         ┌───────┘ Leaf 2 Mean
      │    ─────┘ Leaf 1 Mean
      │    •  •    •• ••     ••• •  • (Data points)
      └────┴────────┴────────┴────────► x
           t₁       t₂       t₃
```

---

## 5. Overfitting, Inductive Bias & Regularization

### 5.1 Inductive Bias & Pathologies
1. **Axis-Aligned Splits**: Decision trees split perpendicularly to coordinate axes ($x_j \le t$). If true decision boundaries are diagonal ($x_1 + x_2 \le 5$), trees must approximate the diagonal with an inefficient "staircase" of dozens of splits.
2. **High Variance**: Small perturbations in training data can cause a completely different feature to be chosen at the root, radically altering the entire tree structure.

### 5.2 Pre-Pruning (Early Stopping Hyperparameters)
Stop splitting before leaves become pure:
- `max_depth`: Limits the maximum distance from root to leaf.
- `min_samples_split`: Minimum instances required in a node to attempt a split.
- `min_samples_leaf`: Minimum instances required in a terminal leaf node (smooths variance).
- `max_leaf_nodes`: Best-first search up to a fixed maximum leaf budget.

### 5.3 Post-Pruning: Minimal Cost-Complexity Pruning
Grow a large tree $T_0$ until all leaves are pure, then prune subtrees that fail to justify their complexity.

Define the **Cost-Complexity Criterion**:

$$R_\alpha(T) = R(T) + \alpha |T|$$

Where:
- $R(T) = \sum_{m=1}^{|T|} \sum_{\mathbf{x}_i \in R_m} L(y_i, \hat{y}_m)$ is the total training error of tree $T$.
- $|T|$ is the number of terminal leaf nodes.
- $\alpha \ge 0$ is the complexity tuning parameter.
  - $\alpha = 0$: The full unpruned tree $T_0$.
  - $\alpha \to \infty$: The single-node root tree.

As $\alpha$ increases, subtrees with the smallest **effective cost per leaf reduction** are collapsed:

$$g(t) = \frac{R(t) - R(T_t)}{|T_t| - 1}$$

The optimal $\alpha^*$ is chosen via K-Fold Cross-Validation.

---

## 6. Feature Importance: Mean Decrease in Impurity (MDI)

Decision trees provide intrinsic interpretability by measuring how much each feature contributed to reducing overall impurity:

$$\text{Importance}(x_j) = \sum_{t \in \text{Nodes split on } j} \frac{N_t}{N} \Delta I(t)$$

Where:
- $N_t$ is the number of samples reaching node $t$.
- $N$ is the total training set size.
- $\Delta I(t) = I(t) - \frac{N_L}{N_t} I(t_L) - \frac{N_R}{N_t} I(t_R)$.

The importances are normalized so $\sum_{j=1}^d \text{Importance}(x_j) = 1.0$.

---

## 7. Complete Python Implementation from Scratch

```python
"""
CART Decision Tree Classifier from Scratch (Pure NumPy)
Supports Gini Impurity, recursive binary splitting, continuous features,
and max_depth / min_samples_split regularization.
"""

import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature          # Index of feature to split on
        self.threshold = threshold      # Split threshold value
        self.left = left                # Left child Node
        self.right = right              # Right child Node
        self.value = value              # Predicted class (if leaf node)

    @property
    def is_leaf(self) -> bool:
        return self.value is not None


class DecisionTreeClassifierScratch:
    def __init__(self, max_depth: int = 10, min_samples_split: int = 2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def _gini(self, y: np.ndarray) -> float:
        if len(y) == 0:
            return 0.0
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return 1.0 - np.sum(probabilities ** 2)

    def _best_split(self, X: np.ndarray, y: np.ndarray):
        best_gain = -1.0
        split_idx, split_thresh = None, None
        current_impurity = self._gini(y)
        n_samples, n_features = X.shape

        for feat_idx in range(n_features):
            values = X[:, feat_idx]
            thresholds = np.unique(values)
            
            # Test candidate midpoints
            for i in range(len(thresholds) - 1):
                thresh = (thresholds[i] + thresholds[i + 1]) / 2.0
                left_mask = values <= thresh
                right_mask = ~left_mask

                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue

                n_l, n_r = np.sum(left_mask), np.sum(right_mask)
                gini_l = self._gini(y[left_mask])
                gini_g = self._gini(y[right_mask])
                weighted_gini = (n_l / n_samples) * gini_l + (n_r / n_samples) * gini_g
                gain = current_impurity - weighted_gini

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = thresh

        return split_idx, split_thresh

    def _build_tree(self, X: np.ndarray, y: np.ndarray, depth: int = 0) -> Node:
        n_samples, _ = X.shape
        n_classes = len(np.unique(y))

        # Base cases: pure node, max depth reached, or insufficient samples
        if depth >= self.max_depth or n_classes == 1 or n_samples < self.min_samples_split:
            leaf_value = np.bincount(y).argmax()
            return Node(value=leaf_value)

        feat_idx, thresh = self._best_split(X, y)
        if feat_idx is None:
            leaf_value = np.bincount(y).argmax()
            return Node(value=leaf_value)

        left_mask = X[:, feat_idx] <= thresh
        right_mask = ~left_mask

        left_child = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_child = self._build_tree(X[right_mask], y[right_mask], depth + 1)
        return Node(feature=feat_idx, threshold=thresh, left=left_child, right=right_child)

    def fit(self, X: np.ndarray, y: np.ndarray):
        self.root = self._build_tree(X, y)
        return self

    def _predict_row(self, node: Node, x: np.ndarray) -> int:
        if node.is_leaf:
            return node.value
        if x[node.feature] <= node.threshold:
            return self._predict_row(node.left, x)
        return self._predict_row(node.right, x)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.array([self._predict_row(self.root, row) for row in X])


# Verification on Synthetic Data
if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.metrics import accuracy_score

    X, y = make_classification(n_samples=200, n_features=4, n_informative=3, random_state=42)
    tree = DecisionTreeClassifierScratch(max_depth=4)
    tree.fit(X, y)
    preds = tree.predict(X)
    print(f"Decision Tree Accuracy: {accuracy_score(y, preds) * 100:.2f}%")
```

---

## 📌 Summary Checklist & Exam Cram Notes

1. **Space Partitioning**: Non-parametric division of space into axis-aligned hyper-rectangles; decision boundary is a collection of orthogonal planes.
2. **Entropy**: $H(S) = -\sum p_i \log_2 p_i$. Measures information uncertainty; basis of ID3 and Information Gain.
3. **Gain Ratio**: $\frac{IG}{\text{SplitInfo}}$. C4.5's defense against high-cardinality attributes like `ID`.
4. **Gini Impurity**: $G(S) = 1 - \sum p_i^2 = 2p(1-p)$ for binary tasks. Computationally superior to entropy; basis of CART.
5. **Regression Trees**: Minimize residual variance; leaves predict local arithmetic mean $\bar{y}_{R_m}$.
6. **Bias-Variance**: Fully grown trees have near-zero bias but massive variance (overfitting); extremely sensitive to training sample shifts.
7. **Pre-Pruning**: Stop growth early using `max_depth`, `min_samples_split`, `min_samples_leaf`.
8. **Cost-Complexity Pruning**: $R_\alpha(T) = R(T) + \alpha |T|$. Balances empirical fit against leaf count $|T|$ via cross-validation.
9. **Feature Importance (MDI)**: Sum of impurity reductions attributed to feature splits weighted by sample volume.

---

## 🧠 Quick Self-Check Questions

1. A dataset contains 40 positive instances and 60 negative instances. Calculate its exact Gini Impurity and Shannon Entropy.
2. Why does an unconstrained decision tree achieve $100\%$ training accuracy on non-contradictory datasets, and why is this dangerous?
3. How does CART determine split thresholds for continuous features in $\mathcal{O}(N \log N)$ time?
4. In Minimal Cost-Complexity Pruning, what happens to the tree topology when $\alpha = 0$? What happens as $\alpha \to \infty$?
5. Why are Decision Trees invariant to monotonic feature scaling (e.g., MinMax or Standard scaling)?
