# Lecture 12: Ensemble Learning — Bagging, Random Forests & Boosting
## Student Notes — SST Classical Machine Learning

---

## 🎯 Learning Objectives

By the end of this lecture, you should be able to:
- Formulate the theoretical foundation of **Ensemble Learning** and prove how **Condorcet's Jury Theorem** enables ensembles of weak learners to outperform any single model.
- Derive the mathematics of **Bootstrap Aggregating (Bagging)**, proving that each bootstrap sample contains $(1 - 1/e) \approx 63.2\%$ unique instances while $\approx 36.8\%$ remain **Out-Of-Bag (OOB)**.
- Formulate **Random Forests** and mathematically prove how feature subsampling ($m = \sqrt{p}$) de-correlates trees, driving ensemble variance down according to $\rho \sigma^2 + \frac{1-\rho}{B}\sigma^2$.
- Contrast the inductive mechanisms of **Bagging (Variance Reduction)** against **Boosting (Bias Reduction)**.
- Derive the **AdaBoost** algorithm step-by-step under Exponential Loss, deriving learner weights $\alpha_t = \frac{1}{2}\ln(\frac{1 - \epsilon_t}{\epsilon_t})$ and sample weight updates.
- Formulate **Gradient Boosting (GBM)** as functional gradient descent, deriving pseudo-residuals as negative gradients of arbitrary differentiable loss functions.
- Formulate **XGBoost (Extreme Gradient Boosting)**, deriving its 2nd-order Taylor expansion, optimal leaf weights $w_j^* = -\frac{G_j}{H_j + \lambda}$, and the tree split Gain formula.
- Build production-ready Bagging and AdaBoost pipelines from scratch in NumPy.

---

## 1. High-Level Philosophy: Condorcet's Jury Theorem

Why does combining multiple models produce superior predictions?

### Condorcet's Jury Theorem (1785)
Suppose $B$ independent voters must decide on a binary truth. Each voter has an individual accuracy $p > 0.5$. The probability $P_{\text{ensemble}}$ that the majority vote is correct follows the binomial cumulative distribution:

$$P_{\text{ensemble}} = \sum_{k=\lfloor B/2 \rfloor + 1}^B \binom{B}{k} p^k (1 - p)^{B-k}$$

As the number of independent voters $B \to \infty$:

$$\lim_{B \to \infty} P_{\text{ensemble}} = 1.0$$

```
 Ensemble Accuracy vs Number of Base Learners (p = 0.60):
 Ensemble Accuracy ▲
             1.00 ┼─────────────────────────────────── 99.9% (B = 100)
                  │                              ╭────
             0.80 ┼                    ╭─────────╯
                  │          ╭─────────╯ (B = 25)
             0.60 ┼──────────╯ Base Learner Accuracy (p = 0.60)
                  │
             0.00 ┼──────────┬──────────┬──────────┬──────►
                  0          25         50        100     B (Number of Learners)
```

> [!CRITICAL]
> **The Independence Assumption**:  
> The theorem holds **if and only if** individual errors are **uncorrelated**.  
> If all models make the exact same mistakes, ensembling yields zero benefit. The core challenge of ensemble learning is **maximizing learner diversity**.

---

## 2. Bagging (Bootstrap Aggregating)

Introduced by Leo Breiman (1996), **Bagging** reduces the variance of high-variance, unstable base estimators (such as deep decision trees) without increasing their bias.

```
 The Bagging Architecture:
                    Training Dataset D (n samples)
                   /              │               \
         Bootstrap Sample D₁    Bootstrap D₂     Bootstrap D_B  (Sample with replacement)
                  │               │               │
            [ Tree 1 ]       [ Tree 2 ]      [ Tree B ]         (Train in parallel)
                  │               │               │
            Prediction ŷ₁    Prediction ŷ₂   Prediction ŷ_B
                   \              │               /
                    ▼             ▼              ▼
                 [ Majority Vote or Average: ŷ_final ]
```

### 2.1 The Mathematics of Bootstrapping
Given a dataset $D$ of size $n$, sample $n$ instances **uniformly at random with replacement**.

The probability that a specific observation $x_i$ is **not selected** in a single draw is $1 - \frac{1}{n}$.  
Across $n$ independent draws, the probability that $x_i$ is omitted from the bootstrap sample is:

$$P(x_i \notin D_b) = \left(1 - \frac{1}{n}\right)^n$$

Taking the mathematical limit as $n \to \infty$:

$$\lim_{n \to \infty} \left(1 - \frac{1}{n}\right)^n = e^{-1} = \frac{1}{e} \approx 0.3679 \approx 36.8\%$$

- **In-Bag Samples**: Each bootstrap sample contains approximately $1 - 36.8\% = \mathbf{63.2\%}$ unique training instances.
- **Out-Of-Bag (OOB) Samples**: Approximately $\mathbf{36.8\%}$ of observations are omitted from any given bootstrap sample.

### 2.2 Out-Of-Bag (OOB) Error: Free Cross-Validation
Because each observation $x_i$ was omitted from roughly $36.8\%$ of the $B$ trees, we can evaluate model performance without a separate validation set:
1. For each instance $x_i$, collect predictions **only** from the subset of trees where $x_i$ was Out-Of-Bag.
2. Aggregate these OOB predictions into $\hat{y}_i^{\text{OOB}}$.
3. Compute the overall OOB score:
   $$\text{OOB Error} = \frac{1}{n}\sum_{i=1}^n L(y_i, \hat{y}_i^{\text{OOB}})$$
- **Industry Insight**: OOB error is an unbiased estimator of generalization error, statistically equivalent to 3-fold cross-validation, with zero extra training overhead!

---

## 3. Random Forests: De-Correlating Trees

While Bagging reduces variance, trees grown on bootstrap samples often look remarkably similar. If a dominant feature exists (e.g., $x_1$), almost every tree selects $x_1$ at the root, making tree predictions highly correlated.

### 3.1 The Variance of Correlated Trees
Let $B$ trees each have individual variance $\sigma^2$ and pairwise correlation $\rho = \text{Corr}(T_i, T_j)$.  
The variance of their ensemble average $\bar{T} = \frac{1}{B} \sum_{b=1}^B T_b$ is:

$$\operatorname{Var}(\bar{T}) = \rho \sigma^2 + \frac{1 - \rho}{B}\sigma^2$$

- As $B \to \infty$, the second term $\frac{1 - \rho}{B}\sigma^2 \to 0$.
- However, the variance is bounded below by the first term: $\rho \sigma^2$!
- **Key Insight**: To reduce variance to near zero, we must drive the correlation $\rho \to 0$.

### 3.2 The Random Subspace Method (Feature Subsampling)
**Random Forests** de-correlates trees by injecting two distinct sources of randomness:
1. **Row Subsampling**: Bootstrap sampling with replacement (Bagging).
2. **Column Subsampling (Random Feature Selection)**: At *every single node split*, the tree is forbidden from evaluating all $p$ features. Instead, it selects a fresh random subset of $m$ features:
   - For **Classification**: $m = \lfloor \sqrt{p} \rfloor$
   - For **Regression**: $m = \lfloor p / 3 \rfloor$

```
 Standard Tree vs Random Forest Split Selection:
 Standard CART:       Evaluates all features:    [ x₁, x₂, x₃, x₄, x₅, x₆ ] ──► Pick best
 Random Forest Node:  Selects random subset:    [ · , x₂, · , · , x₅, ·  ] ──► Pick best
                      (Forces exploration of secondary informative features!)
```

This prevents strong features from monopolizing root splits, drastically reducing $\rho$ and slashing total ensemble variance!

---

## 4. The Boosting Paradigm

While Bagging trains learners in parallel to reduce variance, **Boosting** trains learners sequentially to reduce bias.

```
 The Boosting Sequence:
 Learner 1 (T₁) ──► Calculates Errors ──► Reweights Hard Instances ──► Learner 2 (T₂) ──► ... ──► Weighted Vote
```

| Dimension | Bagging (Random Forest) | Boosting (AdaBoost, GBM, XGBoost) |
| :--- | :--- | :--- |
| **Objective** | Reduce **Variance** (prevent overfitting) | Reduce **Bias** (prevent underfitting) |
| **Base Learners** | Deep, unpruned trees (low bias, high variance) | Shallow trees / Stumps (high bias, low variance) |
| **Execution** | Fully **Parallel** ($\mathcal{O}(1)$ time with multi-core) | Strictly **Sequential** (learner $t$ depends on $t-1$) |
| **Weighting** | Equal voting weights ($1/B$) | Weighted by learner performance $\alpha_t$ |
| **Overfitting Risk**| Plateauing (adding more trees never hurts) | High (adding too many trees causes overfitting) |

---

## 5. AdaBoost (Adaptive Boosting)

Formulated by Freund & Schapire (1996), **AdaBoost.M1** sequentially reweights training samples, forcing subsequent learners to concentrate on previously misclassified points.

```
 AdaBoost Iterative Reweighting:
 Iteration 1:   •  •  •  •  •  •  •  (All samples equal weight: w = 1/n)
                [ Classifier 1 Splits ]
 Iteration 2:   •  •  •  ●  ●  •  •  (Misclassified samples grow larger; focus here!)
                [ Classifier 2 Splits ]
```

### 5.1 The Mathematical Derivation
Let $y_i \in \{-1, +1\}$ and initial weights $w_i^{(1)} = \frac{1}{n}$.

For iteration $t = 1, \dots, T$:
1. **Fit Base Learner**: Train weak learner $h_t(\mathbf{x})$ minimizing weighted training error:
   $$\epsilon_t = \sum_{i=1}^n w_i^{(t)} \mathbb{I}(y_i \neq h_t(\mathbf{x}_i))$$
2. **Compute Learner Weight $\alpha_t$**:
   $$\alpha_t = \frac{1}{2} \ln \left( \frac{1 - \epsilon_t}{\epsilon_t} \right)$$
   - If $\epsilon_t = 0.5$ (random guess): $\alpha_t = \frac{1}{2}\ln(1) = 0$ (learner given zero say).
   - If $\epsilon_t \to 0$ (near perfection): $\alpha_t \to +\infty$.
3. **Update Sample Weights**:
   $$w_i^{(t+1)} = \frac{w_i^{(t)} \exp\left(-\alpha_t y_i h_t(\mathbf{x}_i)\right)}{Z_t}$$
   Where $Z_t = \sum_{i=1}^n w_i^{(t)} \exp(-\alpha_t y_i h_t(\mathbf{x}_i))$ is a normalizing constant so $\sum w_i^{(t+1)} = 1$.
   - **Correctly classified** ($y_i h_t(\mathbf{x}_i) = +1$): $w_i^{(t+1)} \propto w_i^{(t)} e^{-\alpha_t}$ (weight decreases).
   - **Misclassified** ($y_i h_t(\mathbf{x}_i) = -1$): $w_i^{(t+1)} \propto w_i^{(t)} e^{+\alpha_t}$ (weight increases).
4. **Final Ensemble Prediction**:
   $$H(\mathbf{x}) = \operatorname{sign}\left( \sum_{t=1}^T \alpha_t h_t(\mathbf{x}) \right)$$

---

## 6. Gradient Boosting Machines (GBM)

Jerome Friedman (1999) generalized boosting beyond exponential loss by formulating it as **Gradient Descent in Function Space**.

Instead of updating model parameters $\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla_\mathbf{w} L$, Gradient Boosting updates the model predictions $F(\mathbf{x})$ directly:

$$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \eta \cdot h_m(\mathbf{x})$$

### 6.1 The Pseudo-Residual Derivation
To minimize total loss $\sum_{i=1}^n L(y_i, F(\mathbf{x}_i))$, each new tree $h_m(\mathbf{x})$ is fit to the **negative gradient of the loss function** evaluated at the current ensemble predictions:

$$r_{im} = -\left[ \frac{\partial L(y_i, F(\mathbf{x}_i))}{\partial F(\mathbf{x}_i)} \right]_{F(\mathbf{x}) = F_{m-1}(\mathbf{x})}$$

#### For Squared Error Loss ($L(y, F) = \frac{1}{2}(y - F)^2$):
$$r_{im} = -\left[ -(y_i - F(\mathbf{x}_i)) \right] = y_i - F_{m-1}(\mathbf{x}_i)$$
The pseudo-residual is **literally the residual error**! Each tree fits directly to the residual errors left by the preceding ensemble.

#### For Binary Log-Loss ($L(y, F) = \ln(1 + e^{-y F})$ with $y \in \{-1, +1\}$):
$$r_{im} = y_i - p_i, \quad \text{where } p_i = \sigma(F_{m-1}(\mathbf{x}_i))$$
The pseudo-residual is the difference between true label and predicted probability.

### 6.2 Shrinkage (Learning Rate $\eta$)
To avoid overfitting, scale each tree's contribution by a small shrinkage parameter $\eta \in (0.01, 0.1]$:

$$F_m(\mathbf{x}) = F_{m-1}(\mathbf{x}) + \eta \sum_{j=1}^{J_m} \gamma_{jm} \mathbb{I}(\mathbf{x} \in R_{jm})$$

---

## 7. XGBoost (Extreme Gradient Boosting)

Developed by Tianqi Chen (2016), **XGBoost** is the dominant competitive ML algorithm for tabular data. It improves classical GBM via four key innovations:

### 7.1 Second-Order Taylor Expansion
While standard GBM only uses first-order gradients (steepest descent), XGBoost approximates the objective using a **second-order Taylor expansion**:

$$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ L(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(\mathbf{x}_i) + \frac{1}{2} h_i f_t^2(\mathbf{x}_i) \right] + \Omega(f_t)$$

Where:
- $g_i = \frac{\partial L(y_i, \hat{y}_i^{(t-1)})}{\partial \hat{y}_i^{(t-1)}}$ is the 1st-order gradient.
- $h_i = \frac{\partial^2 L(y_i, \hat{y}_i^{(t-1)})}{\partial (\hat{y}_i^{(t-1)})^2}$ is the 2nd-order Hessian.
- $\Omega(f_t) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2$ is the **regularization penalty** on leaf count $T$ and leaf weights $w$.

### 7.2 Optimal Leaf Weight & Split Criterion
Let $I_j = \{i \mid \mathbf{x}_i \in R_j\}$ be the sample indices at leaf $j$. Define $G_j = \sum_{i \in I_j} g_i$ and $H_j = \sum_{i \in I_j} h_i$.

The optimal leaf weight $w_j^*$ that minimizes the objective is derived by setting the derivative to zero:

$$w_j^* = -\frac{G_j}{H_j + \lambda}$$

The resulting minimum loss value (the **Quality Score** of tree structure) is:

$$\text{Score}(T) = -\frac{1}{2}\sum_{j=1}^T \frac{G_j^2}{H_j + \lambda} + \gamma T$$

### 7.3 The Split Gain Formula
When considering a node split into Left ($L$) and Right ($R$) children:

$$\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$

- If $\text{Gain} < 0$, the split is not worth making. $\gamma$ serves as a **pruning threshold**.

---

## 8. Complete Python Implementation from Scratch

```python
"""
AdaBoost Classifier from Scratch (Pure NumPy)
Implements iterative sample reweighting, decision stumps, and weighted voting.
"""

import numpy as np

class DecisionStump:
    def __init__(self):
        self.polarity = 1
        self.feature_idx = None
        self.threshold = None
        self.alpha = None

    def predict(self, X: np.ndarray) -> np.ndarray:
        n_samples = X.shape[0]
        X_column = X[:, self.feature_idx]
        predictions = np.ones(n_samples)
        if self.polarity == 1:
            predictions[X_column < self.threshold] = -1
        else:
            predictions[X_column > self.threshold] = -1
        return predictions


class AdaBoostClassifierScratch:
    def __init__(self, n_estimators: int = 50):
        self.n_estimators = n_estimators
        self.estimators = []

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        # Initialize uniform weights: w_i = 1/N
        w = np.full(n_samples, (1.0 / n_samples))

        for _ in range(self.n_estimators):
            stump = DecisionStump()
            min_error = float('inf')

            # Search best feature and split threshold
            for feat_idx in range(n_features):
                X_column = X[:, feat_idx]
                thresholds = np.unique(X_column)

                for thresh in thresholds:
                    for polarity in [1, -1]:
                        preds = np.ones(n_samples)
                        if polarity == 1:
                            preds[X_column < thresh] = -1
                        else:
                            preds[X_column > thresh] = -1

                        # Weighted error
                        error = np.sum(w[y != preds])

                        if error < min_error:
                            min_error = error
                            stump.polarity = polarity
                            stump.threshold = thresh
                            stump.feature_idx = feat_idx

            # Avoid division by zero
            EPS = 1e-10
            min_error = np.clip(min_error, EPS, 1.0 - EPS)

            # Compute learner weight: alpha = 0.5 * ln((1 - eps) / eps)
            stump.alpha = 0.5 * np.log((1.0 - min_error) / min_error)

            # Update sample weights: w = w * exp(-alpha * y * h(x))
            preds = stump.predict(X)
            w *= np.exp(-stump.alpha * y * preds)
            w /= np.sum(w)  # Normalize

            self.estimators.append(stump)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        stump_preds = [stump.alpha * stump.predict(X) for stump in self.estimators]
        return np.sign(np.sum(stump_preds, axis=0))


# Verification on Synthetic Data
if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.metrics import accuracy_score

    X, y = make_classification(n_samples=200, n_features=6, random_state=42)
    y = np.where(y == 0, -1, 1)  # Convert to {-1, +1}

    clf = AdaBoostClassifierScratch(n_estimators=30)
    clf.fit(X, y)
    preds = clf.predict(X)
    print(f"AdaBoost Classifier Accuracy: {accuracy_score(y, preds) * 100:.2f}%")
```

---

## 📌 Summary Checklist & Exam Cram Notes

1. **Condorcet's Jury Theorem**: Ensembles of independent learners with accuracy $p > 0.5$ approach $100\%$ accuracy as $B \to \infty$.
2. **Bagging**: Trains deep, high-variance models in parallel on bootstrap samples ($63.2\%$ in-bag, $36.8\%$ OOB); slashes variance.
3. **OOB Score**: Internal validation metric evaluated on omitted instances; acts as free 3-fold cross validation.
4. **Random Forest De-correlation**: Randomly subsamples $m = \sqrt{p}$ features per split to drive pairwise correlation $\rho \to 0$, reducing ensemble variance $\rho \sigma^2$.
5. **Boosting Philosophy**: Sequentially trains weak learners (stumps) on reweighted or residual distributions; slashes bias.
6. **AdaBoost Weighting**: $\alpha_t = \frac{1}{2}\ln(\frac{1 - \epsilon_t}{\epsilon_t})$. Misclassified samples receive higher sample weights.
7. **Gradient Boosting (GBM)**: Fits each new tree to the negative gradient (pseudo-residual) of the loss function in prediction space.
8. **XGBoost Advancements**: 2nd-order Taylor series (Gradients $g_i$ + Hessians $h_i$), $L_2$ regularization $\lambda$, tree split penalty $\gamma$.

---

## 🧠 Quick Self-Check Questions

1. In a bootstrap sample of $n$ instances, prove why approximately $36.8\%$ of instances are omitted as $n \to \infty$.
2. Why does adding more trees to a Random Forest never cause overfitting, whereas adding too many trees to Gradient Boosting can cause severe overfitting?
3. In AdaBoost, what happens to the learner weight $\alpha_t$ if the weak learner achieves an error rate of $\epsilon_t = 0.5$? What if $\epsilon_t = 0.01$?
4. What is the difference between the pseudo-residuals of Gradient Boosting under Mean Squared Error loss versus Binary Cross-Entropy loss?
5. How does XGBoost's $\gamma$ hyperparameter serve as an automatic tree-pruning mechanism?
