# Classical Machine Learning (CML) — Master Formula Sheet & Exam Compendium
## Comprehensive Theoretical & Applied Mathematical Reference Across All 15 Lectures & SST End-Term Practice

---

## 📋 Table of Contents
1. [Foundations, Exploratory Data Analysis & Problem Formulation (Lecture 1)](#1-foundations-exploratory-data-analysis--problem-formulation)
2. [Data Preparation, Scaling & Encoding Pipelines (Lecture 2)](#2-data-preparation-scaling--encoding-pipelines)
3. [Linear Regression: Closed-Form OLS & Geometry (Lecture 3)](#3-linear-regression-closed-form-ols--geometry)
4. [Classical Assumptions of OLS & Diagnostics (LINE) (Lecture 4)](#4-classical-assumptions-of-ols--diagnostics-line)
5. [Optimization Foundations: Gradient Descent (Lecture 5)](#5-optimization-foundations-gradient-descent)
6. [Model Complexity, Bias-Variance Tradeoff & Polynomials (Lecture 6)](#6-model-complexity-bias-variance-tradeoff--polynomials)
7. [Cross-Validation & Regularization: Ridge, Lasso & ElasticNet (Lecture 7)](#7-cross-validation--regularization-ridge-lasso--elasticnet)
8. [Classification: Logistic Regression, Odds Ratios & Boundaries (Lecture 8)](#8-classification-logistic-regression-odds-ratios--boundaries)
9. [Classification Metrics, Threshold Tuning & Imbalance (Lectures 8 & 10)](#9-classification-metrics-threshold-tuning--imbalance)
10. [Instance-Based Learning: $k$-Nearest Neighbours (Lecture 9)](#10-instance-based-learning-k-nearest-neighbours)
11. [Tree-Based Models: Decision Trees (CART, ID3, C4.5) (Lecture 11)](#11-tree-based-models-decision-trees-cart-id3-c45)
12. [Ensemble Methods: Bagging, Random Forests & Boosting (Lecture 12)](#12-ensemble-methods-bagging-random-forests--boosting)
13. [Kernel Methods & Support Vector Machines (SVM) (Lecture 13)](#13-kernel-methods--support-vector-machines-svm)
14. [Probabilistic Classifiers: Naive Bayes (Lecture 14)](#14-probabilistic-classifiers-naive-bayes)
15. [Unsupervised Learning & Dimensionality Reduction (Lecture 15)](#15-unsupervised-learning--dimensionality-reduction)
16. [📌 Dedicated Section: Formulas & Step-by-Step Worked Problems from SST End-Term Practice Sheet (Group B)](#16-formulas--step-by-step-worked-problems-from-sst-end-term-practice-sheet-group-b)

---

## 1. Foundations, Exploratory Data Analysis & Problem Formulation

### 1.1 Mitchell's ETP Formal Definition of Machine Learning
A computer program is said to learn from experience $\mathcal{E}$ with respect to some class of tasks $\mathcal{T}$ and performance measure $\mathcal{P}$, if its performance at tasks in $\mathcal{T}$, as measured by $\mathcal{P}$, improves with experience $\mathcal{E}$:
$$\mathcal{P}(\mathcal{T} \mid \mathcal{E}_{t+\Delta t}) > \mathcal{P}(\mathcal{T} \mid \mathcal{E}_t)$$
- **Task ($\mathcal{T}$)**: The formal operational objective (e.g., Flag loan default, classify spam, predict house price).
- **Experience ($\mathcal{E}$)**: The empirical historical training dataset $\mathcal{D} = \{(\mathbf{x}^{(i)}, y^{(i)})\}_{i=1}^n$.
- **Performance ($\mathcal{P}$)**: The quantitative evaluation metric (e.g., Recall, RMSE, ROC-AUC, $F_1$-score).

### 1.2 Learning Paradigms & Loss Frameworks
- **Supervised Learning**: Given labeled pairs $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^n$. Find hypothesis $f: \mathcal{X} \to \mathcal{Y}$ minimizing empirical risk:
  $$\mathcal{R}_{\text{emp}}(f) = \frac{1}{n} \sum_{i=1}^n \mathcal{L}(f(\mathbf{x}_i), y_i)$$
  - **Regression**: Continuous target space $\mathcal{Y} \subseteq \mathbb{R}$.
  - **Classification**: Discrete categorical target space $\mathcal{Y} \in \{1, 2, \dots, K\}$.
- **Unsupervised Learning**: Given unlabelled feature matrix $\mathbf{X} \in \mathbb{R}^{n \times d}$. Model latent structure, density $p(\mathbf{x})$, or low-dimensional manifold:
  $$\min_{\boldsymbol{\theta}} \mathcal{L}(\mathbf{X}; \boldsymbol{\theta})$$

### 1.3 Statistical Measures of Location & Dispersion
- **Arithmetic Mean**:
  $$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$$
  *Property*: Highly sensitive to extreme outliers; minimizes sum of squared deviations $\sum (x_i - c)^2$.
- **Sample Median ($\tilde{x}$)**:
  $$\tilde{x} = \begin{cases} x_{(\frac{n+1}{2})} & \text{if } n \text{ is odd} \\ \frac{1}{2}\left(x_{(\frac{n}{2})} + x_{(\frac{n}{2}+1)}\right) & \text{if } n \text{ is even} \end{cases}$$
  *Property*: $50\%$ breakdown point; robust to outliers; minimizes sum of absolute deviations $\sum |x_i - c|$.
- **Sample Variance ($s^2$) & Standard Deviation ($s$)**:
  $$s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2, \quad s = \sqrt{s^2}$$
- **Interquartile Range (IQR)**:
  $$\text{IQR} = Q_3 - Q_1$$
  Tukey's outlier fences: $[\text{Lower}, \text{Upper}] = [Q_1 - 1.5 \cdot \text{IQR}, \; Q_3 + 1.5 \cdot \text{IQR}]$.

---

## 2. Data Preparation, Scaling & Encoding Pipelines

### 2.1 Feature Scaling Transformations
Feature scaling is mandatory for distance-based algorithms ($k$-NN, SVM, K-Means) and regularized models (Ridge, Lasso) because Euclidean metrics and weight penalty norms are scale-dependent.

| Scaler | Mathematical Formula | Output Range | Outlier Sensitivity |
| :--- | :--- | :--- | :--- |
| **StandardScaler (Z-Score)** | $x' = \frac{x - \mu}{\sigma}$ | $\mu=0, \sigma=1$ | Highly sensitive to outliers |
| **MinMaxScaler** | $x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}} \cdot (b - a) + a$ | $[a, b]$, default $[0, 1]$ | Compresses inliers if extreme outliers exist |
| **RobustScaler** | $x' = \frac{x - Q_2}{Q_3 - Q_1} = \frac{x - \text{median}}{\text{IQR}}$ | Unbounded, median $= 0$ | Robust against heavy-tailed outliers |
| **MaxAbsScaler** | $x' = \frac{x}{\max(|x|)}$ | $[-1, 1]$ | Preserves exact zeros in sparse matrices |

### 2.2 Categorical Encodings
- **One-Hot Encoding (OHE)**: Maps nominal categories $C \in \{c_1, \dots, c_K\}$ to $K$ binary columns:
  $$x_{ij} = \mathbb{I}(c^{(i)} = c_j)$$
  - *Dummy Variable Trap*: When an intercept $\theta_0$ is present, $\sum_{j=1}^K x_{ij} = 1$ causes exact linear dependence. Drop one column (`drop='first'`) to retain $K - 1$ columns.
- **Ordinal Encoding**: Maps ordered levels directly to integer ranks:
  $$E(c) = \{0, 1, \dots, K-1\} \quad \text{strictly preserving } c_{(1)} < c_{(2)} < \dots < c_{(K)}$$
  *Pitfall*: Scikit-learn's `OrdinalEncoder()` defaults to alphabetical sorting unless explicit order is passed via `categories=[[...]]`.
- **Target / Impact Encoding (with Smoothing)**:
  $$\hat{x}_c = \lambda(n_c) \bar{y}_c + (1 - \lambda(n_c)) \bar{y}_{\text{global}}, \quad \lambda(n_c) = \frac{n_c}{n_c + m}$$
  where $n_c$ is category frequency, $\bar{y}_c$ is category target mean, and $m$ is smoothing weight.

### 2.3 Mathematical Data Leakage Rule
Let dataset split be $\mathcal{D} = \mathcal{D}_{\text{train}} \cup \mathcal{D}_{\text{test}}$. All transformation parameters $\boldsymbol{\phi} = (\mu, \sigma, x_{\min}, x_{\max}, \text{imputer\_values})$ must satisfy:
$$\hat{\boldsymbol{\phi}} = g(\mathcal{D}_{\text{train}}) \quad \text{strictly}; \quad \mathcal{D}_{\text{test}}^{\text{scaled}} = T(\mathcal{D}_{\text{test}}; \hat{\boldsymbol{\phi}})$$
Fitting scalers or imputers on $\mathcal{D}_{\text{full}} = \mathcal{D}_{\text{train}} \cup \mathcal{D}_{\text{test}}$ contaminates training statistics with test distribution information (distribution leakage).

---

## 3. Linear Regression: Closed-Form OLS & Geometry

### 3.1 Hypothesis & Intercept Vectorization
$$h_{\boldsymbol{\theta}}(\mathbf{x}) = \theta_0 + \sum_{j=1}^d \theta_j x_j = \boldsymbol{\theta}^T \mathbf{x}, \quad \text{where } \mathbf{x} = [1, x_1, \dots, x_d]^T \in \mathbb{R}^{d+1}$$
Full dataset predictions:
$$\hat{\mathbf{y}} = \mathbf{X}\boldsymbol{\theta} \in \mathbb{R}^n, \quad \mathbf{X} \in \mathbb{R}^{n \times (d+1)}$$

### 3.2 Ordinary Least Squares (OLS) Objective Function
$$J(\boldsymbol{\theta}) = \frac{1}{2n} \|\hat{\mathbf{y}} - \mathbf{y}\|_2^2 = \frac{1}{2n} (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})^T (\mathbf{X}\boldsymbol{\theta} - \mathbf{y})$$
$$J(\boldsymbol{\theta}) = \frac{1}{2n} \left[ \boldsymbol{\theta}^T \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} - 2 \mathbf{y}^T \mathbf{X} \boldsymbol{\theta} + \mathbf{y}^T \mathbf{y} \right]$$

### 3.3 Normal Equation Derivation
Setting the matrix gradient to zero:
$$\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}) = \frac{1}{n} \left( \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} - \mathbf{X}^T \mathbf{y} \right) = \mathbf{0} \implies \mathbf{X}^T \mathbf{X} \boldsymbol{\theta} = \mathbf{X}^T \mathbf{y}$$
$$\boldsymbol{\theta}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$
- **Existence Condition**: Invertible if and only if $\text{rank}(\mathbf{X}) = d + 1$ (full column rank; $n \ge d + 1$ and no perfect collinearity).
- **Pseudoinverse Form**: If $\mathbf{X}^T \mathbf{X}$ is singular, use Moore-Penrose pseudoinverse $\boldsymbol{\theta}^* = \mathbf{X}^+ \mathbf{y}$.

### 3.4 Orthogonal Projection & The Hat Matrix
$$\hat{\mathbf{y}} = \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} = \mathbf{H} \mathbf{y}$$
- **Hat Matrix ($\mathbf{H}$)**: $\mathbf{H} = \mathbf{X}(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \in \mathbb{R}^{n \times n}$.
  - Symmetric: $\mathbf{H}^T = \mathbf{H}$
  - Idempotent: $\mathbf{H}^2 = \mathbf{H}$
  - Projection: Projects $\mathbf{y}$ orthogonally onto $\text{col}(\mathbf{X})$.
- **Residual Operator**:
  $$\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}} = (\mathbf{I} - \mathbf{H})\mathbf{y}, \quad \text{where } (\mathbf{I} - \mathbf{H}) \text{ is symmetric and idempotent}$$
  Orthogonality condition: $\mathbf{X}^T \mathbf{e} = \mathbf{X}^T (\mathbf{I} - \mathbf{H})\mathbf{y} = \mathbf{0}$.

### 3.5 Regression Evaluation Metrics
- **Mean Absolute Error (MAE)**:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
- **Mean Squared Error (MSE)**:
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2$$
- **Root Mean Squared Error (RMSE)**:
  $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
  *Fundamental Inequality*: $\text{RMSE} \ge \text{MAE}$ (by Jensen's inequality). Equality holds if and only if all absolute errors are identical.
- **Coefficient of Determination ($R^2$)**:
  $$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
  - In-sample OLS with intercept: $R^2 \in [0, 1]$.
  - Out-of-sample test set: $R^2 \in (-\infty, 1]$. A negative $R^2$ indicates the model performs worse than predicting the training mean $\bar{y}$.
- **Mean Absolute Percentage Error (MAPE)**:
  $$\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^n \left| \frac{y_i - \hat{y}_i}{y_i} \right|$$

---

## 4. Classical Assumptions of OLS & Diagnostics (LINE)

### 4.1 The LINE Mathematical Checklist
Under true population model $y_i = \boldsymbol{\theta}^T \mathbf{x}_i + \epsilon_i$:

1. **$\mathbf{L}$ — Linearity**:
   $$\mathbb{E}[\epsilon_i \mid \mathbf{X}] = 0 \iff \mathbb{E}[y \mid \mathbf{x}] = \boldsymbol{\theta}^T \mathbf{x}$$
   - *Diagnostic*: Residuals vs Fitted plot $\mathbf{e}$ vs $\hat{\mathbf{y}}$. Curvature indicates non-linearity.
   - *Remedy*: Add polynomial ($x^2$), interaction ($x_1 x_2$), or non-linear transform ($\log x, \sqrt{x}$).
2. **$\mathbf{I}$ — Independence**:
   $$\text{Cov}(\epsilon_i, \epsilon_j \mid \mathbf{X}) = 0 \quad \forall i \ne j$$
   - *Diagnostic*: Durbin-Watson statistic $DW \approx 2(1 - r)$, where $r$ is residual 1st-order autocorrelation.
     $$DW = \frac{\sum_{i=2}^n (e_i - e_{i-1})^2}{\sum_{i=1}^n e_i^2} \in [0, 4]$$
     - $DW \approx 2$: No autocorrelation.
     - $DW < 1.5$: Positive autocorrelation (common in time-series).
     - $DW > 2.5$: Negative autocorrelation.
3. **$\mathbf{N}$ — Normality of Errors**:
   $$\epsilon_i \mid \mathbf{X} \overset{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$$
   - *Diagnostic*: Normal Q-Q plot (residuals plotted against theoretical normal quantiles); Shapiro-Wilk or Jarque-Bera test:
     $$JB = \frac{n}{6}\left(S^2 + \frac{(K - 3)^2}{4}\right) \sim \chi^2_2$$
     where $S$ is sample skewness and $K$ is sample kurtosis.
4. **$\mathbf{E}$ — Equal Variance (Homoscedasticity)**:
   $$\text{Var}(\epsilon_i \mid \mathbf{X}) = \sigma^2 \quad \forall i$$
   - *Diagnostic*: Residuals vs Fitted plot exhibiting a "fan" or "funnel" shape (spread grows with $\hat{y}$); Breusch-Pagan test.
   - *Remedy*: Variance-stabilizing target transform: $y' = \ln(y)$ or Box-Cox:
     $$y^{(\lambda)} = \begin{cases} \frac{y^\lambda - 1}{\lambda} & \text{if } \lambda \ne 0 \\ \ln(y) & \text{if } \lambda = 0 \end{cases}$$

### 4.2 Multicollinearity & Variance Inflation Factor (VIF)
When independent variables are highly intercorrelated:
$$\text{VIF}_j = \frac{1}{1 - R_j^2} = \frac{1}{\text{Tolerance}_j}$$
where $R_j^2$ is the coefficient of determination obtained from regressing feature $x_j$ onto all remaining $d-1$ features.
- $\text{VIF} = 1$: Completely uncorrelated.
- $\text{VIF} > 5$: Moderate collinearity (warrants investigation).
- $\text{VIF} > 10$: Severe multicollinearity; sample variance of coefficient $\text{Var}(\hat{\theta}_j) = \frac{\sigma^2}{(n-1)s_j^2} \text{VIF}_j$ blows up, making weights unstable and uninterpretable.

### 4.3 Matrix Condition Number
$$\kappa(\mathbf{X}^T \mathbf{X}) = \sqrt{\frac{\lambda_{\max}(\mathbf{X}^T \mathbf{X})}{\lambda_{\min}(\mathbf{X}^T \mathbf{X})}}$$
- $\kappa > 30$: Moderate to severe numerical instability.

---

## 5. Optimization Foundations: Gradient Descent

### 5.1 First-Order Gradient Derivation for OLS
Cost function:
$$J(\boldsymbol{\theta}) = \frac{1}{2n} \sum_{i=1}^n (\boldsymbol{\theta}^T \mathbf{x}_i - y_i)^2$$
Scalar partial derivative for parameter $j$:
$$\frac{\partial J}{\partial \theta_j} = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i) x_{ij} = \frac{1}{n} \sum_{i=1}^n \text{Error}_i \cdot \text{Feature}_{ij}$$
Vectorized gradient:
$$\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}) = \frac{1}{n} \mathbf{X}^T (\mathbf{X}\boldsymbol{\theta} - \mathbf{y}) \in \mathbb{R}^{d+1}$$

### 5.2 Parameter Update Rules
- **Batch Gradient Descent (BGD)**:
  $$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \eta \nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}^{(t)}) = \boldsymbol{\theta}^{(t)} - \frac{\eta}{n} \mathbf{X}^T (\mathbf{X}\boldsymbol{\theta}^{(t)} - \mathbf{y})$$
- **Stochastic Gradient Descent (SGD)** (single random sample $i_t$):
  $$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \eta (\boldsymbol{\theta}^T \mathbf{x}_{i_t} - y_{i_t}) \mathbf{x}_{i_t}$$
- **Mini-Batch Gradient Descent (MBGD)** (batch $\mathcal{B} \subset \{1, \dots, n\}$ of size $B$):
  $$\boldsymbol{\theta}^{(t+1)} = \boldsymbol{\theta}^{(t)} - \frac{\eta}{B} \sum_{i \in \mathcal{B}} (\boldsymbol{\theta}^T \mathbf{x}_i - y_i) \mathbf{x}_i$$

### 5.3 Hessian Matrix & Proof of Convexity
$$\mathbf{H}_{jk} = \frac{\partial^2 J}{\partial \theta_j \partial \theta_k} \implies \nabla^2 J(\boldsymbol{\theta}) = \frac{1}{n} \mathbf{X}^T \mathbf{X}$$
For any non-zero vector $\mathbf{v} \ne \mathbf{0}$:
$$\mathbf{v}^T (\mathbf{X}^T \mathbf{X}) \mathbf{v} = (\mathbf{X}\mathbf{v})^T (\mathbf{X}\mathbf{v}) = \|\mathbf{X}\mathbf{v}\|_2^2 \ge 0$$
The Hessian is positive semi-definite (PSD) everywhere. Hence, OLS is globally convex with no local minima.

### 5.4 Advanced Optimization Accelerators
- **Classical Momentum**:
  $$\mathbf{v}_t = \beta \mathbf{v}_{t-1} + \eta \nabla J(\boldsymbol{\theta}_t), \quad \boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \mathbf{v}_t \quad (\beta \approx 0.9)$$
- **RMSProp (Adaptive Learning Rate)**:
  $$\mathbf{s}_t = \beta \mathbf{s}_{t-1} + (1 - \beta) (\nabla J_t \odot \nabla J_t), \quad \boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \frac{\eta}{\sqrt{\mathbf{s}_t + \epsilon}} \odot \nabla J_t$$
- **Adam (Adaptive Moment Estimation)**:
  $$\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \mathbf{g}_t, \quad \mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) \mathbf{g}_t^2$$
  $$\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}, \quad \boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \hat{\mathbf{m}}_t$$

---

## 6. Model Complexity, Bias-Variance Tradeoff & Polynomials

### 6.1 Polynomial Feature Expansion Combinatorics
Given $d$ base features expanded to degree $M$:
$$N_{\text{features}} = \binom{d + M}{M} = \frac{(d + M)!}{d! M!}$$

### 6.2 Mathematical Bias-Variance Decomposition of MSE
Let true target be $y = f(\mathbf{x}) + \epsilon$ with $\mathbb{E}[\epsilon] = 0$ and $\text{Var}(\epsilon) = \sigma_\epsilon^2$. The expected generalization test error for estimator $\hat{f}(\mathbf{x})$ is:
$$\mathbb{E}_{\mathcal{D}, \epsilon} \left[ (y - \hat{f}(\mathbf{x}))^2 \right] = \underbrace{\left( \mathbb{E}[\hat{f}(\mathbf{x})] - f(\mathbf{x}) \right)^2}_{\text{Bias}^2(\hat{f}(\mathbf{x}))} + \underbrace{\mathbb{E}\left[ (\hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}(\mathbf{x})])^2 \right]}_{\text{Variance}(\hat{f}(\mathbf{x}))} + \underbrace{\sigma_\epsilon^2}_{\text{Irreducible Error}}$$

```
  Error ▲
        │   Total Generalization Error
        │        \              /
        │         \   Optimal  /
        │          \     |    /
        │  Bias²    \__  |  _/      Variance
        │   \          \_●_/          /
        │    \___________|___________/
        │    Irreducible Noise (σ²)
        └─────────────────────────────────► Model Complexity (Degree d)
             High Bias               High Variance
            (Underfitting)           (Overfitting)
```

### 6.3 Model Selection & Regularized Complexity Criteria
- **Adjusted $R^2$**:
  $$\bar{R}^2 = 1 - (1 - R^2) \frac{n - 1}{n - p - 1}$$
  where $n$ is sample size and $p$ is the number of explanatory features (excluding intercept). Penalizes the addition of non-informative variables.
- **Akaike Information Criterion (AIC)**:
  $$\text{AIC} = n \ln\left(\frac{\text{SS}_{\text{res}}}{n}\right) + 2p$$
- **Bayesian Information Criterion (BIC)**:
  $$\text{BIC} = n \ln\left(\frac{\text{SS}_{\text{res}}}{n}\right) + p \ln(n)$$
  *Property*: BIC penalizes extra parameters more heavily than AIC ($p \ln n > 2p$ for $n \ge 8$).

---

## 7. Cross-Validation & Regularization: Ridge, Lasso & ElasticNet

### 7.1 Cross-Validation Estimates
- **$K$-Fold Cross-Validation Error**:
  $$\text{CV}_{(K)} = \frac{1}{K} \sum_{k=1}^K \text{MSE}_k$$
- **Stratified $K$-Fold**: Preserves the exact class proportion $p_c = \frac{n_c}{n}$ across every individual fold.

### 7.2 Regularized Objectives Comparison

| Model | Loss Objective $J(\mathbf{w})$ | Penalty Norm | Feature Selection | Analytical Solution |
| :--- | :--- | :--- | :--- | :--- |
| **OLS** | $\frac{1}{n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$ | None | No | $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1}\mathbf{X}^T \mathbf{y}$ |
| **Ridge ($L_2$)** | $\frac{1}{n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \sum_{j=1}^d w_j^2$ | $\|\mathbf{w}\|_2^2$ | No (shrinks $w_j \to 0$) | $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X} + n\lambda \mathbf{I})^{-1}\mathbf{X}^T \mathbf{y}$ |
| **Lasso ($L_1$)** | $\frac{1}{n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \sum_{j=1}^d \|w_j\|$ | $\|\mathbf{w}\|_1$ | **Yes** (forces $w_j = 0$) | No closed form (Coordinate Descent) |
| **ElasticNet** | $\frac{1}{n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda_1 \|\mathbf{w}\|_1 + \lambda_2 \|\mathbf{w}\|_2^2$ | Mix of $L_1$ and $L_2$ | **Yes** (handles collinear groups) | No closed form (Coordinate Descent) |

*(Note: The intercept $w_0$ is strictly excluded from regularization penalties!)*

### 7.3 Ridge Normal Equation & Invertibility
$$\mathbf{w}_{\text{Ridge}} = (\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$$
Even if $\mathbf{X}^T \mathbf{X}$ is rank-deficient ($\text{rank} < d$), adding $\lambda \mathbf{I}$ with $\lambda > 0$ shifts all eigenvalues by $+\lambda$:
$$\lambda_i(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}) = \lambda_i(\mathbf{X}^T \mathbf{X}) + \lambda > 0$$
ensuring the matrix is strictly non-singular and well-conditioned.

### 7.4 Lasso Subgradient & Soft-Thresholding Operator
For orthonormal design ($\mathbf{X}^T \mathbf{X} = \mathbf{I}$), Lasso has a closed-form coordinate solution via the **Soft-Thresholding Operator**:
$$w_j^* = \mathcal{S}_{\lambda}(w_j^{\text{OLS}}) = \text{sign}(w_j^{\text{OLS}}) \max\left(0, \; |w_j^{\text{OLS}}| - \frac{\lambda}{2}\right) = \begin{cases} w_j^{\text{OLS}} - \frac{\lambda}{2} & \text{if } w_j^{\text{OLS}} > \frac{\lambda}{2} \\ 0 & \text{if } |w_j^{\text{OLS}}| \le \frac{\lambda}{2} \\ w_j^{\text{OLS}} + \frac{\lambda}{2} & \text{if } w_j^{\text{OLS}} < -\frac{\lambda}{2} \end{cases}$$

```
    Lasso Soft-Thresholding (S_λ):              Ridge Linear Shrinkage:
          w* ▲                                        w* ▲
             │         /                                 │          /
             │        /                                  │         /  Slope = 1 / (1 + λ)
             │       /                                   │        /
      ───────┼──────•─────► w_OLS                 ───────┼───────/─────► w_OLS
            /│      λ/2                                 /│      /
           / │                                         / │     /
          /  │                                        /  │    /
```

### 7.5 ElasticNet Parametrization in Scikit-Learn
$$\mathcal{L}(\mathbf{w}) = \frac{1}{2n} \|\mathbf{y} - \mathbf{X}\mathbf{w}\|_2^2 + \alpha \cdot \left[ \rho \|\mathbf{w}\|_1 + \frac{1 - \rho}{2} \|\mathbf{w}\|_2^2 \right]$$
where $\alpha = \text{total penalty strength}$, and $\rho = \text{l1\_ratio} \in [0, 1]$.
- $\rho = 1 \implies \text{Pure Lasso}$.
- $\rho = 0 \implies \text{Pure Ridge}$.

---

## 8. Classification: Logistic Regression, Odds Ratios & Boundaries

### 8.1 The Logistic Sigmoid Function
$$\hat{p} = \sigma(z) = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}, \quad z \in \mathbb{R}, \; \hat{p} \in (0, 1)$$
- **Derivative Identity**:
  $$\frac{d\sigma(z)}{dz} = \sigma(z)(1 - \sigma(z)) = \hat{p}(1 - \hat{p})$$

### 8.2 Odds, Logit & Linear Score
- **Odds**:
  $$\text{Odds} = \frac{\hat{p}}{1 - \hat{p}} \in (0, \infty)$$
- **Log-Odds (Logit Transformation)**:
  $$\text{logit}(\hat{p}) = \ln\left(\frac{\hat{p}}{1 - \hat{p}}\right) = z = \mathbf{w}^T \mathbf{x} + w_0$$
  *Fundamental Interpretation*: Logistic regression is linear in the log-odds!
- **Inversion**:
  $$\hat{p} = \frac{\text{Odds}}{1 + \text{Odds}}$$

### 8.3 Binary Cross-Entropy / Log-Loss
For $n$ independent Bernoulli trials:
$$\mathcal{L}(\mathbf{w}, w_0) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \ln \hat{p}_i + (1 - y_i) \ln(1 - \hat{p}_i) \right]$$
- Single observation loss:
  $$\ell(y, \hat{p}) = \begin{cases} -\ln(\hat{p}) & \text{if } y = 1 \\ -\ln(1 - \hat{p}) & \text{if } y = 0 \end{cases}$$
- **Vectorized Gradient**:
  $$\nabla_{\mathbf{w}} \mathcal{L} = \frac{1}{n} \mathbf{X}^T (\hat{\mathbf{p}} - \mathbf{y}) \in \mathbb{R}^{d+1}$$
  *Notice*: Identical functional structure to OLS Gradient, but with $\hat{\mathbf{p}} = \sigma(\mathbf{X}\mathbf{w})$.

### 8.4 Odds Ratio (OR) Interpretation
For a unit increase in feature $x_j \to x_j + 1$:
$$\text{OR}_j = \frac{\text{Odds}(x_j + 1)}{\text{Odds}(x_j)} = \frac{e^{\mathbf{w}^T \mathbf{x} + w_j}}{e^{\mathbf{w}^T \mathbf{x}}} = e^{w_j}$$
- $\text{OR}_j > 1$ ($w_j > 0$): Multiplicative increase in odds by $(e^{w_j} - 1) \times 100\%$.
- $\text{OR}_j < 1$ ($w_j < 0$): Multiplicative decrease in odds by $(1 - e^{w_j}) \times 100\%$.

---

## 9. Classification Metrics, Threshold Tuning & Imbalance

### 9.1 Confusion Matrix Layout

```
                        ACTUAL CLASS
                     Positive (1)     Negative (0)
 PREDICTED   Pos (1)      TP              FP        ──► Precision = TP / (TP + FP)
   CLASS     Neg (0)      FN              TN        ──► NPV = TN / (TN + FN)
                          │               │
                          ▼               ▼
                       Recall        Specificity
                    TP / (TP + FN)  TN / (TN + FP)
```

### 9.2 Complete Metric Formulation Library
- **Accuracy**:
  $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
- **Error Rate**:
  $$\text{Error Rate} = 1 - \text{Accuracy} = \frac{FP + FN}{TP + TN + FP + FN}$$
- **Precision (Positive Predictive Value - PPV)**:
  $$\text{Precision} = \frac{TP}{TP + FP}$$
  *Goal*: Punishes False Positives (crucial in spam filtering, YouTube copyright strikes).
- **Recall / Sensitivity / True Positive Rate (TPR)**:
  $$\text{Recall} = \text{TPR} = \frac{TP}{TP + FN}$$
  *Goal*: Punishes False Negatives (crucial in cancer screening, fraud detection).
- **Specificity / Selectivity / True Negative Rate (TNR)**:
  $$\text{Specificity} = \text{TNR} = \frac{TN}{TN + FP}$$
- **False Positive Rate (FPR)**:
  $$\text{FPR} = \frac{FP}{TN + FP} = 1 - \text{Specificity}$$
- **$F_1$-Score (Harmonic Mean of Precision and Recall)**:
  $$F_1 = \frac{2}{\frac{1}{P} + \frac{1}{R}} = 2 \cdot \frac{P \cdot R}{P + R} = \frac{2 TP}{2 TP + FP + FN}$$
- **Generalized $F_\beta$-Score**:
  $$F_\beta = (1 + \beta^2) \frac{P \cdot R}{\beta^2 P + R} = \frac{(1 + \beta^2)TP}{(1 + \beta^2)TP + FP + \beta^2 FN}$$
  - $\beta = 2$: Recall weighted $2\times$ more than Precision ($F_2$).
  - $\beta = 0.5$: Precision weighted $2\times$ more than Recall ($F_{0.5}$).
- **Balanced Accuracy**:
  $$\text{Balanced Accuracy} = \frac{\text{TPR} + \text{TNR}}{2} = \frac{1}{2}\left(\frac{TP}{TP + FN} + \frac{TN}{TN + FP}\right)$$

### 9.3 Decision Threshold Mechanics & Cost Matrices
Standard default threshold is $\tau = 0.5$ ($\hat{y} = 1 \iff \hat{p} \ge \tau$).
- **Raising threshold ($\tau > 0.5$)**: Model becomes conservative. Fewer positives flagged $\implies \text{Precision} \uparrow, \; \text{Recall} \downarrow$.
- **Lowering threshold ($\tau < 0.5$)**: Model flags aggressively. More positives flagged $\implies \text{Recall} \uparrow, \; \text{Precision} \downarrow$.

### 9.4 Business Cost-Benefit Optimization
Given business cost matrix ($C_{FP}, C_{FN}, C_{TP}, C_{TN}$):
$$\text{Expected Business Cost} = C_{FP} \cdot FP + C_{FN} \cdot FN + C_{TP} \cdot TP + C_{TN} \cdot TN$$
Optimal theoretical Bayes decision threshold:
$$\tau^* = \frac{C_{FP} - C_{TN}}{(C_{FP} - C_{TN}) + (C_{FN} - C_{TP})}$$

### 9.5 Class Imbalance Weighting Formula
Scikit-Learn's `class_weight='balanced'` formula:
$$w_c = \frac{n}{K \cdot n_c}$$
where $n = \text{total samples}$, $K = \text{number of classes}$, and $n_c = \text{count of class } c$.
- Weighted Loss Function:
  $$\mathcal{L}_{\text{balanced}}(\mathbf{w}) = -\frac{1}{n}\sum_{i=1}^n w_{y_i} \left[ y_i \ln \hat{p}_i + (1 - y_i)\ln(1 - \hat{p}_i) \right]$$

---

## 10. Instance-Based Learning: $k$-Nearest Neighbours

### 10.1 Distance Metric Foundations

| Metric | Mathematical Formula | Geometric Meaning |
| :--- | :--- | :--- |
| **Minkowski Distance ($L_p$)** | $D_p(\mathbf{x}, \mathbf{z}) = \left(\sum_{j=1}^d |x_j - z_j|^p\right)^{1/p}$ | Generalized metric space norm |
| **Manhattan Distance ($L_1$, $p=1$)** | $D_1(\mathbf{x}, \mathbf{z}) = \sum_{j=1}^d |x_j - z_j|$ | Grid / City-block distance; less sensitive to high-dim outliers |
| **Euclidean Distance ($L_2$, $p=2$)** | $D_2(\mathbf{x}, \mathbf{z}) = \sqrt{\sum_{j=1}^d (x_j - z_j)^2}$ | Straight-line distance; isotropic |
| **Chebyshev Distance ($L_\infty$)** | $D_\infty(\mathbf{x}, \mathbf{z}) = \max_{j} |x_j - z_j|$ | Maximum single coordinate difference |
| **Cosine Distance** | $D_{\text{cos}}(\mathbf{x}, \mathbf{z}) = 1 - \frac{\mathbf{x} \cdot \mathbf{z}}{\|\mathbf{x}\|_2 \|\mathbf{z}\|_2}$ | Measures angular orientation regardless of magnitude |
| **Hamming Distance** | $D_H(\mathbf{x}, \mathbf{z}) = \frac{1}{d}\sum_{j=1}^d \mathbb{I}(x_j \ne z_j)$ | Fraction of mismatched categorical / binary attributes |

### 10.2 $k$-NN Decision Rules
Let $\mathcal{N}_k(\mathbf{x})$ be the set of $k$ closest training points to query $\mathbf{x}$.
- **Classification (Majority Vote)**:
  $$\hat{y} = \arg\max_{c} \sum_{i \in \mathcal{N}_k(\mathbf{x})} \mathbb{I}(y_i = c)$$
- **Regression (Arithmetic Mean)**:
  $$\hat{y} = \frac{1}{k} \sum_{i \in \mathcal{N}_k(\mathbf{x})} y_i$$
- **Distance-Weighted Regression**:
  $$\hat{y} = \frac{\sum_{i \in \mathcal{N}_k(\mathbf{x})} w_i y_i}{\sum_{i \in \mathcal{N}_k(\mathbf{x})} w_i}, \quad \text{where } w_i = \frac{1}{d(\mathbf{x}, \mathbf{x}_i) + \epsilon}$$

### 10.3 Bias-Variance Profile as a Function of $k$
- **$k = 1$**: Training error $= 0.0$ (memorizes noise). Complex, jagged Voronoi boundaries $\implies$ **Low Bias, Extreme Variance** (Overfitting).
- **$k = n$**: Predicts global majority / overall target mean. Flat, rigid boundary $\implies$ **High Bias, Zero Variance** (Underfitting).

---

## 11. Tree-Based Models: Decision Trees (CART, ID3, C4.5)

### 11.1 Impurity Metrics

```
 Impurity ▲
      1.0 ┼               Shannon Entropy H(p)
      0.8 ┼             /           \
      0.5 ┼ - - - - - - ● Gini G(p) - ● - - - - -
      0.0 ┴─────────────┴───────────┴───────────► p (Class Proportion)
         0.0           0.5         1.0
```

1. **Shannon Entropy (ID3)**:
   $$H(S) = -\sum_{k=1}^K p_k \log_2(p_k)$$
   - Pure node ($p_1 = 1$): $H(S) = 0$ bits.
   - Uniform binary node ($p_1 = p_2 = 0.5$): $H(S) = -\left(\frac{1}{2}\log_2\frac{1}{2} + \frac{1}{2}\log_2\frac{1}{2}\right) = 1.0$ bit.
2. **Gini Impurity (CART)**:
   $$G(S) = 1 - \sum_{k=1}^K p_k^2 = \sum_{k=1}^K p_k (1 - p_k)$$
   - Binary classification shortcut ($p_1 = p, p_2 = 1 - p$):
     $$G_{\text{binary}}(p) = 1 - (p^2 + (1 - p)^2) = 2p(1 - p)$$
   - Pure node: $G = 0$.
   - Uniform binary node: $G = 2(0.5)(0.5) = 0.50$.
   - Theoretical maximum for $K$ classes: $1 - \frac{1}{K}$.

### 11.2 Split Evaluation Criteria
- **Information Gain (ID3)**:
  $$IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
- **Gain Ratio (C4.5)**:
  $$\text{GainRatio}(S, A) = \frac{IG(S, A)}{\text{SplitInfo}_A(S)}, \quad \text{where } \text{SplitInfo}_A(S) = -\sum_{v} \frac{|S_v|}{|S|} \log_2\left(\frac{|S_v|}{|S|}\right)$$
- **Gini Gain (CART)**:
  $$\Delta G(S, A) = G(S) - \left[ \frac{|S_L|}{|S|} G(S_L) + \frac{|S_R|}{|S|} G(S_R) \right]$$
- **Variance Reduction (Regression Trees)**:
  $$\Delta \text{Var}(S, A) = \text{Var}(S) - \left[ \frac{|S_L|}{|S|} \text{Var}(S_L) + \frac{|S_R|}{|S|} \text{Var}(S_R) \right]$$
  Terminal leaf prediction: $\hat{c}_m = \bar{y}_{R_m} = \frac{1}{N_m}\sum_{i \in R_m} y_i$.

### 11.3 Cost-Complexity Post-Pruning (Breiman's Minimal Pruning)
Regularized cost objective over subtree $T \subseteq T_0$:
$$R_\alpha(T) = R(T) + \alpha |T|$$
where $R(T)$ is total leaf error/impurity, $|T|$ is the number of terminal leaves, and $\alpha \ge 0$ is the complexity tuning parameter.
- Effective alpha for internal node $t$:
  $$g(t) = \frac{R(t) - R(T_t)}{|T_t| - 1}$$
  The weakest link (smallest $g(t)$) is collapsed first into a single leaf as $\alpha$ increases.

### 11.4 Mean Decrease in Impurity (MDI / Gini Importance)
$$\text{Importance}(X_j) = \sum_{t \text{ splits on } X_j} \frac{N_t}{N} \Delta I(t)$$
*Vulnerability*: MDI strongly biases toward high-cardinality continuous features over low-cardinality binary features.

---

## 12. Ensemble Methods: Bagging, Random Forests & Boosting

### 12.1 Condorcet's Jury Theorem
For an ensemble of $B$ independent binary classifiers, each with individual accuracy $p > 0.5$, majority voting error approaches zero as $B \to \infty$:
$$P(\text{Majority Correct}) = \sum_{k=\lfloor B/2 \rfloor + 1}^B \binom{B}{k} p^k (1 - p)^{B - k} \xrightarrow[B \to \infty]{} 1.0$$

### 12.2 Bootstrap Aggregation (Bagging) & Out-of-Bag (OOB) Math
Given $n$ samples drawn with replacement:
$$P(\text{Sample } i \text{ NOT selected in } 1 \text{ draw}) = 1 - \frac{1}{n}$$
$$P(\text{Sample } i \text{ NOT selected in } n \text{ draws}) = \left(1 - \frac{1}{n}\right)^n \xrightarrow[n \to \infty]{} e^{-1} \approx 0.3679 \approx 36.8\%$$
- **In-Bag Expected Proportion**: $1 - e^{-1} \approx 63.2\%$.
- **Out-of-Bag Expected Proportion**: $e^{-1} \approx 36.8\%$.
- **OOB Generalization Error**: Evaluates each observation $\mathbf{x}_i$ using strictly those base trees where $\mathbf{x}_i$ was out-of-bag (providing an unbiased cross-validation score without separate splits).

### 12.3 Variance of Correlated Estimators (Random Forest Decorrelation)
Let $B$ trees each have individual variance $\sigma^2$ and pairwise correlation $\rho = \text{Corr}(T_i, T_j)$:
$$\text{Var}\left(\frac{1}{B}\sum_{b=1}^B T_b\right) = \rho \sigma^2 + \frac{1 - \rho}{B}\sigma^2$$
- As $B \to \infty$, the second term drops to 0, leaving the irreducible lower bound $\rho \sigma^2$.
- **Random Forest Fix**: Feature subsampling ($m = \sqrt{p}$ for classification, $m = p/3$ for regression) forces trees to split on different attributes, drastically reducing $\rho$, thus lowering total ensemble variance.

### 12.4 AdaBoost (Adaptive Boosting) Equations
Target $y_i \in \{-1, +1\}$, initial sample weights $w_i^{(1)} = \frac{1}{n}$.

1. **Weighted Error Rate of Weak Learner $h_t$**:
   $$\epsilon_t = \frac{\sum_{i=1}^n w_i^{(t)} \mathbb{I}(y_i \ne h_t(\mathbf{x}_i))}{\sum_{i=1}^n w_i^{(t)}}$$
2. **Learner Stage Weight ($\alpha_t$)**:
   $$\alpha_t = \frac{1}{2} \ln\left(\frac{1 - \epsilon_t}{\epsilon_t}\right)$$
   - If $\epsilon_t = 0.5$ (random guess): $\alpha_t = 0$.
   - If $\epsilon_t \to 0$ (perfect learner): $\alpha_t \to +\infty$.
3. **Sample Distribution Weight Update**:
   $$w_i^{(t+1)} = \frac{w_i^{(t)} \exp\left(-\alpha_t y_i h_t(\mathbf{x}_i)\right)}{Z_t}$$
   where normalization factor $Z_t = 2\sqrt{\epsilon_t(1 - \epsilon_t)}$.
4. **Final Ensemble Decision**:
   $$H(\mathbf{x}) = \text{sign}\left(\sum_{t=1}^T \alpha_t h_t(\mathbf{x})\right)$$

### 12.5 Gradient Boosting Machine (GBM) in Function Space
Initialize with optimal constant: $f_0(\mathbf{x}) = \arg\min_c \sum_{i=1}^n \mathcal{L}(y_i, c)$.
For iterations $m = 1$ to $M$:
1. **Compute Pseudo-Residuals (Negative Gradients)**:
   $$r_{im} = -\left[ \frac{\partial \mathcal{L}(y_i, f(\mathbf{x}_i))}{\partial f(\mathbf{x}_i)} \right]_{f = f_{m-1}}$$
   - For MSE Loss $\frac{1}{2}(y - f)^2$: $r_{im} = y_i - f_{m-1}(\mathbf{x}_i)$ (exact ordinary residuals).
   - For Log-Loss $-[y\ln p + (1-y)\ln(1-p)]$: $r_{im} = y_i - p_{m-1}(\mathbf{x}_i)$.
2. **Fit base tree $h_m(\mathbf{x})$ to targets $r_{im}$**.
3. **Ensemble Update with Shrinkage / Learning Rate ($\eta$)**:
   $$f_m(\mathbf{x}) = f_{m-1}(\mathbf{x}) + \eta \gamma_m h_m(\mathbf{x}), \quad \eta \in (0, 0.2]$$

### 12.6 XGBoost 2nd-Order Taylor Expansion Math
For tree $t$, let $g_i = \partial_{\hat{y}} \mathcal{L}(y_i, \hat{y}^{(t-1)})$ and $h_i = \partial_{\hat{y}}^2 \mathcal{L}(y_i, \hat{y}^{(t-1)})$.
Objective function with leaf complexity penalty:
$$\mathcal{L}^{(t)} \approx \sum_{j=1}^T \left[ G_j w_j + \frac{1}{2}(H_j + \lambda) w_j^2 \right] + \gamma T$$
where $G_j = \sum_{i \in I_j} g_i$ and $H_j = \sum_{i \in I_j} h_i$.
- **Optimal Closed-Form Leaf Weight**:
  $$w_j^* = -\frac{G_j}{H_j + \lambda}$$
- **Optimal Split Gain**:
  $$\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$
  Splits are pruned if $\text{Gain} < 0$.

---

## 13. Kernel Methods & Support Vector Machines (SVM)

### 13.1 Margins & Structural Risk
- **Functional Margin**: $\hat{\gamma}_i = y_i (\mathbf{w}^T \mathbf{x}_i + b)$.
- **Geometric Margin**: $\gamma_i = \frac{\hat{\gamma}_i}{\|\mathbf{w}\|_2} = y_i \left( \frac{\mathbf{w}^T \mathbf{x}_i}{\|\mathbf{w}\|_2} + \frac{b}{\|\mathbf{w}\|_2} \right)$.
- **Total Margin Width between Bounding Hyperplanes**:
  $$\text{Width} = \frac{2}{\|\mathbf{w}\|_2}$$

### 13.2 Optimization Formulations
- **Hard Margin Primal QP**:
  $$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|_2^2 \quad \text{s.t.} \quad y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 \quad \forall i$$
- **Soft Margin Primal QP (Slack Variables $\xi_i$)**:
  $$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|_2^2 + C \sum_{i=1}^n \xi_i \quad \text{s.t.} \quad y_i(\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$
  - $C \to \infty$: Recovers strict Hard Margin (narrow margin, high variance).
  - $C \to 0$: High slack tolerance (wide margin, high bias).
- **Hinge Loss Representation**:
  $$\min_{\mathbf{w}, b} \left[ \frac{1}{2}\|\mathbf{w}\|_2^2 + C \sum_{i=1}^n \max\left(0, \; 1 - y_i(\mathbf{w}^T \mathbf{x}_i + b)\right) \right]$$

### 13.3 KKT Conditions & Wolfe Dual
Construct Lagrangian: $\mathcal{L}(\mathbf{w}, b, \boldsymbol{\xi}, \boldsymbol{\alpha}, \boldsymbol{\mu}) = \frac{1}{2}\|\mathbf{w}\|^2 + C\sum\xi_i - \sum\alpha_i [y_i(\mathbf{w}^T\mathbf{x}_i+b) - 1 + \xi_i] - \sum\mu_i \xi_i$.
Setting derivatives to zero yields: $\mathbf{w} = \sum_{i=1}^n \alpha_i y_i \mathbf{x}_i$ and $\sum \alpha_i y_i = 0$.

- **Wolfe Dual Problem**:
  $$\max_{\boldsymbol{\alpha}} \sum_{i=1}^n \alpha_i - \frac{1}{2}\sum_{i=1}^n \sum_{j=1}^n \alpha_i \alpha_j y_i y_j \langle \mathbf{x}_i, \mathbf{x}_j \rangle \quad \text{s.t.} \quad 0 \le \alpha_i \le C, \quad \sum_{i=1}^n \alpha_i y_i = 0$$
- **KKT Complementary Slackness**:
  $$\alpha_i \left[ y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1 + \xi_i \right] = 0$$
  - $\alpha_i = 0$: Point is outside the margin ($y_i f(\mathbf{x}_i) > 1$). Exerts **zero** influence on the decision boundary.
  - $0 < \alpha_i < C$: **Margin Support Vector**. Lies exactly on the canonical margin hyperplanes ($y_i f(\mathbf{x}_i) = 1, \xi_i = 0$). Used to calculate bias $b^*$:
    $$b^* = y_s - \sum_{i \in SV} \alpha_i y_i K(\mathbf{x}_i, \mathbf{x}_s)$$
  - $\alpha_i = C$: **Non-Margin Support Vector**. Point violates the margin ($\xi_i > 0$).

### 13.4 The Kernel Trick & Mercer Kernels
Data appears exclusively via dot products $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$. Replace with a Mercer kernel $K(\mathbf{x}_i, \mathbf{x}_j) = \langle \phi(\mathbf{x}_i), \phi(\mathbf{x}_j) \rangle$:

1. **Linear**: $K(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$
2. **Polynomial**: $K(\mathbf{x}, \mathbf{z}) = (\gamma \mathbf{x}^T \mathbf{z} + r)^d$
3. **Gaussian Radial Basis Function (RBF)**:
   $$K(\mathbf{x}, \mathbf{z}) = \exp\left(-\gamma \|\mathbf{x} - \mathbf{z}\|_2^2\right) = \exp\left(-\frac{\|\mathbf{x} - \mathbf{z}\|_2^2}{2\sigma^2}\right)$$
   - Projects data into an **infinite-dimensional** Hilbert space.
   - Large $\gamma \implies$ tight, localized Gaussian bells $\implies$ severe overfitting.
   - Small $\gamma \implies$ broad Gaussian bells $\implies$ underfitting.

### 13.5 Support Vector Regression (SVR)
Vapnik's $\epsilon$-insensitive loss function:
$$\mathcal{L}_\epsilon(y, f(\mathbf{x})) = \max(0, \; |y - f(\mathbf{x})| - \epsilon)$$
Errors smaller than $\epsilon$ incur zero penalty, creating a sparse dual solution.

---

## 14. Probabilistic Classifiers: Naive Bayes

### 14.1 Generative vs Discriminative Modeling
- **Discriminative (Logistic Regression, SVM)**: Directly models $P(Y \mid \mathbf{X})$.
- **Generative (Naive Bayes, GMM)**: Models joint distribution $P(\mathbf{X}, Y) = P(\mathbf{X} \mid Y)P(Y)$.

### 14.2 Bayes' Theorem Decomposition
$$P(Y = k \mid \mathbf{X} = \mathbf{x}) = \frac{P(\mathbf{X} = \mathbf{x} \mid Y = k) \cdot P(Y = k)}{P(\mathbf{X} = \mathbf{x})} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}$$
$$\text{Evidence}: P(\mathbf{X} = \mathbf{x}) = \sum_{j=1}^K P(\mathbf{X} = \mathbf{x} \mid Y = j) P(Y = j)$$

### 14.3 The Naive Conditional Independence Assumption
$$P(\mathbf{X} \mid Y = k) = \prod_{j=1}^d P(X_j \mid Y = k)$$
Reduces parameter complexity from exponential $\mathcal{O}(K \cdot 2^d)$ to linear $\mathcal{O}(K \cdot d)$.

### 14.4 Maximum A Posteriori (MAP) Classification Rule
Since evidence $P(\mathbf{X})$ is constant for all candidate classes $k$:
$$\hat{y} = \arg\max_{k \in \{1, \dots, K\}} \left[ P(Y = k) \prod_{j=1}^d P(x_j \mid Y = k) \right]$$
In production, to eliminate floating-point underflow:
$$\hat{y} = \arg\max_{k \in \{1, \dots, K\}} \left[ \ln P(Y = k) + \sum_{j=1}^d \ln P(x_j \mid Y = k) \right]$$

### 14.5 Additive Smoothing (Zero Probability Resolution)
- **Laplace Smoothing ($\alpha = 1$)**:
  $$\hat{P}(x_j = w \mid Y = k) = \frac{N_{w, k} + 1}{N_k + V}$$
  where $N_{w, k}$ is the count of feature $w$ in class $k$, $N_k$ is total token count, and $V$ is vocabulary size.
- **Lidstone Smoothing ($0 < \alpha < 1$)**:
  $$\hat{P}(x_j = w \mid Y = k) = \frac{N_{w, k} + \alpha}{N_k + \alpha V}$$

### 14.6 Naive Bayes Likelihood Variants
1. **Gaussian Naive Bayes (Continuous Features)**:
   $$P(x_j \mid Y = k) = \frac{1}{\sqrt{2\pi \sigma_{jk}^2}} \exp\left( -\frac{(x_j - \mu_{jk})^2}{2\sigma_{jk}^2} \right)$$
2. **Multinomial Naive Bayes (Word Count Vectors)**:
   $$P(\mathbf{x} \mid Y = k) = \frac{(\sum x_j)!}{\prod x_j!} \prod_{j=1}^d p_{jk}^{x_j}$$
3. **Bernoulli Naive Bayes (Binary 0/1 Indicators)**:
   $$P(\mathbf{x} \mid Y = k) = \prod_{j=1}^d \left[ p_{jk}^{x_j} (1 - p_{jk})^{1 - x_j} \right]$$

---

## 15. Unsupervised Learning & Dimensionality Reduction

### 15.1 K-Means Objective (WCSS / Inertia)
$$J(\mathbf{C}, \boldsymbol{\mu}) = \sum_{k=1}^K \sum_{\mathbf{x}_i \in C_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2$$
- **Lloyd's Algorithm Coordinate Descent**:
  - *E-Step (Assignment)*: $r_{ik} = \mathbb{I}\left(k = \arg\min_j \|\mathbf{x}_i - \boldsymbol{\mu}_j\|_2^2\right)$
  - *M-Step (Centroid Update)*: $\boldsymbol{\mu}_k = \frac{\sum_{i=1}^n r_{ik}\mathbf{x}_i}{\sum_{i=1}^n r_{ik}} = \frac{1}{|C_k|} \sum_{\mathbf{x}_i \in C_k} \mathbf{x}_i$
- **K-Means++ Initialization Sampling Probability**:
  $$P(\mathbf{x}_i) = \frac{D(\mathbf{x}_i)^2}{\sum_{j=1}^n D(\mathbf{x}_j)^2}$$
  where $D(\mathbf{x}) = \min_{j < k} \|\mathbf{x} - \boldsymbol{\mu}_j\|_2$. Bound: $\mathbb{E}[J] \le 8(\ln K + 2)J_{\text{opt}}$.

### 15.2 Silhouette Analysis
For point $\mathbf{x}_i \in C_I$:
- Cohesion: $a(i) = \frac{1}{|C_I| - 1} \sum_{j \in C_I, j \ne i} \|\mathbf{x}_i - \mathbf{x}_j\|_2$
- Separation: $b(i) = \min_{J \ne I} \frac{1}{|C_J|} \sum_{j \in C_J} \|\mathbf{x}_i - \mathbf{x}_j\|_2$
- Silhouette Score:
  $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} \in [-1, +1]$$

### 15.3 Hierarchical Agglomerative Clustering Linkages
- Single: $d_{\text{min}}(A, B) = \min_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$
- Complete: $d_{\text{max}}(A, B) = \max_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$
- Average: $d_{\text{avg}}(A, B) = \frac{1}{|A||B|} \sum_{\mathbf{a} \in A} \sum_{\mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$
- Ward's Minimum Variance:
  $$\Delta J(A, B) = \frac{|A||B|}{|A| + |B|} \|\boldsymbol{\mu}_A - \boldsymbol{\mu}_B\|_2^2$$

### 15.4 DBSCAN Density Connectivity
- $\epsilon$-Neighborhood: $N_\epsilon(\mathbf{p}) = \{\mathbf{q} \in \mathcal{D} \mid \|\mathbf{p} - \mathbf{q}\|_2 \le \epsilon\}$.
- **Core Point**: $|N_\epsilon(\mathbf{p})| \ge \text{MinPts}$.
- **Border Point**: $|N_\epsilon(\mathbf{p})| < \text{MinPts}$ but $\mathbf{p} \in N_\epsilon(\mathbf{q})$ for some Core point $\mathbf{q}$.
- **Noise Point**: Neither Core nor Border (label $-1$).

### 15.5 Principal Component Analysis (PCA)
Let $\mathbf{X}_c = \mathbf{X} - \bar{\mathbf{X}} \in \mathbb{R}^{n \times d}$ be zero-centered.
Sample Covariance Matrix:
$$\mathbf{\Sigma} = \frac{1}{n - 1}\mathbf{X}_c^T \mathbf{X}_c \in \mathbb{R}^{d \times d}$$
- **Variance Maximization Lagrangian**:
  $$\mathcal{L}(\mathbf{v}, \lambda) = \mathbf{v}^T \mathbf{\Sigma} \mathbf{v} - \lambda(\mathbf{v}^T \mathbf{v} - 1) \implies \mathbf{\Sigma}\mathbf{v} = \lambda \mathbf{v}$$
  The optimal projection directions are the eigenvectors of $\mathbf{\Sigma}$, and projection variance equals eigenvalue $\lambda$.
- **Singular Value Decomposition (SVD)**:
  $$\mathbf{X}_c = \mathbf{U} \mathbf{S} \mathbf{V}^T \implies \mathbf{\Sigma} = \mathbf{V}\left(\frac{\mathbf{S}^2}{n - 1}\right)\mathbf{V}^T \implies \lambda_j = \frac{s_j^2}{n - 1}$$
- **Explained Variance Ratio (EVR)**:
  $$\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^d \lambda_j} = \frac{s_k^2}{\sum_{j=1}^d s_j^2}$$
- **Standardized Bivariate PCA Shortcut**:
  For two standardized variables with correlation $r$:
  $$\mathbf{\Sigma} = \begin{pmatrix} 1 & r \\ r & 1 \end{pmatrix} \implies \lambda_1 = 1 + r, \; \lambda_2 = 1 - r \implies \text{EVR}_1 = \frac{1 + r}{2}$$
- **PCA Image Compression Storage Count**:
  $$\text{Numbers to Store} = n \cdot k + k \cdot d + d$$
  where $n \cdot k$ is projected latent representations, $k \cdot d$ is the $k$ eigenvector components, and $d$ is the mean image vector.
  $$\text{Compression Ratio} = \frac{n \cdot d}{n \cdot k + k \cdot d + d}$$

---

## 16. Formulas & Step-by-Step Worked Problems from SST End-Term Practice Sheet (Group B)

This section maps every problem from the Scaler School of Technology End-Term Practice Sheet (Group B) to its governing mathematical formula, detailing the exact arithmetic and answer-key verification.

### Section A: Multiple Choice Questions (A1 to A20)

---

#### A1. Mitchell's ETP Formulation
- **Formula**: Learning implies: Performance $\mathcal{P}$ on Task $\mathcal{T}$ improves with Experience $\mathcal{E}$.
- **Application**:
  - $\mathcal{T} = \text{Flag loan applications likely to default}$
  - $\mathcal{E} = \text{Past loan applications with known outcomes (historical labeled data)}$
  - $\mathcal{P} = \text{Recall on new quarterly applications}$
- **Correct Option**: **C**

---

#### A2. Ordinal Encoding Category Order
- **Formula**: Default Scikit-Learn `OrdinalEncoder()` applies alphabetical sorting:
  $$\text{Alphabetical}: \{\text{'High'}: 0, \; \text{'Low'}: 1, \; \text{'Medium'}: 2\}$$
- **Correction**: Must explicitly specify ordinal hierarchy:
  $$\text{categories} = [[\text{"Low"}, \text{"Medium"}, \text{"High"}]] \implies \{\text{'Low'}: 0, \; \text{'Medium'}: 1, \; \text{'High'}: 2\}$$
- **Correct Option**: **B**

---

#### A3. Temporal Data Leakage & Feature Windows
- **Formula**: Backward-looking causal feature condition for time $t$:
  $$x_t = f(\{y_{t-1}, y_{t-2}, \dots, y_{t-k}\}) \quad \text{strictly; } y_{t+1}, y_{t+2} \notin x_t$$
- **Issue**: A 7-day centered window uses $y_{t-3}$ to $y_{t+3}$, leaking future targets into current features. Shuffling destroys time ordering.
- **Fix**: Split chronologically (train on past, test on future) and use strictly backward-looking lag windows.
- **Correct Option**: **D**

---

#### A4. Numerical MAE & RMSE Calculation
- **Given**: $y = [3, 5, 8, 10]$, $\hat{y} = [4, 5, 6, 13]$, $n = 4$.
- **Residual Errors**:
  $$e_i = \hat{y}_i - y_i \implies [4-3, \; 5-5, \; 6-8, \; 13-10] = [1, \; 0, \; -2, \; 3]$$
- **MAE Step**:
  $$\text{MAE} = \frac{1}{n}\sum_{i=1}^n |e_i| = \frac{|1| + |0| + |-2| + |3|}{4} = \frac{1 + 0 + 2 + 3}{4} = \frac{6}{4} = 1.50$$
- **MSE & RMSE Step**:
  $$\text{MSE} = \frac{1}{n}\sum_{i=1}^n e_i^2 = \frac{1^2 + 0^2 + (-2)^2 + 3^2}{4} = \frac{1 + 0 + 4 + 9}{4} = \frac{14}{4} = 3.50$$
  $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{3.50} \approx 1.8708 \approx 1.87$$
- **Correct Option**: **A** ($\text{MAE} = 1.50, \text{RMSE} \approx 1.87$)

---

#### A5. Normal Equation Singularity & Collinearity
- **Formula**: $\boldsymbol{\theta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$.
- **Condition**: $\text{height\_inches} = \frac{\text{height\_cm}}{2.54}$.
- **Consequence**: Two columns are exact scalar multiples $\implies \text{rank}(\mathbf{X}) < d + 1 \implies \det(\mathbf{X}^T \mathbf{X}) = 0 \implies \mathbf{X}^T \mathbf{X}$ is singular (non-invertible).
- **Remedy**: Drop one collinear feature, or apply Ridge regularization ($\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I}$).
- **Correct Option**: **C**

---

#### A6. Residual Diagnostics: Non-Linearity Curvature
- **Formula**: $\mathbb{E}[e \mid \hat{y}] = 0$ must hold across all $\hat{y}$.
- **Pattern**: Residuals vs Fitted has a "U-shape" (positive at ends, negative in center).
- **Diagnosis**: Mean of residuals is non-zero and curved $\implies$ Linearity assumption is violated.
- **Fix**: Add polynomial or non-linear term ($x^2$).
- **Correct Option**: **B**

---

#### A7. Two Steps of Scalar Gradient Descent
- **Given**: $J(w) = (w - 3)^2$, $\frac{dJ}{dw} = 2(w - 3)$, $\eta = 0.1$, $w_0 = 0$.
- **Step 1**:
  $$\nabla J(w_0) = 2(0 - 3) = -6$$
  $$w_1 = w_0 - \eta \nabla J(w_0) = 0 - 0.1(-6) = 0 + 0.60 = 0.60$$
- **Step 2**:
  $$\nabla J(w_1) = 2(0.60 - 3) = 2(-2.40) = -4.80$$
  $$w_2 = w_1 - \eta \nabla J(w_1) = 0.60 - 0.1(-4.80) = 0.60 + 0.48 = 1.08$$
- **Correct Option**: **B** ($1.08$)

---

#### A8. Model Selection via Validation MSE
- **Data**:
  - Degree 1: Train MSE $= 38.2$, Val MSE $= 40.1$ (Underfitting, high bias)
  - Degree 3: Train MSE $= 11.6$, Val MSE $= 13.0$
  - Degree 6: Train MSE $= 9.8$, Val MSE $= \mathbf{12.4}$ (**Minimum validation error**)
  - Degree 12: Train MSE $= 1.9$, Val MSE $= 55.7$ (Overfitting, severe variance)
- **Principle**: Model selection must minimize validation error on unseen data.
- **Correct Option**: **D** (Degree 6)

---

#### A9. Ridge Penalty Scaling Dynamics
- **Objective**: $\mathcal{L}_{\text{Ridge}} = \text{MSE} + \lambda \sum w_j^2$.
- **Effect of $\lambda \to 1000$**:
  - Heavily penalizes weights: $w_j \to 0$.
  - Fits flat line through data $\implies$ Training MSE rises monotonically; model underfits.
- **Correct Option**: **C**

---

#### A10. Why Scale Features Before Regularization
- **Formula**: Penalty $\lambda \sum_{j=1}^d w_j^2$ applies equal penalty to all $w_j$.
- **Scale Impact**: An unscaled feature with large units (e.g. salary in rupees: $1,000,000$) requires a tiny coefficient ($w_j \approx 0.0001$), escaping penalty. A feature in small units (e.g. age: $0.25$) requires a large coefficient and is penalized disproportionately.
- **Correct Option**: **A**

---

#### A11. Logistic Score, Sigmoid & Threshold Classification
- **Given**: $\mathbf{w} = [2, -1]^T, w_0 = -1, \mathbf{x} = [1.5, 1]^T$.
- **Linear Score ($z$)**:
  $$z = \mathbf{w}^T \mathbf{x} + w_0 = (2)(1.5) + (-1)(1) + (-1) = 3.0 - 1.0 - 1.0 = 1.0$$
- **Sigmoid Output ($\hat{p}$)**:
  $$\hat{p} = \sigma(1) = \frac{1}{1 + e^{-1}} = \frac{1}{1 + 0.36788} = \frac{1}{1.36788} \approx 0.7311 \approx 0.73$$
- **Decision at $\tau = 0.5$**: Since $\hat{p} = 0.73 \ge 0.5 \implies \text{Class } 1$.
- **Correct Option**: **D** ($z = 1, \hat{p} \approx 0.73, \text{predict } 1$)

---

#### A12. Spam Filtering & Decision Threshold Shifting
- **Problem**: False Positives (legitimate email sent to spam) are disastrous.
- **Metric**: Precision $= \frac{TP}{TP + FP}$. Punishes False Positives.
- **Action**: Raise decision threshold $\tau$ (e.g., to $0.8$ or $0.9$) so only high-confidence spam is moved to junk.
- **Correct Option**: **A**

---

#### A13. Maximum Log-Loss Evaluation
- **Formula**: For true $y = 1$:
  $$\ell = -\ln(\hat{p})$$
- **Values**:
  - $\hat{p} = 0.99 \implies \ell = -\ln(0.99) \approx 0.010$
  - $\hat{p} = 0.60 \implies \ell = -\ln(0.60) \approx 0.511$
  - $\hat{p} = 0.50 \implies \ell = -\ln(0.50) \approx 0.693$
  - $\hat{p} = 0.05 \implies \ell = -\ln(0.05) \approx 2.996 \approx 3.00$
- **Conclusion**: Confident wrong predictions ($\hat{p} \to 0$ when $y = 1$) incur massive log-loss penalty.
- **Correct Option**: **D** ($\hat{p} = 0.05$)

---

#### A14. $k$-NN Regression Query
- **Given**: $k = 2$, Query $\mathbf{q} = (3, 3)$.
- **Squared Euclidean Distances**:
  - $(1, 1) \to (3-1)^2 + (3-1)^2 = 4 + 4 = 8$
  - $(2, 4) \to (3-2)^2 + (3-4)^2 = 1 + 1 = 2 \quad (y = 18)$
  - $(4, 2) \to (3-4)^2 + (3-2)^2 = 1 + 1 = 2 \quad (y = 14)$
  - $(5, 5) \to (3-5)^2 + (3-5)^2 = 4 + 4 = 8$
  - $(7, 1) \to (3-7)^2 + (3-1)^2 = 16 + 4 = 20$
- **Two Closest Neighbors**: $(2, 4)$ with $y = 18$ and $(4, 2)$ with $y = 14$.
- **Prediction**:
  $$\hat{y} = \frac{18 + 14}{2} = \frac{32}{2} = 16.00$$
- **Correct Option**: **C** ($16.00$)

---

#### A15. Decision Tree Gini Impurity Identification
- **Formula**: $\text{Gini} = 1 - (p_A^2 + p_B^2) = 2p(1 - p)$.
- **Testing 8 Class A, 2 Class B**:
  $$p = \frac{8}{10} = 0.8, \quad 1 - p = \frac{2}{10} = 0.2$$
  $$\text{Gini} = 1 - (0.8^2 + 0.2^2) = 1 - (0.64 + 0.04) = 1 - 0.68 = 0.32$$
  Or shortcut: $2(0.8)(0.2) = 0.32$.
- **Correct Option**: **B** (8 samples of class A and 2 of class B)

---

#### A16. Feature Importance with One-Hot Encoded Dummies
- **Formula**: For categorical variable $C$ expanded into dummy variables $D_1, \dots, D_m$:
  $$\text{Importance}(C) = \sum_{j=1}^m \text{Importance}(D_j)$$
- **Given Values**:
  - $\text{purpose\_auto} = 0.06$
  - $\text{purpose\_education} = 0.04$
  - $\text{purpose\_home} = 0.03$
  - $\text{purpose\_personal} = 0.01$
  $$\text{Total Loan Purpose Importance} = 0.06 + 0.04 + 0.03 + 0.01 = 0.14$$
- Since $0.14 > \text{credit\_score } (0.10)$, loan purpose is the most important feature overall.
- **Correct Option**: **A**

---

#### A17. Optimal Base Estimator for Bagging
- **Formula**: Ensemble Variance: $\text{Var} = \rho \sigma^2 + \frac{1-\rho}{B}\sigma^2$.
- **Principle**: Bagging reduces variance without changing bias. It provides maximum benefit when base learners have **low bias and high variance** (e.g., deep unpruned decision trees).
- **Correct Option**: **C**

---

#### A18. Gradient Boosting Overfitting Remedies
- **Issue**: `learning_rate = 1.0`, `n_estimators = 2000`, `max_depth = 6` achieves 100% train accuracy but collapses on test set (overfitting).
- **Prescription**: Lower learning rate $\eta \in [0.01, 0.1]$, restrict tree depth (`max_depth = 2 to 4`), and apply early stopping on validation loss.
- **Correct Option**: **D**

---

#### A19. K-Means Initialization Pathology & Standard Remedy
- **Observation**: Five runs on same data yield wildly different inertia: $812, 795, 1640, 803, 2210$.
- **Reason**: Lloyd's algorithm converges to local minima determined by initial seeds.
- **Fix**: Use K-Means++ initialization (`init='k-means++'`) and multiple restarts (`n_init > 1`), retaining the run with minimum inertia.
- **Correct Option**: **B**

---

#### A20. Bivariate Standardized PCA Explained Variance
- **Given**: Standardized columns with correlation $r = 0.5$.
- **Covariance Matrix**:
  $$\mathbf{\Sigma} = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 1 \end{pmatrix}$$
- **Eigenvalues**:
  $$\det\begin{pmatrix} 1 - \lambda & 0.5 \\ 0.5 & 1 - \lambda \end{pmatrix} = (1 - \lambda)^2 - 0.25 = 0 \implies 1 - \lambda = \pm 0.5$$
  $$\lambda_1 = 1 + 0.5 = 1.5, \quad \lambda_2 = 1 - 0.5 = 0.5$$
- **Explained Variance Ratio of PC1**:
  $$\text{EVR}_1 = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{1.5}{1.5 + 0.5} = \frac{1.5}{2.0} = 0.75 = 75\%$$
- **Correct Option**: **A** ($75\%$)

---

### Section B: Fill in the Blanks (B1 to B15)

---

#### B1. Task Framing (Regression vs Classification)
- House sale price in rupees is a continuous number $\implies$ **Regression**
- Customer churn (Yes/No) is a discrete binary label $\implies$ **Classification**

---

#### B2. Encodings for Categorical Data
- T-shirt size (S, M, L, XL) has a meaningful natural order $\implies$ **Ordinal** feature, encoded via **OrdinalEncoder** (ordered integers).
- Payment method (UPI, card, cash) has no intrinsic order $\implies$ **Nominal** feature, encoded via **OneHotEncoder** (one-hot / dummy encoding).

---

#### B3. Imputation Strategy for Skewed Features
- A skewed distribution with outliers is best imputed using the **Median** (robust to outliers).
- The median must be computed strictly on the **Training** set only, then applied to the test set.

---

#### B4. Manual $R^2$ Metric Calculation
- **Given**: $y = [2, 4, 9, 13]$, $\hat{y} = [3, 6, 8, 11]$, $n = 4$.
- **Errors ($e_i = \hat{y}_i - y_i$)**:
  $$[3 - 2, \; 6 - 4, \; 8 - 9, \; 11 - 13] = [1, \; 2, \; -1, \; -2]$$
- **Sum of Squared Residuals ($\text{SS}_{\text{res}}$)**:
  $$\text{SS}_{\text{res}} = 1^2 + 2^2 + (-1)^2 + (-2)^2 = 1 + 4 + 1 + 4 = 10$$
- **Target Mean ($\bar{y}$)**:
  $$\bar{y} = \frac{2 + 4 + 9 + 13}{4} = \frac{28}{4} = 7.0$$
- **Total Sum of Squares ($\text{SS}_{\text{tot}}$)**:
  $$\text{SS}_{\text{tot}} = (2 - 7)^2 + (4 - 7)^2 + (9 - 7)^2 + (13 - 7)^2 = (-5)^2 + (-3)^2 + 2^2 + 6^2 = 25 + 9 + 4 + 36 = 74$$
- **$R^2$ Calculation**:
  $$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{10}{74} = 1 - 0.135135 = 0.864865 \approx \mathbf{0.865}$$

---

#### B5. Variance Inflation Factor (VIF) Calculation
- **Given**: Feature $j$ regressed on other features gives $R_j^2 = 0.8$.
- **Formula**:
  $$\text{VIF}_j = \frac{1}{1 - R_j^2} = \frac{1}{1 - 0.8} = \frac{1}{0.2} = \mathbf{5}$$

---

#### B6. Manual Gradient Descent Step
- **Given**: Model $\hat{y} = w \cdot x$, $J(w) = \frac{1}{n}\sum (w x_i - y_i)^2$, $\frac{dJ}{dw} = \frac{2}{n}\sum (w x_i - y_i)x_i$.
- **Data Points**: $(1, 2)$ and $(2, 4)$, $n = 2$, start $w = 0$, $\eta = 0.05$.
- **Residual Errors at $w = 0$**:
  $$e_1 = (0 \cdot 1) - 2 = -2$$
  $$e_2 = (0 \cdot 2) - 4 = -4$$
- **Gradient Calculation**:
  $$\frac{dJ}{dw} = \frac{2}{2} \left[ (-2)(1) + (-4)(2) \right] = 1 \cdot [-2 - 8] = \mathbf{-10}$$
- **Parameter Update**:
  $$w_{\text{new}} = w - \eta \frac{dJ}{dw} = 0 - 0.05(-10) = 0 + 0.50 = \mathbf{0.5}$$

---

#### B7. Adjusted $R^2$ Calculation
- **Given**: $n = 21, p = 5, R^2 = 0.80$.
- **Formula**:
  $$\bar{R}^2 = 1 - (1 - R^2) \frac{n - 1}{n - p - 1}$$
- **Arithmetic**:
  $$\bar{R}^2 = 1 - (1 - 0.80) \cdot \frac{21 - 1}{21 - 5 - 1} = 1 - (0.20) \cdot \frac{20}{15} = 1 - 0.20 \cdot \frac{4}{3} = 1 - \frac{0.80}{3} = 1 - 0.26667 = \mathbf{0.733}$$

---

#### B8. Lasso and Ridge Penalties Computation
- **Given**: Weights $\mathbf{w} = [2, -1, 0, 3]$, $\lambda = 0.5$.
- **Lasso Penalty ($L_1$)**:
  $$\text{Penalty}_{\text{Lasso}} = \lambda \sum_{j} |w_j| = 0.5 \cdot (|2| + |-1| + |0| + |3|) = 0.5 \cdot (2 + 1 + 0 + 3) = 0.5 \cdot 6 = \mathbf{3.0}$$
- **Ridge Penalty ($L_2$)**:
  $$\text{Penalty}_{\text{Ridge}} = \lambda \sum_{j} w_j^2 = 0.5 \cdot (2^2 + (-1)^2 + 0^2 + 3^2) = 0.5 \cdot (4 + 1 + 0 + 9) = 0.5 \cdot 14 = \mathbf{7.0}$$

---

#### B9. Precision, Recall & $F_1$-Score Calculation
- **Given**: $TP = 45, FP = 15, FN = 5$.
- **Precision**:
  $$P = \frac{TP}{TP + FP} = \frac{45}{45 + 15} = \frac{45}{60} = \mathbf{0.750}$$
- **Recall**:
  $$R = \frac{TP}{TP + FN} = \frac{45}{45 + 5} = \frac{45}{50} = \mathbf{0.900}$$
- **$F_1$-Score**:
  $$F_1 = \frac{2 P R}{P + R} = \frac{2(0.750)(0.900)}{0.750 + 0.900} = \frac{1.35}{1.65} = \frac{9}{11} \approx \mathbf{0.818}$$

---

#### B10. Odds, Log-Odds & Linear Score
- **Given**: Predicted probability $\hat{p} = 0.8$.
- **Odds**:
  $$\text{Odds} = \frac{\hat{p}}{1 - \hat{p}} = \frac{0.8}{1 - 0.8} = \frac{0.8}{0.2} = \mathbf{4}$$
- **Log-Odds ($z$)**:
  $$z = \ln(\text{Odds}) = \ln(4) \approx \mathbf{1.386}$$

---

#### B11. Euclidean and Manhattan Distance
- **Given**: Points $\mathbf{p} = (2, -1)$ and $\mathbf{q} = (8, 7)$.
- **Coordinate Differences**: $\Delta x = 8 - 2 = 6$, $\Delta y = 7 - (-1) = 8$.
- **Euclidean ($L_2$)**:
  $$d_{\text{Euclid}} = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = \mathbf{10}$$
- **Manhattan ($L_1$)**:
  $$d_{\text{Manhattan}} = |\Delta x| + |\Delta y| = |6| + |8| = 6 + 8 = \mathbf{14}$$

---

#### B12. Decision Tree Gini Split Gain
- **Parent Node**: 5 samples of class A, 5 of class B ($N = 10$).
  $$G_{\text{parent}} = 1 - \left[\left(\frac{5}{10}\right)^2 + \left(\frac{5}{10}\right)^2\right] = 1 - [0.25 + 0.25] = 0.50$$
- **Left Child Node**: 4 of A, 0 of B ($N_L = 4$). Pure node:
  $$G_L = 1 - \left[\left(\frac{4}{4}\right)^2 + 0\right] = 0$$
- **Right Child Node**: 1 of A, 5 of B ($N_R = 6$).
  $$G_R = 1 - \left[\left(\frac{1}{6}\right)^2 + \left(\frac{5}{6}\right)^2\right] = 1 - \left[\frac{1}{36} + \frac{25}{36}\right] = 1 - \frac{26}{36} = \frac{10}{36} \approx 0.2778$$
- **Weighted Child Gini**:
  $$G_{\text{children}} = \frac{N_L}{N} G_L + \frac{N_R}{N} G_R = \frac{4}{10}(0) + \frac{6}{10}\left(\frac{10}{36}\right) = \frac{60}{360} = \frac{1}{6} \approx \mathbf{0.167}$$
- **Gini Gain**:
  $$\Delta G = G_{\text{parent}} - G_{\text{children}} = 0.50 - \frac{1}{6} = \frac{3}{6} - \frac{1}{6} = \frac{2}{6} = \frac{1}{3} \approx \mathbf{0.333}$$

---

#### B13. Random Forest Feature Subspace
- **Formula**: `max_features='sqrt'` $\implies m = \sqrt{p}$.
- **Given**: $p = 36$ features.
- **Evaluation**:
  $$m = \sqrt{36} = \mathbf{6} \text{ features}$$

---

#### B14. Silhouette Coefficient Computation
- **Given**: Mean intra-cluster distance $a(i) = 1.2$, mean nearest-cluster distance $b(i) = 3.0$.
- **Formula**:
  $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))} = \frac{3.0 - 1.2}{\max(1.2, 3.0)} = \frac{1.8}{3.0} = \mathbf{0.6}$$

---

#### B15. PCA Image Compression Ratio
- **Original Dimensions**: $n = 1000$ images, $d = 100$ pixel columns.
  $$\text{Original Stored Numbers} = 1000 \times 100 = 100,000$$
- **PCA Configuration**: $k = 10$ components.
  - Compressed image scores: $1000 \times 10 = 10,000$
  - Principal component eigenvectors: $10 \times 100 = 1,000$
  - Mean image vector: $1 \times 100 = 100$
  $$\text{Total Numbers Stored} = 10,000 + 1,000 + 100 = \mathbf{11,100}$$
- **Compression Ratio**:
  $$\text{Ratio} = \frac{100,000}{11,100} \approx \mathbf{9.0\times}$$

---

### Section C: Coding & Algorithmic Problems (C1 to C8)

---

#### C1. Regression Metrics from Scratch in NumPy
- **Formulas Implemented**:
  $$\text{MAE} = \frac{1}{n} \sum |y_i - \hat{y}_i|$$
  $$\text{RMSE} = \sqrt{\frac{1}{n}\sum (y_i - \hat{y}_i)^2}$$
  $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
- **Test Case Values**: $y_{\text{true}} = [250, 310, 180, 420, 365, 295]$, $y_{\text{pred}} = [265, 300, 200, 390, 370, 310]$.
  - Errors: $[15, -10, 20, -30, 5, 15] \implies \sum |e_i| = 95 \implies \text{MAE} = \frac{95}{6} = 15.8333$.
  - Squared errors: $[225, 100, 400, 900, 25, 225] \implies \sum e_i^2 = 1875 \implies \text{MSE} = 312.5 \implies \text{RMSE} = \sqrt{312.5} = 17.6777$.
  - Mean target: $\bar{y} = 303.3333 \implies \text{SS}_{\text{tot}} = 35583.3333$.
  - $R^2 = 1 - \frac{1875}{35583.3333} = 0.9473$.
- **Why $\text{RMSE} \ge \text{MAE}$**: Squaring gives larger individual errors ($20$ and $30$) disproportionately higher weight than small misses.

---

#### C2. Manual Sigmoid, Decision Thresholds & Log-Loss
- **Formulas Implemented**:
  $$\sigma(z) = \frac{1}{1 + e^{-z}}, \quad z = \mathbf{X}\mathbf{w} + b$$
  $$\hat{y}_{\text{pred}} = \mathbb{I}(\hat{p} \ge \tau)$$
  $$\text{Log-Loss} = -\frac{1}{n}\sum [y_i \ln(\text{clip}(\hat{p}_i)) + (1 - y_i)\ln(\text{clip}(1 - \hat{p}_i))]$$
  where $\hat{p}$ is clipped to $[10^{-15}, 1 - 10^{-15}]$.
- **Threshold Shift Tradeoff**: Dropping threshold from $0.5 \to 0.3$:
  - True label $1$ with $\hat{p} = 0.4502$ flips from $0 \to 1$ (becomes True Positive).
  - Recall increases: $\frac{2}{3} \to \frac{3}{3} = 1.0$.
  - True label $0$ with $\hat{p} = 0.3917$ flips from $0 \to 1$ (becomes False Positive).
  - Precision decreases: $1.0 \to \frac{3}{4} = 0.75$.

---

#### C3. Mixed-Type Preprocessing Pipeline
- **Pipeline Architecture**:
  - Numeric columns $\to$ `SimpleImputer(strategy='mean')`
  - Ordinal columns $\to$ `OrdinalEncoder(categories=[['Fair', 'Good', 'Excellent'], ['1st', '2nd', '3rd+']])`
  - Nominal column $\to$ `OneHotEncoder(drop='first')`
  - Regressor $\to$ `LinearRegression()`
- **Column Count After Preprocessing**: 2 numeric + 2 ordinal + 2 one-hot fuel dummies (CNG dropped) $= 6$ total columns.

---

#### C4. Polynomial Degree Sweep & Bias-Variance Tradeoff
- **Protocol**:
  $$\text{Pipeline} = [\text{PolynomialFeatures}(d), \text{StandardScaler}(), \text{LinearRegression}()]$$
- **Bias-Variance Pattern**:
  - $d = 1$: High training MAE ($1.1161$) and high CV MAE ($1.1664$) $\implies$ High bias.
  - $d = 6$: Optimal tradeoff: Training MAE $= 0.2249$, CV MAE $= \mathbf{0.2701}$ (lowest CV error).
  - $d = 12$: Training MAE continues dropping to $0.2053$, while CV MAE explodes to $0.6348$ $\implies$ High variance.

---

#### C5. $k$-NN Classifier from Scratch & Memorization Proof
- **Distance Formula**: $d(\mathbf{x}, \mathbf{q}) = \sqrt{\sum_j (x_j - q_j)^2}$.
- **Why Training Accuracy for $k=1$ is Always $1.0$**:
  Every point $\mathbf{x}_i$ in the training set is its own nearest neighbor at distance $d(\mathbf{x}_i, \mathbf{x}_i) = 0.0$. The model simply retrieves the exact ground truth label (memorization, zero bias, extreme variance).

---

#### C6. Decision Tree Pruning with `ccp_alpha`
- **Cost-Complexity Formula**:
  $$R_\alpha(T) = R(T) + \alpha |T|$$
- **Effect of Sweeping `ccp_alpha`**:
  - $\alpha = 0.0$: $18$ leaves, train acc $= 1.000$, test acc $= 0.9231$ (overfitting).
  - $\alpha = 0.005$: $9$ leaves, train acc $= 0.9859$, test acc $= \mathbf{0.9441}$ (optimal pruning removes noise).
  - $\alpha = 0.02$: $4$ leaves, train acc $= 0.9577$, test acc $= 0.9091$ (underfitting).

---

#### C7. Imbalanced Classification & Class Weights
- **Model Evaluation on 8.6% Positives**:
  - Always-0 Baseline Accuracy $= 91.33\%$ (shows why accuracy is a misleading metric for rare classes).
  - Plain Logistic Regression: Test Recall $= 0.7115$, Precision $= 0.8810$.
  - Balanced Logistic Regression (`class_weight='balanced'`):
    - Upscales rare class in loss $\implies$ pushes probabilities up.
    - Test Recall jumps to $0.9231$; Precision drops to $0.4286$.
    - ROC-AUC barely changes ($0.9513 \to 0.9493$) because ROC-AUC measures overall rank ordering across all thresholds, which is invariant to monotonic probability shifts.

---

#### C8. PCA and K-Means on Wine Dataset
- **Formulas**:
  $$\text{EVR}_k = \frac{s_k^2}{\sum s_j^2}, \quad \text{Cumulative EVR} = \sum_{j=1}^k \text{EVR}_j$$
- **Results**:
  - PC1 explains $36.2\%$, PC2 explains $19.2\%$, PC3 explains $11.1\%$.
  - First $10$ components reach $96.2\%$ cumulative variance ($\ge 95\%$).
  - Silhouette prefers $k = 3$ clusters ($s = 0.285$).
  - Adjusted Rand Index (ARI) comparing clustering to ground-truth classes: $\text{ARI} \approx 0.895$ (PCA 2D) vs $\text{ARI} \approx 0.898$ (all 13 scaled features).
  - *Key Insight*: 2 components preserve only $55\%$ of total variance, yet retain almost 100% of the true underlying class separation.
