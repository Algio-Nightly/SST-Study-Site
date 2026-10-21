QUIZ_L13 = {
  "topicId": "lecture-13",
  "lectureNumber": 13,
  "title": "Support Vector Machines: Maximum Margin, Duality & Kernels",
  "description": "20 questions covering Maximum Margin Hyperplanes, geometric vs functional margins, Hard vs Soft margin QP, slack variables, KKT conditions, Wolfe Dual formulation, the Kernel Trick (Mercer's Theorem, RBF gamma), and Support Vector Regression (SVR).",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml-l13-q01",
      "type": "single_choice",
      "question": "What is the primary optimization philosophy that distinguishes Support Vector Machines from Logistic Regression and Perceptrons?",
      "options": [
        {
          "id": "A",
          "text": "Empirical risk minimization via squared error loss"
        },
        {
          "id": "B",
          "text": "Structural risk minimization: Finding the unique separating hyperplane that maximizes the geometric margin to the nearest training samples"
        },
        {
          "id": "C",
          "text": "Maximum likelihood estimation of Gaussian class conditional densities"
        },
        {
          "id": "D",
          "text": "Recursive partitioning of space into axis-aligned hyper-rectangles"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "SVM implements Vapnik's Structural Risk Minimization, seeking the unique decision boundary that maximizes the geometric margin $\\gamma = \\frac{2}{\\|\\mathbf{w}\\|}$, providing theoretical upper bounds on test generalization error.",
      "difficulty": "easy",
      "subtopic": "Maximum Margin Principle"
    },
    {
      "id": "cml-l13-q02",
      "type": "single_choice",
      "question": "Given a separating hyperplane $\\mathbf{w}^T \\mathbf{x} + b = 0$ with normalized functional margin $\\min_i y_i(\\mathbf{w}^T \\mathbf{x}_i + b) = 1$, what is the total geometric width of the margin separating the two classes?",
      "options": [
        {
          "id": "A",
          "text": "$\\frac{1}{\\|\\mathbf{w}\\|}$"
        },
        {
          "id": "B",
          "text": "$\\frac{2}{\\|\\mathbf{w}\\|}$"
        },
        {
          "id": "C",
          "text": "$\\|\\mathbf{w}\\|^2$"
        },
        {
          "id": "D",
          "text": "$2\\|\\mathbf{w}\\|$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The distance from the hyperplane to the closest positive point is $\\frac{1}{\\|\\mathbf{w}\\|}$, and to the closest negative point is $\\frac{1}{\\|\\mathbf{w}\\|}$. The total geometric margin between the supporting planes is $\\frac{2}{\\|\\mathbf{w}\\|}$.",
      "difficulty": "easy",
      "subtopic": "Geometric Margin Math"
    },
    {
      "id": "cml-l13-q03",
      "type": "single_choice",
      "question": "Why is maximizing the geometric margin $\\frac{2}{\\|\\mathbf{w}\\|}$ equivalent to minimizing $\\frac{1}{2}\\|\\mathbf{w}\\|^2$?",
      "options": [
        {
          "id": "A",
          "text": "Maximizing $\\frac{2}{\\|\\mathbf{w}\\|}$ is equivalent to minimizing $\\|\\mathbf{w}\\|$, and squaring and multiplying by $\\frac{1}{2}$ creates a smooth, convex, quadratic objective with easy gradient computation"
        },
        {
          "id": "B",
          "text": "Because $\\|\\mathbf{w}\\|^2$ is always equal to 1"
        },
        {
          "id": "C",
          "text": "Because the margin is independent of $\\mathbf{w}$"
        },
        {
          "id": "D",
          "text": "Because linear regression uses squared loss"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Inverting the fraction converts maximization to minimization. The monotonic transformation $f(z) = \\frac{1}{2} z^2$ preserves the minimum location while yielding a strictly convex Quadratic Programming (QP) problem.",
      "difficulty": "easy",
      "subtopic": "Hard Margin QP Formulation"
    },
    {
      "id": "cml-l13-q04",
      "type": "single_choice",
      "question": "In the Soft-Margin SVM formulation, what role do the slack variables $\\xi_i$ play?",
      "options": [
        {
          "id": "A",
          "text": "They represent the learning rate during gradient descent"
        },
        {
          "id": "B",
          "text": "They quantify the linear distance by which an instance $\\mathbf{x}_i$ violates the canonical margin boundary ($y_i(\\mathbf{w}^T \\mathbf{x}_i + b) \\ge 1 - \\xi_i$ with $\\xi_i \\ge 0$)"
        },
        {
          "id": "C",
          "text": "They determine the number of support vectors"
        },
        {
          "id": "D",
          "text": "They scale the kernel bandwidth"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Slack variables allow points to fall inside the margin ($0 < \\xi_i \\le 1$) or be misclassified ($\\xi_i > 1$), enabling SVM to handle non-linearly separable or noisy real-world datasets.",
      "difficulty": "medium",
      "subtopic": "Soft Margin & Slack"
    },
    {
      "id": "cml-l13-q05",
      "type": "single_choice",
      "question": "What is the effect of setting a very large regularization penalty parameter $C \\to \\infty$ in Soft-Margin SVM?",
      "options": [
        {
          "id": "A",
          "text": "The model becomes highly tolerant of misclassifications, producing a wider margin with higher bias"
        },
        {
          "id": "B",
          "text": "The penalty for margin violations becomes immense, forcing slack variables $\\xi_i \\to 0$, degenerating to a strict Hard-Margin SVM with higher risk of overfitting"
        },
        {
          "id": "C",
          "text": "The model ignores all support vectors"
        },
        {
          "id": "D",
          "text": "The decision boundary becomes spherical"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The objective is $\\min \\frac{1}{2}\\|\\mathbf{w}\\|^2 + C \\sum \\xi_i$. High $C$ prioritizes minimizing misclassification penalty over margin width, forcing $\\xi_i \\to 0$ (narrow margin, low bias, high variance).",
      "difficulty": "medium",
      "subtopic": "C Parameter Tuning"
    },
    {
      "id": "cml-l13-q06",
      "type": "single_choice",
      "question": "According to the Karush-Kuhn-Tucker (KKT) complementary slackness conditions ($\\alpha_i [y_i(\\mathbf{w}^T \\mathbf{x}_i + b) - 1 + \\xi_i] = 0$), which training instances have dual Lagrange multiplier $\\alpha_i > 0$?",
      "options": [
        {
          "id": "A",
          "text": "All training instances in the dataset"
        },
        {
          "id": "B",
          "text": "Only the Support Vectors that lie exactly on the margin boundary or violate the margin"
        },
        {
          "id": "C",
          "text": "Only instances that are completely misclassified"
        },
        {
          "id": "D",
          "text": "Only instances located far away from the decision boundary"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "If a point is strictly outside the margin ($y_i(\\mathbf{w}^T \\mathbf{x}_i + b) > 1$ and $\\xi_i = 0$), KKT complementary slackness mandates $\\alpha_i = 0$. Only points on the margin or violating it have $\\alpha_i > 0$ (Support Vectors).",
      "difficulty": "hard",
      "subtopic": "KKT Conditions"
    },
    {
      "id": "cml-l13-q07",
      "type": "single_choice",
      "question": "In the Wolfe Dual formulation of SVM, how is the weight vector $\\mathbf{w}$ expressed in terms of the support vectors?",
      "options": [
        {
          "id": "A",
          "text": "$\\mathbf{w} = \\sum_{i=1}^n \\alpha_i y_i \\mathbf{x}_i$"
        },
        {
          "id": "B",
          "text": "$\\mathbf{w} = \\frac{1}{n} \\sum_{i=1}^n y_i \\mathbf{x}_i$"
        },
        {
          "id": "C",
          "text": "$\\mathbf{w} = \\sum_{i=1}^n \\frac{\\alpha_i}{\\mathbf{x}_i}$"
        },
        {
          "id": "D",
          "text": "$\\mathbf{w} = \\mathbf{X}^T (\\mathbf{X} \\mathbf{X}^T)^{-1} \\mathbf{y}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Setting $\\nabla_{\\mathbf{w}} \\mathcal{L} = \\mathbf{w} - \\sum \\alpha_i y_i \\mathbf{x}_i = \\mathbf{0}$ yields $\\mathbf{w} = \\sum \\alpha_i y_i \\mathbf{x}_i$. The weight vector is a linear combination exclusively of the Support Vectors (where $\\alpha_i > 0$).",
      "difficulty": "medium",
      "subtopic": "Wolfe Dual Formulation"
    },
    {
      "id": "cml-l13-q08",
      "type": "single_choice",
      "question": "What is the crucial insight of the Wolfe Dual that enables the 'Kernel Trick'?",
      "options": [
        {
          "id": "A",
          "text": "The dual objective function and prediction decision rule depend exclusively on dot products between feature vectors $\\langle \\mathbf{x}_i, \\mathbf{x}_j \\rangle$, never on individual feature coordinates directly"
        },
        {
          "id": "B",
          "text": "The dual objective eliminates the need to compute dot products entirely"
        },
        {
          "id": "C",
          "text": "The dual transforms the problem from quadratic to linear programming"
        },
        {
          "id": "D",
          "text": "The dual ensures that all eigenvalues are negative"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The dual objective is $\\max_\\alpha \\sum \\alpha_i - \\frac{1}{2}\\sum \\sum \\alpha_i \\alpha_j y_i y_j (\\mathbf{x}_i \\cdot \\mathbf{x}_j)$. Because data enters solely via inner products, we can replace $(\\mathbf{x}_i \\cdot \\mathbf{x}_j)$ with a kernel function $K(\\mathbf{x}_i, \\mathbf{x}_j) = \\langle \\phi(\\mathbf{x}_i), \\phi(\\mathbf{x}_j) \\rangle$ without ever calculating the high-dimensional mapping $\\phi(\\mathbf{x})$.",
      "difficulty": "hard",
      "subtopic": "The Kernel Trick"
    },
    {
      "id": "cml-l13-q09",
      "type": "single_choice",
      "question": "What does Mercer's Theorem mathematically guarantee regarding a candidate kernel function $K(\\mathbf{x}, \\mathbf{z})$?",
      "options": [
        {
          "id": "A",
          "text": "It guarantees that the algorithm will converge in $\\mathcal{O}(n)$ time"
        },
        {
          "id": "B",
          "text": "If the kernel matrix $\\mathbf{K}_{ij} = K(\\mathbf{x}_i, \\mathbf{x}_j)$ is symmetric positive semi-definite (PSD), there exists an implicit mapping $\\phi$ into a Hilbert space such that $K(\\mathbf{x}, \\mathbf{z}) = \\langle \\phi(\\mathbf{x}), \\phi(\\mathbf{z}) \\rangle$"
        },
        {
          "id": "C",
          "text": "It proves that the feature space is strictly finite-dimensional"
        },
        {
          "id": "D",
          "text": "It guarantees 100% test accuracy on non-linear data"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Mercer's Theorem provides the necessary and sufficient condition: Any continuous, symmetric, positive semi-definite kernel function corresponds to an inner product in some transformed Hilbert space, ensuring the convex QP optimization remains well-posed.",
      "difficulty": "hard",
      "subtopic": "Mercer Theorem"
    },
    {
      "id": "cml-l13-q10",
      "type": "single_choice",
      "question": "What is the dimension of the implicit feature space $\\phi(\\mathbf{x})$ mapped by the Gaussian Radial Basis Function (RBF) kernel $K(\\mathbf{x}, \\mathbf{z}) = \\exp(-\\gamma \\|\\mathbf{x} - \\mathbf{z}\\|^2)$?",
      "options": [
        {
          "id": "A",
          "text": "$d^2$"
        },
        {
          "id": "B",
          "text": "Infinite $(\\infty)$"
        },
        {
          "id": "C",
          "text": "$2^d$"
        },
        {
          "id": "D",
          "text": "Equal to the sample size $n$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Using Taylor series expansion: $\\exp(z) = \\sum_{k=0}^\\infty \\frac{z^k}{k!}$. The RBF kernel implicitly projects data into an infinite-dimensional reproducing kernel Hilbert space (RKHS).",
      "difficulty": "medium",
      "subtopic": "RBF Kernel & Infinite Dimensions"
    },
    {
      "id": "cml-l13-q11",
      "type": "single_choice",
      "question": "What is the geometric and behavioral consequence of setting an excessively large $\\gamma$ (gamma) in an RBF kernel SVM?",
      "options": [
        {
          "id": "A",
          "text": "The Gaussian bell curves become broad and flat, causing high bias (underfitting)"
        },
        {
          "id": "B",
          "text": "The Gaussian bell curves become extremely narrow and localized spikes around individual training points, causing the model to overfit heavily"
        },
        {
          "id": "C",
          "text": "The decision boundary becomes purely linear"
        },
        {
          "id": "D",
          "text": "All support vectors are eliminated"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Since $\\gamma = \\frac{1}{2\\sigma^2}$, high $\\gamma$ means tiny variance $\\sigma^2$. The kernel drops to zero outside tiny neighborhoods around training points, creating isolated decision islands around individual support vectors (severe overfitting).",
      "difficulty": "medium",
      "subtopic": "Gamma Parameter Tuning"
    },
    {
      "id": "cml-l13-q12",
      "type": "single_choice",
      "question": "In Support Vector Regression (SVR), what is the function of the $\\epsilon$-insensitive tube ($|y - f(\\mathbf{x})| \\le \\epsilon$)?",
      "options": [
        {
          "id": "A",
          "text": "Any training prediction error smaller than $\\epsilon$ incurs zero loss penalty, creating a sparse dual solution where only points outside the tube become support vectors"
        },
        {
          "id": "B",
          "text": "It forces all target values to be between $-\\epsilon$ and $+\\epsilon$"
        },
        {
          "id": "C",
          "text": "It discards outliers larger than $\\epsilon$"
        },
        {
          "id": "D",
          "text": "It sets the maximum number of support vectors to $\\epsilon$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Vapnik's $\\epsilon$-insensitive loss is $\\mathcal{L}_\\epsilon(y, f) = \\max(0, |y - f| - \\epsilon)$. Errors within the tube are ignored, producing sparse models where points inside have $\\alpha_i = \\alpha_i^* = 0$.",
      "difficulty": "medium",
      "subtopic": "Support Vector Regression"
    },
    {
      "id": "cml-l13-q13",
      "type": "multi_choice",
      "question": "Why is feature scaling (e.g. `StandardScaler`) absolutely MANDATORY before training an SVM? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The margin $\\frac{2}{\\|\\mathbf{w}\\|}$ is geometric and relies on Euclidean distances across all feature dimensions."
        },
        {
          "id": "B",
          "text": "A feature with a huge numerical range (e.g., $10^6$) will completely dominate the dot product $\\mathbf{x}_i^T \\mathbf{x}_j$ and RBF kernel distance $\\|\\mathbf{x}_i - \\mathbf{x}_j\\|^2$."
        },
        {
          "id": "C",
          "text": "Features with small ranges (e.g., $[0, 1]$) would be effectively ignored by the quadratic optimizer."
        },
        {
          "id": "D",
          "text": "SVMs cannot compute predictions if features have negative values."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "SVMs compute isotropic Euclidean distances and dot products. Without standardization, large-scale features dominate the norm and margin, rendering smaller-scale features inert. Negative values are completely valid.",
      "difficulty": "easy",
      "subtopic": "Feature Scaling in SVM"
    },
    {
      "id": "cml-l13-q14",
      "type": "multi_choice",
      "question": "Which of the following statements regarding Support Vectors are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Removing non-support vector training points from the dataset changes neither the optimal hyperplane $\\mathbf{w}^*$ nor the bias $b^*$."
        },
        {
          "id": "B",
          "text": "The decision function depends ONLY on the support vectors: $f(\\mathbf{x}) = \\text{sign}\\left(\\sum_{i \\in SV} \\alpha_i y_i K(\\mathbf{x}_i, \\mathbf{x}) + b\\right)$."
        },
        {
          "id": "C",
          "text": "In a dataset of 1,000,000 points, if only 50 become support vectors, test inference scales with the 50 support vectors rather than 1,000,000 points."
        },
        {
          "id": "D",
          "text": "Every training point in a linearly separable dataset is guaranteed to be a support vector."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C capture the fundamental sparsity property of SVMs. D is false: only points on the margin boundaries become support vectors; all interior points have $\\alpha_i = 0$.",
      "difficulty": "medium",
      "subtopic": "Properties of Support Vectors"
    },
    {
      "id": "cml-l13-q15",
      "type": "multi_choice",
      "question": "Which of the following kernel functions satisfy Mercer's condition and are commonly used in machine learning? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Linear Kernel: $K(\\mathbf{x}, \\mathbf{z}) = \\mathbf{x}^T \\mathbf{z}$"
        },
        {
          "id": "B",
          "text": "Polynomial Kernel: $K(\\mathbf{x}, \\mathbf{z}) = (\\gamma \\mathbf{x}^T \\mathbf{z} + r)^d$"
        },
        {
          "id": "C",
          "text": "Gaussian RBF Kernel: $K(\\mathbf{x}, \\mathbf{z}) = \\exp(-\\gamma \\|\\mathbf{x} - \\mathbf{z}\\|^2)$"
        },
        {
          "id": "D",
          "text": "Random Kernel: $K(\\mathbf{x}, \\mathbf{z}) = \\text{uniform}(-1, 1)$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "Linear, Polynomial, and RBF (Gaussian) kernels are proven Mercer positive semi-definite kernels. A random function is not PSD and violates Mercer's theorem.",
      "difficulty": "easy",
      "subtopic": "Mercer Kernels"
    },
    {
      "id": "cml-l13-q16",
      "type": "single_choice",
      "question": "What is the primary computational bottleneck when training a non-linear Kernel SVM on very large datasets ($n > 100,000$)?",
      "options": [
        {
          "id": "A",
          "text": "Linear regression underfitting"
        },
        {
          "id": "B",
          "text": "The kernel Gram matrix $\\mathbf{K} \\in \\mathbb{R}^{n \\times n}$ requires $\\mathcal{O}(n^2)$ memory and standard QP solvers scale between $\\mathcal{O}(n^2)$ and $\\mathcal{O}(n^3)$ in time"
        },
        {
          "id": "C",
          "text": "Decision trees splitting too fast"
        },
        {
          "id": "D",
          "text": "Inability to run on CPUs"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Because kernel methods compute pairwise evaluations between all training samples, memory scales as $\\mathcal{O}(n^2)$ and training time scales as $\\mathcal{O}(n^2)$ to $\\mathcal{O}(n^3)$, making kernel SVMs prohibitive for huge datasets without approximations (like Nyström or Random Fourier Features).",
      "difficulty": "medium",
      "subtopic": "Computational Scalability"
    },
    {
      "id": "cml-l13-q17",
      "type": "multi_choice",
      "question": "How can multi-class classification ($K > 2$ classes) be handled using binary Support Vector Machines? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "One-vs-Rest (OvR / One-vs-All): Train $K$ distinct binary classifiers, each separating class $k$ from all other classes."
        },
        {
          "id": "B",
          "text": "One-vs-One (OvO): Train $\\frac{K(K-1)}{2}$ binary classifiers for every pair of classes, using majority voting for final prediction (Scikit-Learn `SVC` default)."
        },
        {
          "id": "C",
          "text": "Negative Feedback Loop: Randomly permuting binary labels."
        },
        {
          "id": "D",
          "text": "Crammer-Singer Multiclass Formulation: Solving a single combined optimization problem with multi-class margin constraints."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "OvR, OvO, and Crammer-Singer are the standard multi-class formulations for SVMs. Scikit-learn's `SVC` (based on LIBSVM) utilizes One-vs-One.",
      "difficulty": "hard",
      "subtopic": "Multiclass SVM"
    },
    {
      "id": "cml-l13-q18",
      "type": "single_choice",
      "question": "In Soft-Margin SVM, what is the loss function implicitly minimized when written in unconstrained regularized risk form?",
      "options": [
        {
          "id": "A",
          "text": "Hinge Loss: $\\mathcal{L}(y, f) = \\max(0, 1 - y f(\\mathbf{x}))$"
        },
        {
          "id": "B",
          "text": "Log-Loss / Cross-Entropy: $\\mathcal{L}(y, f) = \\ln(1 + e^{-y f})$"
        },
        {
          "id": "C",
          "text": "Mean Squared Error: $\\mathcal{L}(y, f) = (y - f)^2$"
        },
        {
          "id": "D",
          "text": "Exponential Loss: $\\mathcal{L}(y, f) = e^{-y f}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Soft margin SVM minimizes $\\frac{1}{2}\\|\\mathbf{w}\\|^2 + C \\sum \\max(0, 1 - y_i(\\mathbf{w}^T \\mathbf{x}_i + b))$. The penalty $\\max(0, 1 - y f)$ is precisely the Hinge Loss.",
      "difficulty": "medium",
      "subtopic": "Hinge Loss Equivalence"
    },
    {
      "id": "cml-l13-q19",
      "type": "multi_choice",
      "question": "When tuning an SVM with an RBF kernel, which parameter combinations are most likely to result in SEVERE OVERFITTING? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Extremely high $C$ (e.g., $10^5$) combined with extremely high $\\gamma$ (e.g., $100$)"
        },
        {
          "id": "B",
          "text": "Very small $C$ (e.g., $0.001$) combined with very small $\\gamma$ (e.g., $0.001$)"
        },
        {
          "id": "C",
          "text": "High $C$ punishing all slack violations coupled with localized high $\\gamma$ kernels"
        },
        {
          "id": "D",
          "text": "Linear kernel with $C = 0.01$"
        }
      ],
      "correctOptionIds": [
        "A",
        "C"
      ],
      "explanation": "High $C$ forbids margin violations and high $\\gamma$ creates tight localized Gaussian peaks around individual points. Together, they create complex overfitted boundaries around individual training points.",
      "difficulty": "medium",
      "subtopic": "Hyperparameter Interactions"
    },
    {
      "id": "cml-l13-q20",
      "type": "single_choice",
      "question": "How does Platt Scaling enable Scikit-Learn's `SVC(probability=True)` to output calibrated probability estimates $P(Y=1 \\mid \\mathbf{X})$?",
      "options": [
        {
          "id": "A",
          "text": "By calculating the softmax of raw distances"
        },
        {
          "id": "B",
          "text": "By fitting an additional 1D Logistic Regression model on the SVM decision function scores $f(\\mathbf{x})$ via internal 5-fold cross-validation"
        },
        {
          "id": "C",
          "text": "By multiplying the margins by the prior class probabilities"
        },
        {
          "id": "D",
          "text": "By converting the kernel into a Dirichlet distribution"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Platt Scaling fits a sigmoid $P(y=1 \\mid f) = \\frac{1}{1 + \\exp(A f(\\mathbf{x}) + B)}$ on the uncalibrated SVM margins $f(\\mathbf{x})$ using out-of-fold cross-validation.",
      "difficulty": "hard",
      "subtopic": "Platt Scaling Probabilities"
    }
  ]
}
