QUIZ_L02 = {
  "topicId": "lecture-02",
  "lectureNumber": 2,
  "title": "Data Preparation & Preprocessing Pipelines Quiz",
  "description": "25 questions covering train/test split hygiene, data leakage taxonomy, nominal vs ordinal encoding, numerical scalers, missing value imputation, and scikit-learn ColumnTransformer pipelines.",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml02-q01",
      "type": "single_choice",
      "question": "Which of the following describes the correct execution order when preparing data for a machine learning model?",
      "options": [
        {
          "id": "A",
          "text": "StandardScaler().fit(X) on all rows -> train_test_split() -> model.fit()"
        },
        {
          "id": "B",
          "text": "train_test_split() -> scaler.fit(X_train) -> scaler.transform(X_train) and scaler.transform(X_test)"
        },
        {
          "id": "C",
          "text": "scaler.fit(X_test) -> scaler.transform(X_train) to make training fair to test distribution"
        },
        {
          "id": "D",
          "text": "SimpleImputer().fit(X) on all rows -> StandardScaler().fit(X) -> train_test_split()"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Every data statistic (mean, std, median, category levels) MUST be computed strictly from the training partition X_train. The test set X_test represents unseen future data and must only be transformed using parameters learned from X_train. Fitting any preprocessor on the whole dataset X constitutes fit-on-all data leakage.",
      "difficulty": "easy",
      "subtopic": "Train-Test Split Hygiene"
    },
    {
      "id": "cml02-q02",
      "type": "single_choice",
      "question": "You have a categorical feature 'shirt_size' with domain values ['S', 'M', 'L', 'XL'] that possess a natural inherent ordering relevant to fabric consumption. What is the recommended encoding approach for a linear regression model?",
      "options": [
        {
          "id": "A",
          "text": "One-Hot Encoding only, treating sizes as completely unrelated independent vectors"
        },
        {
          "id": "B",
          "text": "Ordinal Encoding mapping {'S': 0, 'M': 1, 'L': 2, 'XL': 3} to preserve the mathematical ordering"
        },
        {
          "id": "C",
          "text": "Assigning random floats without any monotonic guarantee"
        },
        {
          "id": "D",
          "text": "Dropping the feature entirely to prevent dimensionality expansion"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Ordinal features have an intrinsic rank order (S < M < L < XL). Ordinal encoding maps them to ordered integers, allowing linear and parametric models to exploit the monotonic relationship with a single weight parameter. One-hot encoding destroys the order information.",
      "difficulty": "easy",
      "subtopic": "Categorical Encoding"
    },
    {
      "id": "cml02-q03",
      "type": "single_choice",
      "question": "Why is Median imputation generally preferred over Mean imputation when filling missing values in a right-skewed numerical column with extreme outliers (e.g., California household income)?",
      "options": [
        {
          "id": "A",
          "text": "The median is always numerically larger than the mean in right-skewed data."
        },
        {
          "id": "B",
          "text": "The median is robust to extreme outliers, whereas the mean is pulled heavily toward the tail, distorting typical values."
        },
        {
          "id": "C",
          "text": "Scikit-learn's SimpleImputer only supports median and rejects mean strategy."
        },
        {
          "id": "D",
          "text": "The median converts continuous features into discrete categorical bins automatically."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The mean minimizes squared errors and is sensitive to extreme values in the tail of skewed distributions. The median is the 50th percentile (L1 minimizer) and remains robust against outliers, preventing unrealistic synthetic imputation values.",
      "difficulty": "easy",
      "subtopic": "Missing Value Imputation"
    },
    {
      "id": "cml02-q04",
      "type": "single_choice",
      "question": "What is the primary operational consequence of Fit-on-All Preprocessing Leakage on model evaluation?",
      "options": [
        {
          "id": "A",
          "text": "The model will crash with a Python MemoryError during inference."
        },
        {
          "id": "B",
          "text": "The test evaluation metrics become overly optimistic and artificially inflated, masking true generalization degradation in production."
        },
        {
          "id": "C",
          "text": "The model's weights are mathematically forced to zero."
        },
        {
          "id": "D",
          "text": "The test set size increases by a factor of 2."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Preprocessing leakage incorporates information from the test distribution into the training pipeline. The model effectively 'peeks' at the test set, creating deceptively high test scores ('fake-good scores') that collapse when deployed on genuinely unseen live traffic.",
      "difficulty": "easy",
      "subtopic": "Data Leakage Taxonomy"
    },
    {
      "id": "cml02-q05",
      "type": "single_choice",
      "question": "In Scikit-Learn's OneHotEncoder, what is the purpose of setting handle_unknown='ignore'?",
      "options": [
        {
          "id": "A",
          "text": "It ignores all missing NaN values in numerical columns."
        },
        {
          "id": "B",
          "text": "If a brand new, unseen categorical level appears in the test data, it encodes that row as all zeros across one-hot columns rather than raising a ValueError."
        },
        {
          "id": "C",
          "text": "It automatically imputes the most frequent category into the unseen row."
        },
        {
          "id": "D",
          "text": "It silently drops the entire test instance from the dataframe."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In production, test or live query instances may present categories not present in the training set. Setting handle_unknown='ignore' outputs an all-zero vector for unknown categories, guaranteeing that the pipeline does not throw an exception.",
      "difficulty": "medium",
      "subtopic": "Categorical Encoding"
    },
    {
      "id": "cml02-q06",
      "type": "single_choice",
      "question": "Which of the following constitutes an example of Target Leakage?",
      "options": [
        {
          "id": "A",
          "text": "Standardizing house square footage using the training fold's sample mean and variance."
        },
        {
          "id": "B",
          "text": "Including an account status field 'account_closure_date' to predict whether a customer will churn in the next month."
        },
        {
          "id": "C",
          "text": "Imputing missing customer age with the training set median."
        },
        {
          "id": "D",
          "text": "One-hot encoding customer residency country using handle_unknown='ignore'."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Target leakage occurs when a feature contains information that would only exist or be known after the target variable has already occurred. If a customer has an account closure date, churn has already happened; using it produces trivial 100% accuracy during training but is completely unavailable for early churn prevention in reality.",
      "difficulty": "medium",
      "subtopic": "Data Leakage Taxonomy"
    },
    {
      "id": "cml02-q07",
      "type": "single_choice",
      "question": "What is the mathematical transformation applied by StandardScaler to each feature x_j?",
      "options": [
        {
          "id": "A",
          "text": "z = (x_j - x_{min}) / (x_{max} - x_{min})"
        },
        {
          "id": "B",
          "text": "z = (x_j - \\mu_j) / \\sigma_j, where \\mu_j is the sample mean and \\sigma_j is the sample standard deviation."
        },
        {
          "id": "C",
          "text": "z = \\log(x_j + 1)"
        },
        {
          "id": "D",
          "text": "z = (x_j - \\text{median}) / \\text{IQR}"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "StandardScaler computes the Z-score transformation: z = (x - \\mu) / \\sigma, resulting in a rescaled feature with mean = 0 and unit variance (std = 1). Option A is MinMaxScaler, C is Log1p, and D is RobustScaler.",
      "difficulty": "easy",
      "subtopic": "Feature Scaling"
    },
    {
      "id": "cml02-q08",
      "type": "single_choice",
      "question": "When working with financial datasets containing severe, extreme outliers in transaction amounts, which scaler provides the most robust centering and scaling?",
      "options": [
        {
          "id": "A",
          "text": "MinMaxScaler"
        },
        {
          "id": "B",
          "text": "StandardScaler"
        },
        {
          "id": "C",
          "text": "RobustScaler (using median and Interquartile Range IQR)"
        },
        {
          "id": "D",
          "text": "Normalizer (L2 unit vector projection)"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "StandardScaler relies on mean and std, both heavily distorted by extreme outliers. MinMaxScaler compresses non-outlier data into a tiny range [0, 0.001] if an extreme outlier exists. RobustScaler subtracts the median and divides by IQR (75th - 25th percentile), making it insensitive to extreme outliers.",
      "difficulty": "medium",
      "subtopic": "Feature Scaling"
    },
    {
      "id": "cml02-q09",
      "type": "single_choice",
      "question": "An engineer trains a linear model on 100,000 patient records. The feature 'cholesterol_level' has 2% missing values. Which missing value strategy is most appropriate?",
      "options": [
        {
          "id": "A",
          "text": "Deleting the 'cholesterol_level' feature column entirely from the dataset."
        },
        {
          "id": "B",
          "text": "Dropping the 2% rows or imputing missing entries with the training fold's median value."
        },
        {
          "id": "C",
          "text": "Filling missing entries with 999,999 to indicate missingness."
        },
        {
          "id": "D",
          "text": "Refitting the model only on the missing 2% rows."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "When missingness is low (~2%) and the feature is clinically predictive, dropping the entire column discards 98% of valuable information. Median imputation (or dropping the 2% rows) preserves the feature while maintaining data integrity.",
      "difficulty": "easy",
      "subtopic": "Missing Value Imputation"
    },
    {
      "id": "cml02-q10",
      "type": "single_choice",
      "question": "What is the primary architectural advantage of bundling preprocessing transforms into a Scikit-Learn Pipeline object?",
      "options": [
        {
          "id": "A",
          "text": "It automatically converts Python code into CUDA C++ binaries for GPU execution."
        },
        {
          "id": "B",
          "text": "It guarantees that fit() is only called on the training fold during cross-validation, automatically applying learned transforms to validation/test folds without leakage."
        },
        {
          "id": "C",
          "text": "It eliminates the mathematical need for train/test splits entirely."
        },
        {
          "id": "D",
          "text": "It guarantees 100% test accuracy on any dataset."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A Pipeline encapsulates transformers and estimators into a single object. When passed to cross_val_score or GridSearchCV, the pipeline re-fits transformers exclusively on the inner training folds and transforms the inner validation folds, mathematically eliminating preprocessing leakage.",
      "difficulty": "medium",
      "subtopic": "Pipelines & ColumnTransformer"
    },
    {
      "id": "cml02-q11",
      "type": "single_choice",
      "question": "Consider two data points: Point A with (Age = 25, Income = $50,000) and Point B with (Age = 55, Income = $50,200). What happens to Euclidean distance calculations if features are NOT scaled?",
      "options": [
        {
          "id": "A",
          "text": "Age will dominate the distance calculation because 55 is greater than 25."
        },
        {
          "id": "B",
          "text": "Income will completely dominate the distance calculation because the difference of $200 squared is 40,000, while age difference of 30 squared is only 900."
        },
        {
          "id": "C",
          "text": "Euclidean distance automatically standardizes features internally."
        },
        {
          "id": "D",
          "text": "The distance will be identically zero."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Unscaled Euclidean distance sums squared coordinate differences: \\sqrt{\\Delta \\text{Age}^2 + \\Delta \\text{Income}^2}. Features with large raw numerical scales (thousands of dollars) overwhelm features with small units (decades of age), rendering distance-based algorithms blind to smaller-scale variables.",
      "difficulty": "medium",
      "subtopic": "Feature Scaling"
    },
    {
      "id": "cml02-q12",
      "type": "single_choice",
      "question": "When is it mathematically and methodologically acceptable to perform a data cleaning operation BEFORE calling train_test_split()?",
      "options": [
        {
          "id": "A",
          "text": "When computing global column mean and standard deviation for normalization."
        },
        {
          "id": "B",
          "text": "When dropping corrupted rows where the ground-truth target label y is completely missing (label cleaning without statistical aggregation)."
        },
        {
          "id": "C",
          "text": "When applying target encoding based on label averages across categories."
        },
        {
          "id": "D",
          "text": "When fitting a K-Means clusterer to generate new feature IDs."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Dropping rows with corrupted or missing target labels is an example of domain hygiene that does not compute sample statistics or leak test distributions into training features. Any operation computing feature statistics (means, medians, scalers, target-encoders) must occur post-split.",
      "difficulty": "medium",
      "subtopic": "Train-Test Split Hygiene"
    },
    {
      "id": "cml02-q13",
      "type": "single_choice",
      "question": "What is the Dummy Variable Trap in linear regression, and how is it resolved?",
      "options": [
        {
          "id": "A",
          "text": "When one-hot encoding introduces perfect multicollinearity because the dummy columns sum to the constant intercept column; resolved by dropping one dummy column (drop='first')."
        },
        {
          "id": "B",
          "text": "When ordinal encoding is applied to nominal features; resolved by deleting the column."
        },
        {
          "id": "C",
          "text": "When missing values are encoded as -1; resolved by using mean imputation."
        },
        {
          "id": "D",
          "text": "When the learning rate is too small; resolved by multiplying by 10."
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "If a categorical feature has K levels, creating K one-hot binary columns introduces perfect collinearity because \\sum_{k=1}^K d_k = 1 = x_0 (the bias column). This makes the Gram matrix X^T X singular. It is solved by setting drop='first' in OneHotEncoder.",
      "difficulty": "medium",
      "subtopic": "Categorical Encoding"
    },
    {
      "id": "cml02-q14",
      "type": "single_choice",
      "question": "In Scikit-Learn, which composite meta-estimator is specifically designed to apply different preprocessing pipelines to distinct subsets of columns (e.g., scaling numerical columns while one-hot encoding categorical columns)?",
      "options": [
        {
          "id": "A",
          "text": "FeatureUnion"
        },
        {
          "id": "B",
          "text": "ColumnTransformer"
        },
        {
          "id": "C",
          "text": "GridSearchCV"
        },
        {
          "id": "D",
          "text": "VotingClassifier"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "sklearn.compose.ColumnTransformer allows distinct transformer pipelines to be applied to specified column lists (e.g. numeric pipeline to numeric columns, categorical pipeline to string columns) and concatenates their outputs horizontally.",
      "difficulty": "easy",
      "subtopic": "Pipelines & ColumnTransformer"
    },
    {
      "id": "cml02-q15",
      "type": "single_choice",
      "question": "You are building a loan default prediction model using temporal transaction records from 2018 to 2023. What type of train-test split should you perform?",
      "options": [
        {
          "id": "A",
          "text": "Uniform random 80-20 train_test_split() shuffling all records across all years."
        },
        {
          "id": "B",
          "text": "Time-based split: training on historical records (2018 to 2021) and testing on future records (2022 to 2023)."
        },
        {
          "id": "C",
          "text": "Stratified random split shuffling transactions without regard to date."
        },
        {
          "id": "D",
          "text": "K-Fold cross validation with random permutation shuffling."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "When data has a natural temporal dependency, random shuffling causes temporal lookahead leakage (predicting past events using future economic conditions). A time-based cutoff split strictly respects temporal causality.",
      "difficulty": "medium",
      "subtopic": "Train-Test Split Hygiene"
    },
    {
      "id": "cml02-q16",
      "type": "single_choice",
      "question": "Why is it invalid to fit a LabelEncoder to a nominal feature like 'Favorite_Color' ['Red', 'Green', 'Blue'] for a linear regression model?",
      "options": [
        {
          "id": "A",
          "text": "Because strings cannot be represented in Python."
        },
        {
          "id": "B",
          "text": "Because mapping Red=0, Green=1, Blue=2 invents false quantitative distances, implying that Blue is 'twice' Green and Green is equidistant between Red and Blue."
        },
        {
          "id": "C",
          "text": "Because LabelEncoder only works on target vectors y, never feature matrices X."
        },
        {
          "id": "D",
          "text": "Both B and C."
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "Both statements are correct: Mathematically, assigning arbitrary integers to unordered nominal categories creates fictitious linear geometry and distance metrics that distort parametric models. Methodologically, Scikit-Learn explicitly documents LabelEncoder for encoding 1D target labels y, not feature matrices X (OneHotEncoder should be used instead).",
      "difficulty": "medium",
      "subtopic": "Categorical Encoding"
    },
    {
      "id": "cml02-q17",
      "type": "single_choice",
      "question": "What is the role of MissingIndicator in advanced data preparation pipelines?",
      "options": [
        {
          "id": "A",
          "text": "It automatically deletes any column that has missing values."
        },
        {
          "id": "B",
          "text": "It appends binary boolean indicator columns marking whether an observation was originally missing before imputation, preserving missingness signal."
        },
        {
          "id": "C",
          "text": "It replaces missing values with random numbers between 0 and 1."
        },
        {
          "id": "D",
          "text": "It raises an exception whenever an NaN value is detected."
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Often, the fact that a value was missing is itself highly predictive (e.g., missing income on a credit application may signal unemployment). MissingIndicator adds a binary flag column (1 if missing, 0 otherwise) alongside imputed values.",
      "difficulty": "medium",
      "subtopic": "Missing Value Imputation"
    },
    {
      "id": "cml02-q18",
      "type": "single_choice",
      "question": "After fitting a StandardScaler on X_train, what method should be called on X_test?",
      "options": [
        {
          "id": "A",
          "text": "scaler.fit(X_test)"
        },
        {
          "id": "B",
          "text": "scaler.fit_transform(X_test)"
        },
        {
          "id": "C",
          "text": "scaler.transform(X_test)"
        },
        {
          "id": "D",
          "text": "scaler.inverse_transform(X_test)"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "Never call fit() or fit_transform() on test data. You must call scaler.transform(X_test) so the test data is normalized using the exact mean and variance computed from the training distribution.",
      "difficulty": "easy",
      "subtopic": "Feature Scaling"
    },
    {
      "id": "cml02-q19",
      "type": "multi_choice",
      "question": "Which of the following preprocessing transformations MUST be fitted strictly on training data only to prevent data leakage? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "StandardScaler (calculating mean \\mu and standard deviation \\sigma)"
        },
        {
          "id": "B",
          "text": "SimpleImputer (calculating median or mean replacement values)"
        },
        {
          "id": "C",
          "text": "OneHotEncoder (discovering the vocabulary of categorical levels)"
        },
        {
          "id": "D",
          "text": "VarianceThreshold or SelectKBest (calculating feature variances and correlations)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four compute sample statistics or structural dictionaries from data. If fitted on the entire dataset including test folds, test information leaks into model inputs, violating evaluation independence.",
      "difficulty": "medium",
      "subtopic": "Data Leakage Taxonomy"
    },
    {
      "id": "cml02-q20",
      "type": "multi_choice",
      "question": "Which of the following features represent Nominal categories where One-Hot Encoding is appropriate (rather than Ordinal encoding)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Neighborhood / District Name ('Downtown', 'Uptown', 'Suburbs')"
        },
        {
          "id": "B",
          "text": "Device Operating System ('iOS', 'Android', 'Windows')"
        },
        {
          "id": "C",
          "text": "Education Level ('High School', 'Bachelors', 'Masters', 'PhD')"
        },
        {
          "id": "D",
          "text": "Primary Credit Card Color ('Silver', 'Gold', 'Platinum') when benefits scale monotonically"
        }
      ],
      "correctOptionIds": [
        "A",
        "B"
      ],
      "explanation": "Neighborhood and Operating System have no natural mathematical ordering and are nominal (requiring One-Hot Encoding). Education Level has an explicit hierarchical progression, and Credit Card tiers reflect progressive credit limits, making them ordinal.",
      "difficulty": "easy",
      "subtopic": "Categorical Encoding"
    },
    {
      "id": "cml02-q21",
      "type": "multi_choice",
      "question": "Which of the following statements are TRUE regarding Feature Scaling in machine learning? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Gradient descent optimization converges significantly faster on feature-scaled datasets because spherical level sets prevent zig-zagging."
        },
        {
          "id": "B",
          "text": "Distance-based algorithms (such as KNN and SVM with RBF kernels) are highly sensitive to feature scaling."
        },
        {
          "id": "C",
          "text": "Decision Trees and Random Forests are completely invariant to monotonic numerical feature scaling."
        },
        {
          "id": "D",
          "text": "Feature scaling modifies the ground-truth target vector y and corrupts regression metrics."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Statements A, B, and C are true. Tree-based models split on single features at a time based on rank order, making them scale-invariant. Feature scaling is applied strictly to features X, never automatically modifying target y (D is false).",
      "difficulty": "medium",
      "subtopic": "Feature Scaling"
    },
    {
      "id": "cml02-q22",
      "type": "multi_choice",
      "question": "Which of the following scenarios are forms of Data Leakage in an ML pipeline? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Applying SMOTE oversampling on the entire dataset before splitting into train and test folds."
        },
        {
          "id": "B",
          "text": "Using feature selection (e.g. mutual information or ANOVA F-test) on the combined train + test dataset to pick the top 10 features."
        },
        {
          "id": "C",
          "text": "Standardizing features inside a cross-validation loop using an sklearn Pipeline."
        },
        {
          "id": "D",
          "text": "Predicting hospital readmissions using a discharge feature 'total_days_in_intensive_care' that is only recorded after discharge."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "A, B, and D are classic leakage failure modes: SMOTE on all rows creates synthetic samples informed by test distributions; feature selection on all rows selects features correlated with test targets; and D is target leakage. Option C is the correct, leakage-free practice.",
      "difficulty": "hard",
      "subtopic": "Data Leakage Taxonomy"
    },
    {
      "id": "cml02-q23",
      "type": "multi_choice",
      "question": "When configuring MinMaxScaler(feature_range=(0, 1)), what can happen if the test dataset contains values smaller than X_train.min() or larger than X_train.max()? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The transformed test values can fall outside the [0, 1] range (becoming negative or greater than 1.0)."
        },
        {
          "id": "B",
          "text": "MinMaxScaler raises a FatalException and halts execution."
        },
        {
          "id": "C",
          "text": "Setting clip=True forces transformed test values to be strictly bounded within [0, 1]."
        },
        {
          "id": "D",
          "text": "The scaler automatically recomputes min and max from the test set."
        }
      ],
      "correctOptionIds": [
        "A",
        "C"
      ],
      "explanation": "MinMaxScaler uses min and max from training: (x - min_train) / (max_train - min_train). If an unseen test point exceeds max_train, the output exceeds 1.0. Setting clip=True in scikit-learn clips the output to [0, 1]. It never raises an error or recomputes statistics automatically.",
      "difficulty": "hard",
      "subtopic": "Feature Scaling"
    },
    {
      "id": "cml02-q24",
      "type": "multi_choice",
      "question": "Which of the following strategies are mathematically valid approaches for handling missing data in tabular features? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Imputing with central tendency measures (Mean for symmetric data, Median for skewed data)."
        },
        {
          "id": "B",
          "text": "Using an iterative multivariate imputer (e.g., IterativeImputer / MICE) that models each missing feature as a function of other features."
        },
        {
          "id": "C",
          "text": "Replacing all missing values with arbitrary large constants like +999,999 in linear regression models."
        },
        {
          "id": "D",
          "text": "Dropping instances with missing values if missingness is completely at random (MCAR) and comprises a negligible fraction of data."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "A, B, and D are standard statistical strategies. C is hazardous: arbitrary huge numbers severely distort linear regression hyperplanes and gradient descent optimization.",
      "difficulty": "medium",
      "subtopic": "Missing Value Imputation"
    },
    {
      "id": "cml02-q25",
      "type": "multi_choice",
      "question": "Examine the following Scikit-Learn code snippet:\n```python\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.impute import SimpleImputer\nfrom sklearn.preprocessing import StandardScaler, OneHotEncoder\n\npreprocessor = ColumnTransformer([\n    ('num', Pipeline([\n        ('imputer', SimpleImputer(strategy='median')),\n        ('scaler', StandardScaler())\n    ]), ['age', 'income']),\n    ('cat', Pipeline([\n        ('imputer', SimpleImputer(strategy='most_frequent')),\n        ('encoder', OneHotEncoder(handle_unknown='ignore'))\n    ]), ['city', 'gender'])\n])\n```\nWhich of the following statements about this pipeline are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Numerical columns ['age', 'income'] are first imputed with median values and then standardized to zero mean and unit variance."
        },
        {
          "id": "B",
          "text": "Categorical columns ['city', 'gender'] are imputed with the most frequent category and then one-hot encoded."
        },
        {
          "id": "C",
          "text": "Calling preprocessor.fit(X_train) learns the medians, means, standard deviations, and category levels strictly from X_train."
        },
        {
          "id": "D",
          "text": "Calling preprocessor.transform(X_test) will recompute medians and means on X_test."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Statements A, B, and C are completely accurate descriptions of Scikit-Learn's ColumnTransformer architecture. D is false: transform() strictly applies the parameters previously learned by fit() and never recomputes statistics.",
      "difficulty": "medium",
      "subtopic": "Pipelines & ColumnTransformer"
    }
  ]
}
