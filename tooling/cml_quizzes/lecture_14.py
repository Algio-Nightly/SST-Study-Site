QUIZ_L14 = {
  "topicId": "lecture-14",
  "lectureNumber": 14,
  "title": "Naive Bayes Classification: Generative Modeling & MAP Inference",
  "description": "20 questions covering Generative vs Discriminative models, Bayes' Theorem decomposition, the Naive Conditional Independence assumption, Maximum A Posteriori (MAP) decision rules, log-space transformations, Laplace/Lidstone smoothing, and Gaussian/Multinomial/Bernoulli Naive Bayes implementations.",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml-l14-q01",
      "type": "single_choice",
      "question": "What is the foundational theoretical distinction between Generative Classifiers (e.g., Naive Bayes) and Discriminative Classifiers (e.g., Logistic Regression)?",
      "options": [
        {
          "id": "A",
          "text": "Generative classifiers model the joint probability distribution $P(\\mathbf{X}, Y) = P(\\mathbf{X} \\mid Y) P(Y)$, whereas discriminative classifiers directly model the posterior class boundary $P(Y \\mid \\mathbf{X})$"
        },
        {
          "id": "B",
          "text": "Generative models can only be trained with gradient descent"
        },
        {
          "id": "C",
          "text": "Discriminative models cannot be used for multi-class classification"
        },
        {
          "id": "D",
          "text": "Generative models do not use probability theory"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Generative classifiers learn how the data is generated for each class ($P(\\mathbf{X} \\mid Y)$) and apply Bayes' Theorem. Discriminative classifiers focus solely on separating the classes by estimating $P(Y \\mid \\mathbf{X})$ directly.",
      "difficulty": "easy",
      "subtopic": "Generative vs Discriminative"
    },
    {
      "id": "cml-l14-q02",
      "type": "single_choice",
      "question": "In Bayes' Theorem $P(Y=k \\mid \\mathbf{X}=\\mathbf{x}) = \\frac{P(\\mathbf{X}=\\mathbf{x} \\mid Y=k) P(Y=k)}{P(\\mathbf{X}=\\mathbf{x})}$, what is the technical name for the term $P(\\mathbf{X}=\\mathbf{x} \\mid Y=k)$?",
      "options": [
        {
          "id": "A",
          "text": "Prior Probability"
        },
        {
          "id": "B",
          "text": "Class-Conditional Likelihood"
        },
        {
          "id": "C",
          "text": "Marginal Evidence"
        },
        {
          "id": "D",
          "text": "Posterior Probability"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "$P(\\mathbf{X} \\mid Y=k)$ is the Class-Conditional Likelihood. $P(Y=k)$ is the Prior, $P(\\mathbf{X})$ is the Evidence / Marginal probability, and $P(Y=k \\mid \\mathbf{X})$ is the Posterior.",
      "difficulty": "easy",
      "subtopic": "Bayes Theorem Decomposition"
    },
    {
      "id": "cml-l14-q03",
      "type": "single_choice",
      "question": "Why is the Marginal Evidence term $P(\\mathbf{X}=\\mathbf{x})$ routinely ignored when determining the predicted class $\\hat{y}$ under the MAP rule?",
      "options": [
        {
          "id": "A",
          "text": "Because $P(\\mathbf{X}=\\mathbf{x})$ is always zero"
        },
        {
          "id": "B",
          "text": "Because $P(\\mathbf{X}=\\mathbf{x})$ is strictly positive and constant across all candidate classes $k \\in \\{1, \\dots, K\\}$, thus having no effect on the $\\arg\\max$"
        },
        {
          "id": "C",
          "text": "Because it violates Laplace smoothing"
        },
        {
          "id": "D",
          "text": "Because it cannot be computed in polynomial time"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Since $P(\\mathbf{X}=\\mathbf{x}) = \\sum_j P(\\mathbf{X} \\mid Y=j) P(Y=j)$ is identical for all classes $k$ for a given input $\\mathbf{x}$, it acts solely as a normalizer and does not alter the relative ranking or the $\\arg\\max$.",
      "difficulty": "easy",
      "subtopic": "MAP Classification Rule"
    },
    {
      "id": "cml-l14-q04",
      "type": "single_choice",
      "question": "What is the core 'Naive' assumption in Naive Bayes classification?",
      "options": [
        {
          "id": "A",
          "text": "All features are completely uncorrelated in the unconditional sense"
        },
        {
          "id": "B",
          "text": "All features $X_1, X_2, \\dots, X_d$ are conditionally independent given the class label $Y$: $P(\\mathbf{X} \\mid Y=k) = \\prod_{j=1}^d P(X_j \\mid Y=k)$"
        },
        {
          "id": "C",
          "text": "All classes have equal prior probabilities $P(Y=k) = 1/K$"
        },
        {
          "id": "D",
          "text": "The data is linearly separable"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The defining assumption is conditional independence of features given the class: once the class $Y=k$ is known, knowledge of feature $X_i$ provides zero information about feature $X_j$.",
      "difficulty": "easy",
      "subtopic": "Conditional Independence Assumption"
    },
    {
      "id": "cml-l14-q05",
      "type": "single_choice",
      "question": "Without the conditional independence assumption, how many parameters are needed to represent a joint distribution of $d$ binary features for $K$ classes, and what does Naive Bayes reduce this to?",
      "options": [
        {
          "id": "A",
          "text": "From $\\mathcal{O}(K \\cdot 2^d)$ parameters down to linear $\\mathcal{O}(K \\cdot d)$ parameters"
        },
        {
          "id": "B",
          "text": "From $\\mathcal{O}(d)$ to $\\mathcal{O}(1)$"
        },
        {
          "id": "C",
          "text": "From $\\mathcal{O}(d^2)$ to $\\mathcal{O}(d)$"
        },
        {
          "id": "D",
          "text": "From $\\mathcal{O}(K^d)$ to $\\mathcal{O}(K)$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "A full joint table of $d$ binary features per class requires $2^d - 1$ probabilities per class, scaling exponentially as $\\mathcal{O}(K \\cdot 2^d)$. Naive conditional independence requires only $d$ independent probabilities per class: $\\mathcal{O}(K \\cdot d)$.",
      "difficulty": "medium",
      "subtopic": "Parameter Complexity Reduction"
    },
    {
      "id": "cml-l14-q06",
      "type": "single_choice",
      "question": "Why is the Log-Space Transformation $\\ln P(Y=k) + \\sum_{j=1}^d \\ln P(x_j \\mid Y=k)$ mandatory when implementing Naive Bayes in production code?",
      "options": [
        {
          "id": "A",
          "text": "Because probabilities are non-linear"
        },
        {
          "id": "B",
          "text": "To prevent catastrophic floating-point numerical underflow caused by multiplying hundreds of tiny probabilities $p \\in (0, 1)$"
        },
        {
          "id": "C",
          "text": "Because logarithms convert classification into linear regression"
        },
        {
          "id": "D",
          "text": "To eliminate the need for priors"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Multiplying many probabilities (e.g. $10^{-3} \\times 10^{-4} \\times \\dots$) quickly exceeds IEEE-754 double precision limits, underflowing to `0.0`. Working in log space replaces products with stable sums.",
      "difficulty": "easy",
      "subtopic": "Log-Space Transformation"
    },
    {
      "id": "cml-l14-q07",
      "type": "single_choice",
      "question": "What is the 'Zero Probability Problem' in Naive Bayes, and what is its catastrophic consequence during classification?",
      "options": [
        {
          "id": "A",
          "text": "If a feature value never appeared in class $k$ in the training data, $P(x_j \\mid Y=k) = 0$, which multiplies through the entire product and forces the posterior probability for class $k$ to strictly 0, regardless of all other evidence"
        },
        {
          "id": "B",
          "text": "The prior probability is zero for balanced datasets"
        },
        {
          "id": "C",
          "text": "Gradient descent terminates on zero variance"
        },
        {
          "id": "D",
          "text": "The evidence term diverges to infinity"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Because likelihoods are multiplied, a single zero probability $P(x_j \\mid k) = 0$ acts as a veto, wiping out all positive evidence from thousands of other matching features.",
      "difficulty": "medium",
      "subtopic": "Zero Probability Problem"
    },
    {
      "id": "cml-l14-q08",
      "type": "single_choice",
      "question": "Under Additive Laplace Smoothing (add-1 smoothing) for a vocabulary of size $V$, what is the estimated word probability $P(w \\mid c)$ given word count $N_{wc}$ and total tokens $N_c$ in class $c$?",
      "options": [
        {
          "id": "A",
          "text": "$\\frac{N_{wc} + 1}{N_c + V}$"
        },
        {
          "id": "B",
          "text": "$\\frac{N_{wc} + 1}{N_c + 1}$"
        },
        {
          "id": "C",
          "text": "$\\frac{N_{wc}}{N_c + V}$"
        },
        {
          "id": "D",
          "text": "$\\frac{N_{wc} + V}{N_c}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Laplace smoothing adds a pseudocount of $\\alpha = 1$ to each word, adding $1 \\times V$ to the denominator: $\\hat{P}(w \\mid c) = \\frac{N_{wc} + 1}{N_c + V}$, ensuring all probabilities are strictly positive and sum to 1.",
      "difficulty": "medium",
      "subtopic": "Laplace Smoothing"
    },
    {
      "id": "cml-l14-q09",
      "type": "single_choice",
      "question": "In Gaussian Naive Bayes, how is the continuous feature likelihood $P(x_j \\mid Y=k)$ modeled?",
      "options": [
        {
          "id": "A",
          "text": "Using an unconstrained multi-variate Gaussian with full covariance matrix $\\mathbf{\\Sigma}_k$"
        },
        {
          "id": "B",
          "text": "Using a one-dimensional univariate Gaussian probability density: $P(x_j \\mid Y=k) = \\frac{1}{\\sqrt{2\\pi \\sigma_{jk}^2}} \\exp\\left(-\\frac{(x_j - \\mu_{jk})^2}{2\\sigma_{jk}^2}\\right)$"
        },
        {
          "id": "C",
          "text": "Using uniform histograms with equal bin widths"
        },
        {
          "id": "D",
          "text": "Using exponential decay kernels centered at zero"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Gaussian NB models each feature independently as a 1D normal distribution $\\mathcal{N}(\\mu_{jk}, \\sigma_{jk}^2)$ conditioned on class $k$. This corresponds to a multivariate Gaussian with a diagonal covariance matrix.",
      "difficulty": "medium",
      "subtopic": "Gaussian Naive Bayes"
    },
    {
      "id": "cml-l14-q10",
      "type": "single_choice",
      "question": "When is Multinomial Naive Bayes the industry-standard choice compared to Bernoulli Naive Bayes?",
      "options": [
        {
          "id": "A",
          "text": "When features are continuous real numbers like temperature and pressure"
        },
        {
          "id": "B",
          "text": "When features represent discrete occurrence frequencies or word counts (e.g., Bag-of-Words / TF count vectors in NLP)"
        },
        {
          "id": "C",
          "text": "When features are strictly binary 0/1 indicator flags"
        },
        {
          "id": "D",
          "text": "When the dataset has fewer than 10 samples"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Multinomial NB is designed for integer count vectors (e.g. word token frequencies in text). Bernoulli NB is designed for binary binary presence/absence flags (0 or 1).",
      "difficulty": "easy",
      "subtopic": "Multinomial vs Bernoulli NB"
    },
    {
      "id": "cml-l14-q11",
      "type": "single_choice",
      "question": "Why does Bernoulli Naive Bayes explicitly penalize the non-occurrence of words, unlike Multinomial Naive Bayes?",
      "options": [
        {
          "id": "A",
          "text": "Because its likelihood formulation includes both the presence probability $p_{jk}^{x_j}$ and the absence probability $(1 - p_{jk})^{1 - x_j}$"
        },
        {
          "id": "B",
          "text": "Because it divides by zero when $x_j = 0$"
        },
        {
          "id": "C",
          "text": "Because Bernoulli NB only operates on spam emails"
        },
        {
          "id": "D",
          "text": "Because it uses Gaussian density functions"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Bernoulli likelihood is $P(\\mathbf{x} \\mid k) = \\prod [p_{jk}^{x_j} (1 - p_{jk})^{1 - x_j}]$. When a word is absent ($x_j = 0$), it contributes the factor $(1 - p_{jk})$, actively taking the absence of evidence into account.",
      "difficulty": "hard",
      "subtopic": "Bernoulli Naive Bayes"
    },
    {
      "id": "cml-l14-q12",
      "type": "single_choice",
      "question": "What is the theoretical explanation for why Naive Bayes often achieves surprisingly competitive classification accuracy even when its conditional independence assumption is heavily violated?",
      "options": [
        {
          "id": "A",
          "text": "Accurate classification decisions require only that the correct class has the highest rank ($\\arg\\max$), not that the predicted probability distribution is well-calibrated"
        },
        {
          "id": "B",
          "text": "Because violations of independence cancel out automatically via the Central Limit Theorem"
        },
        {
          "id": "C",
          "text": "Because Naive Bayes internally switches to an SVM when features are correlated"
        },
        {
          "id": "D",
          "text": "Because correlation between features has zero impact on joint probability"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "As proven by Domingos & Pazzani (1997), classification requires only ordinal calibration: $\\arg\\max_k P(Y=k \\mid \\mathbf{X})$. Even if correlated features push posterior probabilities to extreme overconfident values (0.9999 or 0.0001), the correct class usually remains on top.",
      "difficulty": "hard",
      "subtopic": "Independence Paradox"
    },
    {
      "id": "cml-l14-q13",
      "type": "multi_choice",
      "question": "Which of the following statements regarding the behavior of Naive Bayes probability estimates are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Naive Bayes probability estimates are notoriously uncalibrated, tending to be pushed extremely close to 0.0 or 1.0 due to redundant correlated features."
        },
        {
          "id": "B",
          "text": "Naive Bayes probabilities should not be taken as literal confidence estimates without post-hoc calibration (e.g. Isotonic Regression or Platt Scaling)."
        },
        {
          "id": "C",
          "text": "Naive Bayes probabilities are mathematically guaranteed to be perfectly calibrated under any feature distribution."
        },
        {
          "id": "D",
          "text": "The zero probability problem causes un-smoothed Naive Bayes to output exact 0.0 probabilities."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Because independence is violated, multiplying redundant likelihoods compounds confidence, pushing probabilities to 0 and 1. They are uncalibrated and require post-processing if accurate confidence scores are needed.",
      "difficulty": "medium",
      "subtopic": "Probability Calibration"
    },
    {
      "id": "cml-l14-q14",
      "type": "multi_choice",
      "question": "What happens if a continuous feature in Gaussian Naive Bayes has zero variance ($\\sigma_{jk}^2 = 0$) within a specific class? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Division by zero occurs in the Gaussian exponent $\\frac{1}{2\\sigma_{jk}^2}$."
        },
        {
          "id": "B",
          "text": "The normalizer $\\frac{1}{\\sqrt{2\\pi \\sigma_{jk}^2}}$ evaluates to division by zero."
        },
        {
          "id": "C",
          "text": "Scikit-Learn's `GaussianNB` adds an epsilon variance smoothing constant (`var_smoothing = 1e-9` times max variance) to the denominator to prevent division by zero."
        },
        {
          "id": "D",
          "text": "The model automatically converts into a Bernoulli Naive Bayes classifier."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Zero variance produces catastrophic division by zero in both the exponential and normalizer. Production packages apply variance smoothing (`var_smoothing`) to add a small fraction of the largest feature variance.",
      "difficulty": "medium",
      "subtopic": "Gaussian NB Numerical Stability"
    },
    {
      "id": "cml-l14-q15",
      "type": "multi_choice",
      "question": "Which of the following are major advantages of Naive Bayes compared to deep neural networks and Support Vector Machines? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Extremely fast training in $\\mathcal{O}(n \\cdot d)$ time requiring only a single pass through the dataset to accumulate count and summary statistics."
        },
        {
          "id": "B",
          "text": "High resilience to irrelevant features (features with identical distributions across all classes contribute equal factors to all classes, cancelling out)."
        },
        {
          "id": "C",
          "text": "Naturally supports incremental / online learning via `partial_fit` since updating counts does not require retraining from scratch."
        },
        {
          "id": "D",
          "text": "Capable of learning non-linear feature interactions without manual feature engineering."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are major strengths of Naive Bayes. D is false: Naive Bayes fundamentally assumes features do not interact conditionally, so it cannot learn feature interactions.",
      "difficulty": "easy",
      "subtopic": "Advantages of Naive Bayes"
    },
    {
      "id": "cml-l14-q16",
      "type": "single_choice",
      "question": "In Lidstone Smoothing, what parameter value $\\alpha$ is typically used relative to Laplace Smoothing?",
      "options": [
        {
          "id": "A",
          "text": "$\\alpha > 10$"
        },
        {
          "id": "B",
          "text": "$0 < \\alpha < 1$ (e.g. $\\alpha = 0.1$ or $0.5$)"
        },
        {
          "id": "C",
          "text": "$\\alpha = 0$"
        },
        {
          "id": "D",
          "text": "$\\alpha = -1$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Laplace smoothing uses $\\alpha = 1$. Lidstone smoothing generalizes this to fractional pseudocounts $0 < \\alpha < 1$, preventing over-smoothing when the vocabulary $V$ is very large.",
      "difficulty": "easy",
      "subtopic": "Lidstone Smoothing"
    },
    {
      "id": "cml-l14-q17",
      "type": "multi_choice",
      "question": "Which real-world domains and problem types are classic strong use cases for Naive Bayes? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Email spam classification and sentiment analysis with Bag-of-Words text representations"
        },
        {
          "id": "B",
          "text": "Real-time streaming classification where inference latency must be under a millisecond"
        },
        {
          "id": "C",
          "text": "High-dimensional sparse text categorization with large vocabulary sizes"
        },
        {
          "id": "D",
          "text": "Self-driving car computer vision tracking bounding boxes across video frames"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Text classification, spam detection, and ultra-fast real-time inference are the marquee applications of Naive Bayes. Vision tracking (D) involves complex spatial and temporal correlations requiring deep CNNs/Transformers.",
      "difficulty": "easy",
      "subtopic": "Applications"
    },
    {
      "id": "cml-l14-q18",
      "type": "single_choice",
      "question": "How does Naive Bayes naturally handle missing feature values during test-time inference?",
      "options": [
        {
          "id": "A",
          "text": "It simply omits the missing feature $x_j$ from the likelihood product $\\prod_{i \\ne j} P(x_i \\mid Y=k)$, effectively marginalizing over all possible values of $x_j$"
        },
        {
          "id": "B",
          "text": "It sets the posterior probability of all classes to zero"
        },
        {
          "id": "C",
          "text": "It imputes missing values using $K$-Nearest Neighbours"
        },
        {
          "id": "D",
          "text": "It throws an unhandled exception because likelihoods require full vectors"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Because features are conditionally independent, marginalizing out a missing attribute $X_j$ corresponds to omitting $\\ln P(x_j \\mid Y=k)$ from the sum, computing the optimal decision based strictly on observed features.",
      "difficulty": "hard",
      "subtopic": "Missing Data Handling"
    },
    {
      "id": "cml-l14-q19",
      "type": "single_choice",
      "question": "What is the relationship between Gaussian Naive Bayes and Logistic Regression for binary classification when all features share the same variance across both classes?",
      "options": [
        {
          "id": "A",
          "text": "Gaussian Naive Bayes implies a posterior distribution $P(Y=1 \\mid \\mathbf{X})$ that has the EXACT parametric functional form of a Logistic Sigmoid $\\sigma(\\mathbf{w}^T \\mathbf{x} + b)$"
        },
        {
          "id": "B",
          "text": "They have opposite decision boundaries"
        },
        {
          "id": "C",
          "text": "Gaussian Naive Bayes produces a quadratic decision boundary while Logistic Regression is linear"
        },
        {
          "id": "D",
          "text": "There is no mathematical connection between them"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "As shown in Mitchell's generative-discriminative pair analysis, if features in both classes share equal variance, the log-odds ratio $\\ln\\frac{P(Y=1|X)}{P(Y=0|X)}$ is strictly linear in $\\mathbf{x}$, yielding the exact logistic sigmoid form $P(Y=1|X) = \\frac{1}{1 + e^{-(\\mathbf{w}^T \\mathbf{x} + b)}}$.",
      "difficulty": "hard",
      "subtopic": "Generative-Discriminative Pairs"
    },
    {
      "id": "cml-l14-q20",
      "type": "multi_choice",
      "question": "Which steps are executed during the training (`fit`) phase of a Gaussian Naive Bayes classifier? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Compute class prior probabilities $\\hat{P}(Y=k) = \\frac{N_k}{N}$."
        },
        {
          "id": "B",
          "text": "For each feature $j$ and class $k$, compute the sample mean $\\mu_{jk} = \\frac{1}{N_k} \\sum_{i \\in C_k} x_{ij}$."
        },
        {
          "id": "C",
          "text": "For each feature $j$ and class $k$, compute the sample variance $\\sigma_{jk}^2 = \\frac{1}{N_k} \\sum_{i \\in C_k} (x_{ij} - \\mu_{jk})^2$."
        },
        {
          "id": "D",
          "text": "Run 100 epochs of stochastic gradient descent to optimize cross-entropy loss."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Gaussian NB has a closed-form analytic maximum likelihood solution: calculating priors, means, and variances in a single closed-form pass. No gradient descent optimization is used.",
      "difficulty": "easy",
      "subtopic": "Gaussian NB Implementation"
    }
  ]
}
