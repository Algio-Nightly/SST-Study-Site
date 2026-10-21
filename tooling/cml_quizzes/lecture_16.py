QUIZ_L16 = {
  "topicId": "lecture-16",
  "lectureNumber": 16,
  "title": "SST CML End-Term Practice Exam (Group B)",
  "description": "20 official examination questions from the Scaler School of Technology CML End-Term Practice Sheet (Group B) covering Mitchell's ETP framing, encoding, temporal leakage, OLS metrics, collinearity, LINE diagnostics, gradient descent, bias-variance polynomial selection, Ridge/Lasso regularization, logistic regression, k-NN, decision trees, bagging, boosting, K-Means, and PCA.",
  "estimatedMinutes": 35,
  "questions": [
    {
      "id": "cml-endterm-b-a01",
      "type": "single_choice",
      "question": "A bank wants a system that flags loan applications that are likely to default. It will learn from 5 years of past applications whose outcomes are known, and the team will judge it by its recall on next quarter's applications. Using Tom Mitchell's definition (task T, experience E, performance P), which mapping is correct?",
      "options": [
        {
          "id": "A",
          "text": "T = recall on next quarter's applications; E = flagging risky applications; P = past applications"
        },
        {
          "id": "B",
          "text": "T = past applications with known outcomes; E = recall; P = flagging risky applications"
        },
        {
          "id": "C",
          "text": "T = flag applications likely to default; E = past applications with known outcomes; P = recall on new applications"
        },
        {
          "id": "D",
          "text": "T = flag applications likely to default; E = recall on new applications; P = past applications with known outcomes"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "T is what the system must do (flag likely defaulters), E is the data it learns from (labelled past applications), and P is how success is scored (recall on unseen applications). The other options shuffle the three roles.",
      "difficulty": "easy",
      "subtopic": "Mitchell's ETP Framework"
    },
    {
      "id": "cml-endterm-b-a02",
      "type": "single_choice",
      "question": "A column `satisfaction` takes the values Low, Medium, High. You write `OrdinalEncoder().fit(X_train[['satisfaction']])` without any other arguments and feed the codes to a linear model. What happens, and what is the fix?",
      "options": [
        {
          "id": "A",
          "text": "sklearn detects the natural order, so Low = 0, Medium = 1, High = 2 and nothing needs fixing."
        },
        {
          "id": "B",
          "text": "The categories are sorted alphabetically (High = 0, Low = 1, Medium = 2), so the real order is scrambled; pass categories=[['Low', 'Medium', 'High']] to the encoder."
        },
        {
          "id": "C",
          "text": "OrdinalEncoder cannot handle strings, so one-hot encoding is the only option."
        },
        {
          "id": "D",
          "text": "The codes change randomly every time fit is called, so you must set random_state."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "By default OrdinalEncoder sorts the categories it sees alphabetically: High = 0, Low = 1, Medium = 2. For an ordinal feature, specify the natural order explicitly using categories=[['Low', 'Medium', 'High']] so the integer codes become 0, 1, 2.",
      "difficulty": "medium",
      "subtopic": "Ordinal Encoding"
    },
    {
      "id": "cml-endterm-b-a03",
      "type": "single_choice",
      "question": "You forecast daily sales from 3 years of data. A teammate uses `train_test_split` with `shuffle=True` and adds the feature 'average sales over a 7-day window centred on the day' (using the 3 days before and the 3 days after). Test RMSE looks excellent, but the model fails once deployed. What is the most likely cause and fix?",
      "options": [
        {
          "id": "A",
          "text": "The model underfits; add polynomial features."
        },
        {
          "id": "B",
          "text": "RMSE is the wrong metric; report R² instead."
        },
        {
          "id": "C",
          "text": "The learning rate is too high; lower it and retrain."
        },
        {
          "id": "D",
          "text": "Temporal leakage: the random split and the centred window let the model see future values. Split by time (train on earlier dates, test on later dates) and only build features from the past."
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "At test/deployment time, future sales are unknown. The 7-day centered window looks 3 days into the future, and shuffling mixes future dates into training rows. This causes severe temporal leakage. The fix is a chronological split with backward-looking rolling features only.",
      "difficulty": "medium",
      "subtopic": "Temporal Data Leakage"
    },
    {
      "id": "cml-endterm-b-a04",
      "type": "single_choice",
      "question": "True values $y = [3, 5, 8, 10]$ and predictions $\\hat{y} = [4, 5, 6, 13]$. Using $\\text{MAE} = \\frac{1}{n}\\sum |\\hat{y}_i - y_i|$ and $\\text{RMSE} = \\sqrt{\\frac{1}{n}\\sum (\\hat{y}_i - y_i)^2}$, which pair is correct?",
      "options": [
        {
          "id": "A",
          "text": "MAE = 1.50, RMSE ≈ 1.87"
        },
        {
          "id": "B",
          "text": "MAE = 1.50, RMSE = 3.50"
        },
        {
          "id": "C",
          "text": "MAE = 0.50, RMSE ≈ 1.87"
        },
        {
          "id": "D",
          "text": "MAE = 3.50, RMSE = 1.50"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Residual errors $\\hat{y} - y = [1, 0, -2, 3]$. MAE = (1 + 0 + 2 + 3)/4 = 6/4 = 1.50. Squared errors = [1, 0, 4, 9] sum to 14, giving MSE = 14/4 = 3.50, and RMSE = sqrt(3.50) ≈ 1.87.",
      "difficulty": "easy",
      "subtopic": "Regression Metrics"
    },
    {
      "id": "cml-endterm-b-a05",
      "type": "single_choice",
      "question": "Your design matrix contains both `height_cm` and `height_inches` (`height_inches = height_cm / 2.54`). You solve the normal equation $\\boldsymbol{\theta} = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$. What goes wrong?",
      "options": [
        {
          "id": "A",
          "text": "Nothing; more features always make the closed form more accurate."
        },
        {
          "id": "B",
          "text": "The normal equation only works with a single feature."
        },
        {
          "id": "C",
          "text": "The two columns are perfectly collinear, so $\\mathbf{X}^T \\mathbf{X}$ is singular (not invertible). Drop one of the columns, or use a pseudoinverse or Ridge."
        },
        {
          "id": "D",
          "text": "The closed form diverges unless the features are scaled first."
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "One column is an exact scalar multiple of the other, making the columns of X linearly dependent. Therefore X^T X is rank-deficient and has determinant zero (singular), making matrix inversion impossible.",
      "difficulty": "medium",
      "subtopic": "Normal Equation Singularity"
    },
    {
      "id": "cml-endterm-b-a06",
      "type": "single_choice",
      "question": "After fitting OLS, the residuals-vs-fitted plot shows a clear U-shape: residuals are positive at both ends and negative in the middle, with roughly constant spread. Which LINE assumption is violated, and what is a sensible first remedy?",
      "options": [
        {
          "id": "A",
          "text": "Equal variance; log-transform the target."
        },
        {
          "id": "B",
          "text": "Linearity; add a transformed or polynomial term (for example $x^2$) for the feature driving the curve, then re-check the residuals."
        },
        {
          "id": "C",
          "text": "Independence; shuffle the rows and refit."
        },
        {
          "id": "D",
          "text": "Normality; delete the points with the largest residuals."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A systematic curved pattern in the conditional mean of residuals indicates that the true relationship is non-linear, violating the Linearity assumption. Adding a quadratic ($x^2$) or polynomial term models the curve. A fan shape would indicate heteroscedasticity.",
      "difficulty": "medium",
      "subtopic": "LINE Diagnostics"
    },
    {
      "id": "cml-endterm-b-a07",
      "type": "single_choice",
      "question": "You minimise $J(w) = (w - 3)^2$ with gradient descent, starting from $w = 0$ with learning rate $\\eta = 0.1$. The derivative is $\\frac{dJ}{dw} = 2(w - 3)$. What is $w$ after two updates?",
      "options": [
        {
          "id": "A",
          "text": "0.60"
        },
        {
          "id": "B",
          "text": "1.08"
        },
        {
          "id": "C",
          "text": "1.20"
        },
        {
          "id": "D",
          "text": "3.00"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Update rule: w := w - η (dJ/dw). Step 1: dJ/dw = 2(0 - 3) = -6, so w1 = 0 - 0.1(-6) = 0.60. Step 2: dJ/dw = 2(0.60 - 3) = -4.8, so w2 = 0.60 - 0.1(-4.8) = 0.60 + 0.48 = 1.08.",
      "difficulty": "medium",
      "subtopic": "Gradient Descent Updates"
    },
    {
      "id": "cml-endterm-b-a08",
      "type": "single_choice",
      "question": "You fit polynomial regression of different degrees and record: degree 1: train MSE 38.2, validation MSE 40.1; degree 3: train 11.6, validation 13.0; degree 6: train 9.8, validation 12.4; degree 12: train 1.9, validation 55.7. Which degree should you pick?",
      "options": [
        {
          "id": "A",
          "text": "Degree 12, because it has the lowest training MSE."
        },
        {
          "id": "B",
          "text": "Degree 1, because the simplest model is always best."
        },
        {
          "id": "C",
          "text": "Degree 3, because its train and validation MSE are closest to each other."
        },
        {
          "id": "D",
          "text": "Degree 6, because it has the lowest validation MSE; degree 12 overfits (high variance) and degree 1 underfits (high bias)."
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "Model selection strictly chooses the hypothesis that minimizes validation error (generalization error). Degree 6 has the lowest validation MSE (12.4). Degree 12 exhibits severe overfitting (train 1.9 vs val 55.7).",
      "difficulty": "medium",
      "subtopic": "Bias-Variance Tradeoff"
    },
    {
      "id": "cml-endterm-b-a09",
      "type": "single_choice",
      "question": "On standardised features you increase the Ridge penalty alpha ($\\lambda$) from 0.001 to 1000. Which statement is typically true?",
      "options": [
        {
          "id": "A",
          "text": "Training MSE keeps falling and the weights grow larger."
        },
        {
          "id": "B",
          "text": "Most weights become exactly zero, just as with Lasso."
        },
        {
          "id": "C",
          "text": "Training MSE rises as the weights are shrunk toward 0; a very large alpha underfits."
        },
        {
          "id": "D",
          "text": "Alpha has no effect once the features are standardised."
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "The Ridge loss is MSE + λ sum(w_j^2). As λ increases, the penalty forces weights toward zero, restricting model capacity. Training MSE rises, and extreme λ forces all weights to ~0, causing underfitting.",
      "difficulty": "medium",
      "subtopic": "Ridge Regularization"
    },
    {
      "id": "cml-endterm-b-a10",
      "type": "single_choice",
      "question": "Why should you scale features (fit the scaler on the training set) before Ridge, Lasso or Elastic Net?",
      "options": [
        {
          "id": "A",
          "text": "The penalty acts on weight sizes, and weight sizes depend on each feature's units. Without scaling, a feature in large units gets a tiny weight and is hardly penalised, while a feature in small units is penalised heavily."
        },
        {
          "id": "B",
          "text": "Scaling makes the MSE convex; without it Ridge has many local minima."
        },
        {
          "id": "C",
          "text": "sklearn's Ridge raises an error when features are not scaled."
        },
        {
          "id": "D",
          "text": "Scaling removes the need to choose alpha with cross-validation."
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Penalties λ sum(w_j^2) or λ sum|w_j| treat all weights equally. However, weight magnitude is inversely proportional to feature scale. Unscaled large-unit features have tiny weights and escape penalization, while small-unit features are shrunk unfairly.",
      "difficulty": "medium",
      "subtopic": "Scaling Before Regularization"
    },
    {
      "id": "cml-endterm-b-a11",
      "type": "single_choice",
      "question": "A logistic regression model has score $z = \\mathbf{w}^T \\mathbf{x} + w_0$ with $\\mathbf{w} = (2, -1)$ and $w_0 = -1$. For $\\mathbf{x} = (1.5, 1)$, what are $z$, $\\hat{p} = \\sigma(z) = \\frac{1}{1 + e^{-z}}$, and the predicted class with threshold 0.5?",
      "options": [
        {
          "id": "A",
          "text": "z = 1, p_hat ≈ 0.27, predict 0"
        },
        {
          "id": "B",
          "text": "z = 3, p_hat ≈ 0.95, predict 1"
        },
        {
          "id": "C",
          "text": "z = -1, p_hat ≈ 0.27, predict 0"
        },
        {
          "id": "D",
          "text": "z = 1, p_hat ≈ 0.73, predict 1"
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "z = 2(1.5) + (-1)(1) + (-1) = 3 - 1 - 1 = 1. p_hat = 1 / (1 + e^(-1)) = 1 / (1 + 0.3679) ≈ 0.731. Since 0.731 >= 0.5, the predicted class is 1.",
      "difficulty": "easy",
      "subtopic": "Logistic Regression Inference"
    },
    {
      "id": "cml-endterm-b-a12",
      "type": "single_choice",
      "question": "An email spam filter moves suspected spam to a junk folder. Losing a genuine email to junk is very costly for users; letting a little spam reach the inbox is only mildly annoying. Treating spam as the positive class, which metric should you prioritise, and which way should you move the decision threshold?",
      "options": [
        {
          "id": "A",
          "text": "Precision; raise the threshold so that only very confident spam is moved."
        },
        {
          "id": "B",
          "text": "Recall; lower the threshold so that more spam is caught."
        },
        {
          "id": "C",
          "text": "Accuracy; keep the threshold fixed at 0.5."
        },
        {
          "id": "D",
          "text": "Recall; raise the threshold."
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "A genuine email flagged as spam is a False Positive. Precision = TP / (TP + FP) penalizes false positives. Raising the threshold requires higher model confidence before flagging an email as spam, raising precision.",
      "difficulty": "medium",
      "subtopic": "Precision vs Recall Tradeoffs"
    },
    {
      "id": "cml-endterm-b-a13",
      "type": "single_choice",
      "question": "For one example with true label $y = 1$, which predicted probability $\\hat{p}$ gives the largest log-loss $\\ell = -(y \\ln\\hat{p} + (1 - y)\\ln(1 - \\hat{p}))$?",
      "options": [
        {
          "id": "A",
          "text": "p_hat = 0.99"
        },
        {
          "id": "B",
          "text": "p_hat = 0.60"
        },
        {
          "id": "C",
          "text": "p_hat = 0.50"
        },
        {
          "id": "D",
          "text": "p_hat = 0.05"
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "When y = 1, loss is -ln(p_hat). -ln(0.99) ≈ 0.01; -ln(0.60) ≈ 0.51; -ln(0.50) ≈ 0.69; -ln(0.05) ≈ 3.00. Confidently predicting the wrong class (0.05 when true class is 1) incurs the steepest log-loss penalty.",
      "difficulty": "medium",
      "subtopic": "Log-Loss Dynamics"
    },
    {
      "id": "cml-endterm-b-a14",
      "type": "single_choice",
      "question": "k-NN regression with $k = 2$ and Euclidean distance. Training points $(x_1, x_2) \\to y$: $(1, 1) \\to 10$, $(2, 4) \\to 18$, $(4, 2) \\to 14$, $(5, 5) \\to 26$, $(7, 1) \\to 20$. What is the prediction for query $(3, 3)$?",
      "options": [
        {
          "id": "A",
          "text": "17.60"
        },
        {
          "id": "B",
          "text": "22.00"
        },
        {
          "id": "C",
          "text": "16.00"
        },
        {
          "id": "D",
          "text": "19.33"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "Squared distances from (3,3): to (1,1): 4+4=8; to (2,4): 1+1=2; to (4,2): 1+1=2; to (5,5): 4+4=8; to (7,1): 16+4=20. The 2 nearest neighbors are (2,4) with y=18 and (4,2) with y=14. Prediction = (18 + 14)/2 = 16.00.",
      "difficulty": "easy",
      "subtopic": "k-NN Regression"
    },
    {
      "id": "cml-endterm-b-a15",
      "type": "single_choice",
      "question": "Which decision-tree node has Gini impurity 0.32, using $\\text{Gini} = 1 - \\sum_c p_c^2$?",
      "options": [
        {
          "id": "A",
          "text": "9 samples of class A and 1 of class B"
        },
        {
          "id": "B",
          "text": "8 samples of class A and 2 of class B"
        },
        {
          "id": "C",
          "text": "5 samples of class A and 5 of class B"
        },
        {
          "id": "D",
          "text": "10 samples of class A and 0 of class B"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "For 8/2 split: p_A = 0.8, p_B = 0.2. Gini = 1 - (0.8^2 + 0.2^2) = 1 - (0.64 + 0.04) = 0.32 (or binary shortcut 2 * 0.8 * 0.2 = 0.32). Option A gives 0.18, C gives 0.50, and D gives 0.0.",
      "difficulty": "easy",
      "subtopic": "Gini Impurity Calculation"
    },
    {
      "id": "cml-endterm-b-a16",
      "type": "single_choice",
      "question": "A decision tree is fitted on loan data where `loan_purpose` was one-hot encoded into 4 columns. `feature_importances_` gives: purpose_auto 0.06, purpose_education 0.04, purpose_home 0.03, purpose_personal 0.01, and credit_score 0.10. Which statement is correct?",
      "options": [
        {
          "id": "A",
          "text": "Importance is reported per dummy column. Summing the dummies gives 0.14 for loan_purpose as a whole, which is more than credit_score's 0.10 in this fitted tree."
        },
        {
          "id": "B",
          "text": "loan_purpose is unimportant because every one of its dummies is below credit_score."
        },
        {
          "id": "C",
          "text": "Importances are like logistic regression coefficients, so their signs show the direction of the effect."
        },
        {
          "id": "D",
          "text": "With one-hot encoding the dummies of one category must all have equal importance."
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "When an original categorical variable is one-hot encoded, its total feature importance is the sum of the importances of its constituent dummy columns: 0.06 + 0.04 + 0.03 + 0.01 = 0.14.",
      "difficulty": "medium",
      "subtopic": "Decision Tree Feature Importances"
    },
    {
      "id": "cml-endterm-b-a17",
      "type": "single_choice",
      "question": "Bagging (bootstrap aggregating) usually gives the biggest test-set improvement when the base model is:",
      "options": [
        {
          "id": "A",
          "text": "A decision stump (max_depth = 1), because bagging mainly removes bias."
        },
        {
          "id": "B",
          "text": "A linear regression with no features."
        },
        {
          "id": "C",
          "text": "A deep, unpruned decision tree, because it has low bias but high variance, and averaging many such trees reduces the variance."
        },
        {
          "id": "D",
          "text": "Any model; bagging improves all models by the same amount."
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "Averaging models trained on bootstrap replicates cancels out high variance while preserving the low bias of deep unpruned trees. Stumps already have low variance, so bagging provides little benefit.",
      "difficulty": "medium",
      "subtopic": "Bagging Variance Reduction"
    },
    {
      "id": "cml-endterm-b-a18",
      "type": "single_choice",
      "question": "A gradient boosting model with `learning_rate = 1.0`, `n_estimators = 2000` and `max_depth = 6` reaches 100% training accuracy, but its test accuracy is lower than the same model with `n_estimators = 200`. What is the most sensible next step?",
      "options": [
        {
          "id": "A",
          "text": "Raise the learning rate further so that it converges faster."
        },
        {
          "id": "B",
          "text": "Replace boosting with bagging of 2000 stumps."
        },
        {
          "id": "C",
          "text": "Remove the test set and report training accuracy."
        },
        {
          "id": "D",
          "text": "It is overfitting: use a smaller learning rate, shallower trees (max_depth around 2 to 4), and choose the number of trees with a validation set or early stopping."
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "High learning rate (1.0), deep trees (max_depth=6), and excessive boosting iterations allow the ensemble to chase residual noise and overfit. Standard fixes are shrinkage (learning_rate <= 0.1), shallow trees, and early stopping.",
      "difficulty": "medium",
      "subtopic": "Gradient Boosting Regularization"
    },
    {
      "id": "cml-endterm-b-a19",
      "type": "single_choice",
      "question": "You run `KMeans(n_clusters=4, init='random', n_init=1)` on the same data five times, changing only `random_state`. The final inertia values are 812, 795, 1640, 803 and 2210. What best explains this, and what is the standard fix?",
      "options": [
        {
          "id": "A",
          "text": "The data changes between runs; fix it by calling fit only once."
        },
        {
          "id": "B",
          "text": "KMeans only converges to a local minimum that depends on the starting centroids. Use init='k-means++' (spread-out seeds) and n_init > 1, keeping the run with the lowest inertia."
        },
        {
          "id": "C",
          "text": "Inertia is random noise; report the average of the five values."
        },
        {
          "id": "D",
          "text": "The runs with higher inertia show that k is too small, so k should be increased until all runs agree."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Lloyd's algorithm is sensitive to seed initialization and frequently traps in sub-optimal local minima. Using K-Means++ initialization spreads initial seeds probabilistically, and n_init runs multiple restarts retaining the lowest-inertia solution.",
      "difficulty": "medium",
      "subtopic": "K-Means Initialization"
    },
    {
      "id": "cml-endterm-b-a20",
      "type": "single_choice",
      "question": "Two standardised columns have correlation $r = 0.5$. PCA is run on these two columns. What share of the total variance does PC1 explain?",
      "options": [
        {
          "id": "A",
          "text": "75%"
        },
        {
          "id": "B",
          "text": "50%"
        },
        {
          "id": "C",
          "text": "25%"
        },
        {
          "id": "D",
          "text": "100%"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "For two standardized columns, the 2x2 covariance matrix has eigenvalues 1 + r and 1 - r. For r = 0.5, eigenvalues are 1.5 and 0.5. Total variance = 2.0. Explained variance ratio of PC1 = 1.5 / 2.0 = 0.75 = 75%.",
      "difficulty": "medium",
      "subtopic": "Bivariate Standardized PCA"
    }
  ]
}
