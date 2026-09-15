QUIZ_L10 = {
  "topicId": "lecture-10",
  "lectureNumber": 10,
  "title": "Industrial Machine Learning: Churn Prediction & Model Operationalization",
  "description": "20 questions covering industrial end-to-end pipelines, asymmetric business cost matrices, dummy baseline benchmarks, Odds Ratios, Permutation Feature Importance, SHAP values, and production monitoring (Data Drift vs Concept Drift).",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml-l10-q01",
      "type": "single_choice",
      "question": "In an industrial customer churn prediction system, why is evaluating model performance using a business Cost-Benefit Matrix superior to evaluating standard accuracy or F1 score alone?",
      "options": [
        {
          "id": "A",
          "text": "Because standard ML metrics implicitly assume that false positives and false negatives carry identical economic consequences, whereas in business, losing a customer ($FN$) is typically vastly more expensive than sending a retention discount ($FP$)"
        },
        {
          "id": "B",
          "text": "Because cost-benefit matrices run faster on GPUs"
        },
        {
          "id": "C",
          "text": "Because accuracy cannot be computed for binary classification"
        },
        {
          "id": "D",
          "text": "Because cost matrices eliminate the need for cross-validation"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Standard accuracy and F1 weigh errors symmetrically or harmonically without financial calibration. A business matrix maps each confusion quadrant ($TP, FP, TN, FN$) to exact dollar revenues and retention intervention costs, directly measuring bottom-line ROI.",
      "difficulty": "easy",
      "subtopic": "Business Cost-Benefit Matrix"
    },
    {
      "id": "cml-l10-q02",
      "type": "single_choice",
      "question": "Why is it mandatory in modern MLOps to benchmark a candidate machine learning model against Scikit-Learn's `DummyClassifier(strategy='most_frequent')`?",
      "options": [
        {
          "id": "A",
          "text": "To verify that the model can learn at least some meaningful signal beyond trivial majority-class guessing"
        },
        {
          "id": "B",
          "text": "To compute the matrix inverse of the target vector"
        },
        {
          "id": "C",
          "text": "To initialize the weights of logistic regression"
        },
        {
          "id": "D",
          "text": "To remove collinear features automatically"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "On imbalanced datasets (e.g. 95% non-churn), a naive model that predicts non-churn 100% of the time gets 95% accuracy with zero predictive intelligence. A dummy baseline establishes the true 'zero-skill' floor that any deployed model must decisively surpass.",
      "difficulty": "easy",
      "subtopic": "Dummy Baselines"
    },
    {
      "id": "cml-l10-q03",
      "type": "single_choice",
      "question": "In a Logistic Regression model, if the estimated coefficient for feature $x_j$ is $\\beta_j = +0.693$ (where $\\ln(2) \\approx 0.693$), how does a 1-unit increase in $x_j$ affect the odds of churning?",
      "options": [
        {
          "id": "A",
          "text": "The probability of churning increases by exactly 69.3%"
        },
        {
          "id": "B",
          "text": "The odds of churning are multiplied by $e^{0.693} \\approx 2.0$ (churn odds double)"
        },
        {
          "id": "C",
          "text": "The churn rate decreases by half"
        },
        {
          "id": "D",
          "text": "The customer lifetime value drops by $0.693"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In logistic regression, $\\ln(\\text{Odds}) = \\sum \\beta_i x_i$. An increase $\\Delta x_j = 1$ leads to $\\ln(\\text{Odds}_\\text{new}) = \\ln(\\text{Odds}) + \\beta_j \\implies \\text{Odds}_\\text{new} = \\text{Odds} \\times e^{\\beta_j}$. Here $e^{0.693} \\approx 2.0$, meaning the odds of churn double.",
      "difficulty": "medium",
      "subtopic": "Odds Ratio Interpretation"
    },
    {
      "id": "cml-l10-q04",
      "type": "single_choice",
      "question": "How does Permutation Feature Importance quantify the importance of a predictor variable in a trained model?",
      "options": [
        {
          "id": "A",
          "text": "By computing the magnitude of the model's weight coefficients $\\|w\\|_2$"
        },
        {
          "id": "B",
          "text": "By randomly shuffling the values of that feature column in the validation set and measuring the resulting drop in model evaluation score (e.g., ROC-AUC)"
        },
        {
          "id": "C",
          "text": "By training a new model without that feature from scratch"
        },
        {
          "id": "D",
          "text": "By calculating the Pearson correlation between that feature and the target"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Permutation importance breaks the relationship between feature $j$ and target $y$ by shuffling column $j$ in the validation set while keeping other columns intact. The larger the drop in model score, the more critical feature $j$ was to prediction.",
      "difficulty": "medium",
      "subtopic": "Permutation Feature Importance"
    },
    {
      "id": "cml-l10-q05",
      "type": "single_choice",
      "question": "What mathematical property makes SHAP (SHapley Additive exPlanations) values uniquely principled for local and global model explainability?",
      "options": [
        {
          "id": "A",
          "text": "They are rooted in cooperative game theory (Shapley values), guaranteeing efficiency, symmetry, dummy player zero attribution, and additivity"
        },
        {
          "id": "B",
          "text": "They evaluate gradients in $O(1)$ time for any neural network"
        },
        {
          "id": "C",
          "text": "They only work on linear regression models"
        },
        {
          "id": "D",
          "text": "They eliminate all multicollinearity from the dataset"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Lundberg and Lee (2017) proved that SHAP values are the ONLY additive feature attribution method satisfying efficiency (attributions sum to the difference between model output and expected value), symmetry, dummy/null effect, and monotonicity.",
      "difficulty": "hard",
      "subtopic": "SHAP Values Foundation"
    },
    {
      "id": "cml-l10-q06",
      "type": "single_choice",
      "question": "In Python ML engineering, why is `joblib.dump(pipeline, 'model.joblib')` preferred over Python's built-in `pickle` for serializing Scikit-Learn models?",
      "options": [
        {
          "id": "A",
          "text": "`joblib` automatically encrypts the model file using AES-256"
        },
        {
          "id": "B",
          "text": "`joblib` is optimized to serialize and deserialize large NumPy arrays with minimal overhead using memory-mapping techniques"
        },
        {
          "id": "C",
          "text": "`pickle` cannot serialize Scikit-Learn pipelines"
        },
        {
          "id": "D",
          "text": "`joblib` converts the model into C++ source code"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "`joblib` is tailored for scientific Python objects containing large continuous NumPy ndarrays, serializing them significantly faster and enabling efficient memory-mapped read access (`mmap_mode`).",
      "difficulty": "easy",
      "subtopic": "Model Serialization"
    },
    {
      "id": "cml-l10-q07",
      "type": "single_choice",
      "question": "What is the crucial operational distinction between 'Covariate Shift' (Data Drift) and 'Concept Drift' in deployed machine learning systems?",
      "options": [
        {
          "id": "A",
          "text": "Covariate Shift is a change in the input feature distribution $P(X)$ while the target mapping $P(Y|X)$ remains constant; Concept Drift is a change in the underlying relationship $P(Y|X)$ between features and targets"
        },
        {
          "id": "B",
          "text": "Covariate Shift affects only regression models, while Concept Drift affects only classification models"
        },
        {
          "id": "C",
          "text": "Covariate Shift occurs on the server, while Concept Drift occurs in the mobile client"
        },
        {
          "id": "D",
          "text": "There is no difference; they are interchangeable terms"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "In Data Drift (Covariate Shift), users' characteristics change ($P(X)$ shifts, e.g., younger users join), but the behavioral rules stay same. In Concept Drift, customer habits change ($P(Y|X)$ shifts, e.g. a competitor launches a superior service so previously loyal demographics churn).",
      "difficulty": "medium",
      "subtopic": "Data Drift vs Concept Drift"
    },
    {
      "id": "cml-l10-q08",
      "type": "single_choice",
      "question": "Which statistical test is standardly used by MLOps monitoring systems (e.g., Evidently AI) to detect Covariate Shift in continuous numerical features between reference and production data?",
      "options": [
        {
          "id": "A",
          "text": "Two-sample Kolmogorov-Smirnov (K-S) test"
        },
        {
          "id": "B",
          "text": "Durbin-Watson test"
        },
        {
          "id": "C",
          "text": "Shapiro-Wilk normality test"
        },
        {
          "id": "D",
          "text": "Breusch-Pagan test"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The two-sample Kolmogorov-Smirnov test is a non-parametric test comparing the empirical cumulative distribution functions of two samples ($D = \\sup_x |F_1(x) - F_2(x)|$), ideal for detecting shifts in arbitrary continuous feature distributions.",
      "difficulty": "medium",
      "subtopic": "Statistical Drift Detection"
    },
    {
      "id": "cml-l10-q09",
      "type": "single_choice",
      "question": "What metric is widely used in commercial credit scoring and risk modeling to measure distribution stability between development and production populations?",
      "options": [
        {
          "id": "A",
          "text": "Population Stability Index (PSI): $\\text{PSI} = \\sum (P_i - Q_i) \\times \\ln(P_i / Q_i)$"
        },
        {
          "id": "B",
          "text": "Adjusted $R^2$"
        },
        {
          "id": "C",
          "text": "Variance Inflation Factor (VIF)"
        },
        {
          "id": "D",
          "text": "Akaike Information Criterion (AIC)"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "PSI is a symmetric Kullback-Leibler divergence measuring shift between reference ($P$) and production ($Q$). Rules of thumb: $\\text{PSI} < 0.1$ indicates stable distribution; $\\text{PSI} > 0.25$ indicates significant shift requiring model retraining.",
      "difficulty": "hard",
      "subtopic": "Population Stability Index"
    },
    {
      "id": "cml-l10-q10",
      "type": "single_choice",
      "question": "When serving a Scikit-Learn classification model via a real-time REST API (e.g. with FastAPI), how should incoming JSON request payloads be preprocessed?",
      "options": [
        {
          "id": "A",
          "text": "Feed the raw dictionary directly to `pipeline.predict_proba()`, letting the bundled Pipeline handle imputation, one-hot encoding, and scaling seamlessly in one call"
        },
        {
          "id": "B",
          "text": "Manually re-run `fit_transform` on the single incoming JSON row"
        },
        {
          "id": "C",
          "text": "Train a new model on the single request payload"
        },
        {
          "id": "D",
          "text": "Convert all text fields to ASCII byte sums"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Packaging transformations and estimators into a single Scikit-Learn `Pipeline` ensures that `pipeline.predict_proba(df)` executes the exact same frozen `transform` steps calibrated during training, preventing training-serving skew.",
      "difficulty": "easy",
      "subtopic": "Inference API Architecture"
    },
    {
      "id": "cml-l10-q11",
      "type": "single_choice",
      "question": "What is 'Training-Serving Skew' in production machine learning systems?",
      "options": [
        {
          "id": "A",
          "text": "A discrepancy between how features are computed or transformed during model training vs. how they are computed during live production serving"
        },
        {
          "id": "B",
          "text": "The difference in clock time between CPU training and GPU serving"
        },
        {
          "id": "C",
          "text": "The difference between training loss and test loss"
        },
        {
          "id": "D",
          "text": "A bug where the database runs out of disk storage"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Training-serving skew occurs when live production data pipelines compute features differently than the offline batch ETL training scripts (e.g. using slightly different timezone definitions, differing categorical encodings, or missing scalers).",
      "difficulty": "easy",
      "subtopic": "Training-Serving Skew"
    },
    {
      "id": "cml-l10-q12",
      "type": "single_choice",
      "question": "In customer churn retention, what is the 'Do Not Disturb' or 'Sleeping Dogs' customer segment in Uplift Modeling?",
      "options": [
        {
          "id": "A",
          "text": "Customers who will stay if and only if they receive an incentive"
        },
        {
          "id": "B",
          "text": "Customers who would have stayed if left alone, but the retention contact (e.g. reminder email) annoys them or reminds them of the recurring fee, causing them to churn"
        },
        {
          "id": "C",
          "text": "Customers who have already deleted their account"
        },
        {
          "id": "D",
          "text": "Customers who generate zero revenue"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In Uplift Modeling, 'Sleeping Dogs' are customers whose churn probability actually increases if contacted. Standard churn models mistakenly target them with promotions, unintentionally accelerating churn.",
      "difficulty": "medium",
      "subtopic": "Uplift Modeling"
    },
    {
      "id": "cml-l10-q13",
      "type": "single_choice",
      "question": "Why is Pydantic widely utilized in Python production inference services (like FastAPI) for machine learning?",
      "options": [
        {
          "id": "A",
          "text": "To enforce strict schema typing, validate incoming input data bounds, and reject malformed requests with informative 422 HTTP errors before hitting the model"
        },
        {
          "id": "B",
          "text": "To compile Python bytecode to assembly"
        },
        {
          "id": "C",
          "text": "To compute eigenvalues of the design matrix"
        },
        {
          "id": "D",
          "text": "To replace NumPy array calculations"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Pydantic validates input schemas (data types, range bounds, required fields), guaranteeing that live inputs conform strictly to expectations and blocking corrupt payloads before they reach the ML pipeline.",
      "difficulty": "easy",
      "subtopic": "Schema Validation with Pydantic"
    },
    {
      "id": "cml-l10-q14",
      "type": "single_choice",
      "question": "In production ML monitoring, what is 'Shadow Deployment' (Dark Launching)?",
      "options": [
        {
          "id": "A",
          "text": "Deploying the new model at midnight when server traffic is minimal"
        },
        {
          "id": "B",
          "text": "Routing live production traffic to the new candidate model in parallel with the incumbent model, recording its predictions and latency for evaluation without serving its outputs to actual users"
        },
        {
          "id": "C",
          "text": "Serving predictions with all user IDs encrypted"
        },
        {
          "id": "D",
          "text": "Deploying the model without version control tags"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Shadow deployment sends real production requests to the candidate model silently. This tests real-world throughput, latency, and predictive behavior against production distributions without risking user experience or business KPIs.",
      "difficulty": "medium",
      "subtopic": "Deployment Strategies"
    },
    {
      "id": "cml-l10-q15",
      "type": "multi_choice",
      "question": "Which of the following metrics are essential to log and monitor continuously for a deployed production ML model? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Prediction latency (p50, p95, p99 percentiles in milliseconds)"
        },
        {
          "id": "B",
          "text": "Input feature distribution statistics (mean, variance, missing value percentages)"
        },
        {
          "id": "C",
          "text": "Output prediction distribution (fraction of positive predictions over time)"
        },
        {
          "id": "D",
          "text": "System metrics (CPU, RAM utilization, and HTTP error rates)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "Complete production observability requires monitoring infrastructure performance (A, D), data quality/drift (B), and concept/prediction shifts (C).",
      "difficulty": "easy",
      "subtopic": "MLOps Observability"
    },
    {
      "id": "cml-l10-q16",
      "type": "multi_choice",
      "question": "Which of the following statements about feature importance methods are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Logistic regression coefficients $\\beta_j$ reflect feature importance only if all features have been standardized to identical scales"
        },
        {
          "id": "B",
          "text": "Permutation feature importance is model-agnostic and can be evaluated on any trained black-box model"
        },
        {
          "id": "C",
          "text": "SHAP provides both local explanations (for individual predictions) and global explanations (aggregated across all samples)"
        },
        {
          "id": "D",
          "text": "Permutation importance computed on the training set is always more reliable than on the validation set"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are accurate explainability principles. D is FALSE: permutation importance on the training set can be misleadingly high for overfitted features; it should be computed on held-out validation data.",
      "difficulty": "medium",
      "subtopic": "Explainability Principles"
    },
    {
      "id": "cml-l10-q17",
      "type": "multi_choice",
      "question": "When designing an end-to-end customer churn retention workflow, which operational considerations are critical? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Aligning the prediction window (e.g. predicting churn in the next 30 days) with the marketing team's campaign cycle time"
        },
        {
          "id": "B",
          "text": "Excluding contemporaneous features from the churn month to prevent temporal target leakage"
        },
        {
          "id": "C",
          "text": "Calculating the net profitability of retention incentives (discounts, calls) vs the risk of churn"
        },
        {
          "id": "D",
          "text": "Retraining the model every 5 seconds to eliminate concept drift"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C reflect core enterprise data science engineering. D is absurd and impractical; monthly or weekly batch retraining is customary for churn models.",
      "difficulty": "medium",
      "subtopic": "Industrial Workflow Design"
    },
    {
      "id": "cml-l10-q18",
      "type": "multi_choice",
      "question": "Which of the following actions should an engineering team take upon detecting statistically significant Concept Drift in a deployed classifier? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Trigger an automated retraining pipeline on recent labeled production ground truth"
        },
        {
          "id": "B",
          "text": "Inspect feature importance changes to understand how user behaviors evolved"
        },
        {
          "id": "C",
          "text": "Consider falling back to a rules-based system or previous baseline if model performance degrades severely"
        },
        {
          "id": "D",
          "text": "Permanently delete all historical logs to hide the performance drop"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A updates the model to recent reality; B diagnoses the cause; C provides graceful degradation and risk mitigation. D violates engineering ethics and operational governance.",
      "difficulty": "easy",
      "subtopic": "Handling Concept Drift"
    },
    {
      "id": "cml-l10-q19",
      "type": "multi_choice",
      "question": "Which of the following deployment paradigms are standardly employed for serving machine learning models in production? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Real-time synchronous inference via REST/gRPC API microservices"
        },
        {
          "id": "B",
          "text": "Offline batch inference (e.g. daily cron jobs writing churn predictions to a SQL data warehouse)"
        },
        {
          "id": "C",
          "text": "Edge / Embedded deployment directly on mobile client devices"
        },
        {
          "id": "D",
          "text": "Canary deployment (routing a small fraction 5% of user traffic to a new model version before full rollout)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four are standard deployment patterns in modern machine learning systems architecture.",
      "difficulty": "easy",
      "subtopic": "Deployment Paradigms"
    },
    {
      "id": "cml-l10-q20",
      "type": "multi_choice",
      "question": "Which of the following statements regarding the business economics of churn prediction are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Acquiring a new customer is generally 5x to 25x more expensive than retaining an existing customer"
        },
        {
          "id": "B",
          "text": "A retention campaign with a 10% save rate can still be highly profitable if the customer lifetime value (CLV) is sufficiently high"
        },
        {
          "id": "C",
          "text": "Maximizing raw classification accuracy will always maximize net business profits"
        },
        {
          "id": "D",
          "text": "The optimal probability threshold for taking action depends directly on the cost of the retention incentive and the expected value of customer retention"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "A and B are foundational business economics principles of retention. D governs optimal threshold selection via decision theory. C is false because accuracy ignores asymmetric error costs.",
      "difficulty": "medium",
      "subtopic": "Churn Business Economics"
    }
  ]
}
