# Classical Machine Learning (CML) — Master Syntax & Code Compendium
## Comprehensive Python, NumPy, Pandas & Scikit-Learn API Reference Across All 15 Lectures & Exam Scenarios

> [!NOTE]
> This master cheatsheet provides production-grade, syntactically exact code snippets and architectural patterns for Classical Machine Learning in Python. It covers the complete data science stack (**Pandas**, **NumPy**, **Scikit-Learn**, **Statsmodels**, and **XGBoost/LightGBM**), structured from raw data manipulation to complex multi-transformer pipelines, custom scratch implementations, and the official Scaler End-Term Practice Sheet (Group B) Section C solutions.

---

## 📋 Table of Contents
1. [Core Data Manipulation: Pandas & NumPy Essentials](#1-core-data-manipulation-pandas--numpy-essentials)
2. [Preprocessing & Pipelines (`sklearn.preprocessing`, `sklearn.compose`)](#2-preprocessing--pipelines-sklearnpreprocessing-sklearncompose)
3. [Linear Models & Diagnostics (`sklearn.linear_model`, `statsmodels`)](#3-linear-models--diagnostics-sklearnlinearmodel-statsmodels)
4. [Iterative Optimization & Custom Gradient Descent](#4-iterative-optimization--custom-gradient-descent)
5. [Regularization, Model Selection & CV (`sklearn.model_selection`)](#5-regularization-model-selection--cv-sklearnmodelselection)
6. [Logistic Regression & Decision Boundaries](#6-logistic-regression--decision-boundaries)
7. [Classification Evaluation Metrics & Imbalance (`sklearn.metrics`)](#7-classification-evaluation-metrics--imbalance-sklearnmetrics)
8. [Instance-Based Learning: $k$-Nearest Neighbours (`sklearn.neighbors`)](#8-instance-based-learning-k-nearest-neighbours-sklearnneighbors)
9. [Decision Trees & Cost-Complexity Pruning (`sklearn.tree`)](#9-decision-trees--cost-complexity-pruning-sklearntree)
10. [Ensemble Methods: Random Forests & Boosting (`sklearn.ensemble`, `xgboost`)](#10-ensemble-methods-random-forests--boosting-sklearnensemble-xgboost)
11. [Kernel Methods & Support Vector Machines (`sklearn.svm`)](#11-kernel-methods--support-vector-machines-sklearnsvm)
12. [Probabilistic Classifiers: Naive Bayes (`sklearn.naive_bayes`)](#12-probabilistic-classifiers-naive-bayes-sklearnnaivebayes)
13. [Clustering & Unsupervised Learning (`sklearn.cluster`, `scipy`)](#13-clustering--unsupervised-learning-sklearncluster-scipy)
14. [Dimensionality Reduction: PCA & Manifolds (`sklearn.decomposition`)](#14-dimensionality-reduction-pca--manifolds-sklearndecomposition)
15. [Model Interpretability: Permutation Importance & SHAP](#15-model-interpretability-permutation-importance--shap)
16. [📌 Exam Reference Implementations: SST Practice Sheet Section C (C1 to C8)](#16-exam-reference-implementations-sst-practice-sheet-section-c-c1-to-c8)

---

## 1. Core Data Manipulation: Pandas & NumPy Essentials

### 1.1 Exploratory Data Analysis & Cleaning in Pandas
```python
import pandas as pd
import numpy as np

# 1. Inspecting Dataset & Missing Values
df = pd.read_csv("data.csv")
print(df.shape)                     # (n_rows, n_cols)
print(df.info())                    # Column types, memory, non-null counts
print(df.isna().sum().to_dict())    # Count of missing values per column
print(df.describe(include="all"))   # Summary statistics (mean, std, quartiles, mode)

# 2. Filtering & Conditional Selection
subset = df.loc[(df["age"] > 25) & (df["salary"] <= 100000), ["name", "salary"]]

# 3. Categorical Exploration & Frequency Tables
print(df["category"].value_counts(dropna=False, normalize=True)) # Proportions
ct = pd.crosstab(df["true_class"], df["cluster"], margins=True)  # Confusion/Cluster cross-tab

# 4. Outlier Detection via Interquartile Range (IQR)
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR
outliers = df[(df["price"] < lower_fence) | (df["price"] > upper_fence)]
```

### 1.2 Vectorized Linear Algebra & Matrix Math in NumPy
```python
import numpy as np

# 1. Vector & Matrix Creation
X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], dtype=float) # Shape (3, 2)
y = np.array([10.0, 20.0, 30.0], dtype=float)                     # Shape (3,)

# 2. Matrix Multiplication & Inversion (Normal Equation)
X_b = np.c_[np.ones((X.shape[0], 1)), X]      # Prepend column of 1s (Intercept trick)
theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y # Closed-form OLS: (X^T X)^(-1) X^T y
theta_pinv = np.linalg.pinv(X_b) @ y           # Robust Moore-Penrose pseudoinverse

# 3. Pairwise Euclidean Distance via Broadcasting: (n, d) to (m, d) -> (n, m)
# (A[:, None, :] - B[None, :, :])^2 summed across feature axis
def pairwise_distances(A, B):
    return np.sqrt(np.sum((A[:, np.newaxis, :] - B[np.newaxis, :, :]) ** 2, axis=2))

# 4. Sorting & Top-K Ranking
arr = np.array([50, 10, 40, 20, 30])
sorted_indices = np.argsort(arr)                # [1, 3, 4, 2, 0]
top_2_smallest_idx = np.argsort(arr)[:2]        # [1, 3]

# 5. Majority Voting for Classification
votes = np.array([1, 1, 2, 0, 1, 2])
most_frequent_class = np.bincount(votes).argmax() # 1

# 6. Numerical Stability: Clipping Probabilities
p_hat = np.array([0.0, 0.5, 1.0])
p_clipped = np.clip(p_hat, 1e-15, 1.0 - 1e-15)  # Prevents log(0) in Cross-Entropy
```

---

## 2. Preprocessing & Pipelines (`sklearn.preprocessing`, `sklearn.compose`)

### 2.1 Feature Scaling Transformations
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler

# 1. Standard Scaler: (x - mean) / std -> Zero mean, unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # FIT ONLY ON TRAIN
X_test_scaled = scaler.transform(X_test)       # TRANSFORM TEST WITHOUT FITTING

# 2. Min-Max Scaler: (x - min) / (max - min) -> Bounded [0, 1]
minmax = MinMaxScaler(feature_range=(0, 1))
X_train_norm = minmax.fit_transform(X_train)

# 3. Robust Scaler: (x - median) / IQR -> Resilient to extreme outliers
robust = RobustScaler(quantile_range=(25.0, 75.0))
X_train_robust = robust.fit_transform(X_train)
```

### 2.2 Categorical Encoders
```python
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# 1. One-Hot Encoding for Nominal Features (e.g., Payment Method: UPI, Card, Cash)
# drop='first' drops 1st dummy column to prevent dummy variable collinearity trap
ohe = OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore")
X_cat_ohe = ohe.fit_transform(df[["payment_method"]])
feature_names = ohe.get_feature_names_out(["payment_method"])

# 2. Ordinal Encoding for Ordered Levels (e.g., Low < Medium < High)
# MUST pass explicit category ordering to avoid alphabetical sorting pitfall!
ord_enc = OrdinalEncoder(categories=[["Low", "Medium", "High"]])
X_ord = ord_enc.fit_transform(df[["satisfaction"]]) # Low=0, Medium=1, High=2
```

### 2.3 The Leakage-Free `ColumnTransformer` & `Pipeline` Architecture
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

num_cols = ["age_years", "km_driven"]
ord_cols = ["condition", "owner"]
nom_cols = ["fuel"]

# 1. Construct ColumnTransformer mapping specific transformers to column groups
preprocessor = ColumnTransformer([
    ("num", SimpleImputer(strategy="mean"), num_cols),
    ("ord", OrdinalEncoder(categories=[["Fair", "Good", "Excellent"], ["1st", "2nd", "3rd+"]]), ord_cols),
    ("nom", OneHotEncoder(drop="first", sparse_output=False), nom_cols)
])

# 2. Chain with Estimator inside Pipeline
pipeline = Pipeline([
    ("pre", preprocessor),
    ("reg", LinearRegression())
])

# 3. Strict train-test split FIRST, then fit pipeline on train only
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# 4. Predict and evaluate cleanly
predictions = pipeline.predict(X_test)

# 5. Accessing intermediate transformed features
num_transformed_cols = pipeline.named_steps["pre"].transform(X_train.head()).shape[1]
```

---

## 3. Linear Models & Diagnostics (`sklearn.linear_model`, `statsmodels`)

### 3.1 Ordinary Least Squares in Scikit-Learn
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Fit Model
ols = LinearRegression(fit_intercept=True)
ols.fit(X_train, y_train)

# Model Parameters
weights = ols.coef_      # Slope parameters (theta_1, ..., theta_d)
intercept = ols.intercept_ # Bias parameter (theta_0)

# Predictions & Metrics
y_pred = ols.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"MAE: {mae:.4f} | RMSE: {rmse:.4f} | R²: {r2:.4f}")
```

### 3.2 Regression Diagnostics & LINE Assumptions in Statsmodels
```python
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. Fit OLS with Full Statistical Summary
X_sm = sm.add_constant(X_train) # Statsmodels requires manual intercept column!
model_sm = sm.OLS(y_train, X_sm).fit()
print(model_sm.summary())       # P-values, R², F-statistic, AIC, BIC, Condition No.

# 2. Residual Analysis
residuals = model_sm.resid
fitted_values = model_sm.fittedvalues

# 3. Variance Inflation Factor (VIF) Calculation
# VIF > 5 to 10 indicates severe multicollinearity
vif_data = pd.DataFrame()
vif_data["feature"] = X_sm.columns
vif_data["VIF"] = [variance_inflation_factor(X_sm.values, i) for i in range(X_sm.shape[1])]
print(vif_data)

# 4. Durbin-Watson Autocorrelation Statistic
from statsmodels.stats.stattools import durbin_watson
dw_stat = durbin_watson(residuals) # Close to 2.0 indicates uncorrelated residuals
```

---

## 4. Iterative Optimization & Custom Gradient Descent

### 4.1 Vectorized Gradient Descent from Scratch in Pure NumPy
```python
import numpy as np

def batch_gradient_descent(X, y, lr=0.01, epochs=1000, tol=1e-6):
    n_samples, n_features = X.shape
    # Add dummy column of 1s for intercept
    X_b = np.c_[np.ones((n_samples, 1)), X]
    w = np.zeros(n_features + 1) # Initialize weights to 0
    cost_history = []

    for epoch in range(epochs):
        # 1. Forward Pass: Predictions
        y_hat = X_b @ w
        # 2. Residual Errors
        errors = y_hat - y
        # 3. Cost (MSE)
        cost = (1 / (2 * n_samples)) * np.sum(errors ** 2)
        cost_history.append(cost)
        # 4. Vectorized Gradient: (2/n) * X_b^T @ errors  (or 1/n depending on 1/2 factor)
        gradient = (1 / n_samples) * (X_b.T @ errors)
        # 5. Parameter Update
        w_prev = w.copy()
        w -= lr * gradient
        # 6. Early Stopping Check
        if np.linalg.norm(w - w_prev) < tol:
            print(f"Converged at epoch {epoch}")
            break

    return w, cost_history
```

### 4.2 Mini-Batch Gradient Descent Generator
```python
def get_mini_batches(X, y, batch_size=32, shuffle=True):
    n_samples = X.shape[0]
    indices = np.arange(n_samples)
    if shuffle:
        np.random.shuffle(indices)
    for start_idx in range(0, n_samples, batch_size):
        batch_idx = indices[start_idx : start_idx + batch_size]
        yield X[batch_idx], y[batch_idx]
```

---

## 5. Regularization, Model Selection & CV (`sklearn.model_selection`)

### 5.1 Ridge, Lasso & ElasticNet Implementation
```python
from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV, ElasticNet

# 1. Ridge Regression (L2 penalty: alpha * sum(w_j^2))
# Higher alpha -> shrinks weights closer to 0, prevents overfitting
ridge = Ridge(alpha=10.0, fit_intercept=True)
ridge.fit(X_train_scaled, y_train)

# 2. RidgeCV: Efficient internal cross-validation across penalty alphas
ridge_cv = RidgeCV(alphas=np.logspace(-3, 3, 7), cv=5)
ridge_cv.fit(X_train_scaled, y_train)
print(f"Optimal Ridge Alpha: {ridge_cv.alpha_}")

# 3. Lasso Regression (L1 penalty: alpha * sum(|w_j|))
# Forces non-essential weights to EXACTLY ZERO (Automatic Feature Selection)
lasso = Lasso(alpha=0.1, max_iter=2000)
lasso.fit(X_train_scaled, y_train)
zeroed_features = np.sum(lasso.coef_ == 0)

# 4. ElasticNet (Combination of L1 and L2)
# l1_ratio=1.0 is pure Lasso; l1_ratio=0.0 is pure Ridge
enet = ElasticNet(alpha=0.5, l1_ratio=0.7)
enet.fit(X_train_scaled, y_train)
```

### 5.2 Cross-Validation & Hyperparameter Tuning
```python
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score, GridSearchCV

# 1. K-Fold Cross Validation for Regression
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(
    estimator=pipeline, 
    X=X_train, 
    y=y_train, 
    cv=kf, 
    scoring="neg_mean_absolute_error" # Note: Sklearn maximizes negative loss
)
cv_mae = -cv_scores.mean()

# 2. Stratified K-Fold for Classification (Preserves class balance)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 3. Grid Search Cross-Validation
param_grid = {
    "reg__alpha": [0.01, 0.1, 1.0, 10.0, 100.0]
}
grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1
)
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
print("Best Params:", grid_search.best_params_)
```

---

## 6. Logistic Regression & Decision Boundaries

### 6.1 Logistic Regression & Probability Thresholding
```python
from sklearn.linear_model import LogisticRegression

# 1. Instantiate and Fit Logistic Model
logreg = LogisticRegression(
    penalty="l2", 
    C=1.0,                   # Inverse regularization strength: smaller C = stronger penalty
    solver="lbfgs", 
    max_iter=1000, 
    class_weight="balanced", # Automatically balances rare classes in loss
    random_state=42
)
logreg.fit(X_train, y_train)

# 2. Extracting Coefficients & Odds Ratios
weights = logreg.coef_[0]
odds_ratios = np.exp(weights) # Multiplicative change in odds per unit increase

# 3. Predicting Probabilities & Custom Thresholding
# Standard .predict() uses threshold 0.5:
probs = logreg.predict_proba(X_test)[:, 1] # P(y=1 | x)

# Custom decision threshold: e.g., tau = 0.3 to increase recall
custom_threshold = 0.3
y_custom_pred = (probs >= custom_threshold).astype(int)
```

### 6.2 Pure NumPy Sigmoid & Log-Loss
```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.asarray(z, dtype=float)))

def predict_proba_manual(X, w, b):
    z = np.asarray(X, dtype=float) @ np.asarray(w, dtype=float) + b
    return sigmoid(z)

def log_loss_manual(y_true, y_prob, eps=1e-15):
    y_true = np.asarray(y_true, dtype=float)
    p = np.clip(np.asarray(y_prob, dtype=float), eps, 1.0 - eps)
    return -np.mean(y_true * np.log(p) + (1.0 - y_true) * np.log(1.0 - p))
```

---

## 7. Classification Evaluation Metrics & Imbalance (`sklearn.metrics`)

### 7.1 Confusion Matrix & Core Metric Suite
```python
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, 
    recall_score, f1_score, roc_auc_score, roc_curve, 
    classification_report
)

# 1. Unpacking 2x2 Confusion Matrix: [[TN, FP], [FN, TP]]
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# 2. Core Classification Metrics
acc  = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0) # TP / (TP + FP)
rec  = recall_score(y_test, y_pred)                     # TP / (TP + FN)
f1   = f1_score(y_test, y_pred)                         # 2PR / (P + R)
auc  = roc_auc_score(y_test, probs)                     # Area under ROC curve

print(f"TN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")
print(f"Accuracy: {acc:.4f} | Prec: {prec:.4f} | Rec: {rec:.4f} | F1: {f1:.4f} | AUC: {auc:.4f}")

# 3. Comprehensive Multi-Class / Binary Report
print(classification_report(y_test, y_pred, digits=4))
```

### 7.2 ROC Curve & Cost-Benefit Analysis
```python
# 1. ROC Curve Points
fpr, tpr, thresholds = roc_curve(y_test, probs)

# 2. Business Cost-Benefit Calculation
# Cost of FN (losing churner): $500; Cost of FP (discount sent to non-churner): $50
def calculate_business_cost(y_true, y_prob, threshold, c_fp=50, c_fn=500):
    preds = (y_prob >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, preds).ravel()
    return fp * c_fp + fn * c_fn

threshold_grid = np.linspace(0.1, 0.9, 81)
costs = [calculate_business_cost(y_test, probs, t) for t in threshold_grid]
optimal_threshold = threshold_grid[np.argmin(costs)]
print(f"Cost-Optimal Decision Threshold: {optimal_threshold:.2f}")
```

---

## 8. Instance-Based Learning: $k$-Nearest Neighbours (`sklearn.neighbors`)

### 8.1 Scikit-Learn $k$-NN Classifier & Regressor
```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# 1. Classification (MANDATORY: Scale features first!)
knn_clf = KNeighborsClassifier(
    n_neighbors=5, 
    weights="uniform",     # Or 'distance' for inverse-distance weighting
    metric="minkowski", 
    p=2                    # p=2 is Euclidean distance; p=1 is Manhattan
)
knn_clf.fit(X_train_scaled, y_train)
y_pred = knn_clf.predict(X_test_scaled)

# 2. Regression
knn_reg = KNeighborsRegressor(n_neighbors=3, weights="distance")
knn_reg.fit(X_train_scaled, y_train)
```

### 8.2 Pure NumPy $k$-NN Classifier from Scratch
```python
import numpy as np

def knn_predict(X_train, y_train, X_query, k=5):
    X_train = np.asarray(X_train, float)
    y_train = np.asarray(y_train).astype(int)
    preds = []
    
    for q in np.asarray(X_query, float):
        # Compute Euclidean distance from query point q to all training points
        distances = np.sqrt(np.sum((X_train - q) ** 2, axis=1))
        # Get indices of k smallest distances
        nearest_indices = np.argsort(distances, kind="stable")[:k]
        # Majority vote among nearest labels
        majority_vote = np.bincount(y_train[nearest_indices]).argmax()
        preds.append(majority_vote)
        
    return np.array(preds)
```

---

## 9. Decision Trees & Cost-Complexity Pruning (`sklearn.tree`)

### 9.1 Decision Tree Classifier & Hyperparameter Constraints
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

# 1. Fit Decision Tree with Pre-Pruning Stopping Criteria
dt = DecisionTreeClassifier(
    criterion="gini",          # Or 'entropy' / 'log_loss'
    max_depth=4,               # Constrains maximum depth
    min_samples_split=10,      # Min samples required to split an internal node
    min_samples_leaf=5,        # Min samples required at a leaf node
    random_state=42
)
dt.fit(X_train, y_train)

# 2. Extract Feature Importances (Mean Decrease in Impurity - MDI)
importances = pd.Series(dt.feature_importances_, index=feature_names).sort_values(ascending=False)
print("Top 5 Features:\n", importances.head(5))

# 3. Visualizing Tree Hierarchy
tree_rules = export_text(dt, feature_names=list(feature_names))
print(tree_rules)
```

### 9.2 Minimal Cost-Complexity Post-Pruning (`ccp_alpha`)
```python
# 1. Compute Cost-Complexity Pruning Path
path = dt.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# 2. Sweep Alphas over Cross-Validation to Find Optimal Tree Size
clfs = []
for alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=42, ccp_alpha=alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)

# As alpha increases, leaf count drops monotonically:
leaf_counts = [clf.get_n_leaves() for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]
optimal_clf = clfs[np.argmax(test_scores)]
```

---

## 10. Ensemble Methods: Random Forests & Boosting (`sklearn.ensemble`, `xgboost`)

### 10.1 Random Forest with Out-of-Bag (OOB) Scoring
```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

# Random Forest Classifier (Decorrelates trees via feature subsampling)
rf = RandomForestClassifier(
    n_estimators=200,      # Number of parallel trees
    max_features="sqrt",   # Sample m = sqrt(p) features at each split
    oob_score=True,        # Free Out-Of-Bag generalization validation
    n_jobs=-1,             # Parallel CPU execution
    random_state=42
)
rf.fit(X_train, y_train)

print(f"OOB Score: {rf.oob_score_:.4f}")
print(f"Test Accuracy: {rf.score(X_test, y_test):.4f}")
```

### 10.2 Gradient Boosting & Modern Tree Boosters
```python
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

# 1. Scikit-Learn Gradient Boosting Classifier
gbm = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,    # Shrinkage parameter eta
    max_depth=3,           # Shallow weak learners
    subsample=0.8,         # Stochastic Gradient Boosting row ratio
    random_state=42
)
gbm.fit(X_train, y_train)

# 2. Extreme Gradient Boosting (XGBoost)
xgb = XGBClassifier(
    n_estimators=300,
    learning_rate=0.03,
    max_depth=4,
    reg_lambda=1.0,        # L2 leaf regularization
    reg_alpha=0.1,         # L1 leaf regularization
    gamma=0.2,             # Minimum split loss reduction threshold
    eval_metric="logloss",
    early_stopping_rounds=15, # Early stopping on validation split
    random_state=42
)
xgb.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    verbose=False
)
```

---

## 11. Kernel Methods & Support Vector Machines (`sklearn.svm`)

### 11.1 Support Vector Classification (SVC) & Support Vector Regression (SVR)
```python
from sklearn.svm import SVC, SVR, LinearSVC

# 1. Non-Linear RBF Kernel SVM (MANDATORY: Scale features!)
svc_rbf = SVC(
    C=1.0,                 # Misclassification penalty (Higher C = narrower margin, lower bias)
    kernel="rbf",          # Radial Basis Function
    gamma="scale",         # Kernel bandwidth gamma = 1 / (d * Var(X))
    probability=True,      # Enables Platt Scaling for predict_proba()
    random_state=42
)
svc_rbf.fit(X_train_scaled, y_train)

# 2. Inspecting Support Vectors
support_vector_indices = svc_rbf.support_
n_support_vectors_per_class = svc_rbf.n_support_
print(f"Total Support Vectors: {len(support_vector_indices)}")

# 3. Decision Function (Geometric Distance to Separating Hyperplane)
distances = svc_rbf.decision_function(X_test_scaled)

# 4. Support Vector Regression (SVR) with Epsilon-Insensitive Tube
svr = SVR(kernel="rbf", C=10.0, epsilon=0.1) # Zero penalty within +/- 0.1 tube
svr.fit(X_train_scaled, y_train)
```

---

## 12. Probabilistic Classifiers: Naive Bayes (`sklearn.naive_bayes`)

### 12.1 The Three Classical Naive Bayes Paradigms
```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

# 1. Gaussian Naive Bayes (Continuous Real-Valued Features)
# Models P(x_j | y) via 1D Normal distribution N(mu_jk, sigma_jk^2)
gnb = GaussianNB(var_smoothing=1e-9) # Variance smoothing prevents division by zero
gnb.fit(X_train, y_train)

# Inspect Learned Parameters
class_priors = gnb.class_prior_ # P(Y=k)
feature_means = gnb.theta_      # Mean per class & feature
feature_variances = gnb.var_    # Variance per class & feature

# 2. Multinomial Naive Bayes (Discrete Word Frequency Counts / TF Vectors)
# alpha=1.0 is Additive Laplace Smoothing; alpha < 1.0 is Lidstone Smoothing
mnb = MultinomialNB(alpha=1.0)
mnb.fit(X_train_counts, y_train)

# 3. Bernoulli Naive Bayes (Binary 0/1 Feature Indicators)
bnb = BernoulliNB(alpha=1.0, binarize=0.0)
bnb.fit(X_train_binary, y_train)

# 4. Incremental Online Learning via partial_fit()
gnb.partial_fit(X_batch, y_batch, classes=np.unique(y_train))
```

---

## 13. Clustering & Unsupervised Learning (`sklearn.cluster`, `scipy`)

### 13.1 K-Means Clustering & Silhouette Evaluation
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples, adjusted_rand_score

# 1. Run K-Means with K-Means++ Initialization
kmeans = KMeans(
    n_clusters=3,
    init="k-means++",      # Probabilistic D(x)^2 seed initialization
    n_init=10,             # Number of random seed restarts (keeps lowest inertia)
    max_iter=300,
    random_state=42
)
kmeans.fit(X_scaled)

# 2. Extract Clustering Attributes
cluster_labels = kmeans.labels_
cluster_centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_ # Within-Cluster Sum of Squares (WCSS)

# 3. Silhouette Score: In [-1, +1]
sil_score = silhouette_score(X_scaled, cluster_labels)
print(f"Inertia: {inertia:.2f} | Silhouette Score: {sil_score:.4f}")

# 4. Evaluating Clustering Against Ground Truth (External Metric)
ari = adjusted_rand_score(y_true, cluster_labels) # 1.0 is perfect clustering
```

### 13.2 Hierarchical Clustering & Dendrogram
```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# 1. Scikit-Learn Agglomerative Clustering
hac = AgglomerativeClustering(
    n_clusters=3,
    metric="euclidean",
    linkage="ward"         # 'ward', 'complete', 'average', 'single'
)
hac_labels = hac.fit_predict(X_scaled)

# 2. Scipy Linkage Matrix & Dendrogram
Z = linkage(X_scaled, method="ward")
plt.figure(figsize=(10, 5))
dendrogram(Z, truncate_mode="lastp", p=12)
plt.title("Hierarchical Dendrogram (Ward Linkage)")
```

### 13.3 DBSCAN (Density-Based Spatial Clustering)
```python
from sklearn.cluster import DBSCAN

# 1. Density-Based Clustering
dbscan = DBSCAN(eps=0.5, min_samples=5, metric="euclidean")
db_labels = dbscan.fit_predict(X_scaled)

# 2. Point Taxonomy
# Noise points are explicitly labeled as -1
n_clusters = len(set(db_labels)) - (1 if -1 in db_labels else 0)
n_noise = np.sum(db_labels == -1)
core_samples_mask = np.zeros_like(db_labels, dtype=bool)
core_samples_mask[dbscan.core_sample_indices_] = True

print(f"Clusters Discovered: {n_clusters} | Noise Points: {n_noise}")
```

---

## 14. Dimensionality Reduction: PCA & Manifolds (`sklearn.decomposition`)

### 14.1 Principal Component Analysis (PCA)
```python
from sklearn.decomposition import PCA

# 1. PCA with Fixed Number of Components (MANDATORY: Scale features!)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled) # Shape: (n_samples, 2)

# 2. Inspecting Variance Metrics
eigenvalues = pca.explained_variance_
evr = pca.explained_variance_ratio_ # Percentage variance explained per component
cumulative_evr = np.cumsum(evr)
print("EVR per PC:", np.round(evr, 4))
print("Cumulative EVR:", np.round(cumulative_evr, 4))

# 3. PCA Specifying Variance Threshold (e.g., retain 95% of total variance)
pca_95 = PCA(n_components=0.95)
X_pca_95 = pca_95.fit_transform(X_scaled)
print(f"Components retained for 95% variance: {pca_95.n_components_}")

# 4. Reconstruction: Inverse Transform back to original feature space
X_reconstructed = pca.inverse_transform(X_pca)
reconstruction_error = np.mean((X_scaled - X_reconstructed) ** 2)
```

---

## 15. Model Interpretability: Permutation Importance & SHAP

### 15.1 Permutation Feature Importance
```python
from sklearn.inspection import permutation_importance

# Evaluates degradation in test metric when feature columns are randomly shuffled
perm_importance = permutation_importance(
    estimator=pipeline,
    X=X_test,
    y=y_test,
    scoring="roc_auc",
    n_repeats=10,
    random_state=42
)

perm_df = pd.DataFrame({
    "feature": X_test.columns,
    "importance_mean": perm_importance.importances_mean,
    "importance_std": perm_importance.importances_std
}).sort_values(by="importance_mean", ascending=False)
print(perm_df.head(10))
```

---

## 16. Exam Reference Implementations: SST Practice Sheet Section C (C1 to C8)

Full, executable reference solutions in pure Python/NumPy/Scikit-Learn corresponding directly to Section C of the official SST Practice Sheet.

### C1. Regression Metrics from Scratch in NumPy
```python
import numpy as np

def regression_metrics(y_true, y_pred):
    """
    Returns {'mae': ..., 'rmse': ..., 'r2': ...} rounded to 4 decimals using pure NumPy.
    """
    y = np.asarray(y_true, dtype=float)
    p = np.asarray(y_pred, dtype=float)
    err = p - y
    
    mae = np.mean(np.abs(err))
    rmse = np.sqrt(np.mean(err ** 2))
    
    ss_res = np.sum(err ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1.0 - (ss_res / ss_tot)
    
    return {
        "mae": round(float(mae), 4),
        "rmse": round(float(rmse), 4),
        "r2": round(float(r2), 4)
    }

# Test Verification
y_t = [250, 310, 180, 420, 365, 295]
y_p = [265, 300, 200, 390, 370, 310]
print(regression_metrics(y_t, y_p))
# Output: {'mae': 15.8333, 'rmse': 17.6777, 'r2': 0.9473}
# RMSE >= MAE because squaring weights large deviations (20 and 30) heavily.
```

### C2. Sigmoid, Thresholds and Log-Loss from Scratch
```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.asarray(z, dtype=float)))

def predict_proba_manual(X, w, b):
    return sigmoid(np.asarray(X, dtype=float) @ np.asarray(w, dtype=float) + b)

def predict_label(p, threshold=0.5):
    return (np.asarray(p) >= threshold).astype(int)

def log_loss_manual(y_true, y_prob, eps=1e-15):
    y = np.asarray(y_true, dtype=float)
    p = np.clip(np.asarray(y_prob, dtype=float), eps, 1.0 - eps)
    return float(-np.mean(y * np.log(p) + (1.0 - y) * np.log(1.0 - p)))

# Test Verification
X_c2 = [[0.5, 1.2], [1.5, -0.3], [-1.0, 0.8], [2.0, 1.0], [0.0, 0.0]]
w_c2 = [1.2, -0.7]
b_c2 = -0.2
y_c2 = [0, 1, 0, 1, 1]

p_hat = predict_proba_manual(X_c2, w_c2, b_c2)
print("p_hat:", np.round(p_hat, 4)) # [0.3917, 0.8594, 0.1235, 0.8176, 0.4502]
print("labels @0.5:", predict_label(p_hat, 0.5)) # [0, 1, 0, 1, 0]
print("labels @0.3:", predict_label(p_hat, 0.3)) # [1, 1, 0, 1, 1]
print("log-loss:", round(log_loss_manual(y_c2, p_hat), 4)) # 0.356
```

### C3. Mixed-Type Preprocessing Pipeline for Resale Car Pricing
```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def build_car_pipeline(ord_encoder):
    num_cols = ["age_years", "km_driven"]
    ord_cols = ["condition", "owner"]
    nom_cols = ["fuel"]
    
    pre = ColumnTransformer([
        ("num", SimpleImputer(strategy="mean"), num_cols),
        ("ord", ord_encoder, ord_cols),
        ("nom", OneHotEncoder(drop="first", sparse_output=False), nom_cols),
    ])
    return Pipeline([("pre", pre), ("reg", LinearRegression())])

# Correct Ordinal Hierarchy: Fair < Good < Excellent; 1st < 2nd < 3rd+
correct_ord = OrdinalEncoder(categories=[["Fair", "Good", "Excellent"], ["1st", "2nd", "3rd+"]])
pipe3 = build_car_pipeline(correct_ord)
# Total columns after preprocessing: 2 numeric + 2 ordinal + 2 one-hot fuel (CNG dropped) = 6 columns
```

### C4. Polynomial Degree Selection via Cross-Validated MAE
```python
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_absolute_error

def poly_lr(d):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=d, include_bias=False)),
        ("sc", StandardScaler()),
        ("lr", LinearRegression())
    ])

cv = KFold(n_splits=4, shuffle=True, random_state=1)
rows = []
for d in range(1, 13):
    cv_mae = -cross_val_score(poly_lr(d), X_train, y_train, cv=cv, scoring="neg_mean_absolute_error").mean()
    m = poly_lr(d).fit(X_train, y_train)
    tr_mae = mean_absolute_error(y_train, m.predict(X_train))
    rows.append((d, round(float(tr_mae), 4), round(float(cv_mae), 4)))

cv_table = pd.DataFrame(rows, columns=["degree", "train_mae", "cv_mae"])
best_degree = int(cv_table.loc[cv_table["cv_mae"].idxmin(), "degree"]) # Degree 6
```

### C5. $k$-NN Classifier Scratch & Parameter Sweep
```python
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

# Choosing k via 5-fold Stratified CV
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_acc = {}
for k in [1, 3, 5, 7, 9, 11, 13, 15]:
    pipe = Pipeline([("sc", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=k))])
    cv_acc[k] = round(float(cross_val_score(pipe, X_tr, y_tr, cv=skf).mean()), 4)

best_k = max(cv_acc, key=lambda k: (cv_acc[k], -k)) # k = 5
```

### C6. Decision Tree Depth, Pruning (`ccp_alpha`) & Importances
```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

# 1. Depth sweep
skf6 = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for d in [1, 2, 3, 4, 5, 6, 8, None]:
    tree = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_tr, y_tr)
    cv_acc = cross_val_score(DecisionTreeClassifier(max_depth=d, random_state=42), X_tr, y_tr, cv=skf6).mean()

# 2. Pruning sweep
for a in [0.0, 0.005, 0.01, 0.02]:
    t = DecisionTreeClassifier(ccp_alpha=a, random_state=42).fit(X_tr, y_tr)
    print(f"Alpha: {a} | Leaves: {t.get_n_leaves()} | Test Acc: {t.score(X_te, y_te):.4f}")
```

### C7. Imbalanced Classification & `class_weight='balanced'`
```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_score, recall_score, roc_auc_score

# Baseline Plain vs Balanced Logistic Regression
plain_pipe = Pipeline([("sc", StandardScaler()), ("lr", LogisticRegression(max_iter=1000))]).fit(X_tr, y_tr)
bal_pipe = Pipeline([("sc", StandardScaler()), ("lr", LogisticRegression(max_iter=1000, class_weight="balanced"))]).fit(X_tr, y_tr)

# Balancing raises Recall significantly (e.g. 0.71 -> 0.92) while Precision drops (0.88 -> 0.43)
# ROC-AUC barely changes because ranking order remains preserved across probability shifts.
```

### C8. PCA and K-Means Pipeline on Wine Dataset
```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.metrics import adjusted_rand_score, silhouette_score

# 1. PCA Variance Evaluation
pca = PCA().fit(StandardScaler().fit_transform(X))
cum_ratio = np.cumsum(pca.explained_variance_ratio_)
n_95 = int(np.argmax(cum_ratio >= 0.95) + 1) # 10 components retain >= 95%

# 2. Pipeline: Scale -> PCA (2D) -> K-Means (k=3)
pipe8 = Pipeline([
    ("sc", StandardScaler()),
    ("pca", PCA(n_components=2)),
    ("km", KMeans(n_clusters=3, n_init=10, random_state=42))
])
pipe8.fit(X)
cluster_labels = pipe8.named_steps["km"].labels_
ari = adjusted_rand_score(y_true, cluster_labels) # ARI ≈ 0.895
```
