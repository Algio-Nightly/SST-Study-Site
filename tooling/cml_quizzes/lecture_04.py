QUIZ_L04 = {
  "topicId": "lecture-04",
  "lectureNumber": 4,
  "title": "Classical Assumptions of Ordinary Least Squares (LINE) & Diagnostics",
  "description": "25 comprehensive questions covering the LINE assumptions (Linearity, Independence, Normality, Equal Variance/Homoscedasticity), Residual Analysis, Multicollinearity, VIF, and Python diagnostics.",
  "estimatedMinutes": 35,
  "questions": [
    {
      "id": "cml-l04-q01",
      "type": "single_choice",
      "question": "In a multiple linear regression model with $n$ observations and $p$ predictor features (excluding intercept), what are the degrees of freedom associated with the Residual Sum of Squares ($SSE$)?",
      "options": [
        {
          "id": "A",
          "text": "$n - 1$"
        },
        {
          "id": "B",
          "text": "$n - p$"
        },
        {
          "id": "C",
          "text": "$n - p - 1$"
        },
        {
          "id": "D",
          "text": "$n - 2p$"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "The degrees of freedom for the residuals is $n - (p + 1) = n - p - 1$, where $p + 1$ parameters (one intercept $\\beta_0$ and $p$ slope coefficients $\\beta_1, \\dots, \\beta_p$) are estimated from the data.",
      "difficulty": "easy",
      "subtopic": "Degrees of Freedom"
    },
    {
      "id": "cml-l04-q02",
      "type": "single_choice",
      "question": "What does the 'L' in the LINE acronym for classical OLS assumptions formally require?",
      "options": [
        {
          "id": "A",
          "text": "The relationship between predictors $X_j$ and $Y$ must be strictly linear in the input variables $X$"
        },
        {
          "id": "B",
          "text": "The regression model must be linear in the parameters $\\beta$, even if features are nonlinear transformations of inputs"
        },
        {
          "id": "C",
          "text": "The loss function must be linear rather than quadratic"
        },
        {
          "id": "D",
          "text": "The residuals must lie strictly along a straight line in a scatter plot"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "OLS requires linearity in the parameters (coefficients $\\beta$), meaning $Y = X\\beta + \\epsilon$. Features can be nonlinear functions of inputs (e.g., $x^2$, $\\log(x)$), but $\\beta$ must enter linearly.",
      "difficulty": "medium",
      "subtopic": "Linearity Assumption"
    },
    {
      "id": "cml-l04-q03",
      "type": "single_choice",
      "question": "If the Variance Inflation Factor (VIF) of an explanatory variable is calculated as 10, what percentage of that variable's variance is explained by the other explanatory variables in the model?",
      "options": [
        {
          "id": "A",
          "text": "10%"
        },
        {
          "id": "B",
          "text": "50%"
        },
        {
          "id": "C",
          "text": "90%"
        },
        {
          "id": "D",
          "text": "99%"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "By definition, $\\text{VIF}_j = \\frac{1}{1 - R_j^2}$. If $\\text{VIF}_j = 10$, then $1 - R_j^2 = \\frac{1}{10} = 0.10$, which implies $R_j^2 = 0.90$ (90% of the variance is explained by other features).",
      "difficulty": "easy",
      "subtopic": "VIF Calculation"
    },
    {
      "id": "cml-l04-q04",
      "type": "single_choice",
      "question": "Which visual pattern in a plot of Residuals vs. Fitted Values ($\\hat{y}$) provides unmistakable diagnostic evidence of heteroscedasticity?",
      "options": [
        {
          "id": "A",
          "text": "A completely random horizontal band of points centered around residual = 0 with uniform spread"
        },
        {
          "id": "B",
          "text": "A distinct megaphone, funnel, or fan shape where the vertical spread of residuals widens or narrows as $\\hat{y}$ increases"
        },
        {
          "id": "C",
          "text": "A parabolic U-shaped curve in the residuals"
        },
        {
          "id": "D",
          "text": "All residuals clustering tightly along a $45^\\circ$ diagonal line"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Heteroscedasticity means non-constant error variance $\\text{Var}(\\epsilon_i | X) \\neq \\sigma^2$. A funnel/fan shape indicates that error variance scales with the magnitude of predictions.",
      "difficulty": "easy",
      "subtopic": "Heteroscedasticity"
    },
    {
      "id": "cml-l04-q05",
      "type": "single_choice",
      "question": "In a linear regression analysis, severe multicollinearity among predictors directly causes which of the following mathematical consequences?",
      "options": [
        {
          "id": "A",
          "text": "Severe bias in the estimated regression coefficients $\\hat{\\beta}$"
        },
        {
          "id": "B",
          "text": "Drastic inflation in the variance and standard errors of $\\hat{\\beta}_j$, leading to unstable coefficient estimates and high p-values"
        },
        {
          "id": "C",
          "text": "A collapse of the model's overall $R^2$ to near zero regardless of correlation with $Y$"
        },
        {
          "id": "D",
          "text": "A reduction in the total degrees of freedom for the residual sum of squares"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Multicollinearity does not induce bias in $\\hat{\\beta}$, nor does it degrade overall prediction $R^2$. Instead, it makes $(X^TX)$ nearly singular, inflating the diagonal elements of $(X^TX)^{-1}$ and causing massive variance/standard errors in $\\hat{\\beta}_j$.",
      "difficulty": "medium",
      "subtopic": "Multicollinearity Consequences"
    },
    {
      "id": "cml-l04-q06",
      "type": "single_choice",
      "question": "Which Python library and module provides the official `variance_inflation_factor` function commonly used in classical econometrics and ML diagnostics?",
      "options": [
        {
          "id": "A",
          "text": "`from sklearn.linear_model import variance_inflation_factor`"
        },
        {
          "id": "B",
          "text": "`from statsmodels.stats.outliers_influence import variance_inflation_factor`"
        },
        {
          "id": "C",
          "text": "`from scipy.spatial.distance import variance_inflation_factor`"
        },
        {
          "id": "D",
          "text": "`from sklearn.metrics import variance_inflation_factor`"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "`variance_inflation_factor` is implemented in `statsmodels.stats.outliers_influence`.",
      "difficulty": "easy",
      "subtopic": "Python Diagnostics"
    },
    {
      "id": "cml-l04-q07",
      "type": "single_choice",
      "question": "What is the primary consequence of violating the homoscedasticity assumption (i.e., presence of heteroscedasticity) when estimating OLS regression parameters?",
      "options": [
        {
          "id": "A",
          "text": "OLS coefficient estimates $\\hat{\\beta}$ become biased and asymptotically inconsistent"
        },
        {
          "id": "B",
          "text": "OLS coefficient estimates $\\hat{\\beta}$ remain unbiased, but they are no longer BLUE (Best Linear Unbiased Estimator) and standard error estimates are biased"
        },
        {
          "id": "C",
          "text": "The true residual mean $\\mathbb{E}[e]$ becomes strictly positive"
        },
        {
          "id": "D",
          "text": "The coefficient of determination $R^2$ exceeds 1.0"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Under heteroscedasticity, $\\mathbb{E}[\\hat{\\beta}] = \\beta$ (unbiasedness is preserved), but the Gauss-Markov theorem fails: OLS is no longer minimum variance (BLUE), and standard errors calculated as $\\sigma^2(X^TX)^{-1}$ are wrong, invalidating t-tests and p-values.",
      "difficulty": "hard",
      "subtopic": "Gauss-Markov Violations"
    },
    {
      "id": "cml-l04-q08",
      "type": "single_choice",
      "question": "The Durbin-Watson statistic $d$ tests for first-order serial correlation in residuals. If the test yields $d \\approx 0$, what does this indicate?",
      "options": [
        {
          "id": "A",
          "text": "Zero autocorrelation; residuals are completely independent"
        },
        {
          "id": "B",
          "text": "Strong positive first-order autocorrelation among residuals"
        },
        {
          "id": "C",
          "text": "Strong negative first-order autocorrelation among residuals"
        },
        {
          "id": "D",
          "text": "Severe non-normality of residuals"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The Durbin-Watson statistic is $d \\approx 2(1 - r)$, where $r$ is the sample autocorrelation of residuals. When $r \\approx +1$ (strong positive autocorrelation), $d \\approx 2(1 - 1) = 0$. A value of $d \\approx 2$ indicates no autocorrelation, and $d \\approx 4$ indicates strong negative autocorrelation.",
      "difficulty": "medium",
      "subtopic": "Independence & Autocorrelation"
    },
    {
      "id": "cml-l04-q09",
      "type": "single_choice",
      "question": "When interpreting a Normal Quantile-Quantile (Q-Q) plot of standardized residuals, what does an 'S-shaped' curve with heavy tails (points falling above the reference line on the right and below on the left) signify?",
      "options": [
        {
          "id": "A",
          "text": "The residuals follow a perfectly standard normal distribution"
        },
        {
          "id": "B",
          "text": "The residuals have heavier tails (leptokurtic) than a normal distribution, with more extreme outliers than expected"
        },
        {
          "id": "C",
          "text": "The regression model is severely underfitted with respect to degree 1 terms"
        },
        {
          "id": "D",
          "text": "The residuals are strictly bounded within $[-1, 1]$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In a Q-Q plot, points straying above the $45^\\circ$ line at the high positive end and below it at the low negative end indicate heavy tails (extreme residuals occurring with higher frequency than expected under a Gaussian distribution).",
      "difficulty": "medium",
      "subtopic": "Normality of Residuals"
    },
    {
      "id": "cml-l04-q10",
      "type": "single_choice",
      "question": "Why is the assumption of normally distributed errors $\\epsilon \\sim \\mathcal{N}(0, \\sigma^2 I)$ required in classical linear regression?",
      "options": [
        {
          "id": "A",
          "text": "To guarantee that the OLS point estimates $\\hat{\\beta}$ are unbiased"
        },
        {
          "id": "B",
          "text": "To guarantee that the Gauss-Markov theorem holds (making OLS BLUE)"
        },
        {
          "id": "C",
          "text": "To enable exact small-sample statistical inference (t-tests, F-tests, and confidence intervals) for parameters"
        },
        {
          "id": "D",
          "text": "To ensure that $(X^TX)$ is strictly non-singular"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "Unbiasedness and the Gauss-Markov BLUE property require only $\\mathbb{E}[\\epsilon|X]=0$ and $\\text{Var}(\\epsilon|X)=\\sigma^2 I$ without any normality assumption! Normality is strictly needed for exact finite-sample distributions of test statistics ($t$ and $F$) and confidence intervals.",
      "difficulty": "hard",
      "subtopic": "Role of Normality"
    },
    {
      "id": "cml-l04-q11",
      "type": "single_choice",
      "question": "Suppose a categorical feature 'City' has 4 unique values: ['NYC', 'London', 'Tokyo', 'Paris']. If a student creates 4 one-hot encoded binary columns and includes all 4 along with an intercept $\\beta_0$ in an OLS model, what mathematical failure occurs?",
      "options": [
        {
          "id": "A",
          "text": "Target leakage, because city names reveal future targets"
        },
        {
          "id": "B",
          "text": "Perfect multicollinearity (Dummy Variable Trap), making $X^TX$ singular and non-invertible"
        },
        {
          "id": "C",
          "text": "Heteroscedasticity due to unequal population sizes among cities"
        },
        {
          "id": "D",
          "text": "Negative $R^2$ on the training set"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The sum of the 4 indicator columns equals a vector of ones: $\\sum_{k=1}^4 D_k = \\mathbf{1}$, which is identical to the constant intercept column $x_0 = \\mathbf{1}$. This creates exact linear dependence, $\\det(X^TX)=0$, known as the Dummy Variable Trap. One category must be omitted (creating $k-1$ dummies).",
      "difficulty": "easy",
      "subtopic": "Dummy Variable Trap"
    },
    {
      "id": "cml-l04-q12",
      "type": "single_choice",
      "question": "Which of the following statistical tests is specifically designed to detect heteroscedasticity by regressing squared residuals on the original regressors and their cross-products?",
      "options": [
        {
          "id": "A",
          "text": "Durbin-Watson Test"
        },
        {
          "id": "B",
          "text": "White Test"
        },
        {
          "id": "C",
          "text": "Shapiro-Wilk Test"
        },
        {
          "id": "D",
          "text": "Ramsey RESET Test"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The White Test (1980) tests for heteroscedasticity without assuming a specific functional form of error variance by regressing $e_i^2$ on regressors, their squares, and cross-products ($n R^2 \\sim \\chi^2$).",
      "difficulty": "medium",
      "subtopic": "Statistical Diagnostics"
    },
    {
      "id": "cml-l04-q13",
      "type": "single_choice",
      "question": "If a residual plot against fitted values displays a pronounced U-shaped parabolic curve, which OLS assumption is violated, and what is the standard remedy?",
      "options": [
        {
          "id": "A",
          "text": "Normality is violated; remove outliers with Cook's distance > 1"
        },
        {
          "id": "B",
          "text": "Linearity is violated; introduce polynomial terms (e.g. $X^2$) or nonlinear feature transformations"
        },
        {
          "id": "C",
          "text": "Independence is violated; apply first-differencing"
        },
        {
          "id": "D",
          "text": "Homoscedasticity is violated; switch to Ridge regression"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A curved pattern in residuals plotted against $\\hat{y}$ or $X$ reveals systematic non-linear relationships that the linear model failed to capture. Adding polynomial features (e.g. $X^2$) or transforming features corrects the linearity violation.",
      "difficulty": "easy",
      "subtopic": "Linearity Diagnostics"
    },
    {
      "id": "cml-l04-q14",
      "type": "single_choice",
      "question": "What is the effective mathematical remedy for OLS regression when heteroscedasticity is known and the error variances $\\sigma_i^2 = \\text{Var}(\\epsilon_i)$ are known up to a proportional constant?",
      "options": [
        {
          "id": "A",
          "text": "Ordinary Least Squares with L1 Lasso penalty"
        },
        {
          "id": "B",
          "text": "Weighted Least Squares (WLS) minimizing $\\sum_{i=1}^n w_i (y_i - x_i^T\\beta)^2$ with weights $w_i = 1 / \\sigma_i^2$"
        },
        {
          "id": "C",
          "text": "Dropping the observations with highest variance"
        },
        {
          "id": "D",
          "text": "Replacing all continuous features with min-max normalized features"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Weighted Least Squares (WLS), a special case of Generalized Least Squares (GLS), weights each observation inversely proportional to its variance ($w_i = 1/\\sigma_i^2$), transforming the model into one with homoscedastic errors that restores the BLUE property.",
      "difficulty": "hard",
      "subtopic": "WLS & Heteroscedasticity"
    },
    {
      "id": "cml-l04-q15",
      "type": "single_choice",
      "question": "What threshold of the Variance Inflation Factor (VIF) is universally recognized in applied ML and econometrics as a rule-of-thumb warning sign of severe multicollinearity?",
      "options": [
        {
          "id": "A",
          "text": "$\\text{VIF} > 1.0$"
        },
        {
          "id": "B",
          "text": "$\\text{VIF} > 2.0$"
        },
        {
          "id": "C",
          "text": "$\\text{VIF} > 5 \\text{ to } 10$"
        },
        {
          "id": "D",
          "text": "$\\text{VIF} > 100$"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "A common rule of thumb is that $\\text{VIF} > 5$ warrants inspection, and $\\text{VIF} > 10$ indicates severe multicollinearity where over 90% of the predictor's variance is explained by other predictors.",
      "difficulty": "easy",
      "subtopic": "VIF Guidelines"
    },
    {
      "id": "cml-l04-q16",
      "type": "single_choice",
      "question": "When two predictors $X_1$ and $X_2$ are perfectly collinear ($X_2 = 2 X_1$), what happens to the condition number of the design matrix $X^TX$?",
      "options": [
        {
          "id": "A",
          "text": "The condition number becomes 1.0"
        },
        {
          "id": "B",
          "text": "The condition number becomes negative"
        },
        {
          "id": "C",
          "text": "The condition number becomes infinite (or exceeds machine precision $\\sim 10^{16}$)"
        },
        {
          "id": "D",
          "text": "The condition number matches the correlation coefficient $r_{12} = 1.0$"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "The condition number is $\\kappa(A) = \\sqrt{\\lambda_{\\max} / \\lambda_{\\min}}$. With perfect collinearity, the smallest eigenvalue $\\lambda_{\\min} = 0$, driving the condition number to infinity, indicating a non-invertible matrix.",
      "difficulty": "medium",
      "subtopic": "Matrix Condition Number"
    },
    {
      "id": "cml-l04-q17",
      "type": "single_choice",
      "question": "In residual diagnostics, what is Cook's Distance ($D_i$) specifically used to measure?",
      "options": [
        {
          "id": "A",
          "text": "The distance between the regression hyperplane and the coordinate origin"
        },
        {
          "id": "B",
          "text": "The combined influence of the $i$-th observation on all fitted values when that observation is omitted from the model"
        },
        {
          "id": "C",
          "text": "The Euclidean distance between training and test sets"
        },
        {
          "id": "D",
          "text": "The autocorrelation between observation $i$ and observation $i-1$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Cook's distance measures the aggregate shift in fitted values $\\sum_{j=1}^n (\\hat{y}_j - \\hat{y}_{j(i)})^2 / (p \\cdot s^2)$ when observation $i$ is deleted, identifying highly influential points (high leverage combined with large residual).",
      "difficulty": "medium",
      "subtopic": "Influence & Cook's Distance"
    },
    {
      "id": "cml-l04-q18",
      "type": "single_choice",
      "question": "What is the Breusch-Pagan test specifically used for in regression analysis?",
      "options": [
        {
          "id": "A",
          "text": "Testing whether the error terms exhibit serial autocorrelation"
        },
        {
          "id": "B",
          "text": "Testing the null hypothesis of homoscedasticity against the alternative of heteroscedasticity"
        },
        {
          "id": "C",
          "text": "Testing whether the regression coefficients are jointly zero"
        },
        {
          "id": "D",
          "text": "Testing whether the residuals follow a student-t distribution"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The Breusch-Pagan test evaluates the null hypothesis $H_0$: errors have constant variance (homoscedasticity) against $H_1$: error variance is an auxiliary linear function of the independent variables.",
      "difficulty": "medium",
      "subtopic": "Statistical Diagnostics"
    },
    {
      "id": "cml-l04-q19",
      "type": "multi_choice",
      "question": "Which of the following conditions or data modeling mistakes directly lead to multicollinearity in a multiple linear regression model? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Including both Temperature in Celsius and Temperature in Fahrenheit as distinct predictors"
        },
        {
          "id": "B",
          "text": "Falling into the Dummy Variable Trap by including all $k$ one-hot encoded categories alongside a constant intercept"
        },
        {
          "id": "C",
          "text": "Including two distinct economic variables that naturally track each other very closely over time (e.g., GDP and Total Consumption Expenditure)"
        },
        {
          "id": "D",
          "text": "Standardizing all continuous features using Z-score normalization"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A ($F = 1.8C + 32$ is an exact linear combination), B (sum of dummy columns equals the intercept column $\\mathbf{1}$), and C (high empirical correlation) all cause multicollinearity. D (standardizing) does NOT cause multicollinearity; in fact, centering polynomial features can reduce structural multicollinearity.",
      "difficulty": "medium",
      "subtopic": "Multicollinearity Causes"
    },
    {
      "id": "cml-l04-q20",
      "type": "multi_choice",
      "question": "Which of the following methods are mathematically valid and practically effective in detecting or mitigating multicollinearity in linear regression? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Calculating the Variance Inflation Factor (VIF) for each predictor"
        },
        {
          "id": "B",
          "text": "Applying L2 Ridge Regularization ($X^TX + \\lambda I$), which stabilizes matrix inversion by adding $\\lambda$ to the eigenvalues"
        },
        {
          "id": "C",
          "text": "Using Principal Component Analysis (PCA) to transform correlated predictors into orthogonal principal components"
        },
        {
          "id": "D",
          "text": "Dropping one of the highly correlated redundant features from the feature matrix"
        },
        {
          "id": "E",
          "text": "Multiplying all target $y$ values by a large scalar constant"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "A detects it; B, C, and D mitigate it (Ridge makes $(X^TX + \\lambda I)$ well-conditioned, PCA decorrelates features, dropping removes redundancy). E does not alter the collinearity of $X$ at all.",
      "difficulty": "medium",
      "subtopic": "Mitigating Multicollinearity"
    },
    {
      "id": "cml-l04-q21",
      "type": "multi_choice",
      "question": "Which of the following statements regarding the impact of multicollinearity on an OLS model are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The overall predictive power ($R^2$ and $\\hat{y}$) of the model on data from the same distribution remains largely unaffected"
        },
        {
          "id": "B",
          "text": "The individual regression coefficients become highly sensitive to minor changes or additions in the training data"
        },
        {
          "id": "C",
          "text": "Individual t-statistic p-values may indicate that neither feature is significant, even though the overall F-test confirms the model is highly significant"
        },
        {
          "id": "D",
          "text": "The OLS estimator $\\hat{\\beta}$ becomes mathematically biased such that $\\mathbb{E}[\\hat{\\beta}] \\neq \\beta$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are classic hallmarks of multicollinearity: predictions work well, but individual coefficient interpretations collapse and standard errors explode. D is FALSE: OLS remains strictly unbiased under multicollinearity, provided $X$ has full rank or we take the pseudoinverse.",
      "difficulty": "hard",
      "subtopic": "Multicollinearity Impact"
    },
    {
      "id": "cml-l04-q22",
      "type": "multi_choice",
      "question": "Which of the following diagnostic plots are essential in verifying the LINE assumptions for a multiple linear regression model? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Residuals vs. Fitted Values plot (verifies linearity and homoscedasticity)"
        },
        {
          "id": "B",
          "text": "Normal Q-Q plot of standardized residuals (verifies error normality)"
        },
        {
          "id": "C",
          "text": "Scale-Location (Spread-Location) plot of $\\sqrt{|\\text{standardized residuals}|}$ vs. fitted values (evaluates homoscedasticity)"
        },
        {
          "id": "D",
          "text": "Residuals vs. Leverage plot with Cook's distance contours (identifies influential outliers)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four plots comprise the standard 'Diagnostic Quartet' provided by statistical software (e.g. `plot(model)` in R, statsmodels diagnostic plots in Python) to assess linearity, homoscedasticity, normality, and influential leverage points.",
      "difficulty": "medium",
      "subtopic": "Diagnostic Plots"
    },
    {
      "id": "cml-l04-q23",
      "type": "multi_choice",
      "question": "What valid remedial actions can an engineer take if the residuals exhibit severe heteroscedasticity? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Apply a concave power transformation to the target variable $y$, such as $\\log(y)$ or a Box-Cox transformation"
        },
        {
          "id": "B",
          "text": "Use Heteroscedasticity-Consistent (HC) Robust Standard Errors (White-Huber 'sandwich' estimator) for hypothesis testing"
        },
        {
          "id": "C",
          "text": "Switch to Weighted Least Squares (WLS) if the variance structure can be modeled"
        },
        {
          "id": "D",
          "text": "Discard the intercept term $\\beta_0$ from the regression equation"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A stabilizes variance when target scale increases with variance. B corrects standard error bias without changing OLS coefficients. C reweights observations to achieve homoscedastic errors. D is incorrect and typically creates severe bias.",
      "difficulty": "hard",
      "subtopic": "Heteroscedasticity Remedies"
    },
    {
      "id": "cml-l04-q24",
      "type": "multi_choice",
      "question": "Which of the following assumptions are required specifically by the Gauss-Markov Theorem to guarantee that OLS is the Best Linear Unbiased Estimator (BLUE)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Strict exogeneity: $\\mathbb{E}[\\epsilon_i | X] = 0$ for all $i$"
        },
        {
          "id": "B",
          "text": "Homoscedasticity: $\\text{Var}(\\epsilon_i | X) = \\sigma^2$ (constant variance)"
        },
        {
          "id": "C",
          "text": "No autocorrelation: $\\text{Cov}(\\epsilon_i, \\epsilon_j | X) = 0$ for all $i \\neq j$"
        },
        {
          "id": "D",
          "text": "Errors must strictly follow a Gaussian normal distribution: $\\epsilon_i \\sim \\mathcal{N}(0, \\sigma^2)$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "The Gauss-Markov theorem requires only finite mean zero, constant variance, and zero covariance (A, B, C). It does NOT require normality (D)! BLUE holds even for non-normal errors.",
      "difficulty": "hard",
      "subtopic": "Gauss-Markov Theorem"
    },
    {
      "id": "cml-l04-q25",
      "type": "multi_choice",
      "question": "Suppose an analyst computes the VIF for 3 predictors in an auxiliary regression. Which of the following statements about auxiliary regressions and VIF are mathematically correct? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The auxiliary regression for feature $X_j$ regresses $X_j$ on all other $p-1$ predictors to find $R_j^2$"
        },
        {
          "id": "B",
          "text": "If feature $X_1$ is completely orthogonal to all other predictors, its auxiliary $R_1^2 = 0$, giving $\\text{VIF}_1 = 1$"
        },
        {
          "id": "C",
          "text": "The variance of the estimated coefficient $\\hat{\\beta}_j$ is directly proportional to $\\text{VIF}_j$: $\\text{Var}(\\hat{\\beta}_j) = \\frac{\\sigma^2}{\\sum (x_{ij} - \\bar{x}_j)^2} \\times \\text{VIF}_j$"
        },
        {
          "id": "D",
          "text": "A VIF of 100 means the standard error of the coefficient is multiplied by $\\sqrt{100} = 10$ relative to an orthogonal setting"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All statements are mathematically exact: $\\text{VIF}_j = 1/(1-R_j^2)$ measures the variance inflation factor. The standard error is inflated by $\\sqrt{\\text{VIF}_j}$, so $\\text{VIF}=100$ multiplies standard error by $\\sqrt{100} = 10$.",
      "difficulty": "hard",
      "subtopic": "VIF Mathematical Properties"
    }
  ]
}
