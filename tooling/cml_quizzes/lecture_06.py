QUIZ_L06 = {
  "topicId": "lecture-06",
  "lectureNumber": 6,
  "title": "Generalization: Bias-Variance Decomposition & Polynomial Fitting",
  "description": "25 questions covering Polynomial Regression, feature explosion, underfitting vs overfitting, mathematical Bias-Variance decomposition, irreducible error, Occam's razor, and model complexity curves.",
  "estimatedMinutes": 35,
  "questions": [
    {
      "id": "cml-l06-q01",
      "type": "single_choice",
      "question": "Why is Polynomial Regression mathematically classified as a 'linear model' despite fitting nonlinear curves to data?",
      "options": [
        {
          "id": "A",
          "text": "Because it always fits a straight line in the original input space"
        },
        {
          "id": "B",
          "text": "Because the model is linear in the parameters (coefficients $\\beta$), satisfying $y = X_\\text{poly} \\beta + \\epsilon$"
        },
        {
          "id": "C",
          "text": "Because the loss function is linear with respect to residual errors"
        },
        {
          "id": "D",
          "text": "Because the degree of the polynomial is restricted to 1"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Linearity in machine learning and statistics refers strictly to linearity with respect to the unknown parameters $\\beta$. In $y = \\beta_0 + \\beta_1 x + \\beta_2 x^2 + \\dots + \\beta_d x^d$, each term $\\beta_j$ enters linearly, allowing closed-form OLS solutions.",
      "difficulty": "easy",
      "subtopic": "Linearity in Parameters"
    },
    {
      "id": "cml-l06-q02",
      "type": "single_choice",
      "question": "In the mathematical Bias-Variance decomposition of the expected test mean squared error $\\mathbb{E}[(y - \\hat{f}(x))^2]$, what are the three fundamental components?",
      "options": [
        {
          "id": "A",
          "text": "$\\text{Bias}(\\hat{f}(x)) + \\text{Variance}(\\hat{f}(x)) + \\text{Residuals}$"
        },
        {
          "id": "B",
          "text": "$[\\text{Bias}(\\hat{f}(x))]^2 + \\text{Var}(\\hat{f}(x)) + \\sigma^2$ (where $\\sigma^2$ is irreducible error)"
        },
        {
          "id": "C",
          "text": "$\\text{Precision} + \\text{Recall} + F_1$"
        },
        {
          "id": "D",
          "text": "$R^2 + \\text{Adjusted } R^2 + SSE$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The expected generalization error decomposes exactly as $\\mathbb{E}[(y - \\hat{f}(x))^2] = [\\mathbb{E}[\\hat{f}(x)] - f(x)]^2 + \\mathbb{E}[(\\hat{f}(x) - \\mathbb{E}[\\hat{f}(x)])^2] + \\text{Var}(\\epsilon) = \\text{Bias}^2 + \\text{Variance} + \\sigma^2$.",
      "difficulty": "medium",
      "subtopic": "Bias-Variance Decomposition"
    },
    {
      "id": "cml-l06-q03",
      "type": "single_choice",
      "question": "What is 'irreducible error' ($\\sigma^2$) in the context of supervised learning?",
      "options": [
        {
          "id": "A",
          "text": "The training loss that remains after running 1000 epochs of gradient descent"
        },
        {
          "id": "B",
          "text": "The noise inherent in the true data-generating process (unobserved variables, measurement error) that no model can eliminate"
        },
        {
          "id": "C",
          "text": "The error caused by choosing an insufficiently high polynomial degree"
        },
        {
          "id": "D",
          "text": "The rounding error inherent in 32-bit floating point arithmetic"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Irreducible error $\\sigma^2 = \\text{Var}(\\epsilon)$ is the variance of the true label noise conditioned on $x$. Even if we knew the true function $f(x)$ perfectly, we cannot predict individual unobserved stochastic fluctuations $\\epsilon$.",
      "difficulty": "easy",
      "subtopic": "Irreducible Error"
    },
    {
      "id": "cml-l06-q04",
      "type": "single_choice",
      "question": "What mathematical phenomenon occurs if you fit an $n$-degree polynomial regression model to exactly $n+1$ distinct data points?",
      "options": [
        {
          "id": "A",
          "text": "The model will have high bias and low variance"
        },
        {
          "id": "B",
          "text": "The model interpolates all $n+1$ points perfectly, achieving $R^2 = 1.0$ and training error = 0, but oscillates wildly between points with massive test error (overfitting)"
        },
        {
          "id": "C",
          "text": "The model will automatically regularize itself to a simple line"
        },
        {
          "id": "D",
          "text": "The normal equation matrix $X^TX$ is guaranteed to be non-invertible"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "By polynomial interpolation (Lagrange interpolation), an $n$-degree polynomial with $n+1$ coefficients can pass exactly through any $n+1$ distinct points. This zeroes out training MSE but introduces extreme oscillatory variance (Runge's phenomenon) on unseen points.",
      "difficulty": "medium",
      "subtopic": "Exact Interpolation & Runge"
    },
    {
      "id": "cml-l06-q05",
      "type": "single_choice",
      "question": "When model complexity (e.g., polynomial degree) increases continuously, how do training error and validation/test error typically behave?",
      "options": [
        {
          "id": "A",
          "text": "Both training error and validation error decrease monotonically to 0"
        },
        {
          "id": "B",
          "text": "Training error increases, while validation error decreases monotonically"
        },
        {
          "id": "C",
          "text": "Training error decreases monotonically toward 0, while validation error exhibits a U-shaped curve (decreasing then exploding upwards)"
        },
        {
          "id": "D",
          "text": "Both training and validation error remain completely constant"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "As complexity increases, the model fits the training data more tightly, driving training error monotonically downward. However, validation error decreases while bias drops, reaches a sweet spot, and then surges upward as variance dominates (classic U-shaped curve).",
      "difficulty": "easy",
      "subtopic": "Complexity Curves"
    },
    {
      "id": "cml-l06-q06",
      "type": "single_choice",
      "question": "A machine learning model exhibits very high training error (e.g., 25% MSE) and an almost identical high test error (26% MSE). What diagnosis and initial prescription should you make?",
      "options": [
        {
          "id": "A",
          "text": "High Variance (Overfitting); add L1/L2 regularization and collect more training samples"
        },
        {
          "id": "B",
          "text": "High Bias (Underfitting); increase model capacity, add polynomial/interaction terms, or use a richer model class"
        },
        {
          "id": "C",
          "text": "Target leakage; re-split the dataset into train and test folds"
        },
        {
          "id": "D",
          "text": "Multicollinearity; drop half of the features"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "When both training and test errors are unacceptably high and close together, the model lacks sufficient capacity to capture the underlying pattern (high bias / underfitting). The remedy is increasing model complexity or feature engineering.",
      "difficulty": "easy",
      "subtopic": "High Bias Diagnosis"
    },
    {
      "id": "cml-l06-q07",
      "type": "single_choice",
      "question": "A machine learning model exhibits 0.1% training MSE, but its test set MSE is 38.5%. What diagnosis and remedy are appropriate?",
      "options": [
        {
          "id": "A",
          "text": "High Bias; remove regularization to let the model fit deeper"
        },
        {
          "id": "B",
          "text": "High Variance (Overfitting); introduce regularization, simplify the model, or collect more training data"
        },
        {
          "id": "C",
          "text": "Data scaling error; multiply test features by 100"
        },
        {
          "id": "D",
          "text": "Gauss-Markov failure; switch to Normal Equation"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A vast generalization gap (near-zero training error accompanied by high test error) is the textbook indicator of high variance / overfitting. Remedies include regularization, feature selection, and augmenting training data.",
      "difficulty": "easy",
      "subtopic": "High Variance Diagnosis"
    },
    {
      "id": "cml-l06-q08",
      "type": "single_choice",
      "question": "In Scikit-Learn, which class is used to generate polynomial and interaction features from an input matrix $X$?",
      "options": [
        {
          "id": "A",
          "text": "`sklearn.preprocessing.PolynomialFeatures`"
        },
        {
          "id": "B",
          "text": "`sklearn.linear_model.PolynomialRegression`"
        },
        {
          "id": "C",
          "text": "`sklearn.feature_selection.PolyFeatures`"
        },
        {
          "id": "D",
          "text": "`sklearn.decomposition.PolynomialKernel`"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "`PolynomialFeatures` is the transformer in `sklearn.preprocessing` that expands a feature vector $[x_1, x_2]$ into $[1, x_1, x_2, x_1^2, x_1 x_2, x_2^2]$ up to a specified `degree`.",
      "difficulty": "easy",
      "subtopic": "Scikit-Learn Preprocessing"
    },
    {
      "id": "cml-l06-q09",
      "type": "single_choice",
      "question": "If you have $p = 10$ input features and you generate polynomial features of degree $d = 3$ (including intercept), how does the total number of features expand?",
      "options": [
        {
          "id": "A",
          "text": "$10 \\times 3 = 30$ features"
        },
        {
          "id": "B",
          "text": "$\\binom{10 + 3}{3} = \\frac{13 \\times 12 \\times 11}{6} = 286$ features"
        },
        {
          "id": "C",
          "text": "$10^3 = 1000$ features"
        },
        {
          "id": "D",
          "text": "$3^{10} = 59{,}049$ features"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The number of monomials of degree up to $d$ in $p$ variables (including intercept) is given by the multiset combination $\\binom{p+d}{d} = \\frac{(p+d)!}{p! d!}$. For $p=10, d=3$, $\\binom{13}{3} = \\frac{13 \\times 12 \\times 11}{3 \\times 2 \\times 1} = 286$.",
      "difficulty": "hard",
      "subtopic": "Feature Combinatorics"
    },
    {
      "id": "cml-l06-q10",
      "type": "single_choice",
      "question": "What is the philosophical and scientific principle known as 'Occam\u2019s Razor' in machine learning model selection?",
      "options": [
        {
          "id": "A",
          "text": "Models should always use as many features as computationally feasible to maximize capacity"
        },
        {
          "id": "B",
          "text": "Among competing hypotheses or models that explain the data equally well, the simplest one (with fewest assumptions and parameters) should be selected"
        },
        {
          "id": "C",
          "text": "All features must be cut into binary categories using decision trees"
        },
        {
          "id": "D",
          "text": "The fastest training algorithm is always preferred regardless of accuracy"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Occam's razor (lex parsimoniae) dictates that simpler models with comparable empirical fit generalize better because they possess fewer degrees of freedom to memorize idiosyncratic dataset noise.",
      "difficulty": "easy",
      "subtopic": "Occam's Razor"
    },
    {
      "id": "cml-l06-q11",
      "type": "single_choice",
      "question": "Why does generating high-degree polynomial terms (e.g. $x, x^2, x^3, x^4, x^5$) without centering or scaling induce severe numerical instability in OLS regression?",
      "options": [
        {
          "id": "A",
          "text": "Because polynomial terms of the same variable are naturally highly collinear, leading to massive condition numbers in $X^TX$"
        },
        {
          "id": "B",
          "text": "Because high powers evaluate to imaginary complex numbers for real inputs"
        },
        {
          "id": "C",
          "text": "Because polynomial regression requires all targets to be zero-centered"
        },
        {
          "id": "D",
          "text": "Because it violates the linear independence of columns in an uninvertible way"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "As powers increase, curves like $x^2, x^3, x^4$ track each other closely on positive domains, producing high structural multicollinearity and causing $X^TX$ to have tiny eigenvalues and near-singular condition numbers.",
      "difficulty": "medium",
      "subtopic": "Polynomial Multicollinearity"
    },
    {
      "id": "cml-l06-q12",
      "type": "single_choice",
      "question": "What is the Akaike Information Criterion (AIC) formula for linear models with $k$ parameters, and how is it used in model selection?",
      "options": [
        {
          "id": "A",
          "text": "$\\text{AIC} = 2k - 2\\ln(\\hat{L})$; models with lower AIC are preferred as they balance likelihood against complexity penalty $2k$"
        },
        {
          "id": "B",
          "text": "$\\text{AIC} = k \\ln(n) - 2\\ln(\\hat{L})$; models with highest AIC are preferred"
        },
        {
          "id": "C",
          "text": "$\\text{AIC} = \\frac{SSE}{n - k}$"
        },
        {
          "id": "D",
          "text": "$\\text{AIC} = R^2 - \\text{Adjusted } R^2$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "AIC rewards goodness of fit (log-likelihood $\\ln(\\hat{L})$) while penalizing the number of estimated parameters ($2k$). Minimizing AIC identifies the most parsimonious model.",
      "difficulty": "medium",
      "subtopic": "Information Criteria"
    },
    {
      "id": "cml-l06-q13",
      "type": "single_choice",
      "question": "How does the Bayesian Information Criterion (BIC) penalty compare to the Akaike Information Criterion (AIC) penalty for large sample sizes ($n > e^2 \\approx 7.4$)?",
      "options": [
        {
          "id": "A",
          "text": "BIC has a weaker penalty, favoring overly complex models"
        },
        {
          "id": "B",
          "text": "BIC penalizes complexity by $k \\ln(n)$ instead of $2k$, imposing a harsher penalty for additional parameters when $n > 7$ and favoring simpler models"
        },
        {
          "id": "C",
          "text": "BIC and AIC have identical mathematical formulas"
        },
        {
          "id": "D",
          "text": "BIC does not depend on sample size $n$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "BIC replaces the constant $2k$ penalty with $k \\ln(n)$. When $n > 8$, $\\ln(n) > 2$, which penalizes extra parameters more severely than AIC, steering selection toward simpler, more parsimonious models.",
      "difficulty": "hard",
      "subtopic": "BIC vs AIC"
    },
    {
      "id": "cml-l06-q14",
      "type": "single_choice",
      "question": "How does increasing the size of the training dataset $m$ affect the bias and variance of a fixed-complexity model?",
      "options": [
        {
          "id": "A",
          "text": "It increases variance and reduces bias"
        },
        {
          "id": "B",
          "text": "It reduces model variance because the estimator converges to its expected prediction, but does not eliminate asymptotic model bias"
        },
        {
          "id": "C",
          "text": "It eliminates irreducible error $\\sigma^2$"
        },
        {
          "id": "D",
          "text": "It makes the training loss drop strictly to zero"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "More training samples suppress sample-to-sample parameter variance (by the Law of Large Numbers, $\\text{Var}(\\hat{\\beta}) \\propto 1/n$). However, if the underlying model is fundamentally misspecified (e.g. fitting a straight line to a sine wave), the structural bias remains unchanged.",
      "difficulty": "medium",
      "subtopic": "Sample Size vs Bias-Variance"
    },
    {
      "id": "cml-l06-q15",
      "type": "single_choice",
      "question": "In polynomial regression, what is 'Runge's phenomenon'?",
      "options": [
        {
          "id": "A",
          "text": "The failure of gradient descent to converge when features are scaled"
        },
        {
          "id": "B",
          "text": "Violent oscillations at the edges of an interpolation interval when fitting high-degree polynomials with equidistant interpolation points"
        },
        {
          "id": "C",
          "text": "The linear decay of the condition number of a Vandermonde matrix"
        },
        {
          "id": "D",
          "text": "The saturation of the sigmoid activation function"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Discovered by Carl Runge in 1901, fitting high-degree polynomials over equidistant grid points causes wild oscillations near the boundaries of the domain, illustrating the perils of high-order polynomial overfitting.",
      "difficulty": "medium",
      "subtopic": "Runge's Phenomenon"
    },
    {
      "id": "cml-l06-q16",
      "type": "single_choice",
      "question": "If you evaluate a model on the same data it was trained on, which of the following is fundamentally true?",
      "options": [
        {
          "id": "A",
          "text": "The measured training error is an optimistic, downwardly-biased estimate of the true generalization error"
        },
        {
          "id": "B",
          "text": "The training error is always equal to the irreducible error $\\sigma^2$"
        },
        {
          "id": "C",
          "text": "The training error provides an unbiased estimate of future performance"
        },
        {
          "id": "D",
          "text": "The training error is always higher than the test error"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Because optimization algorithms minimize empirical risk on the training set, parameters adapt to both signal and idiosyncratic training noise. Thus, training error is systematically overly optimistic.",
      "difficulty": "easy",
      "subtopic": "Generalization Principles"
    },
    {
      "id": "cml-l06-q17",
      "type": "single_choice",
      "question": "What is the primary role of interaction features (e.g. $x_1 x_2$) created by `PolynomialFeatures(interaction_only=True)`?",
      "options": [
        {
          "id": "A",
          "text": "To capture synergistic effects where the impact of feature $x_1$ on $y$ depends on the level of feature $x_2$"
        },
        {
          "id": "B",
          "text": "To enforce orthogonality between $x_1$ and $x_2$"
        },
        {
          "id": "C",
          "text": "To reduce the dimensionality of the feature space"
        },
        {
          "id": "D",
          "text": "To replace the intercept term with a quadratic constant"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Interaction terms model moderating/synergistic effects: $\\frac{\\partial y}{\\partial x_1} = \\beta_1 + \\beta_{12} x_2$, allowing the slope with respect to $x_1$ to vary as a linear function of $x_2$.",
      "difficulty": "easy",
      "subtopic": "Interaction Effects"
    },
    {
      "id": "cml-l06-q18",
      "type": "single_choice",
      "question": "In learning curves plotting error vs. training set size $m$, what visual signature indicates an underfitting model (high bias)?",
      "options": [
        {
          "id": "A",
          "text": "A huge gap between training error (0.01) and validation error (0.90) that never closes"
        },
        {
          "id": "B",
          "text": "Both training error and validation error plateau quickly at an unacceptably high error level with little to no gap between them"
        },
        {
          "id": "C",
          "text": "Validation error dropping strictly to zero while training error rises"
        },
        {
          "id": "D",
          "text": "Training error continuously decreasing as $m \\to \\infty$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "With high bias, increasing training samples provides no benefit because the model family itself is too rigid. Training error rises slightly and validation error drops slightly until both converge to a high, flat plateau.",
      "difficulty": "medium",
      "subtopic": "Learning Curves Diagnostics"
    },
    {
      "id": "cml-l06-q19",
      "type": "multi_choice",
      "question": "Which of the following actions are effective strategies to reduce high variance (overfitting) in a regression model? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Collect and train on more labeled training data"
        },
        {
          "id": "B",
          "text": "Apply regularization penalties (e.g., Ridge L2 or Lasso L1)"
        },
        {
          "id": "C",
          "text": "Reduce the polynomial degree or perform feature selection to prune unneeded features"
        },
        {
          "id": "D",
          "text": "Add higher-order polynomial terms and interaction combinations"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A (more data anchors parameter estimation), B (regularization constrains weights), and C (reducing capacity reduces variance) all combat overfitting. D adds capacity, worsening overfitting.",
      "difficulty": "easy",
      "subtopic": "Combatting High Variance"
    },
    {
      "id": "cml-l06-q20",
      "type": "multi_choice",
      "question": "Which of the following statements about the Bias-Variance tradeoff are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "A very simple linear model fitted to a complex non-linear reality will typically suffer from high bias and low variance"
        },
        {
          "id": "B",
          "text": "A high-degree polynomial fitted to a small dataset will typically suffer from low bias and high variance"
        },
        {
          "id": "C",
          "text": "Irreducible error can be reduced to zero by using an ensemble of deep models"
        },
        {
          "id": "D",
          "text": "The optimal model complexity minimizes the sum of squared bias and variance, achieving the minimum of the U-shaped expected test loss curve"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "A, B, and D are foundational principles of the Bias-Variance tradeoff. C is false because irreducible error stems from unobserved factors and measurement noise in $y$, not model inadequacy.",
      "difficulty": "medium",
      "subtopic": "Tradeoff Principles"
    },
    {
      "id": "cml-l06-q21",
      "type": "multi_choice",
      "question": "Suppose you fit a polynomial regression model using Scikit-Learn: `make_pipeline(PolynomialFeatures(degree=5), LinearRegression())`. Which steps are required to ensure numerical stability and proper model evaluation? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Insert a feature scaler like `StandardScaler()` after `PolynomialFeatures` to normalize the disparate scales of high-order polynomial powers"
        },
        {
          "id": "B",
          "text": "Evaluate the model using a held-out test set or K-Fold Cross-Validation rather than reporting training $R^2$ alone"
        },
        {
          "id": "C",
          "text": "Fit the scaler and polynomial transformer strictly on the training folds and transform the validation/test folds"
        },
        {
          "id": "D",
          "text": "Compute predictions using the test set targets $y_\\text{test}$ as feature inputs"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A standardizes powers to prevent numerical collinearity issues; B guarantees generalization assessment; C prevents data leakage. D is nonsensical and causes direct target leakage.",
      "difficulty": "medium",
      "subtopic": "Polynomial Pipeline Best Practices"
    },
    {
      "id": "cml-l06-q22",
      "type": "multi_choice",
      "question": "Which metrics or criteria naturally penalize model complexity when comparing competing models? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Adjusted $R^2 = 1 - (1 - R^2) \\frac{n-1}{n-p-1}$"
        },
        {
          "id": "B",
          "text": "Akaike Information Criterion (AIC)"
        },
        {
          "id": "C",
          "text": "Bayesian Information Criterion (BIC)"
        },
        {
          "id": "D",
          "text": "Standard Raw $R^2$ on the training set"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Adjusted $R^2$, AIC, and BIC all include explicit penalty terms for the number of parameters $p$. Raw $R^2$ monotonically increases whenever any predictor is added, regardless of usefulness.",
      "difficulty": "easy",
      "subtopic": "Penalized Model Comparison"
    },
    {
      "id": "cml-l06-q23",
      "type": "multi_choice",
      "question": "Which of the following are consequences of the 'Curse of Dimensionality' when expanding features via high-degree polynomials in multiple variables? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Combinatorial explosion in the number of columns, quickly exceeding the sample size $p \\gg n$"
        },
        {
          "id": "B",
          "text": "Data points become isolated and sparse in high-dimensional space, requiring exponentially more data to maintain sampling density"
        },
        {
          "id": "C",
          "text": "Distances between any pair of points become nearly uniform, degrading geometric distance-based estimators"
        },
        {
          "id": "D",
          "text": "The closed-form Normal Equation runs in $O(1)$ constant time"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are direct mathematical effects of high dimensionality. D is false: Normal Equation scales as $O(p^3)$, becoming impossibly slow as feature dimension explodes.",
      "difficulty": "medium",
      "subtopic": "Curse of Dimensionality"
    },
    {
      "id": "cml-l06-q24",
      "type": "multi_choice",
      "question": "What happens when an engineer relies strictly on raw training $R^2$ to choose the polynomial degree for a dataset? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The engineer will inevitably choose the highest degree evaluated, because training $R^2$ never decreases with added degrees"
        },
        {
          "id": "B",
          "text": "The selected model will almost certainly suffer from severe overfitting and poor out-of-sample generalization"
        },
        {
          "id": "C",
          "text": "The engineer will identify the true underlying degree of the data generating process"
        },
        {
          "id": "D",
          "text": "The model will fit noise and random fluctuations in the training set as if they were true structural signal"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Adding features expands the column space of $X$, always reducing or keeping constant the orthogonal projection error $SSE$. Thus training $R^2$ will always favor maximum complexity (A, B, D). C is false.",
      "difficulty": "easy",
      "subtopic": "Pitfalls of Training R2"
    },
    {
      "id": "cml-l06-q25",
      "type": "multi_choice",
      "question": "Which of the following statements regarding the expected test error decomposition $\\mathbb{E}[(y - \\hat{f}(x))^2] = \\text{Bias}^2 + \\text{Var} + \\sigma^2$ are mathematically TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "$\\text{Bias}(\\hat{f}(x)) = \\mathbb{E}_{\\mathcal{D}}[\\hat{f}(x; \\mathcal{D})] - f(x)$ represents the difference between the average model prediction across all possible training datasets and the true function value"
        },
        {
          "id": "B",
          "text": "$\\text{Var}(\\hat{f}(x)) = \\mathbb{E}_{\\mathcal{D}}[(\\hat{f}(x; \\mathcal{D}) - \\mathbb{E}_{\\mathcal{D}}[\\hat{f}(x; \\mathcal{D})])^2]$ measures how much the model predictions scatter around their own expectation for different training datasets"
        },
        {
          "id": "C",
          "text": "The cross-term $2 \\mathbb{E}[(f(x) - \\mathbb{E}[\\hat{f}(x)])(\\mathbb{E}[\\hat{f}(x)] - \\hat{f}(x))]$ vanishes to zero because the first factor is non-random and $\\mathbb{E}[\\mathbb{E}[\\hat{f}] - \\hat{f}] = 0$"
        },
        {
          "id": "D",
          "text": "Increasing the training set size $n \\to \\infty$ forces $\\sigma^2 \\to 0$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C describe the exact mathematical proof and definitions of the bias-variance decomposition. D is FALSE: irreducible error $\\sigma^2 = \\text{Var}(\\epsilon)$ is a property of the data-generating process and does not change with sample size $n$.",
      "difficulty": "hard",
      "subtopic": "Formal Bias-Variance Proof"
    }
  ]
}
