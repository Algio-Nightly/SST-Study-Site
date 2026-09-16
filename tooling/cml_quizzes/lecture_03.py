QUIZ_L03 = {
  "description": "30 questions covering hypothesis formulation, OLS cost function, Gaussian MLE derivation, Normal Equation matrix calculus, Hat Matrix orthogonal projection, regression metrics (MAE, MSE, RMSE, R^2, Adjusted R^2), and numerical calculations from the SST Sample Practice Paper.",
  "estimatedMinutes": 35,
  "lectureNumber": 3,
  "questions": [
    {
      "correctOptionIds": [
        "C"
      ],
      "difficulty": "medium",
      "explanation": "1. Mean of Y: $\\bar{y} = \\frac{2 + 4 + 6 + 8}{4} = 5.0$.\n2. Total Sum of Squares (SST): (2-5)^2 + (4-5)^2 + (6-5)^2 + (8-5)^2 = 9 + 1 + 1 + 9 = 20.0.\n3. Residual errors: e = [2-2.5, 4-3.5, 6-6.5, 8-7.5] = [-0.5, +0.5, -0.5, +0.5].\n4. Sum of Squared Errors (SSE): (-0.5)^2 + (0.5)^2 + (-0.5)^2 + (0.5)^2 = 0.25 + 0.25 + 0.25 + 0.25 = 1.0.\n5. $R^2 = 1 - \\frac{1.0}{20.0} = 1 - 0.05 = 0.95$.",
      "id": "cml03-q01",
      "options": [
        {
          "id": "A",
          "text": "0.80"
        },
        {
          "id": "B",
          "text": "0.90"
        },
        {
          "id": "C",
          "text": "0.95"
        },
        {
          "id": "D",
          "text": "0.98"
        }
      ],
      "question": "The following observed training points are given:\nX = [1, 2, 3, 4]\nY = [2, 4, 6, 8]\nA fitted regression model predicts:\n$\\hat{y} = [2.5, 3.5, 6.5, 7.5]$\nWhat is the exact value of $R^2$? Use $R^2 = 1 - \\frac{SSE}{SST}$.",
      "subtopic": "R^2 & Metric Calculations",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "medium",
      "explanation": "Given $R^2$ = 0.84, n = 20, p = 3:\n1 - $R^2$ = 0.16.\nDegrees of freedom factor: (n - 1) / (n - p - 1) = (20 - 1) / (20 - 3 - 1) = 19 / 16 = 1.1875.\nPenalty product: 0.16 * 1.1875 = 0.190.\n$R^2_{\\text{adj}} = 1 - 0.190 = 0.810$.",
      "id": "cml03-q02",
      "options": [
        {
          "id": "A",
          "text": "0.800"
        },
        {
          "id": "B",
          "text": "0.810"
        },
        {
          "id": "C",
          "text": "0.840"
        },
        {
          "id": "D",
          "text": "0.860"
        }
      ],
      "question": "For a regression model, $R^2$ = 0.84, sample size n = 20, and number of predictors p = 3. Calculate the Adjusted $R^2$ using:\n$R^2_{\\text{adj}} = 1 - (1 - $R^2$) \\frac{n - 1}{n - p - 1}$",
      "subtopic": "Adjusted R^2",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "$R^2$ (the Coefficient of Determination) measures the proportion of total variance in the dependent response variable Y that is statistically explained by the independent predictor features in the model: $R^2 = 1 - \\frac{SS_{\\text{res}}}{SS_{\\text{tot}}}$.",
      "id": "cml03-q03",
      "options": [
        {
          "id": "A",
          "text": "70% of the individual predictions are exactly correct with zero error."
        },
        {
          "id": "B",
          "text": "70% of the total variation in the target variable is explained by the linear relationship with the fitted model predictors."
        },
        {
          "id": "C",
          "text": "The model achieves 70% classification accuracy on binary thresholds."
        },
        {
          "id": "D",
          "text": "70% of the input features have statistically significant p-values."
        }
      ],
      "question": "A fitted regression model yields $R^2$ = 0.70 on a holdout evaluation dataset. Which statement is the best statistical interpretation?",
      "subtopic": "R^2 & Metric Calculations",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "Raw training $R^2$ monotonically increases (or remains constant) whenever any feature is added, even pure random noise. Adjusted $R^2$ penalizes additional features via the degrees of freedom ratio (n - 1)/(n - p - 1), decreasing if an added feature fails to reduce SSE sufficiently.",
      "id": "cml03-q04",
      "options": [
        {
          "id": "A",
          "text": "It always yields a higher numerical value than raw $R^2$."
        },
        {
          "id": "B",
          "text": "It incorporates a mathematical penalty for the number of predictors p, counteracting the fact that raw training $R^2$ never decreases when adding features."
        },
        {
          "id": "C",
          "text": "It can only be used for classification models with cross-entropy."
        },
        {
          "id": "D",
          "text": "It removes the requirement for a train/test split entirely."
        }
      ],
      "question": "Why is Adjusted $R^2$ preferred over raw $R^2$ when comparing regression models with different numbers of predictors?",
      "subtopic": "Adjusted R^2",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "Adding a predictor gives the least-squares optimization extra degrees of freedom, guaranteeing $SS_{\\text{res}} \\le SS_{\\text{res,old}}$; therefore raw $R^2$ cannot decrease. However, if the new predictor explains less variance than the penalty term (n-1)/(n-p-1), Adjusted $R^2$ decreases.",
      "id": "cml03-q05",
      "options": [
        {
          "id": "A",
          "text": "$R^2$ can decrease substantially."
        },
        {
          "id": "B",
          "text": "$R^2$ cannot decrease when a predictor is added, while Adjusted $R^2$ may decrease."
        },
        {
          "id": "C",
          "text": "Adjusted $R^2$ must always increase unconditionally."
        },
        {
          "id": "D",
          "text": "Both metrics must remain completely unchanged."
        }
      ],
      "question": "A new predictor feature is added to an ordinary least squares linear regression model. Which statement is generally true regarding $R^2$ and Adjusted $R^2$ on the training set?",
      "subtopic": "Adjusted R^2",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "OLS explicitly minimizes the sum of squared residuals: $J(\\boldsymbol{\\theta}) = \\frac{1}{2} \\sum_{i=1}^n (y^{(i)} - \\boldsymbol{\\theta}^T \\mathbf{x}^{(i)})^2 = \\frac{1}{2} \\|\\mathbf{y} - X\\boldsymbol{\\theta}\\|_2^2$.",
      "id": "cml03-q06",
      "options": [
        {
          "id": "A",
          "text": "Sum of absolute errors (L1 loss)"
        },
        {
          "id": "B",
          "text": "Sum of squared residuals: $\\sum_{i=1}^n (y^{(i)} - \\hat{y}^{(i)})^2$"
        },
        {
          "id": "C",
          "text": "Classification hinge loss"
        },
        {
          "id": "D",
          "text": "Variance Inflation Factor (VIF)"
        }
      ],
      "question": "In Ordinary Least Squares (OLS) linear regression, what mathematical objective quantity is minimized during model fitting?",
      "subtopic": "OLS Objective",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "C"
      ],
      "difficulty": "easy",
      "explanation": "Residual is defined as actual minus predicted: $e = y - \\hat{y}$ = 15 - 12 = +3$.",
      "id": "cml03-q07",
      "options": [
        {
          "id": "A",
          "text": "-3"
        },
        {
          "id": "B",
          "text": "0"
        },
        {
          "id": "C",
          "text": "+3"
        },
        {
          "id": "D",
          "text": "27"
        }
      ],
      "question": "For a single observation, the actual ground-truth value is $y = 15$ and the regression prediction is $\\hat{y} = 12$. What is the residual error $e = y - \\hat{y}$?",
      "subtopic": "R^2 & Metric Calculations",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "A severe disparity between near-zero training error and high test error is the hallmark signature of overfitting (high model variance).",
      "id": "cml03-q08",
      "options": [
        {
          "id": "A",
          "text": "Underfitting due to excessive model bias"
        },
        {
          "id": "B",
          "text": "Overfitting (high variance; model memorized idiosyncratic training noise)"
        },
        {
          "id": "C",
          "text": "Zero variance in the target distribution"
        },
        {
          "id": "D",
          "text": "Perfect statistical generalization"
        }
      ],
      "question": "A regression model achieves near-zero training error (MSE = 0.001) but exhibits very high error on the held-out test set (MSE = 48.2). What is the most likely diagnosis?",
      "subtopic": "Model Diagnostics",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "Adjusted $R^2$ penalizes Model 2 for consuming 24 additional degrees of freedom without improving predictive variance explained. Occam's razor favors Model 1.",
      "id": "cml03-q09",
      "options": [
        {
          "id": "A",
          "text": "Classification Accuracy"
        },
        {
          "id": "B",
          "text": "Adjusted $R^2$ (or AIC / BIC)"
        },
        {
          "id": "C",
          "text": "Precision score"
        },
        {
          "id": "D",
          "text": "Recall score"
        }
      ],
      "question": "Two candidate linear regression models achieve identical holdout $R^2$ = 0.78, but Model 1 uses 4 predictors while Model 2 uses 28 predictors. Which complexity-aware metric allows a principled comparison?",
      "subtopic": "Adjusted R^2",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "A"
      ],
      "difficulty": "medium",
      "explanation": "Option A strictly implements the mathematical formulas: $SSE = \\sum (y - \\hat{y})^2$, $SST = \\sum (y - \\bar{y})^2$, $R^2 = 1 - \\frac{SSE}{SST}$, and $R^2_{\\text{adj}} = 1 - (1 - $R^2$) \\frac{n - 1}{n - p - 1}$.",
      "id": "cml03-q10",
      "options": [
        {
          "id": "A",
          "text": "sse = np.sum((y_true - y_pred)**2)\nsst = np.sum((y_true - np.mean(y_true))**2)\nr2 = 1 - (sse / sst)\nr2_adj = 1 - (1 - r2) * (len(y_true) - 1) / (len(y_true) - p - 1)"
        },
        {
          "id": "B",
          "text": "sse = np.mean(y_true - y_pred)\nsst = np.var(y_pred)\nr2 = sse / sst\nr2_adj = r2 * (p / len(y_true))"
        },
        {
          "id": "C",
          "text": "r2 = np.corrcoef(y_true, y_pred)\nr2_adj = r2 - p"
        },
        {
          "id": "D",
          "text": "sse = np.max(np.abs(y_true - y_pred))\nsst = np.min(y_true)\nr2 = 1 - sse/sst\nr2_adj = r2"
        }
      ],
      "question": "Which Python implementation correctly calculates $R^2$ and Adjusted $R^2$ using NumPy from first principles without relying on scikit-learn?",
      "subtopic": "Code Implementation",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "By defining $x_0 = 1$ for every observation, the augmented feature vector $\\mathbf{x} = [1, x_1, \\dots, x_d]^T$ and parameter vector $\\boldsymbol{\\theta} = [\\theta_0, \\theta_1, \\dots, \\theta_d]^T$ combine into $h(\\mathbf{x}) = \\boldsymbol{\\theta}^T \\mathbf{x}$.",
      "id": "cml03-q11",
      "options": [
        {
          "id": "A",
          "text": "Setting all slope parameters $\\theta_1, \\dots, \\theta_d$ to zero."
        },
        {
          "id": "B",
          "text": "Appending a dummy constant feature $x_0 = 1$ to every feature vector $\\mathbf{x}$, allowing hypothesis $h_{\\boldsymbol{\\theta}}(\\mathbf{x}) = \\theta_0 + \\sum_{j=1}^d \\theta_j x_j$ to be expressed as a single vector dot product $\\boldsymbol{\\theta}^T \\mathbf{x}$."
        },
        {
          "id": "C",
          "text": "Centering the target variable y so that the intercept is eliminated entirely."
        },
        {
          "id": "D",
          "text": "Using a random number generator to initialize $\\theta_0$."
        }
      ],
      "question": "What is the Intercept Trick in multivariate linear regression?",
      "subtopic": "Hypothesis & Intercept Trick",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "easy",
      "explanation": "Differentiating (h(x) - y)^2 by the chain rule produces 2(h(x) - y)x. Multiplying by 1/2 cancels the 2, leaving the clean gradient expression (h(x) - y)x.",
      "id": "cml03-q12",
      "options": [
        {
          "id": "A",
          "text": "It guarantees that the cost function is convex."
        },
        {
          "id": "B",
          "text": "It is an algebraic convenience that neatly cancels the power of 2 when taking the first derivative $\\nabla_{\\boldsymbol{\\theta}} J$."
        },
        {
          "id": "C",
          "text": "It ensures the learning rate $\\alpha$ does not exceed 1.0."
        },
        {
          "id": "D",
          "text": "It converts the cost into a probability density function."
        }
      ],
      "question": "In the Ordinary Least Squares objective $J(\\boldsymbol{\\theta}) = \\frac{1}{2m} \\sum_{i=1}^m (h_{\\boldsymbol{\\theta}}(\\mathbf{x}^{(i)}) - y^{(i)})^2$, what is the role of the leading constant factor 1/2?",
      "subtopic": "OLS Objective",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "hard",
      "explanation": "Maximizing the log-likelihood of Gaussian densities $\\ln L = -n\\ln(\\sqrt{2\\pi}\\sigma) - \\frac{1}{2\\sigma^2}\\sum (y^{(i)} - \\boldsymbol{\\theta}^T\\mathbf{x}^{(i)})^2$. Dropping constants and inverting the negative sign exactly yields minimization of the OLS sum of squared errors.",
      "id": "cml03-q13",
      "options": [
        {
          "id": "A",
          "text": "When the target variable follows a Poisson distribution."
        },
        {
          "id": "B",
          "text": "When the observation noise errors $\\epsilon^{(i)}$ are additive, independent, and identically distributed (i.i.d.) Gaussian: $\\epsilon^{(i)} \\sim \\mathcal{N}(0, \\sigma^2)$."
        },
        {
          "id": "C",
          "text": "When the features follow a uniform distribution in [0, 1]."
        },
        {
          "id": "D",
          "text": "When the errors follow a Cauchy distribution."
        }
      ],
      "question": "Under what probabilistic assumption is minimizing the Ordinary Least Squares cost function mathematically equivalent to Maximum Likelihood Estimation (MLE)?",
      "subtopic": "MLE Derivation",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "medium",
      "explanation": "Setting the matrix gradient $\\nabla_{\\boldsymbol{\\theta}} J = X^T X \\boldsymbol{\\theta} - X^T \\mathbf{y} = \\mathbf{0}$ yields $X^T X \\boldsymbol{\\theta} = X^T \\mathbf{y}$. Multiplying by $(X^TX)^{-1}$ gives $\\boldsymbol{\\theta}^* = (X^TX)^{-1} X^T \\mathbf{y}$.",
      "id": "cml03-q14",
      "options": [
        {
          "id": "A",
          "text": "$\\boldsymbol{\\theta}^* = X (X^TX)^{-1} \\mathbf{y}$"
        },
        {
          "id": "B",
          "text": "$\\boldsymbol{\\theta}^* = (X^TX)^{-1} X^T \\mathbf{y}$"
        },
        {
          "id": "C",
          "text": "$\\boldsymbol{\\theta}^* = (XX^T)^{-1} X \\mathbf{y}$"
        },
        {
          "id": "D",
          "text": "$\\boldsymbol{\\theta}^* = X^T (XX^T)^{-1} \\mathbf{y}$"
        }
      ],
      "question": "Assuming the Gram matrix $X^TX$ is non-singular (full column rank), what is the celebrated analytical closed-form solution known as the Normal Equation?",
      "subtopic": "Normal Equation",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "hard",
      "explanation": "The prediction $\\hat{\\mathbf{y}} = X\\boldsymbol{\\theta}^*$ is a linear combination of the columns of $X$ and thus lies in $\\text{col}(X)$. The residual error vector $\\mathbf{e} = \\mathbf{y} - \\hat{\\mathbf{y}}$ is orthogonal (perpendicular / normal) to every column of $X$: $X^T(\\mathbf{y} - X\\boldsymbol{\\theta}^*) = \\mathbf{0}$.",
      "id": "cml03-q15",
      "options": [
        {
          "id": "A",
          "text": "It is an arbitrary rotation of the target vector $\\mathbf{y}$ into the null space of X."
        },
        {
          "id": "B",
          "text": "It is the orthogonal projection of the observed target vector $\\mathbf{y}$ onto the column space of the design matrix, $\\text{col}(X)$."
        },
        {
          "id": "C",
          "text": "It is the tangent hyperplane intersecting the origin."
        },
        {
          "id": "D",
          "text": "It is a non-linear kernel embedding."
        }
      ],
      "question": "What is the geometric interpretation of the prediction vector $\\hat{\\mathbf{y}} = X\\boldsymbol{\\theta}^*$ produced by Ordinary Least Squares in $\\mathbb{R}^n$?",
      "subtopic": "Geometric Projection",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "A"
      ],
      "difficulty": "hard",
      "explanation": "H is symmetric (H = H^T) and idempotent (H^2 = H). Using the cyclic property of the trace: \\text{Tr}(H) = \\text{Tr}(X(X^TX)^{-1} X^T) = \\text{Tr}((X^TX)^{-1} ($X^TX$)) = \\text{Tr}(I_{d+1}) = d + 1 (the number of fitted parameters).",
      "id": "cml03-q16",
      "options": [
        {
          "id": "A",
          "text": "$H$ projects $\\mathbf{y}$ onto $\\hat{\\mathbf{y}}$ (it puts the 'hat' on $y$); its trace equals the effective degrees of freedom ($d + 1$)."
        },
        {
          "id": "B",
          "text": "H is the inverse of the covariance matrix; its trace is always 0."
        },
        {
          "id": "C",
          "text": "H is an upper-triangular matrix; its trace is equal to n."
        },
        {
          "id": "D",
          "text": "H is a scalar loss value; its trace is undefined."
        }
      ],
      "question": "What is the Hat Matrix H = X(X^TX)^{-1} X^T, and what is its mathematical trace \\text{Tr}(H)?",
      "subtopic": "Hat Matrix",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "medium",
      "explanation": "Computing the Gram matrix $X^TX$ requires $\\mathcal{O}(n d^2)$ operations. Inverting the $(d+1) \\times (d+1)$ Gram matrix requires $\\mathcal{O}(d^3)$ operations. Total complexity is $\\mathcal{O}(n d^2 + d^3)$.",
      "id": "cml03-q17",
      "options": [
        {
          "id": "A",
          "text": "$\\mathcal{O}(n \\log d)$"
        },
        {
          "id": "B",
          "text": "$\\mathcal{O}(n d^2 + d^3)$"
        },
        {
          "id": "C",
          "text": "\\mathcal{O}(d)"
        },
        {
          "id": "D",
          "text": "\\mathcal{O}(n^3)"
        }
      ],
      "question": "What is the computational time complexity of solving the Normal Equation $\\boldsymbol{\\theta}^* = (X^TX)^{-1} X^T \\mathbf{y}$ for a dataset with $n$ instances and $d$ features?",
      "subtopic": "Computational Complexity",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "A"
      ],
      "difficulty": "medium",
      "explanation": "Inverting a matrix when $d > 10{,}000$ is computationally prohibitive or impossible due to $\\mathcal{O}(d^3)$ scaling. Gradient descent scales as $\\mathcal{O}(k \\cdot nd)$, making it far superior for high-dimensional or streaming big-data settings.",
      "id": "cml03-q18",
      "options": [
        {
          "id": "A",
          "text": "When the number of features d is extremely large (e.g., d > 10,000) or when training data arrives in a continuous stream."
        },
        {
          "id": "B",
          "text": "Only when the cost function is non-convex."
        },
        {
          "id": "C",
          "text": "Never; the Normal Equation is always faster regardless of d."
        },
        {
          "id": "D",
          "text": "Only when feature scaling is omitted."
        }
      ],
      "question": "When should an engineer prefer iterative Gradient Descent over the analytical Normal Equation for linear regression?",
      "subtopic": "Computational Complexity",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "medium",
      "explanation": "On a test set, $R^2 = 1 - \\frac{SS_{\\text{res}}}{SS_{\\text{tot}}}$. If a model performs worse than a simple horizontal line predicting the mean of the training target, SS_{res} exceeds SS_{tot}, driving $R^2$ below zero (indicating catastrophic failure).",
      "id": "cml03-q19",
      "options": [
        {
          "id": "A",
          "text": "No, because squares are always non-negative."
        },
        {
          "id": "B",
          "text": "Yes, on a held-out test set if the model makes worse predictions than the naive baseline model $\\hat{y} = \\bar{y}_{\\text{train}}$, causing $SS_{\\text{res}} > SS_{\\text{tot}}$."
        },
        {
          "id": "C",
          "text": "Yes, but only if the learning rate is negative."
        },
        {
          "id": "D",
          "text": "No, Scikit-learn clips $R^2$ to [0, 1] automatically."
        }
      ],
      "question": "Can the Coefficient of Determination $R^2$ ever be negative?",
      "subtopic": "R^2 & Metric Calculations",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "medium",
      "explanation": "Regression coefficients measure partial linear associations conditional on holding other features constant ('ceteris paribus'). If total square footage is held constant, adding another bedroom forces every room to be smaller and more cramped.",
      "id": "cml03-q20",
      "options": [
        {
          "id": "A",
          "text": "Building an additional bedroom causes property value to decrease by $12,000."
        },
        {
          "id": "B",
          "text": "Holding square footage and other covariates constant, each additional bedroom associates with an estimated $12,000 decrease in price (reflecting smaller, more cramped room layouts)."
        },
        {
          "id": "C",
          "text": "The model has a syntax error in the gradient descent loop."
        },
        {
          "id": "D",
          "text": "Bedrooms is an irrelevant feature with zero variance."
        }
      ],
      "question": "In a fitted housing price model, \\widehat{\\text{Price}} = 50,000 + 150(\\text{SqFt}) - 12,000(\\text{Bedrooms}). How should the negative coefficient on 'Bedrooms' (-12,000) be interpreted?",
      "subtopic": "Coefficient Interpretation",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "medium",
      "explanation": "Association does not imply causation. Regression coefficients reflect conditional correlation; without randomized controlled trials or causal identification strategies (instrumental variables, DAGs), unobserved confounders bias coefficients away from true causal effects.",
      "id": "cml03-q21",
      "options": [
        {
          "id": "A",
          "text": "Because linear algebra cannot be computed on observational data."
        },
        {
          "id": "B",
          "text": "Because omitted variable bias, confounders, selection bias, and reverse causality create non-causal associations between X and Y."
        },
        {
          "id": "C",
          "text": "Because Scikit-Learn algorithms are proprietary."
        },
        {
          "id": "D",
          "text": "Because linear regression assumes zero variance in features."
        }
      ],
      "question": "Why are observational regression coefficients $\\boldsymbol{\\theta}$ generally NOT valid causal effect estimates?",
      "subtopic": "Coefficient Interpretation",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "B"
      ],
      "difficulty": "hard",
      "explanation": "The rank of $X \\in \\mathbb{R}^{n \\times (d+1)}$ is at most $n$. The Gram matrix $X^TX$ is $(d+1) \\times (d+1)$. If $n < d+1$, $X^TX$ has rank at most $n < d+1$, making it rank-deficient and singular ($\\det = 0$). Regularization (Ridge) is required to make it invertible.",
      "id": "cml03-q22",
      "options": [
        {
          "id": "A",
          "text": "$X^TX$ becomes an identity matrix."
        },
        {
          "id": "B",
          "text": "$X^TX$ is strictly non-invertible (singular) because its rank is at most n < d+1, yielding infinitely many solutions that achieve zero training error."
        },
        {
          "id": "C",
          "text": "$X^TX$ has a determinant of $+\\infty$."
        },
        {
          "id": "D",
          "text": "The Normal Equation automatically defaults to L1 Lasso."
        }
      ],
      "question": "What happens to the Gram matrix $X^TX$ when the number of features d exceeds the number of training observations n (d > n)?",
      "subtopic": "Normal Equation",
      "type": "single_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "difficulty": "medium",
      "explanation": "A, B, and C are mathematical facts: both share y's units; squaring makes RMSE sensitive to large misses; and by Jensen's inequality RMSE >= MAE. D is false: MAE has a non-differentiable corner at error = 0, whereas MSE is $C^\\infty$ smooth.",
      "id": "cml03-q23",
      "options": [
        {
          "id": "A",
          "text": "Both MAE and RMSE are expressed in the exact same physical units as the target variable y."
        },
        {
          "id": "B",
          "text": "RMSE penalizes large outlier errors much more severely than MAE because errors are squared before averaging."
        },
        {
          "id": "C",
          "text": "RMSE is always greater than or equal to MAE (RMSE >= MAE)."
        },
        {
          "id": "D",
          "text": "MAE is everywhere smoothly differentiable, whereas RMSE has an undefined gradient at zero."
        }
      ],
      "question": "Which of the following statements are TRUE regarding the comparison between MAE (Mean Absolute Error) and RMSE (Root Mean Squared Error)? (Select ALL that apply)",
      "subtopic": "R^2 & Metric Calculations",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "difficulty": "medium",
      "explanation": "A, B, and C cause rank-deficiency in X, rendering $X^TX$ singular. D (standardization) maintains matrix rank and often improves numerical stability.",
      "id": "cml03-q24",
      "options": [
        {
          "id": "A",
          "text": "The number of training samples n is smaller than the number of features d (n < d)."
        },
        {
          "id": "B",
          "text": "Two or more feature columns are exact linear duplicates (perfect multicollinearity, e.g., square feet and square meters)."
        },
        {
          "id": "C",
          "text": "The dummy variable trap: including all K one-hot columns while also retaining the constant intercept column $x_0 = 1$."
        },
        {
          "id": "D",
          "text": "All features have been standardized using StandardScaler."
        }
      ],
      "question": "Which of the following conditions cause the Gram matrix $X^TX$ to become non-invertible (singular)? (Select ALL that apply)",
      "subtopic": "Normal Equation",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "difficulty": "hard",
      "explanation": "A, B, and C are fundamental projection matrix theorems. D is false: \\text{Tr}(H) = d + 1 (the number of parameters), not n.",
      "id": "cml03-q25",
      "options": [
        {
          "id": "A",
          "text": "H is symmetric: H = H^T."
        },
        {
          "id": "B",
          "text": "H is idempotent: H^2 = H."
        },
        {
          "id": "C",
          "text": "The diagonal elements h_{ii} represent the statistical leverage of the i-th training observation."
        },
        {
          "id": "D",
          "text": "The trace of H is equal to the sample size n."
        }
      ],
      "question": "Which of the following statements regarding the Hat Matrix H = X(X^TX)^{-1} X^T are mathematically TRUE? (Select ALL that apply)",
      "subtopic": "Hat Matrix",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "difficulty": "medium",
      "explanation": "All four statements are mathematically correct characterizations of $R^2$.",
      "id": "cml03-q26",
      "options": [
        {
          "id": "A",
          "text": "On the training set with an intercept term, $R^2$ is guaranteed to lie in the interval [0, 1]."
        },
        {
          "id": "B",
          "text": "$R^2$ measures the fraction of target variance explained by the model."
        },
        {
          "id": "C",
          "text": "Adding random Gaussian noise features to an OLS training set will never cause training $R^2$ to decrease."
        },
        {
          "id": "D",
          "text": "A negative test $R^2$ means the model performs worse than simply predicting the training mean baseline \\bar{y}."
        }
      ],
      "question": "Which of the following statements about $R^2$ (Coefficient of Determination) are TRUE? (Select ALL that apply)",
      "subtopic": "R^2 & Metric Calculations",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "difficulty": "hard",
      "explanation": "A, B, and C are the three core theoretical justifications of OLS. D is false: OLS is notoriously sensitive to outliers precisely because errors are squared.",
      "id": "cml03-q27",
      "options": [
        {
          "id": "A",
          "text": "From statistical decision theory, minimizing expected squared error estimates the conditional expectation E[Y | X = x]."
        },
        {
          "id": "B",
          "text": "Under the assumption of additive i.i.d. Gaussian error, OLS is the Maximum Likelihood Estimator (MLE)."
        },
        {
          "id": "C",
          "text": "The OLS cost function is strictly convex and everywhere infinitely differentiable ($C^\\infty$), enabling clean analytical and gradient solutions."
        },
        {
          "id": "D",
          "text": "OLS completely eliminates the influence of extreme outliers."
        }
      ],
      "question": "Which of the following are valid justifications for minimizing Sum of Squared Errors (OLS) rather than Sum of Absolute Errors (L1)? (Select ALL that apply)",
      "subtopic": "OLS Objective",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "difficulty": "hard",
      "explanation": "A, B, and D depend heavily on scaling: GD convergence requires scaling; coefficient comparison requires scaling; and L2 regularization penalizes $\\sum \\theta_j^2$ which is scale-dependent. C is invariant: unregularized OLS predictions are invariant to non-singular linear feature transformations.",
      "id": "cml03-q28",
      "options": [
        {
          "id": "A",
          "text": "The speed and stability of Gradient Descent convergence."
        },
        {
          "id": "B",
          "text": "The direct comparability of standardized regression coefficients $\\theta_j$ to determine relative feature importance."
        },
        {
          "id": "C",
          "text": "The exact analytical predictions $\\hat{\\mathbf{y}}$ produced by the Normal Equation (assuming full rank and no numerical precision issues)."
        },
        {
          "id": "D",
          "text": "L2 regularization shrinkage dynamics (Ridge regression)."
        }
      ],
      "question": "In multivariate linear regression, which of the following operations are affected by whether feature scaling was performed? (Select ALL that apply)",
      "subtopic": "Feature Scaling",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "difficulty": "hard",
      "explanation": "Because the first column of $X$ is the intercept $x_0 = 1$, the normal equation implies $\\mathbf{1}^T \\mathbf{e} = \\sum e_i = 0$, so mean is zero. Furthermore, $\\hat{\\mathbf{y}} \\in \\text{col}(X)$ while $\\mathbf{e} \\perp \\text{col}(X)$, so $\\mathbf{e}^T \\hat{\\mathbf{y}} = 0$.",
      "id": "cml03-q29",
      "options": [
        {
          "id": "A",
          "text": "The sum of the training residuals is strictly zero: $\\sum_{i=1}^n e_i = 0$."
        },
        {
          "id": "B",
          "text": "The sample mean of the training residuals is strictly zero: \\bar{e} = 0."
        },
        {
          "id": "C",
          "text": "The residual vector $\\mathbf{e}$ is orthogonal to the fitted prediction vector $\\hat{\\mathbf{y}}$: $\\mathbf{e}^T \\hat{\\mathbf{y}} = 0$."
        },
        {
          "id": "D",
          "text": "The residual vector is identical to the design matrix X."
        }
      ],
      "question": "Which of the following statements regarding the residual error vector $\\mathbf{e} = \\mathbf{y} - \\hat{\\mathbf{y}}$ in an OLS model with an intercept term are TRUE? (Select ALL that apply)",
      "subtopic": "Geometric Projection",
      "type": "multi_choice"
    },
    {
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "difficulty": "medium",
      "explanation": "A, B, and D are true: Adding noise slightly fits chance fluctuations in the training sample, so raw $R^2$ stays same or rises slightly. However, Adjusted $R^2$ drops due to the penalty, correctly alerting the engineer to avoid useless complexity.",
      "id": "cml03-q30",
      "options": [
        {
          "id": "A",
          "text": "Raw training $R^2$ will slightly increase or remain identical."
        },
        {
          "id": "B",
          "text": "Adjusted $R^2$ will decrease because the degrees of freedom penalty (n-1)/(n-p-1) outweighs the negligible reduction in SSE."
        },
        {
          "id": "C",
          "text": "Adjusted $R^2$ will increase to 1.0."
        },
        {
          "id": "D",
          "text": "Adjusted $R^2$ correctly signals that adding the noise variable damaged model parsimony."
        }
      ],
      "question": "What happens to Adjusted $R^2$ when an uninformative noise predictor (pure random Gaussian numbers uncorrelated with y) is added to a regression model? (Select ALL that apply)",
      "subtopic": "Adjusted R^2",
      "type": "multi_choice"
    }
  ],
  "title": "Multivariate Linear Regression Deep Dive Quiz",
  "topicId": "lecture-03"
}
