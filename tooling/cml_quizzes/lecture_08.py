QUIZ_L08 = {
  "topicId": "lecture-08",
  "lectureNumber": 8,
  "title": "Classification: Logistic Regression, Thresholds & Imbalance",
  "description": "30 questions covering Logistic Regression mathematics, Sigmoid activation, Log-Loss/Cross-Entropy, Confusion Matrix metrics, ROC-AUC vs PR-AUC, threshold optimization, and handling imbalanced datasets.",
  "estimatedMinutes": 45,
  "questions": [
    {
      "id": "cml-l08-q01",
      "type": "single_choice",
      "question": "What is the primary mathematical reason why standard Ordinary Least Squares (OLS) Linear Regression is inappropriate for binary classification targets $y \\in \\{0, 1\\}$?",
      "options": [
        {
          "id": "A",
          "text": "Linear regression produces unbounded predictions that can range from $-\\infty$ to $+\\infty$, violating the probabilistic constraint $p \\in [0, 1]$"
        },
        {
          "id": "B",
          "text": "Linear regression cannot be optimized using gradient descent"
        },
        {
          "id": "C",
          "text": "Linear regression always outputs zero for any discrete variable"
        },
        {
          "id": "D",
          "text": "Linear regression requires all input features to be binary"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "OLS predicts continuous values $\\hat{y} = X\\beta$, which can easily be $< 0$ or $> 1$. Furthermore, squaring discrete 0/1 residuals unfairly penalizes extremely correct confident predictions and causes the decision boundary to skew when distant outliers are added.",
      "difficulty": "easy",
      "subtopic": "Linear Regression Limitations"
    },
    {
      "id": "cml-l08-q02",
      "type": "single_choice",
      "question": "What is the definition of 'odds' in probability theory, and what is its mapping to the logistic regression logit?",
      "options": [
        {
          "id": "A",
          "text": "$\\text{Odds} = p \\times (1 - p)$"
        },
        {
          "id": "B",
          "text": "$\\text{Odds} = \\frac{p}{1 - p}$; the log-odds (logit) $\\ln\\left(\\frac{p}{1 - p}\\right)$ is modeled as a linear function of features $w^T x + b$"
        },
        {
          "id": "C",
          "text": "$\\text{Odds} = 1 - p$"
        },
        {
          "id": "D",
          "text": "$\\text{Odds} = \\frac{1}{p}$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Odds is the ratio of the probability of success to failure: $\\frac{p}{1-p} \\in [0, \\infty)$. Taking the natural logarithm gives the logit $\\ln\\left(\\frac{p}{1-p}\\right) \\in (-\\infty, +\\infty)$, which maps the unconstrained real line directly onto a valid probability space via the sigmoid inverse.",
      "difficulty": "medium",
      "subtopic": "Odds & Logit"
    },
    {
      "id": "cml-l08-q03",
      "type": "single_choice",
      "question": "What is the mathematical derivative of the standard sigmoid function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$ with respect to $z$?",
      "options": [
        {
          "id": "A",
          "text": "$\\sigma'(z) = \\sigma(z)(1 - \\sigma(z))$"
        },
        {
          "id": "B",
          "text": "$\\sigma'(z) = 1 - \\sigma(z)^2$"
        },
        {
          "id": "C",
          "text": "$\\sigma'(z) = e^{-z}$"
        },
        {
          "id": "D",
          "text": "$\\sigma'(z) = \\frac{\\sigma(z)}{1 + e^{-z}}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Using the quotient rule: $\\frac{d}{dz}[ (1 + e^{-z})^{-1} ] = -(1 + e^{-z})^{-2}(-e^{-z}) = \\frac{e^{-z}}{(1 + e^{-z})^2} = \\frac{1}{1 + e^{-z}} \\cdot \\frac{e^{-z}}{1 + e^{-z}} = \\sigma(z)(1 - \\sigma(z))$.",
      "difficulty": "easy",
      "subtopic": "Sigmoid Calculus"
    },
    {
      "id": "cml-l08-q04",
      "type": "single_choice",
      "question": "What is the Binary Cross-Entropy (Log-Loss) formula for a dataset of $m$ instances with true labels $y^{(i)} \\in \\{0, 1\\}$ and predicted probabilities $\\hat{y}^{(i)}$?",
      "options": [
        {
          "id": "A",
          "text": "$J(w) = -\\frac{1}{m} \\sum_{i=1}^m \\left[ y^{(i)} \\ln(\\hat{y}^{(i)}) + (1 - y^{(i)}) \\ln(1 - \\hat{y}^{(i)}) \\right]$"
        },
        {
          "id": "B",
          "text": "$J(w) = \\frac{1}{2m} \\sum_{i=1}^m (y^{(i)} - \\hat{y}^{(i)})^2$"
        },
        {
          "id": "C",
          "text": "$J(w) = \\sum_{i=1}^m |y^{(i)} - \\hat{y}^{(i)}|$"
        },
        {
          "id": "D",
          "text": "$J(w) = -\\frac{1}{m} \\sum_{i=1}^m \\frac{y^{(i)}}{\\hat{y}^{(i)}}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Binary cross-entropy is the negative log-likelihood of the Bernoulli distribution: when $y=1$, loss is $-\\ln(\\hat{y})$; when $y=0$, loss is $-\\ln(1-\\hat{y})$. As predicted probability moves toward the wrong label, loss approaches infinity.",
      "difficulty": "easy",
      "subtopic": "Log-Loss Formula"
    },
    {
      "id": "cml-l08-q05",
      "type": "single_choice",
      "question": "What is the vectorized gradient $\\nabla_w J(w)$ of the Binary Cross-Entropy loss for Logistic Regression with predictions $\\hat{y} = \\sigma(Xw)$?",
      "options": [
        {
          "id": "A",
          "text": "$\\nabla_w J(w) = \\frac{1}{m} X^T (\\hat{y} - y)$"
        },
        {
          "id": "B",
          "text": "$\\nabla_w J(w) = -\\frac{1}{m} X^T (\\frac{y}{\\hat{y}})$"
        },
        {
          "id": "C",
          "text": "$\\nabla_w J(w) = \\frac{1}{m} (X^TXw - y)$"
        },
        {
          "id": "D",
          "text": "$\\nabla_w J(w) = \\frac{1}{m} \\sum (\\hat{y} - y)^2$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Remarkably, because $\\sigma'(z) = \\sigma(z)(1-\\sigma(z))$, the denominator in the derivative of the log terms cancels cleanly with the sigmoid derivative, yielding the exact same elegant vectorized gradient formula as linear regression: $\\nabla_w J(w) = \\frac{1}{m} X^T(\\hat{y} - y)$.",
      "difficulty": "medium",
      "subtopic": "Logistic Gradient Derivation"
    },
    {
      "id": "cml-l08-q06",
      "type": "single_choice",
      "question": "What is the geometric shape and equation of the decision boundary produced by a standard Logistic Regression model with features $x \\in \\mathbb{R}^p$ and classification threshold $0.5$?",
      "options": [
        {
          "id": "A",
          "text": "A circle defined by $\\|x\\|^2 = r^2$"
        },
        {
          "id": "B",
          "text": "A flat linear hyperplane defined by $w^T x + b = 0$"
        },
        {
          "id": "C",
          "text": "A parabolic cone"
        },
        {
          "id": "D",
          "text": "A step function with infinite discontinuities"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "At probability threshold 0.5, $\\sigma(w^Tx + b) = 0.5 \\iff \\frac{1}{1 + e^{-(w^Tx+b)}} = 0.5 \\iff e^{-(w^Tx+b)} = 1 \\iff w^Tx + b = 0$, which is the equation of an affine linear hyperplane in feature space.",
      "difficulty": "easy",
      "subtopic": "Linear Decision Boundary"
    },
    {
      "id": "cml-l08-q07",
      "type": "single_choice",
      "question": "A dataset contains 990 non-fraudulent transactions and 10 fraudulent transactions (1% positive class). A naive dummy model predicts 'Non-Fraud' for every single transaction. What is its Accuracy and Recall on the fraud class?",
      "options": [
        {
          "id": "A",
          "text": "Accuracy = 99%, Recall = 0%"
        },
        {
          "id": "B",
          "text": "Accuracy = 50%, Recall = 50%"
        },
        {
          "id": "C",
          "text": "Accuracy = 99%, Recall = 99%"
        },
        {
          "id": "D",
          "text": "Accuracy = 1%, Recall = 100%"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Out of 1000 total cases, it gets 990 correct (99% accuracy). However, $TP = 0$ out of 10 actual frauds, so $\\text{Recall} = \\frac{0}{10} = 0\\%$. This classic dilemma is known as the 'Accuracy Paradox'.",
      "difficulty": "easy",
      "subtopic": "Accuracy Paradox"
    },
    {
      "id": "cml-l08-q08",
      "type": "single_choice",
      "question": "In medical cancer diagnosis, failing to detect a patient who actually has cancer is catastrophic, whereas falsely flagging a healthy patient for a follow-up test is manageable. Which metric must be prioritized and maximized?",
      "options": [
        {
          "id": "A",
          "text": "Precision"
        },
        {
          "id": "B",
          "text": "Recall (Sensitivity / True Positive Rate)"
        },
        {
          "id": "C",
          "text": "Specificity"
        },
        {
          "id": "D",
          "text": "Overall Accuracy"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Failing to detect an actual disease is a False Negative ($FN$). Minimizing $FN$ is achieved by maximizing Recall = $\\frac{TP}{TP + FN}$.",
      "difficulty": "easy",
      "subtopic": "Recall in High-Stakes Domains"
    },
    {
      "id": "cml-l08-q09",
      "type": "single_choice",
      "question": "In an automated email spam filtering system, automatically moving an important job offer email to the Spam folder is unacceptable to users. Which metric must be prioritized?",
      "options": [
        {
          "id": "A",
          "text": "Precision (minimizing False Positives)"
        },
        {
          "id": "B",
          "text": "Recall (minimizing False Negatives)"
        },
        {
          "id": "C",
          "text": "Log-Loss alone"
        },
        {
          "id": "D",
          "text": "Mean Absolute Error"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "A legitimate email flagged as spam is a False Positive ($FP$). Maximizing Precision = $\\frac{TP}{TP + FP}$ ensures that when the system declares an email is spam, it is almost certainly correct.",
      "difficulty": "easy",
      "subtopic": "Precision in Low-Tolerance Domains"
    },
    {
      "id": "cml-l08-q10",
      "type": "single_choice",
      "question": "What is the formula and definition for the $F_1$ score?",
      "options": [
        {
          "id": "A",
          "text": "Arithmetic mean of Precision and Recall: $\\frac{P + R}{2}$"
        },
        {
          "id": "B",
          "text": "Harmonic mean of Precision and Recall: $2 \\frac{P \\cdot R}{P + R} = \\frac{2 TP}{2 TP + FP + FN}$"
        },
        {
          "id": "C",
          "text": "Geometric mean: $\\sqrt{P \\cdot R}$"
        },
        {
          "id": "D",
          "text": "Ratio of True Positives to False Positives: $\\frac{TP}{FP}$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The $F_1$ score is the harmonic mean of Precision and Recall. The harmonic mean heavily penalizes extreme imbalances: if either Precision or Recall collapses to 0, $F_1$ collapses to 0, unlike the arithmetic mean.",
      "difficulty": "easy",
      "subtopic": "F1 Score Definition"
    },
    {
      "id": "cml-l08-q11",
      "type": "single_choice",
      "question": "In the generalized $F_\\beta$ score formula $F_\\beta = (1 + \\beta^2) \\frac{\\text{Precision} \\times \\text{Recall}}{\\beta^2 \\text{Precision} + \\text{Recall}}$, which value of $\\beta$ places TWICE as much emphasis on Recall as on Precision?",
      "options": [
        {
          "id": "A",
          "text": "$\\beta = 0.5$"
        },
        {
          "id": "B",
          "text": "$\\beta = 1.0$"
        },
        {
          "id": "C",
          "text": "$\\beta = 2.0$ ($F_2$ score)"
        },
        {
          "id": "D",
          "text": "$\\beta = 4.0$"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "In $F_\\beta$, $\\beta$ measures the relative weight of Recall to Precision. $\\beta = 2$ gives the $F_2$ score, weighting Recall twice as heavily as Precision.",
      "difficulty": "medium",
      "subtopic": "F-beta Score"
    },
    {
      "id": "cml-l08-q12",
      "type": "single_choice",
      "question": "What are the axes of the Receiver Operating Characteristic (ROC) curve?",
      "options": [
        {
          "id": "A",
          "text": "X-axis: Precision, Y-axis: Recall"
        },
        {
          "id": "B",
          "text": "X-axis: False Positive Rate ($FPR = 1 - \\text{Specificity}$), Y-axis: True Positive Rate ($TPR = \\text{Recall}$)"
        },
        {
          "id": "C",
          "text": "X-axis: Threshold, Y-axis: Accuracy"
        },
        {
          "id": "D",
          "text": "X-axis: Number of Features, Y-axis: Loss"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The ROC curve plots the False Positive Rate ($FPR = \\frac{FP}{FP+TN}$) on the x-axis against the True Positive Rate ($TPR = \\frac{TP}{TP+FN}$) on the y-axis across all decision thresholds $\\tau \\in [0, 1]$.",
      "difficulty": "easy",
      "subtopic": "ROC Curve Axes"
    },
    {
      "id": "cml-l08-q13",
      "type": "single_choice",
      "question": "What is the probabilistic interpretation of the Area Under the ROC Curve (ROC-AUC)?",
      "options": [
        {
          "id": "A",
          "text": "The exact probability that the model will be 100% accurate in production"
        },
        {
          "id": "B",
          "text": "The probability that the classifier will rank a randomly chosen positive instance higher than a randomly chosen negative instance: $P(\\hat{y}_+ > \\hat{y}_-)$"
        },
        {
          "id": "C",
          "text": "The ratio of training loss to validation loss"
        },
        {
          "id": "D",
          "text": "The fraction of data points lying within 1 standard deviation of the mean"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "ROC-AUC is equivalent to the Wilcoxon-Mann-Whitney U-statistic: it equals the probability that a randomly selected positive sample receives a higher predicted probability/score than a randomly selected negative sample.",
      "difficulty": "medium",
      "subtopic": "ROC-AUC Interpretation"
    },
    {
      "id": "cml-l08-q14",
      "type": "single_choice",
      "question": "Why can the ROC-AUC score be deceptively high and provide an overly optimistic assessment of a classifier on a heavily imbalanced dataset (e.g. 99.9% negative class)?",
      "options": [
        {
          "id": "A",
          "text": "Because the large number of true negatives ($TN$) inflates the denominator of $FPR = \\frac{FP}{FP + TN}$, keeping FPR near zero even with numerous False Positives"
        },
        {
          "id": "B",
          "text": "Because ROC-AUC only evaluates the positive class"
        },
        {
          "id": "C",
          "text": "Because ROC curves require non-convex loss functions"
        },
        {
          "id": "D",
          "text": "Because ROC-AUC is strictly bounded by 0.5"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "When negatives are overwhelming (e.g. 1,000,000 TN), even 1,000 False Positives yields $FPR = \\frac{1000}{1001000} \\approx 0.001$, giving an almost perfect-looking ROC curve while the actual Precision $\\frac{TP}{TP+FP}$ may be abysmal. The Precision-Recall (PR) curve is preferred here.",
      "difficulty": "hard",
      "subtopic": "ROC-AUC on Imbalanced Data"
    },
    {
      "id": "cml-l08-q15",
      "type": "single_choice",
      "question": "What is the expected baseline Area Under the Precision-Recall Curve (PR-AUC) for a random dummy classifier on a dataset with positive class proportion $P = \\frac{N_\\text{pos}}{N_\\text{total}}$?",
      "options": [
        {
          "id": "A",
          "text": "Always 0.5 regardless of class balance"
        },
        {
          "id": "B",
          "text": "Equal to the fraction of positive instances $P$ in the dataset"
        },
        {
          "id": "C",
          "text": "Always 0.0"
        },
        {
          "id": "D",
          "text": "Always 1.0"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Unlike ROC-AUC (whose uninformative baseline is always 0.5), a random guesser achieves Precision equal to class prevalence $P = \\frac{N_\\text{pos}}{N_\\text{total}}$ at all recall levels. Hence baseline PR-AUC equals the positive class fraction $P$.",
      "difficulty": "medium",
      "subtopic": "PR Baseline"
    },
    {
      "id": "cml-l08-q16",
      "type": "single_choice",
      "question": "How does Synthetic Minority Over-sampling Technique (SMOTE) generate new synthetic positive training instances?",
      "options": [
        {
          "id": "A",
          "text": "By duplicating existing minority points verbatim with exact replacement"
        },
        {
          "id": "B",
          "text": "By selecting k-nearest neighbors among minority samples and interpolating along the line segment connecting them: $x_\\text{new} = x_i + \\lambda (x_{zi} - x_i)$ with $\\lambda \\in [0, 1]$"
        },
        {
          "id": "C",
          "text": "By adding Gaussian noise to the majority class instances"
        },
        {
          "id": "D",
          "text": "By inverting the labels of misclassified points"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Chawla et al. (2002) introduced SMOTE: for each minority instance, it finds its $k$-NN in feature space and draws synthetic samples along the line segments connecting them, enriching feature support without simple duplicate memorization.",
      "difficulty": "medium",
      "subtopic": "SMOTE Algorithm"
    },
    {
      "id": "cml-l08-q17",
      "type": "single_choice",
      "question": "When applying SMOTE or any oversampling technique, on which portion of the data MUST it be executed?",
      "options": [
        {
          "id": "A",
          "text": "Strictly on the training split/fold; NEVER on the validation or test splits"
        },
        {
          "id": "B",
          "text": "On the entire raw dataset before doing any train-test splitting"
        },
        {
          "id": "C",
          "text": "Strictly on the test set alone"
        },
        {
          "id": "D",
          "text": "Only on the features that have categorical encoding"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Applying SMOTE before splitting creates synthetic samples between points that end up in both training and test sets, causing severe data leakage and yielding fraudulent test metrics. Test sets must reflect real-world distributions.",
      "difficulty": "medium",
      "subtopic": "SMOTE Hygiene"
    },
    {
      "id": "cml-l08-q18",
      "type": "single_choice",
      "question": "How does setting `class_weight='balanced'` in Scikit-Learn's `LogisticRegression` adjust the loss function?",
      "options": [
        {
          "id": "A",
          "text": "It resamples the data automatically via SMOTE under the hood"
        },
        {
          "id": "B",
          "text": "It weights each class inversely proportional to its class frequency: $w_c = \\frac{n_\\text{samples}}{n_\\text{classes} \\times n_{c}}$, penalizing mistakes on the minority class much more severely"
        },
        {
          "id": "C",
          "text": "It sets the decision threshold strictly to 0.1"
        },
        {
          "id": "D",
          "text": "It removes majority samples until classes are equal"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Cost-sensitive weighting modifies the objective function $\\min_w -\\sum w_{y_i} \\log P(y_i|x_i)$. Rare classes receive large weights, forcing the gradient descent solver to treat minority errors with high penalty.",
      "difficulty": "medium",
      "subtopic": "Class Weighting"
    },
    {
      "id": "cml-l08-q19",
      "type": "single_choice",
      "question": "If you lower the classification probability threshold from $\\tau = 0.50$ to $\\tau = 0.20$ for predicting the positive class, what is the typical effect on Recall and Precision?",
      "options": [
        {
          "id": "A",
          "text": "Recall increases (or stays same), while Precision typically decreases"
        },
        {
          "id": "B",
          "text": "Recall decreases, while Precision increases"
        },
        {
          "id": "C",
          "text": "Both Recall and Precision increase to 1.0"
        },
        {
          "id": "D",
          "text": "Both Recall and Precision drop to 0.0"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Lowering the threshold makes it easier to predict positive, catching more true positives ($FN \\downarrow \\implies \\text{Recall} \\uparrow$), but introducing more false positives ($FP \\uparrow \\implies \\text{Precision} \\downarrow$).",
      "difficulty": "easy",
      "subtopic": "Threshold Shifting"
    },
    {
      "id": "cml-l08-q20",
      "type": "single_choice",
      "question": "In multinomial classification with $K > 2$ mutually exclusive classes, which activation function generalizes the binary sigmoid to output a valid probability distribution over all $K$ classes?",
      "options": [
        {
          "id": "A",
          "text": "Softmax: $P(y = k | x) = \\frac{e^{z_k}}{\\sum_{j=1}^K e^{z_j}}$"
        },
        {
          "id": "B",
          "text": "Hyperbolic Tangent (Tanh)"
        },
        {
          "id": "C",
          "text": "Rectified Linear Unit (ReLU)"
        },
        {
          "id": "D",
          "text": "Standard Normal Cumulative Distribution Function (Probit)"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The Softmax function normalizes a vector of arbitrary real logits $z$ into non-negative values that sum strictly to 1, providing the standard multinomial logistic regression activation.",
      "difficulty": "easy",
      "subtopic": "Multinomial Softmax"
    },
    {
      "id": "cml-l08-q21",
      "type": "single_choice",
      "question": "What is the Matthews Correlation Coefficient (MCC), and why is it considered one of the most robust single metrics for binary classification evaluation on imbalanced data?",
      "options": [
        {
          "id": "A",
          "text": "It computes the correlation between features and labels"
        },
        {
          "id": "B",
          "text": "It takes into account all four cells of the confusion matrix ($TP, TN, FP, FN$) and ranges from $-1$ to $+1$, yielding high scores only if the prediction is good across both classes"
        },
        {
          "id": "C",
          "text": "It is identical to the ROC-AUC score divided by 2"
        },
        {
          "id": "D",
          "text": "It ignores True Negatives entirely to focus on minority precision"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "MCC is defined as $\\frac{TP \\times TN - FP \\times FN}{\\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$. It evaluates all 4 quadrants symmetrically and returns a high score only if the model excels on both negative and positive classes.",
      "difficulty": "hard",
      "subtopic": "Matthews Correlation Coefficient"
    },
    {
      "id": "cml-l08-q22",
      "type": "single_choice",
      "question": "What occurs during training of Logistic Regression if the two classes are perfectly linearly separable and NO regularization penalty is applied?",
      "options": [
        {
          "id": "A",
          "text": "The weights $w$ explode to infinity ($\\|w\\| \\to \\infty$) as the solver attempts to drive predicted probabilities to exact 1 and 0"
        },
        {
          "id": "B",
          "text": "The model immediately defaults to predicting 0.5 for all samples"
        },
        {
          "id": "C",
          "text": "The loss function becomes strictly non-convex"
        },
        {
          "id": "D",
          "text": "The Hessian matrix becomes identity"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "If classes are linearly separable, the log-loss can be made arbitrarily close to 0 by scaling the weights $w$ to infinity, forcing $\\sigma(w^T x) \\to 1$ or $0$. Regularization (L2 penalty) is essential to prevent weight explosion.",
      "difficulty": "hard",
      "subtopic": "Separability & Weight Explosion"
    },
    {
      "id": "cml-l08-q23",
      "type": "multi_choice",
      "question": "Which of the following statements about the Sigmoid function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$ are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Its output range is strictly bounded within the open interval $(0, 1)$"
        },
        {
          "id": "B",
          "text": "It is symmetric about the point $(0, 0.5)$, such that $\\sigma(-z) = 1 - \\sigma(z)$"
        },
        {
          "id": "C",
          "text": "Its maximum gradient occurs at $z = 0$, where $\\sigma'(0) = 0.25$"
        },
        {
          "id": "D",
          "text": "For very large positive or negative $z$, the gradient $\\sigma'(z) \\approx 0$ (saturation / vanishing gradient)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four are key mathematical properties of the standard sigmoid curve: range $(0, 1)$, point symmetry $\\sigma(-z) = 1 - \\sigma(z)$, peak derivative $0.5 \\times 0.5 = 0.25$ at $z=0$, and flat tails at the extremes.",
      "difficulty": "medium",
      "subtopic": "Sigmoid Properties"
    },
    {
      "id": "cml-l08-q24",
      "type": "multi_choice",
      "question": "Which of the following are valid formulas derived from the 2x2 confusion matrix with entries TP, FP, TN, FN? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "$\\text{Precision} = \\frac{TP}{TP + FP}$"
        },
        {
          "id": "B",
          "text": "$\\text{Recall (TPR)} = \\frac{TP}{TP + FN}$"
        },
        {
          "id": "C",
          "text": "$\\text{Specificity (TNR)} = \\frac{TN}{TN + FP}$"
        },
        {
          "id": "D",
          "text": "$\\text{False Positive Rate (FPR)} = 1 - \\text{Specificity} = \\frac{FP}{TN + FP}$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four definitions are canonical standards in classification statistics and machine learning diagnostics.",
      "difficulty": "easy",
      "subtopic": "Confusion Matrix Taxonomy"
    },
    {
      "id": "cml-l08-q25",
      "type": "multi_choice",
      "question": "Which of the following techniques are effective for training machine learning models on severely imbalanced datasets? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Cost-sensitive learning by applying class weights in the loss function (`class_weight='balanced'`)"
        },
        {
          "id": "B",
          "text": "Synthetic oversampling of the minority class using SMOTE strictly within training folds"
        },
        {
          "id": "C",
          "text": "Tuning the decision threshold based on business costs rather than defaulting to 0.5"
        },
        {
          "id": "D",
          "text": "Reporting training accuracy as the sole success metric"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are proven industry strategies for class imbalance. D is disastrous due to the accuracy paradox.",
      "difficulty": "easy",
      "subtopic": "Imbalance Solutions"
    },
    {
      "id": "cml-l08-q26",
      "type": "multi_choice",
      "question": "Which of the following statements comparing ROC Curves and Precision-Recall (PR) Curves are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "ROC curves are invariant to class distribution shifts because TPR and FPR are calculated independently within each class"
        },
        {
          "id": "B",
          "text": "PR curves are sensitive to class skew because Precision includes both positive ($TP$) and negative ($FP$) class predictions in its denominator"
        },
        {
          "id": "C",
          "text": "On heavily skewed datasets where the positive class is rare, PR curves provide a much more realistic picture of algorithm utility than ROC curves"
        },
        {
          "id": "D",
          "text": "A perfect classifier achieves an area of 1.0 under both ROC and PR curves"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four statements are scientifically exact (Davis & Goadrich 2006): ROC evaluates within-class rates; PR incorporates cross-class ratios, highlighting precision collapses in rare positive settings.",
      "difficulty": "hard",
      "subtopic": "ROC vs PR Deep Comparison"
    },
    {
      "id": "cml-l08-q27",
      "type": "multi_choice",
      "question": "When constructing a commercial fraud detection model where each false negative costs $500 in direct losses and each false positive costs $5 in manual review, what strategy should the ML engineer pursue? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Lower the classification threshold well below 0.5 to catch far more fraudulent transactions, accepting higher false positives"
        },
        {
          "id": "B",
          "text": "Optimize the decision threshold to minimize expected total dollar cost: $\\text{Cost} = 500 \\times FN + 5 \\times FP$"
        },
        {
          "id": "C",
          "text": "Tune the model to maximize the $F_\\beta$ score with $\\beta > 1$ (e.g. $F_2$) rather than standard $F_1$ or accuracy"
        },
        {
          "id": "D",
          "text": "Raise the threshold to 0.95 to eliminate false alarms completely"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Because FN is 100x more expensive than FP, the engineer must prioritize recall by lowering threshold (A), minimizing business cost function (B), and weighting recall higher via $F_\\beta$ (C). D does the opposite, allowing massive fraud losses.",
      "difficulty": "medium",
      "subtopic": "Cost-Benefit Decision Optimization"
    },
    {
      "id": "cml-l08-q28",
      "type": "multi_choice",
      "question": "Which of the following statements about multi-class classification strategies for binary classifiers like Logistic Regression are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "One-vs-Rest (OvR / One-vs-All) trains $K$ separate binary models, each distinguishing class $k$ from all remaining $K-1$ classes combined"
        },
        {
          "id": "B",
          "text": "One-vs-One (OvO) trains $\\frac{K(K-1)}{2}$ binary models, each distinguishing between a specific pair of classes"
        },
        {
          "id": "C",
          "text": "Multinomial Logistic Regression (Softmax Regression) fits all classes jointly in a single model using categorical cross-entropy"
        },
        {
          "id": "D",
          "text": "One-vs-One requires fewer models than One-vs-Rest when $K = 10$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are standard multi-class paradigms. D is FALSE: for $K=10$, OvR requires 10 models, whereas OvO requires $\\frac{10 \\times 9}{2} = 45$ models.",
      "difficulty": "medium",
      "subtopic": "Multiclass Strategies"
    },
    {
      "id": "cml-l08-q29",
      "type": "multi_choice",
      "question": "Which of the following conditions guarantee that the Binary Cross-Entropy loss surface for Logistic Regression is strictly convex with no suboptimal local minima? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The Hessian matrix $H = \\frac{1}{m} X^T D X$ (where $D$ is a diagonal matrix with positive entries $D_{ii} = \\hat{y}_i(1 - \\hat{y}_i) > 0$) is positive semi-definite for any design matrix $X$"
        },
        {
          "id": "B",
          "text": "The model uses linear logit combinations $z = w^T x + b$ without non-convex hidden activations"
        },
        {
          "id": "C",
          "text": "Adding L2 regularization adds a positive definite matrix $\\lambda I$, making the objective strictly convex with a unique global minimum"
        },
        {
          "id": "D",
          "text": "The target classes must have exactly equal 50-50 sample counts"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are mathematical foundations of logistic loss convexity. Class proportions (D) do not alter the convexity of the Hessian.",
      "difficulty": "hard",
      "subtopic": "Loss Convexity & Hessian"
    },
    {
      "id": "cml-l08-q30",
      "type": "multi_choice",
      "question": "Which of the following statements about probability calibration (e.g. Platt Scaling or Isotonic Regression) in classification models are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "A well-calibrated classifier ensures that among instances predicted with probability 0.8, approximately 80% truly belong to the positive class"
        },
        {
          "id": "B",
          "text": "Uncalibrated models can produce high ROC-AUC (correct ranking) while producing badly distorted absolute probability estimates"
        },
        {
          "id": "C",
          "text": "Calibration plots (reliability diagrams) plot the mean predicted probability against the observed empirical fraction of positives in binned intervals"
        },
        {
          "id": "D",
          "text": "Calibration always changes the ROC curve and alters the ranking order of samples"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are true definitions of calibration and reliability diagrams. D is FALSE: monotonic calibration (like Platt scaling or isotonic regression) preserves rank order, leaving ROC-AUC unchanged while fixing probability magnitudes.",
      "difficulty": "hard",
      "subtopic": "Probability Calibration"
    }
  ]
}
