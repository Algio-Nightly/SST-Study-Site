QUIZ_L07 = {
  "topicId": "lecture-07",
  "lectureNumber": 7,
  "title": "Model Selection & Regularization: Ridge, Lasso & Elastic Net",
  "description": "30 questions covering Cross-Validation protocols, Ridge (L2) shrinkage, Lasso (L1) sparsity, Elastic Net, geometric constraint regions, SVD spectral analysis, and hyperparameter tuning.",
  "estimatedMinutes": 45,
  "questions": [
    {
      "id": "cml-l07-q01",
      "type": "single_choice",
      "question": "What is the closed-form analytical solution for Ridge Regression parameters $\\hat{\\beta}_\\text{ridge}$ with regularization parameter $\\lambda > 0$ and design matrix $X$?",
      "options": [
        {
          "id": "A",
          "text": "$\\hat{\\beta}_\\text{ridge} = (X^TX + \\lambda I)^{-1} X^Ty$"
        },
        {
          "id": "B",
          "text": "$\\hat{\\beta}_\\text{ridge} = (X^TX - \\lambda I)^{-1} X^Ty$"
        },
        {
          "id": "C",
          "text": "$\\hat{\\beta}_\\text{ridge} = X^T (X X^T + \\lambda I) y$"
        },
        {
          "id": "D",
          "text": "$\\hat{\\beta}_\\text{ridge} = (X^TX)^{-1} X^Ty - \\lambda \\mathbf{1}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Minimizing $\\frac{1}{2}\\|y - X\\beta\\|^2 + \\frac{\\lambda}{2}\\|\\beta\\|^2$ yields gradient $-X^T(y - X\\beta) + \\lambda \\beta = 0 \\implies (X^TX + \\lambda I)\\beta = X^Ty \\implies \\hat{\\beta}_\\text{ridge} = (X^TX + \\lambda I)^{-1} X^Ty$.",
      "difficulty": "easy",
      "subtopic": "Ridge Closed Form"
    },
    {
      "id": "cml-l07-q02",
      "type": "single_choice",
      "question": "Why is the matrix $(X^TX + \\lambda I)$ always invertible for any real design matrix $X$ whenever $\\lambda > 0$, even if $p > n$ or columns are collinear?",
      "options": [
        {
          "id": "A",
          "text": "Because $I$ removes all zeros from the data matrix $X$"
        },
        {
          "id": "B",
          "text": "Because $X^TX$ is positive semi-definite (eigenvalues $\\ge 0$), so adding $\\lambda I$ shifts all eigenvalues strictly to $\\lambda_i + \\lambda > 0$, guaranteeing positive definiteness and full rank"
        },
        {
          "id": "C",
          "text": "Because $\\lambda$ sets all off-diagonal covariance terms to zero"
        },
        {
          "id": "D",
          "text": "Because it forces the determinant to equal 1"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Let $X^TX v = \\mu v$ with $\\mu \\ge 0$. Then $(X^TX + \\lambda I)v = (\\mu + \\lambda) v$. Since $\\lambda > 0$, all eigenvalues $\\mu + \\lambda \\ge \\lambda > 0$. Every eigenvalue is strictly positive, making the matrix strictly positive definite, invertible, and well-conditioned.",
      "difficulty": "medium",
      "subtopic": "Ridge Matrix Invertibility"
    },
    {
      "id": "cml-l07-q03",
      "type": "single_choice",
      "question": "Why does Lasso ($L_1$) regularization produce strictly sparse solutions (setting coefficients exactly to zero), whereas Ridge ($L_2$) regularization only shrinks coefficients toward zero?",
      "options": [
        {
          "id": "A",
          "text": "Because Lasso uses gradient descent while Ridge uses the Normal Equation"
        },
        {
          "id": "B",
          "text": "Because the L1 ball constraint $\\sum |\\beta_j| \\le t$ has sharp corners/vertices on the coordinate axes, where elliptical MSE loss contours frequently make first contact"
        },
        {
          "id": "C",
          "text": "Because Ridge regression operates only on positive numbers"
        },
        {
          "id": "D",
          "text": "Because Lasso minimizes training error faster than Ridge"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In two dimensions, the $L_1$ constraint region is a diamond with corners on the axes ($\\{\\beta_1=0\\}$ or $\\{\\beta_2=0\\}$). The expanding elliptical loss contours are statistically far more likely to hit these pointy vertices first, yielding solutions where some $\\beta_j = 0$. The $L_2$ ball is a smooth sphere with no sharp corners.",
      "difficulty": "medium",
      "subtopic": "L1 Sparsity Geometry"
    },
    {
      "id": "cml-l07-q04",
      "type": "single_choice",
      "question": "Why is the intercept term $\\beta_0$ conventionally excluded from the regularization penalty in Ridge, Lasso, and Elastic Net?",
      "options": [
        {
          "id": "A",
          "text": "Because penalizing $\\beta_0$ would make the optimization problem non-convex"
        },
        {
          "id": "B",
          "text": "Because shrinking $\\beta_0$ toward zero would make the model's predictions dependent on an arbitrary shift in the origin of the target variable $y$"
        },
        {
          "id": "C",
          "text": "Because Scikit-Learn cannot compute the derivative of the intercept"
        },
        {
          "id": "D",
          "text": "Because the intercept is always equal to 1"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The intercept captures the baseline expected value $\\bar{y}$ when all $X=0$. If $\\beta_0$ were penalized toward 0, shifting $y$ by an arbitrary constant (e.g. converting Celsius to Kelvin) would drastically distort model predictions.",
      "difficulty": "medium",
      "subtopic": "Intercept Penalization"
    },
    {
      "id": "cml-l07-q05",
      "type": "single_choice",
      "question": "What is the critical reason why features MUST be centered and standardized (e.g. using `StandardScaler`) before applying Ridge or Lasso regularization?",
      "options": [
        {
          "id": "A",
          "text": "Because unstandardized features cannot be multiplied in matrix form"
        },
        {
          "id": "B",
          "text": "Because the regularization penalty treats all coefficient magnitudes $\\beta_j$ equally; features on larger scales have tiny coefficients and are barely penalized, while features on smaller scales have huge coefficients and are unfairly over-penalized"
        },
        {
          "id": "C",
          "text": "Because regularization only works if all features are strictly positive"
        },
        {
          "id": "D",
          "text": "To convert the loss function from non-convex to convex"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "If feature $x_1$ is measured in dollars and $x_2$ in millions of dollars, the OLS coefficient $\\beta_2$ is $10^6$ times smaller than $\\beta_1$. Regularization adds $\\lambda \\sum \\beta_j^2$, penalizing $\\beta_1$ a trillion times more harshly simply due to unit choice. Standardization removes scale arbitrariness.",
      "difficulty": "easy",
      "subtopic": "Standardization Requirement"
    },
    {
      "id": "cml-l07-q06",
      "type": "single_choice",
      "question": "For an orthogonal design matrix where $X^TX = I$, what is the closed-form coordinate-wise thresholding operator for the Lasso estimator $\\hat{\\beta}_j^\\text{lasso}$ as a function of OLS estimate $\\hat{\\beta}_j^\\text{ols}$?",
      "options": [
        {
          "id": "A",
          "text": "$\\hat{\\beta}_j^\\text{lasso} = \\frac{\\hat{\\beta}_j^\\text{ols}}{1 + \\lambda}$"
        },
        {
          "id": "B",
          "text": "$\\hat{\\beta}_j^\\text{lasso} = \\text{sign}(\\hat{\\beta}_j^\\text{ols}) \\max(0, |\\hat{\\beta}_j^\\text{ols}| - \\frac{\\lambda}{2})$ (Soft-Thresholding Operator)"
        },
        {
          "id": "C",
          "text": "$\\hat{\\beta}_j^\\text{lasso} = \\hat{\\beta}_j^\\text{ols} - \\lambda$"
        },
        {
          "id": "D",
          "text": "$\\hat{\\beta}_j^\\text{lasso} = \\begin{cases} 0 & \\text{if } |\\hat{\\beta}_j^\\text{ols}| < \\lambda \\\\ \\hat{\\beta}_j^\\text{ols} & \\text{otherwise} \\end{cases}$ (Hard-Thresholding Operator)"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Under an orthogonal design, Lasso yields the exact Soft-Thresholding operator $S_{\\lambda/2}(\\hat{\\beta}_j^\\text{ols}) = \\text{sign}(\\hat{\\beta}_j^\\text{ols}) \\max(0, |\\hat{\\beta}_j^\\text{ols}| - \\frac{\\lambda}{2})$, which translates coefficients toward zero by $\\frac{\\lambda}{2}$ and sets them to 0 if $|\\hat{\\beta}| \\le \\frac{\\lambda}{2}$.",
      "difficulty": "hard",
      "subtopic": "Soft-Thresholding Operator"
    },
    {
      "id": "cml-l07-q07",
      "type": "single_choice",
      "question": "What is a major limitation of standard Lasso regression when applied to high-dimensional datasets where the number of predictors $p$ exceeds the number of observations $n$ ($p > n$)?",
      "options": [
        {
          "id": "A",
          "text": "Lasso cannot be computed using coordinate descent"
        },
        {
          "id": "B",
          "text": "Lasso can select at most $n$ non-zero features before saturating"
        },
        {
          "id": "C",
          "text": "Lasso coefficients diverge to infinity"
        },
        {
          "id": "D",
          "text": "Lasso always selects all $p$ features"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "When $p > n$, the Lasso convex optimization problem can select at most $n$ features with non-zero coefficients. If there are hundreds of truly informative features and $n < p$, Lasso is mathematically incapable of identifying more than $n$ of them.",
      "difficulty": "hard",
      "subtopic": "Lasso Limitations"
    },
    {
      "id": "cml-l07-q08",
      "type": "single_choice",
      "question": "When two or more features are highly correlated with each other, how do Ridge and Lasso behave differently?",
      "options": [
        {
          "id": "A",
          "text": "Ridge selects one feature at random and zeroes the other; Lasso shrinks both coefficients equally"
        },
        {
          "id": "B",
          "text": "Ridge shrinks both coefficients toward each other, giving them roughly equal weights; Lasso arbitrarily picks one feature and drives the other to zero"
        },
        {
          "id": "C",
          "text": "Both methods fail and return NaN"
        },
        {
          "id": "D",
          "text": "Neither method alters the coefficients relative to OLS"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Due to strict convexity of the $L_2$ norm, Ridge encourages correlated features to share coefficients (grouping effect: $\\beta_1 \\approx \\beta_2$). Lasso has flat linear indifference lines along $|\\beta_1| + |\\beta_2| = c$, causing it to arbitrarily select one and zero the other.",
      "difficulty": "medium",
      "subtopic": "Correlated Features: Ridge vs Lasso"
    },
    {
      "id": "cml-l07-q09",
      "type": "single_choice",
      "question": "What is Elastic Net regression, and how does it overcome the limitations of Lasso?",
      "options": [
        {
          "id": "A",
          "text": "It combines an L1 norm penalty and an L2 norm penalty, enabling both feature selection (sparsity) and the grouping effect for correlated features"
        },
        {
          "id": "B",
          "text": "It uses an L0 penalty to find the exact optimal subset of features in polynomial time"
        },
        {
          "id": "C",
          "text": "It fits a polynomial spline on the residuals of Ridge regression"
        },
        {
          "id": "D",
          "text": "It replaces gradient descent with genetic algorithms"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Elastic Net penalty is $\\lambda_1 \\|\\beta\\|_1 + \\lambda_2 \\|\\beta\\|_2^2$. The strictly convex quadratic $L_2$ term forces correlated features to be selected together (grouping effect) and allows selecting more than $n$ features when $p > n$, while the $L_1$ term enforces sparsity.",
      "difficulty": "medium",
      "subtopic": "Elastic Net Formulation"
    },
    {
      "id": "cml-l07-q10",
      "type": "single_choice",
      "question": "In Scikit-Learn's `ElasticNet(alpha=..., l1_ratio=...)`, what does `l1_ratio = 1.0` correspond to?",
      "options": [
        {
          "id": "A",
          "text": "Pure Ridge regression"
        },
        {
          "id": "B",
          "text": "Pure Lasso regression"
        },
        {
          "id": "C",
          "text": "Ordinary Least Squares with no penalty"
        },
        {
          "id": "D",
          "text": "Equal 50-50 mix of L1 and L2"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In Scikit-Learn's parameterization, the penalty is $\\alpha \\cdot (\\text{l1\\_ratio} \\|\\beta\\|_1 + \\frac{1 - \\text{l1\\_ratio}}{2} \\|\\beta\\|_2^2)$. Setting `l1_ratio = 1.0` eliminates the L2 term completely, recovering pure Lasso.",
      "difficulty": "easy",
      "subtopic": "Scikit-Learn ElasticNet"
    },
    {
      "id": "cml-l07-q11",
      "type": "single_choice",
      "question": "As the regularization strength $\\lambda \\to \\infty$ in Ridge regression, what happens to the estimated coefficients $\\hat{\\beta}$ and the model's Bias and Variance?",
      "options": [
        {
          "id": "A",
          "text": "Coefficients $\\hat{\\beta} \\to \\infty$, Bias $\\to 0$, Variance $\\to \\infty$"
        },
        {
          "id": "B",
          "text": "Slope coefficients $\\hat{\\beta}_j \\to 0$, Bias increases to its maximum, and Variance drops to 0 (the model predicts a constant $\\bar{y}$)"
        },
        {
          "id": "C",
          "text": "Coefficients match OLS estimates, Bias and Variance remain unchanged"
        },
        {
          "id": "D",
          "text": "The model interpolates the training points perfectly"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "As $\\lambda \\to \\infty$, $(X^TX + \\lambda I)^{-1} \\approx \\frac{1}{\\lambda} I \\to \\mathbf{0}$, shrinking all slope coefficients to zero. The model degrades into predicting a flat constant $\\hat{y} = \\bar{y}$, which has zero variance across sample realizations but maximal structural bias.",
      "difficulty": "medium",
      "subtopic": "Asymptotic Regularization Behavior"
    },
    {
      "id": "cml-l07-q12",
      "type": "single_choice",
      "question": "In K-Fold Cross-Validation with $K = 5$, what fraction of the data is used for training and validation in each of the 5 iterations?",
      "options": [
        {
          "id": "A",
          "text": "50% training, 50% validation"
        },
        {
          "id": "B",
          "text": "80% training, 20% validation"
        },
        {
          "id": "C",
          "text": "90% training, 10% validation"
        },
        {
          "id": "D",
          "text": "20% training, 80% validation"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In 5-fold CV, the dataset is partitioned into 5 disjoint equal subsets. In each iteration, $K-1 = 4$ folds (80%) are used for training and the remaining 1 fold (20%) is held out for validation.",
      "difficulty": "easy",
      "subtopic": "K-Fold Basics"
    },
    {
      "id": "cml-l07-q13",
      "type": "single_choice",
      "question": "What is Leave-One-Out Cross-Validation (LOOCV), and what is its primary characteristic regarding variance of the test error estimate?",
      "options": [
        {
          "id": "A",
          "text": "LOOCV uses $K=n$ folds; each model is trained on $n-1$ points and tested on 1 point. It is approximately unbiased for generalization error, but the error estimates across folds are highly correlated, leading to higher variance than 5- or 10-fold CV"
        },
        {
          "id": "B",
          "text": "LOOCV is strictly identical to a 50-50 train-test split"
        },
        {
          "id": "C",
          "text": "LOOCV produces parameter estimates with zero bias and zero variance"
        },
        {
          "id": "D",
          "text": "LOOCV is computationally much faster than a single train-test split"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "In LOOCV, $K=n$. Because each model is trained on almost the entire dataset ($n-1$ points), the training sets are nearly identical and their validation errors are strongly positively correlated. The mean of highly correlated variables has higher variance than the mean of less correlated variables.",
      "difficulty": "hard",
      "subtopic": "LOOCV Properties"
    },
    {
      "id": "cml-l07-q14",
      "type": "single_choice",
      "question": "Why is 'Stratified K-Fold' preferred over standard K-Fold for classification tasks with imbalanced classes?",
      "options": [
        {
          "id": "A",
          "text": "It ensures that each fold contains exactly the same percentage of each target class as the complete dataset, preventing folds with zero positive instances"
        },
        {
          "id": "B",
          "text": "It sorts the features by variance before splitting"
        },
        {
          "id": "C",
          "text": "It eliminates the need for computing the confusion matrix"
        },
        {
          "id": "D",
          "text": "It increases the number of training samples by 5x"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Standard random splitting on imbalanced data (e.g. 1% fraud) can produce validation folds with zero fraud cases, rendering metric evaluation invalid. Stratified K-Fold preserves class proportions across all folds.",
      "difficulty": "easy",
      "subtopic": "Stratified K-Fold"
    },
    {
      "id": "cml-l07-q15",
      "type": "single_choice",
      "question": "What is the insidious data science flaw known as 'Pre-split Preprocessing Leakage' during Cross-Validation?",
      "options": [
        {
          "id": "A",
          "text": "Fitting a Scaler, Imputer, or Feature Selector on the entire dataset BEFORE passing the data to `cross_val_score` or K-Fold"
        },
        {
          "id": "B",
          "text": "Training a model with both L1 and L2 penalties simultaneously"
        },
        {
          "id": "C",
          "text": "Using an odd number of folds for K-Fold Cross Validation"
        },
        {
          "id": "D",
          "text": "Normalizing continuous variables using min-max scaling"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "If transformations like `fit_transform` compute dataset-level statistics (mean, variance, imputed medians, or selected top-correlated features) before splitting, information from the validation folds leaks into the training process, resulting in overly optimistic validation scores.",
      "difficulty": "medium",
      "subtopic": "CV Leakage"
    },
    {
      "id": "cml-l07-q16",
      "type": "single_choice",
      "question": "In Scikit-Learn, how do you completely prevent data leakage during Cross-Validation when preprocessing data?",
      "options": [
        {
          "id": "A",
          "text": "Use `sklearn.pipeline.Pipeline` or `make_pipeline` containing the transformers and estimator, and pass the pipeline to `cross_val_score`"
        },
        {
          "id": "B",
          "text": "Always set `random_state=0` in `train_test_split`"
        },
        {
          "id": "C",
          "text": "Scale the target variable $y$ instead of the feature matrix $X$"
        },
        {
          "id": "D",
          "text": "Use `cross_validate` with `return_train_score=True`"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Passing a `Pipeline` into cross-validation ensures that in each fold, `fit` and `transform` are called strictly on the training fold, and only `transform` is called on the validation fold.",
      "difficulty": "easy",
      "subtopic": "Scikit-Learn Pipeline"
    },
    {
      "id": "cml-l07-q17",
      "type": "single_choice",
      "question": "In SVD spectral analysis of Ridge regression with singular values $\\sigma_j$ of $X$, how are the OLS coefficients shrunk along each principal direction $v_j$?",
      "options": [
        {
          "id": "A",
          "text": "Shrunk by the factor $\\frac{\\sigma_j^2}{\\sigma_j^2 + \\lambda}$"
        },
        {
          "id": "B",
          "text": "Multiplied by $\\lambda$"
        },
        {
          "id": "C",
          "text": "Shrunk by $\\frac{1}{\\sigma_j}$"
        },
        {
          "id": "D",
          "text": "Set to 0 if $\\sigma_j < \\lambda$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Substituting $X = U \\Sigma V^T$ into the Ridge equation yields $\\hat{\\beta}_\\text{ridge} = V (\\Sigma^2 + \\lambda I)^{-1} \\Sigma U^T y = \\sum_j \\frac{\\sigma_j}{\\sigma_j^2 + \\lambda} u_j^T y \\, v_j$. Relative to OLS ($\\frac{1}{\\sigma_j}$), each component is shrunk by $\\frac{\\sigma_j^2}{\\sigma_j^2 + \\lambda}$. Components with small singular values (high collinearity/noise) are shrunk most aggressively.",
      "difficulty": "hard",
      "subtopic": "Spectral Analysis of Ridge"
    },
    {
      "id": "cml-l07-q18",
      "type": "single_choice",
      "question": "What is the 'Effective Degrees of Freedom' $\\text{df}(\\lambda)$ of a Ridge regression model with singular values $\\sigma_j$?",
      "options": [
        {
          "id": "A",
          "text": "$\\text{df}(\\lambda) = \\sum_{j=1}^p \\frac{\\sigma_j^2}{\\sigma_j^2 + \\lambda}$"
        },
        {
          "id": "B",
          "text": "$\\text{df}(\\lambda) = p - \\lambda$"
        },
        {
          "id": "C",
          "text": "$\\text{df}(\\lambda) = n - p - 1$"
        },
        {
          "id": "D",
          "text": "$\\text{df}(\\lambda) = \\frac{p}{\\lambda}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The effective degrees of freedom is the trace of the hat matrix $H_\\lambda = X(X^TX + \\lambda I)^{-1}X^T$. Since $\\text{Tr}(H_\\lambda) = \\sum_j \\frac{\\sigma_j^2}{\\sigma_j^2 + \\lambda}$, when $\\lambda=0$, $\\text{df}=p$; as $\\lambda \\to \\infty$, $\\text{df} \\to 0$.",
      "difficulty": "hard",
      "subtopic": "Effective Degrees of Freedom"
    },
    {
      "id": "cml-l07-q19",
      "type": "single_choice",
      "question": "In Scikit-Learn, which class implements efficient built-in Leave-One-Out or K-Fold cross-validation for Ridge regression without recomputing the full SVD at every fold?",
      "options": [
        {
          "id": "A",
          "text": "`sklearn.linear_model.RidgeCV`"
        },
        {
          "id": "B",
          "text": "`sklearn.linear_model.LassoCV`"
        },
        {
          "id": "C",
          "text": "`sklearn.model_selection.GridSearchCV`"
        },
        {
          "id": "D",
          "text": "`sklearn.linear_model.SGDClassifier`"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "`RidgeCV` uses generalized cross-validation (GCV) formulas to evaluate multiple values of $\\alpha$ virtually for free after performing a single matrix decomposition.",
      "difficulty": "easy",
      "subtopic": "RidgeCV & GCV"
    },
    {
      "id": "cml-l07-q20",
      "type": "single_choice",
      "question": "What happens in cross-validation if a student uses standard K-Fold on financial time-series data with strong temporal trends?",
      "options": [
        {
          "id": "A",
          "text": "Training accuracy drops to 0%"
        },
        {
          "id": "B",
          "text": "Temporal look-ahead leakage occurs (future data is used to predict past data), yielding misleadingly optimistic CV scores that crash in production"
        },
        {
          "id": "C",
          "text": "The model automatically discovers seasonal cycles"
        },
        {
          "id": "D",
          "text": "The learning rate converges instantly"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Standard K-Fold randomly shuffles samples, allowing models to peek into future days to predict historical prices (look-ahead bias). For time-series, `TimeSeriesSplit` (walk-forward expanding window) must be used.",
      "difficulty": "medium",
      "subtopic": "Time-Series CV"
    },
    {
      "id": "cml-l07-q21",
      "type": "single_choice",
      "question": "Which algorithm is standardly used to solve the non-differentiable Lasso $L_1$ optimization problem efficiently?",
      "options": [
        {
          "id": "A",
          "text": "Cyclic Coordinate Descent"
        },
        {
          "id": "B",
          "text": "LAPACK direct matrix inversion"
        },
        {
          "id": "C",
          "text": "Gram-Schmidt Orthogonalization"
        },
        {
          "id": "D",
          "text": "Simplex linear programming alone"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Because the $|\\beta_j|$ penalty is non-differentiable at 0, standard gradient descent cannot be directly applied. Coordinate Descent optimizes one coordinate $\\beta_j$ at a time using the 1D soft-thresholding operator while holding other coordinates fixed, cycling through all features rapidly.",
      "difficulty": "medium",
      "subtopic": "Coordinate Descent"
    },
    {
      "id": "cml-l07-q22",
      "type": "single_choice",
      "question": "What is the 'One-Standard-Error' rule (1-SE rule) advocated by Hastie, Tibshirani, and Friedman for selecting regularized models?",
      "options": [
        {
          "id": "A",
          "text": "Select the most complex model whose training error is within 1 standard error of 0"
        },
        {
          "id": "B",
          "text": "Choose the most parsimonious (simplest / most regularized) model whose CV error is within 1 standard error of the minimum CV error"
        },
        {
          "id": "C",
          "text": "Reject any model whose test error has a standard error greater than 1.0"
        },
        {
          "id": "D",
          "text": "Add 1 standard deviation to all predicted $\\hat{y}$ values"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The 1-SE rule embodies Occam's razor: instead of blindly picking the parameter with the absolute lowest empirical CV error (which might just be noisy), select the simplest model whose performance is statistically indistinguishable (within 1 SE) from the best.",
      "difficulty": "hard",
      "subtopic": "1-SE Rule"
    },
    {
      "id": "cml-l07-q23",
      "type": "multi_choice",
      "question": "Which of the following statements comparing Ridge ($L_2$) and Lasso ($L_1$) regression are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Ridge has an analytical closed-form solution: $\\hat{\\beta}_\\text{ridge} = (X^TX + \\lambda I)^{-1}X^Ty$"
        },
        {
          "id": "B",
          "text": "Lasso performs automatic feature selection by forcing some coefficients to become exactly zero"
        },
        {
          "id": "C",
          "text": "Ridge regression is generally preferred when many features each have small but meaningful non-zero effects"
        },
        {
          "id": "D",
          "text": "Lasso regression always retains all features with non-zero weights regardless of $\\lambda$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are classic characterizations. D is FALSE: Lasso's hallmark feature is setting weights to exact zeros as $\\lambda$ increases.",
      "difficulty": "easy",
      "subtopic": "Ridge vs Lasso Comparison"
    },
    {
      "id": "cml-l07-q24",
      "type": "multi_choice",
      "question": "Which of the following are consequences of increasing the regularization hyperparameter $\\lambda$ in regularized linear models? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The model becomes simpler and less prone to overfitting"
        },
        {
          "id": "B",
          "text": "The variance of the parameter estimates decreases"
        },
        {
          "id": "C",
          "text": "The bias of the model increases"
        },
        {
          "id": "D",
          "text": "The training set $R^2$ monotonically increases"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Regularization trades off variance for bias (A, B, C). Training $R^2$ always decreases (or stays flat) because the parameter space is more constrained away from the unconstrained OLS minimum.",
      "difficulty": "medium",
      "subtopic": "Regularization Dynamics"
    },
    {
      "id": "cml-l07-q25",
      "type": "multi_choice",
      "question": "Why is Cross-Validation preferred over a single Train-Test split for model evaluation on moderate-sized datasets? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "A single train-test split performance metric depends heavily on how the random split fell (high estimation variance)"
        },
        {
          "id": "B",
          "text": "Cross-validation uses all observations for both training and validation across the folds, providing a more reliable and robust performance estimate"
        },
        {
          "id": "C",
          "text": "Cross-validation provides an estimate of the variability / standard deviation of model performance"
        },
        {
          "id": "D",
          "text": "Cross-validation completely eliminates the need for having a final held-out test set in commercial deployments"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are primary statistical advantages of CV. D is false: in industry, a final untouched test set is still retained to evaluate the final selected model and verify end-to-end pipeline integrity.",
      "difficulty": "medium",
      "subtopic": "Cross-Validation Benefits"
    },
    {
      "id": "cml-l07-q26",
      "type": "multi_choice",
      "question": "Which of the following statements about Elastic Net are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "It overcomes Lasso's limitation of selecting at most $n$ predictors when $p > n$"
        },
        {
          "id": "B",
          "text": "It exhibits a 'grouping effect', where highly correlated predictors enter or leave the model together"
        },
        {
          "id": "C",
          "text": "It requires tuning two hyperparameters: overall penalty strength ($\\alpha$) and L1/L2 mixing ratio (`l1_ratio`)"
        },
        {
          "id": "D",
          "text": "It is computationally faster than simple OLS regression"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are foundational properties of Zou & Hastie's (2005) Elastic Net. D is false; solving Elastic Net requires iterative coordinate descent with 2D hyperparameter grids, which is computationally more intensive than a single OLS fit.",
      "difficulty": "medium",
      "subtopic": "Elastic Net Properties"
    },
    {
      "id": "cml-l07-q27",
      "type": "multi_choice",
      "question": "Which of the following operations represent forms of data leakage when performing K-Fold Cross Validation? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Computing target encoding (replacing categories with mean $y$) on the entire dataset before creating CV splits"
        },
        {
          "id": "B",
          "text": "Selecting the top 10 features most correlated with $y$ on the whole dataset prior to running CV"
        },
        {
          "id": "C",
          "text": "Imputing missing values with the dataset-wide median before splitting"
        },
        {
          "id": "D",
          "text": "Fitting a PCA transformer strictly on the training fold and transforming the validation fold"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C leak validation labels and distribution statistics into the training pipeline. D is the correct, leakage-free procedure.",
      "difficulty": "hard",
      "subtopic": "Leakage Taxonomy in CV"
    },
    {
      "id": "cml-l07-q28",
      "type": "multi_choice",
      "question": "When inspecting a coefficient regularization path plot (tracing $\\beta_j$ vs. $-\\log(\\alpha)$ or $\\lambda$), which patterns are characteristic of Lasso? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Coefficients start at zero for very large $\\lambda$ and suddenly branch out away from zero at specific threshold points as $\\lambda$ decreases"
        },
        {
          "id": "B",
          "text": "The path is piecewise linear between change points"
        },
        {
          "id": "C",
          "text": "All coefficients are strictly smooth asymptotically decaying curves that never touch the zero axis"
        },
        {
          "id": "D",
          "text": "Some coefficients may enter the model, become non-zero, and later return to exactly zero as $\\lambda$ changes"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Lasso regularization paths are piecewise linear (LARS algorithm) with sharp entry and exit kinks (A, B, D). Smooth asymptotic decay that never touches zero (C) describes Ridge paths, not Lasso.",
      "difficulty": "hard",
      "subtopic": "Regularization Paths"
    },
    {
      "id": "cml-l07-q29",
      "type": "multi_choice",
      "question": "Which of the following cross-validation splitting strategies in Scikit-Learn are suited for structured or non-i.i.d. data? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "`TimeSeriesSplit` (for sequentially ordered temporal data)"
        },
        {
          "id": "B",
          "text": "`GroupKFold` (ensures observations from the same patient/user do not appear in both train and validation sets)"
        },
        {
          "id": "C",
          "text": "`StratifiedKFold` (preserves class label distributions in imbalanced targets)"
        },
        {
          "id": "D",
          "text": "`KFold(shuffle=False)` on randomly shuffled data"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A handles temporal ordering, B handles clustered/grouped data to prevent subject leakage, and C handles target class imbalance. D does not provide structural grouping guarantees.",
      "difficulty": "medium",
      "subtopic": "Specialized CV Splitters"
    },
    {
      "id": "cml-l07-q30",
      "type": "multi_choice",
      "question": "Which of the following statements regarding the geometric properties of regularized regression in parameter space are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The L2 penalty corresponds to a spherical Euclidean norm ball $\\{\\beta : \\sum \\beta_j^2 \\le t\\}$"
        },
        {
          "id": "B",
          "text": "The L1 penalty corresponds to a cross-polytope / hyperoctahedron diamond $\\{\\beta : \\sum |\\beta_j| \\le t\\}$ with non-differentiable vertices on the axes"
        },
        {
          "id": "C",
          "text": "Elastic Net forms a contour with rounded edges and soft corners, combining aspects of both sphere and diamond"
        },
        {
          "id": "D",
          "text": "L0 regularization corresponds to finding points lying on coordinate hyperplanes, but is an NP-hard combinatorial optimization problem"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four statements are foundational geometric insights in statistical learning theory (Tibshirani 1996, Zou & Hastie 2005).",
      "difficulty": "hard",
      "subtopic": "Geometric Foundations"
    }
  ]
}
