QUIZ_L01 = {
  "topicId": "lecture-01",
  "lectureNumber": 1,
  "title": "Introduction to Classical Machine Learning Quiz",
  "description": "20 questions covering Mitchell's ETP framework, ML vs classical programming, regression vs classification, supervised vs unsupervised paradigms, and the exploratory DSML toolbox.",
  "estimatedMinutes": 25,
  "questions": [
    {
      "id": "cml01-q01",
      "type": "single_choice",
      "question": "You want to display and analyze the distribution and modality of exam scores for 200 students in a cohort. Which exploratory visualization is best suited for this task?",
      "options": [
        {
          "id": "A",
          "text": "Bar Plot comparing individual student scores"
        },
        {
          "id": "B",
          "text": "Histogram (or Kernel Density Estimate plot)"
        },
        {
          "id": "C",
          "text": "Scatter Plot against student roll numbers"
        },
        {
          "id": "D",
          "text": "Line Plot connecting chronological submissions"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A Histogram bins continuous numeric values into intervals and plots their frequency counts, making it the canonical plot to reveal distribution shape, skewness, and modality (e.g., unimodal vs bimodal). Bar plots are for discrete categorical counts, scatter plots display bivariate associations, and line plots track sequential/temporal order.",
      "difficulty": "easy",
      "subtopic": "DSML Exploratory Toolbox"
    },
    {
      "id": "cml01-q02",
      "type": "single_choice",
      "question": "Which statement captures the fundamental operational difference between Classical (Rule-Based) Programming and Machine Learning?",
      "options": [
        {
          "id": "A",
          "text": "Classical programming operates on floating point numbers, whereas machine learning only operates on integers and strings."
        },
        {
          "id": "B",
          "text": "In classical programming, human engineers handcraft explicit logic/rules; in machine learning, algorithms extract statistical patterns and decision boundaries directly from data."
        },
        {
          "id": "C",
          "text": "Classical programming requires cloud GPUs, while machine learning algorithms only run on local CPU threads."
        },
        {
          "id": "D",
          "text": "Machine learning completely eliminates the need for test sets, validation, or debugging."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In classical programming: Input + Handcrafted Rules -> Output. In machine learning: Input + Labeled Outcomes (or structural data) -> Learning Algorithm -> Learned Hypothesis/Rules. ML is chosen when the underlying mapping is too complex, noisy, or dynamic to manually specify with deterministic if/else logic.",
      "difficulty": "easy",
      "subtopic": "ML vs Classical Programming"
    },
    {
      "id": "cml01-q03",
      "type": "single_choice",
      "question": "According to Tom Mitchell's foundational definition of Machine Learning, a computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if:",
      "options": [
        {
          "id": "A",
          "text": "Its execution speed increases linearly with the size of dataset E."
        },
        {
          "id": "B",
          "text": "Its performance at tasks in T, as measured by P, improves with experience E."
        },
        {
          "id": "C",
          "text": "It can replace human software engineers without any domain oversight."
        },
        {
          "id": "D",
          "text": "Its training error drops monotonically to zero on experience E."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Tom Mitchell (1997) formally defines learning: 'A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.'",
      "difficulty": "easy",
      "subtopic": "Mitchell's ETP Framework"
    },
    {
      "id": "cml01-q04",
      "type": "single_choice",
      "question": "In an autonomous email spam filtering system, which triplet correctly identifies Mitchell's E, T, and P components?",
      "options": [
        {
          "id": "A",
          "text": "E: Precision score; T: Receiving SMTP packets; P: Historical spam database"
        },
        {
          "id": "B",
          "text": "E: Historical emails with human spam/ham labels; T: Classifying an incoming email as spam or non-spam; P: F1-score or Accuracy on held-out test emails"
        },
        {
          "id": "C",
          "text": "E: Python scikit-learn library; T: Running gradient descent; P: Number of CPU clock cycles"
        },
        {
          "id": "D",
          "text": "E: Unlabeled server logs; T: Writing regex filters; P: Network bandwidth utilized"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Experience E is the training data (historical emails labeled as spam or ham). Task T is the target decision (classifying an incoming email). Performance measure P evaluates generalization quality (e.g., F1-score or accuracy on unseen emails).",
      "difficulty": "easy",
      "subtopic": "Mitchell's ETP Framework"
    },
    {
      "id": "cml01-q05",
      "type": "single_choice",
      "question": "What is the primary technical distinction between Classification and Regression in supervised learning?",
      "options": [
        {
          "id": "A",
          "text": "Classification uses continuous inputs, whereas regression only accepts discrete categorical inputs."
        },
        {
          "id": "B",
          "text": "Classification maps inputs to a discrete categorical label; regression maps inputs to a continuous real-valued quantity."
        },
        {
          "id": "C",
          "text": "Regression requires gradient descent, whereas classification can only be solved using closed-form linear algebra."
        },
        {
          "id": "D",
          "text": "Classification models can never output probabilities, only hard binary integers 0 or 1."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The distinction lies strictly in the nature of the output target: Classification targets are discrete categories (e.g., churn: {yes, no} or digits: {0,...,9}), whereas Regression targets are continuous real numbers in R (e.g., house price in dollars, temperature). Both can accept continuous, discrete, or mixed input features.",
      "difficulty": "easy",
      "subtopic": "Supervised Task Taxonomy"
    },
    {
      "id": "cml01-q06",
      "type": "single_choice",
      "question": "A real estate agency has a historical database of property transactions with features such as square footage, bedroom count, and past sale prices. A client asks: 'What is the estimated market sale price for a 3-bedroom, 1800 sq.ft home in Sector 4?' Which ML paradigm is required?",
      "options": [
        {
          "id": "A",
          "text": "Unsupervised Clustering"
        },
        {
          "id": "B",
          "text": "Supervised Regression"
        },
        {
          "id": "C",
          "text": "Supervised Binary Classification"
        },
        {
          "id": "D",
          "text": "Dimensionality Reduction (PCA)"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Because the historical data contains ground-truth targets (sale price), it is supervised learning. Because the predicted target (market sale price in currency) is a continuous numerical variable, it is a regression problem.",
      "difficulty": "easy",
      "subtopic": "Supervised Task Taxonomy"
    },
    {
      "id": "cml01-q07",
      "type": "single_choice",
      "question": "A team has 50,000 raw customer feedback text comments without any pre-existing tags or labels. Leadership wants to discover latent thematic buckets (e.g., shipping delays, billing errors, packaging quality). Which paradigm should be employed?",
      "options": [
        {
          "id": "A",
          "text": "Supervised Classification"
        },
        {
          "id": "B",
          "text": "Unsupervised Learning (Clustering / Topic Modeling)"
        },
        {
          "id": "C",
          "text": "Supervised Polynomial Regression"
        },
        {
          "id": "D",
          "text": "Reinforcement Learning with immediate reward signals"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Because there are no pre-existing ground-truth labels provided during training, the algorithm must discover intrinsic structure and clusters directly from feature representations. This is unsupervised learning.",
      "difficulty": "easy",
      "subtopic": "Supervised vs Unsupervised"
    },
    {
      "id": "cml01-q08",
      "type": "single_choice",
      "question": "A human resources department has established 4 predefined candidate hiring bands: 'Reject', 'Intern', 'L1 SDE', 'L2 SDE'. They ask a data scientist to build a system to assign new applicant resumes into these 4 specific bands based on previous historical interview evaluations. What should the data scientist recommend?",
      "options": [
        {
          "id": "A",
          "text": "An unsupervised K-Means clustering algorithm that invents 4 arbitrary clusters based on resume text."
        },
        {
          "id": "B",
          "text": "A supervised multi-class classification model trained on past resumes and their assigned hiring band labels."
        },
        {
          "id": "C",
          "text": "A supervised univariate linear regression model predicting applicant age."
        },
        {
          "id": "D",
          "text": "Refusing machine learning because categorical labels cannot be represented mathematically."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Because the groups are well-defined, predetermined corporate bands and historical labeled instances exist, this is a supervised multi-class classification problem. Unsupervised clustering invents arbitrary geometric clusters that rarely align with predetermined corporate rubrics.",
      "difficulty": "easy",
      "subtopic": "Supervised vs Unsupervised"
    },
    {
      "id": "cml01-q09",
      "type": "single_choice",
      "question": "When a logistic regression classifier outputs p(y = 1 | x) = 0.82, does this turn the problem into a regression task?",
      "options": [
        {
          "id": "A",
          "text": "Yes, because the output is a continuous real number between 0 and 1."
        },
        {
          "id": "B",
          "text": "No; class probabilities are intermediate confidence scores for discrete decision boundaries, not continuous target variables of the physical system."
        },
        {
          "id": "C",
          "text": "Yes, because mean squared error must now be used as the loss function."
        },
        {
          "id": "D",
          "text": "No, because probabilities can only take integer values in machine learning."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Estimating posterior class probabilities P(Y=k|X) is an intermediate statistical mechanism for optimal decision making under uncertainty. The underlying task remains discrete classification, evaluated with classification metrics (Log-loss, ROC-AUC, F1), not regression metrics like RMSE.",
      "difficulty": "medium",
      "subtopic": "Classification vs Regression"
    },
    {
      "id": "cml01-q10",
      "type": "single_choice",
      "question": "In the DSML Python ecosystem, which library is specifically optimized for vectorized N-dimensional array manipulations, linear algebra, and memory-contiguous broadcasting?",
      "options": [
        {
          "id": "A",
          "text": "Pandas"
        },
        {
          "id": "B",
          "text": "Matplotlib"
        },
        {
          "id": "C",
          "text": "NumPy"
        },
        {
          "id": "D",
          "text": "BeautifulSoup"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "NumPy provides the foundational C-implemented ndarray structure, vectorized broadcasting, and BLAS/LAPACK linear algebra bindings upon which Scikit-Learn and Pandas are built.",
      "difficulty": "easy",
      "subtopic": "DSML Exploratory Toolbox"
    },
    {
      "id": "cml01-q11",
      "type": "single_choice",
      "question": "Which of the following scenarios is an example of an ill-defined machine learning initiative?",
      "options": [
        {
          "id": "A",
          "text": "Predicting customer churn (yes/no) using 12 months of billing history, evaluated via holdout F1-score."
        },
        {
          "id": "B",
          "text": "'Applying AI to make our corporate supply chain more innovative and agile' without specifying data inputs, operational decisions, or quantifiable metrics."
        },
        {
          "id": "C",
          "text": "Estimating hospital length of stay (days) from triage vitals, measured by Mean Absolute Error on unseen admissions."
        },
        {
          "id": "D",
          "text": "Classifying chest X-rays into normal vs pneumonia using labeled radiologist scans, optimized for sensitivity at a fixed false-positive rate."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Without a concrete Task T, Experience E, and measurable Performance metric P (Mitchell's criteria), an initiative is merely vague executive aspiration rather than an actionable machine learning engineering problem.",
      "difficulty": "easy",
      "subtopic": "Mitchell's ETP Framework"
    },
    {
      "id": "cml01-q12",
      "type": "single_choice",
      "question": "Why is it dangerous to optimize a machine learning model exclusively for training set accuracy?",
      "options": [
        {
          "id": "A",
          "text": "Because training set accuracy cannot exceed 50% mathematically."
        },
        {
          "id": "B",
          "text": "Because a sufficiently complex model can simply memorize incidental training noise, yielding high training accuracy but disastrous generalization to unseen data (overfitting)."
        },
        {
          "id": "C",
          "text": "Because scikit-learn models crash if training accuracy reaches 100%."
        },
        {
          "id": "D",
          "text": "Because training accuracy only applies to unsupervised clustering problems."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The ultimate objective of machine learning is generalization to unseen test distributions. Memorizing idiosyncratic training noise (overfitting) produces deceptive training performance that collapses in production.",
      "difficulty": "easy",
      "subtopic": "Generalization & Evaluation"
    },
    {
      "id": "cml01-q13",
      "type": "single_choice",
      "question": "You are asked to plot the bivariate relationship between employee years of experience and annual compensation to verify whether a linear model is appropriate. Which visualization should you generate?",
      "options": [
        {
          "id": "A",
          "text": "Scatter Plot with experience on the x-axis and compensation on the y-axis"
        },
        {
          "id": "B",
          "text": "Pie Chart showing distribution of employee departments"
        },
        {
          "id": "C",
          "text": "Histogram of employee IDs"
        },
        {
          "id": "D",
          "text": "Heatmap of a single 1D array"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "A 2D Scatter Plot directly maps two continuous variables against perpendicular Cartesian axes, immediately revealing whether their relationship is linear, monotonic, curved, or homoscedastic.",
      "difficulty": "easy",
      "subtopic": "DSML Exploratory Toolbox"
    },
    {
      "id": "cml01-q14",
      "type": "single_choice",
      "question": "A financial hedge fund wants to predict the continuous stock price of a company 10 minutes into the future using order-book data. How is this learning problem categorized?",
      "options": [
        {
          "id": "A",
          "text": "Unsupervised Association Rule Mining"
        },
        {
          "id": "B",
          "text": "Supervised Time-Series Regression"
        },
        {
          "id": "C",
          "text": "Unsupervised Density Estimation"
        },
        {
          "id": "D",
          "text": "Semi-supervised Clustering"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Because historical prices serve as continuous ground-truth target values y in R, this is a supervised regression task operating across temporal sequences.",
      "difficulty": "easy",
      "subtopic": "Supervised Task Taxonomy"
    },
    {
      "id": "cml01-q15",
      "type": "single_choice",
      "question": "What is the key difference between Clustering and Classification?",
      "options": [
        {
          "id": "A",
          "text": "Clustering requires ground-truth labels; classification discovers clusters autonomously."
        },
        {
          "id": "B",
          "text": "Clustering is unsupervised and discovers groupings based on feature geometry; classification is supervised and predicts pre-assigned category labels."
        },
        {
          "id": "C",
          "text": "Clustering is only used for image data; classification is only used for tabular data."
        },
        {
          "id": "D",
          "text": "Clustering outputs continuous targets; classification outputs real-valued vectors."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Clustering invents and identifies clusters without predefined target names or human feedback. Classification maps data points to pre-existing, human-defined target categories using labeled historical training examples.",
      "difficulty": "easy",
      "subtopic": "Supervised vs Unsupervised"
    },
    {
      "id": "cml01-q16",
      "type": "multi_choice",
      "question": "Which of the following statements are TRUE regarding the characteristics of Classification algorithms? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Classification models map input feature vectors to discrete target categories."
        },
        {
          "id": "B",
          "text": "Classification algorithms can accept both discrete categorical features and continuous real-valued features as inputs."
        },
        {
          "id": "C",
          "text": "Classification algorithms can output calibrated class posterior probabilities P(y = c | x)."
        },
        {
          "id": "D",
          "text": "Classification is only possible if the input feature matrix X has fewer than 3 features."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Statements A, B, and C are correct: Classification targets are discrete; inputs can be discrete, continuous, or mixed; and modern classifiers compute class probabilities. D is false as classifiers routinely scale to thousands of features.",
      "difficulty": "medium",
      "subtopic": "Supervised Task Taxonomy"
    },
    {
      "id": "cml01-q17",
      "type": "multi_choice",
      "question": "Which of the following tasks represent Supervised Learning problems? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Predicting whether a credit card transaction is fraudulent based on 10,000 labeled past transactions."
        },
        {
          "id": "B",
          "text": "Grouping website visitors into unlabelled shopping personas based purely on clickstream session duration."
        },
        {
          "id": "C",
          "text": "Predicting house prices using historical transactions with known sales values."
        },
        {
          "id": "D",
          "text": "Forecasting tomorrow's peak electrical grid load in megawatts given historical weather and load logs."
        }
      ],
      "correctOptionIds": [
        "A",
        "C",
        "D"
      ],
      "explanation": "A, C, and D are supervised learning because they train on paired inputs and known ground-truth targets (binary fraud labels, continuous sale prices, and continuous megawatt loads). Option B is unsupervised customer segmentation (clustering).",
      "difficulty": "medium",
      "subtopic": "Supervised vs Unsupervised"
    },
    {
      "id": "cml01-q18",
      "type": "multi_choice",
      "question": "Under Tom Mitchell's framework (E, T, P), which of the following performance measures P are appropriate when task T is Supervised Continuous Regression? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Mean Absolute Error (MAE)"
        },
        {
          "id": "B",
          "text": "Root Mean Squared Error (RMSE)"
        },
        {
          "id": "C",
          "text": "Coefficient of Determination (R^2)"
        },
        {
          "id": "D",
          "text": "Confusion Matrix Accuracy"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "MAE, RMSE, and R^2 are standard continuous regression metrics. Accuracy is an evaluation metric exclusively designed for discrete classification.",
      "difficulty": "easy",
      "subtopic": "Mitchell's ETP Framework"
    },
    {
      "id": "cml01-q19",
      "type": "multi_choice",
      "question": "Which of the following conditions strongly suggest that a classical rule-based software approach should be favored over a complex Machine Learning model? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The business logic is strictly deterministic, fully understood, and easily encoded in clear if/else rules (e.g., calculating statutory sales tax)."
        },
        {
          "id": "B",
          "text": "Zero historical data or ground-truth examples exist from which an algorithm could learn."
        },
        {
          "id": "C",
          "text": "The problem requires identifying subtle visual cancer patterns across millions of noisy pixel arrays."
        },
        {
          "id": "D",
          "text": "The system requires 100% mathematical auditability and deterministic zero-tolerance execution dictated by legal statute."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Classical programming excels when domain rules are deterministic, stable, legally audited, and easily hand-coded, or when no training data exists. Visual pattern recognition across pixels (C) is a classic machine learning domain where handcrafted rules fail.",
      "difficulty": "medium",
      "subtopic": "ML vs Classical Programming"
    },
    {
      "id": "cml01-q20",
      "type": "multi_choice",
      "question": "In the standard DSML exploratory workflow, which pairs correctly match the analytical question to its most effective visualization tool? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Assessing the distribution and tail behavior of a single continuous feature -> Histogram / KDE plot"
        },
        {
          "id": "B",
          "text": "Comparing aggregate metric totals across discrete nominal categories -> Bar Plot"
        },
        {
          "id": "C",
          "text": "Inspecting the pairwise correlation and linear relationship between two numeric columns -> Scatter Plot"
        },
        {
          "id": "D",
          "text": "Tracking the temporal price drift of an asset over an ordered timestamp sequence -> Line Plot"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four are canonical exploratory data analysis (EDA) pairings: Histograms for distributions, Bar plots for categorical comparisons, Scatter plots for bivariate numeric relationships, and Line plots for chronologically ordered trends.",
      "difficulty": "easy",
      "subtopic": "DSML Exploratory Toolbox"
    }
  ]
}
