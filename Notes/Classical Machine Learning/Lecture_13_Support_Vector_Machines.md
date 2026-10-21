# Lecture 13: Support Vector Machines (SVM) & Kernel Methods
## Student Notes — SST Classical Machine Learning

---

## 🎯 Learning Objectives

By the end of this lecture, you should be able to:
- Formulate the **Maximum Margin Hyperplane** and explain why maximizing the geometric margin minimizes structural risk (Vapnik-Chervonenkis dimension).
- Distinguish between **Functional Margin** ($\hat{\gamma}_i = y_i(\mathbf{w}^T \mathbf{x}_i + b)$) and **Geometric Margin** ($\gamma_i = \frac{y_i(\mathbf{w}^T \mathbf{x}_i + b)}{\|\mathbf{w}\|}$).
- Formulate the **Hard Margin SVM** as a constrained convex quadratic optimization problem: $\min \frac{1}{2}\|\mathbf{w}\|^2$ s.t. $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$.
- Extend the formulation to **Soft Margin SVM** using **Slack Variables** ($\xi_i$) and the regularization budget parameter $C$.
- Apply the method of **Lagrange Multipliers** and derive the **Karush-Kuhn-Tucker (KKT) Conditions**, proving why only points with $\alpha_i > 0$ (**Support Vectors**) dictate the decision boundary.
- Derive the **Wolfe Dual Formulation** and recognize that the entire optimization problem depends strictly on pairwise **inner products** $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$.
- Formulate the **Kernel Trick** via Mercer's Theorem, mapping low-dimensional input vectors into infinite-dimensional Hilbert spaces without explicitly computing coordinates.
- Analyze the behavior and hyperparameters of core kernel functions: **Linear**, **Polynomial**, and **Radial Basis Function (RBF / Gaussian)**.
- Formulate **Support Vector Regression (SVR)** with an $\epsilon$-insensitive loss tube.
- Build an end-to-end SVM optimization pipeline in Python.

---

## 1. High-Level Philosophy: The Maximum Margin

For any linearly separable dataset, infinitely many hyperplanes can separate the classes with $100\%$ training accuracy. Which one is objectively the best?

```
 Infinitely Many Valid Separators:            The Unique Maximum Margin Hyperplane:
       x₂ ▲                                          x₂ ▲             Support Vector
          │     o    o      /                           │     o    o      ▲
          │   o   o        /   +                        │   o   o        │   +
          │  o            /   + +                       │  o        ─────┼─── + +
          │              /  +                           │   Margin: 2/‖w‖│  +
          │             /   + +                         │        ◄───────┼──────►
          │   o        /                                │   o       ─────┼───
          │           /                                 │                │
          └──────────/─────────────►                    └────────────────┴────────►
                     Plane A                            -1               +1
                                                        wᵀx + b = -1    wᵀx + b = +1
                                                               wᵀx + b = 0
```

### Why Maximize the Margin?
- **Robustness to Noise**: Points near the boundary are most susceptible to measurement error or test distribution shift. Placing the boundary as far as possible from all training points maximizes noise tolerance.
- **Statistical Learning Theory (Vapnik)**: Vladimir Vapnik proved that the generalization error bound scales inversely with the margin:

  $$\text{Generalization Error} \le \text{Training Error} + \mathcal{O}\left( \sqrt{\frac{R^2 / \gamma^2}{n}} \right)$$

  Where $\gamma$ is the geometric margin and $R$ is the bounding radius of the data. Maximizing margin $\gamma$ directly minimizes the upper bound on generalization error!

---

## 2. Hard Margin SVM Formulation

Let labels be encoded as $y_i \in \{-1, +1\}$ and the decision boundary be the hyperplane:

$$\mathbf{w}^T \mathbf{x} + b = 0$$

The decision rule is:

$$\hat{y} = \operatorname{sign}(\mathbf{w}^T \mathbf{x} + b)$$

### 2.1 Functional vs. Geometric Margin
1. **Functional Margin** with respect to instance $(\mathbf{x}_i, y_i)$:
   $$\hat{\gamma}_i = y_i(\mathbf{w}^T \mathbf{x}_i + b)$$
   - *Problem*: Arbitrarily scaling $\mathbf{w} \to 2\mathbf{w}$ and $b \to 2b$ doubles $\hat{\gamma}_i$ without changing the physical decision boundary.
2. **Geometric Margin** (Euclidean perpendicular distance from $\mathbf{x}_i$ to the hyperplane):
   $$\gamma_i = \frac{y_i(\mathbf{w}^T \mathbf{x}_i + b)}{\|\mathbf{w}\|_2}$$
   - Invariant to positive scaling of $\mathbf{w}$ and $b$.

### 2.2 The Optimization Objective
We seek to maximize the margin of the closest point:

$$\max_{\mathbf{w}, b} \gamma \quad \text{subject to } \frac{y_i(\mathbf{w}^T \mathbf{x}_i + b)}{\|\mathbf{w}\|} \ge \gamma, \quad \forall i$$

Because we can scale $(\mathbf{w}, b)$ arbitrarily without altering the boundary, we fix the functional margin of the closest support vector to exactly $1$:

$$\min_{i} y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$$

Then the geometric margin of the support vectors becomes:

$$\gamma = \frac{1}{\|\mathbf{w}\|_2}$$

Maximizing the margin width $\frac{2}{\|\mathbf{w}\|}$ is mathematically equivalent to minimizing $\frac{1}{2}\|\mathbf{w}\|^2$:

$$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|_2^2 \quad \text{subject to } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad \forall i \in \{1, \dots, n\}$$

> [!NOTE]
> This is a **Convex Quadratic Programming (QP)** problem with linear inequality constraints. It possesses a strictly unique global minimum with zero local optima!

---

## 3. Soft Margin SVM: Slack Variables & $C$

Real-world datasets are rarely linearly separable. Outliers or overlapping distributions would make Hard Margin SVM infeasible (no solution exists).

```
 Hard Margin vs Soft Margin:
 Hard Margin: Infeasible due to 1 outlier!     Soft Margin: Slack variables (ξ) allow violations!
        x₂ ▲                                        x₂ ▲
           │   o    o     /                            │   o    o     /  ξ₁ > 0 (Within margin)
           │     o       /   +                         │     o       / ──+ (Margin)
           │            /   + +                        │            /   + +
           │     + ◄── / ── Outlier ruins it!          │     + ◄── / ── ξ₂ > 1 (Misclassified)
           │          /                                │          /
           └─────────/──────────►                      └─────────/──────────►
```

### 3.1 Slack Variables ($\xi_i$)
Cortes & Vapnik (1995) introduced non-negative slack variables $\xi_i \ge 0$:
- $\xi_i = 0$: Instance is on or outside the correct margin boundary.
- $0 < \xi_i \le 1$: Instance is within the margin, but still on the correct side of the decision boundary.
- $\xi_i > 1$: Instance is on the wrong side of the decision boundary (**misclassified**).

### 3.2 The Primal Objective
$$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|^2 + C \sum_{i=1}^n \xi_i \quad \text{subject to } y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$

### 3.3 The Role of Hyperparameter $C$
$C$ controls the **trade-off between margin width and classification error**:
- **Large $C$ (Hard Margin tendency)**: High penalty for misclassifications. Forces a narrow margin to fit every data point. **Low bias, high variance** (risk of overfitting).
- **Small $C$ (Soft Margin tendency)**: Tolerates many margin violations to achieve a wide margin. **High bias, low variance** (more robust to noise).

---

## 4. Duality & Karush-Kuhn-Tucker (KKT) Conditions

To solve the constrained optimization problem and unlock non-linear kernels, we construct the **Lagrangian Function**:

$$\mathcal{L}(\mathbf{w}, b, \boldsymbol{\xi}, \boldsymbol{\alpha}, \boldsymbol{\beta}) = \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n \alpha_i \left[ y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1 + \xi_i \right] - \sum_{i=1}^n \beta_i \xi_i$$

Where $\alpha_i \ge 0$ and $\beta_i \ge 0$ are Lagrange multipliers.

### 4.1 Stationarity Conditions
Setting partial derivatives to zero:
1. $\nabla_\mathbf{w} \mathcal{L} = \mathbf{w} - \sum_{i=1}^n \alpha_i y_i \mathbf{x}_i = \mathbf{0} \implies \mathbf{w} = \sum_{i=1}^n \alpha_i y_i \mathbf{x}_i$
2. $\frac{\partial \mathcal{L}}{\partial b} = -\sum_{i=1}^n \alpha_i y_i = 0 \implies \sum_{i=1}^n \alpha_i y_i = 0$
3. $\frac{\partial \mathcal{L}}{\partial \xi_i} = C - \alpha_i - \beta_i = 0 \implies \alpha_i + \beta_i = C$

### 4.2 The KKT Complementary Slackness Conditions
At the optimal solution:
$$\alpha_i \left[ y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1 + \xi_i \right] = 0$$
$$\beta_i \xi_i = 0 \iff (C - \alpha_i)\xi_i = 0$$

### 4.3 Why Support Vectors Matter
From complementary slackness, exactly three cases exist for each training instance:

| Lagrange Multiplier | Slack $\xi_i$ | Geometric Location | Status |
| :--- | :--- | :--- | :--- |
| **$\alpha_i = 0$** | $\xi_i = 0$ | $y_i(\mathbf{w}^T \mathbf{x}_i + b) > 1$ | Well outside the margin; **has zero influence on $\mathbf{w}$**! |
| **$0 < \alpha_i < C$** | $\xi_i = 0$ | $y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$ | **Free Support Vector**: Sits exactly on the margin boundary. |
| **$\alpha_i = C$** | $\xi_i > 0$ | $y_i(\mathbf{w}^T \mathbf{x}_i + b) < 1$ | **Bounded Support Vector**: Inside the margin or misclassified. |

> [!IMPORTANT]
> **The Extreme Sparsity of SVMs**:  
> In a dataset of 1,000,000 points, typically only a few dozen points have $\alpha_i > 0$.  
> **All points with $\alpha_i = 0$ could be deleted from the dataset, and the resulting model would remain 100% mathematically identical!**

---

## 5. The Wolfe Dual Formulation

Substituting the stationarity relations back into the Lagrangian eliminates $\mathbf{w}$, $b$, and $\boldsymbol{\xi}$, yielding the **Dual Problem**:

$$\max_{\boldsymbol{\alpha}} \sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle$$

$$\text{Subject to: } \quad 0 \le \alpha_i \le C, \quad \sum_{i=1}^n \alpha_i y_i = 0$$

### The Core Revelation:
Notice that the feature vectors appear **strictly as inner products**: $\langle \mathbf{x}_i, \mathbf{x}_j \rangle = \mathbf{x}_i^T \mathbf{x}_j$!  
We never need individual coordinates of $\mathbf{x}$; we only need the pairwise dot products between instances.

---

## 6. The Kernel Trick & Mercer's Theorem

If data is not linearly separable in the input space $\mathbb{R}^d$, we can project it into a higher-dimensional feature space $\mathcal{H}$ via a non-linear mapping $\phi(\mathbf{x})$:

$$\mathbf{x} \in \mathbb{R}^d \xrightarrow{\phi} \phi(\mathbf{x}) \in \mathcal{H}$$

In $\mathcal{H}$, the data becomes linearly separable!

```
 1D Non-Separable Data:                  Projected to 2D: φ(x) = (x, x²):
      o    o   +   +   +   o   o                 x² ▲   Separating Hyperplane!
   ───o────o───+───+───+───o───o──► x               │      o         o
                                                    │        \     /
                                                    │     +   \ + /   +
                                                    └──────────\─/────────► x
```

### The Kernel Trick
Computing high-dimensional projections $\phi(\mathbf{x})$ directly is computationally catastrophic (e.g., polynomial mapping of degree $10$ in $100$ dimensions creates $>10^{13}$ features!).

**The Kernel Trick** computes the inner product in $\mathcal{H}$ directly using the low-dimensional vectors:

$$K(\mathbf{x}_i, \mathbf{x}_j) = \langle \phi(\mathbf{x}_i), \phi(\mathbf{x}_j) \rangle$$

### Mercer's Theorem (1909)
Any continuous symmetric function $K(\mathbf{x}, \mathbf{z})$ is a valid kernel if and only if its Gram matrix $K_{ij} = K(\mathbf{x}_i, \mathbf{x}_j)$ is **positive semi-definite** for all finite point sets.

### Common Kernel Functions:

| Kernel Name | Mathematical Definition | Key Hyperparameters & Notes |
| :--- | :--- | :--- |
| **Linear** | $K(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$ | Fast; for high-dimensional sparse data (text, genomics). |
| **Polynomial** | $K(\mathbf{x}, \mathbf{z}) = (\gamma \mathbf{x}^T \mathbf{z} + c)^d$ | Degree $d$, coefficient $c$. Models feature interactions. |
| **Radial Basis Function (RBF)** | $K(\mathbf{x}, \mathbf{z}) = \exp\left(-\gamma \|\mathbf{x} - \mathbf{z}\|^2\right)$ | **Infinite-dimensional Hilbert space**! $\gamma = \frac{1}{2\sigma^2}$. |
| **Sigmoid** | $K(\mathbf{x}, \mathbf{z}) = \tanh(\gamma \mathbf{x}^T \mathbf{z} + c)$ | Emulates a 2-layer Neural Network. |

### The RBF Kernel Hyperparameter $\gamma$:
- **Large $\gamma$**: Narrow Gaussian bells. Each support vector has a tiny localized sphere of influence. **High variance (overfitting)**; decision boundary wraps tightly around individual instances.
- **Small $\gamma$**: Broad Gaussian bells. Wide sphere of influence; boundary becomes smooth and near-linear. **High bias (underfitting)**.

---

## 7. Support Vector Regression (SVR)

In regression, rather than maximizing margin between classes, SVM fits an **$\epsilon$-insensitive tube** around the data:

$$\mathcal{L}_\epsilon(y, \hat{y}) = \max(0, |y - \hat{y}| - \epsilon)$$

```
 Support Vector Regression (ε-Insensitive Tube):
    y ▲                                   +ε Tube Boundary
      │                 ╭─────────────╮
      │             ╭───╯    •   •    ╰─── Predicted Function f(x)
      │         ╭───╯      •   •   •
      │     ╭───╯    •   •                -ε Tube Boundary
      │ •   │ (Errors inside tube ignored!)
      └───•─┴────────────────────────────────► x
```

- Any error smaller than $\epsilon$ incurs **zero penalty**!
- Only points falling outside the tube act as support vectors.

---

## 8. Complete Python Implementation with scikit-learn

```python
"""
Support Vector Machine: Hyperplane, Support Vectors, and RBF Kernel Tuning
Demonstrates soft-margin C tuning and RBF gamma grid exploration.
"""

import numpy as np
from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# 1. Generate non-linearly separable dataset
X, y = make_moons(n_samples=500, noise=0.25, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 2. Fit Linear SVM vs RBF Kernel SVM
linear_svm = SVC(kernel="linear", C=1.0)
linear_svm.fit(X_train, y_train)

rbf_svm = SVC(kernel="rbf", C=10.0, gamma=2.0)
rbf_svm.fit(X_train, y_train)

# 3. Evaluate Performance
y_pred_linear = linear_svm.predict(X_test)
y_pred_rbf = rbf_svm.predict(X_test)

print(f"Linear SVM Accuracy: {accuracy_score(y_test, y_pred_linear) * 100:.2f}%")
print(f"RBF Kernel SVM Accuracy: {accuracy_score(y_test, y_pred_rbf) * 100:.2f}%")
print(f"Number of Support Vectors (RBF): {len(rbf_svm.support_vectors_)} / {len(X_train)}")
```

---

## 📌 Summary Checklist & Exam Cram Notes

1. **Max Margin Principle**: Maximizing the geometric margin $\frac{2}{\|\mathbf{w}\|}$ minimizes the structural risk upper bound.
2. **Hard Margin QP**: $\min \frac{1}{2}\|\mathbf{w}\|^2$ s.t. $y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1$. Requires linear separability.
3. **Soft Margin & Slack**: Slack variables $\xi_i \ge 0$ allow bounded margin violations; controlled by penalty $C$.
4. **Hyperparameter $C$**: Large $C$ = narrow margin, high variance; small $C$ = wide margin, high bias.
5. **KKT Sparsity**: Only points with $\alpha_i > 0$ are Support Vectors. Points with $\alpha_i = 0$ can be deleted with zero change to model.
6. **Wolfe Dual**: $\max_\alpha \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle$. Optimization depends strictly on pairwise inner products!
7. **Kernel Trick**: Replaces $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$ with $K(\mathbf{x}_i, \mathbf{x}_j)$ to compute dot products in infinite-dimensional Hilbert space without mapping coordinates.
8. **RBF Hyperparameter $\gamma$**: Large $\gamma$ = narrow localized Gaussian peaks (overfitting); small $\gamma$ = broad flat distributions (underfitting).

---

## 🧠 Quick Self-Check Questions

1. In a linearly separable problem, three support vectors have coordinates $(1, 1)$, $(2, 0)$, and $(2, 3)$. If all other 10,000 data points are deleted, does the decision boundary move?
2. What is the geometric difference between an instance with $\alpha_i = C$ versus an instance with $0 < \alpha_i < C$?
3. How does the RBF kernel map points into an infinite-dimensional feature space? Prove using Taylor series of the exponential function.
4. Why is Feature Scaling (Standardization) strictly mandatory before training a Support Vector Machine?
5. In Support Vector Regression (SVR), what does the $\epsilon$ parameter represent, and what happens to the number of support vectors as $\epsilon \to 0$?
