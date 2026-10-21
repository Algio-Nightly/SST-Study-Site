QUIZ_L12 = {
  "topicId": "lecture-12",
  "lectureNumber": 12,
  "title": "Ensemble Learning: Bagging, Random Forests, AdaBoost & Gradient Boosting",
  "description": "20 questions covering Condorcet's Jury Theorem, Bootstrap Aggregation (Bagging), Out-Of-Bag (OOB) error estimation, Random Forest variance reduction, AdaBoost sample weight updates, Gradient Boosting optimization in function space, and XGBoost 2nd-order Taylor expansions.",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml-l12-q01",
      "type": "single_choice",
      "question": "According to Condorcet's Jury Theorem, what condition must hold for an ensemble of $B$ independent classifiers (voting by simple majority) to approach zero error probability as $B \\to \\infty$?",
      "options": [
        {
          "id": "A",
          "text": "Each individual classifier must have accuracy $p = 1.0$"
        },
        {
          "id": "B",
          "text": "Each individual classifier must perform strictly better than random guessing ($p > 0.5$) and make statistically independent errors"
        },
        {
          "id": "C",
          "text": "The classifiers must be trained on identical subsets of data"
        },
        {
          "id": "D",
          "text": "The number of features must exceed the number of samples"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Condorcet's Jury Theorem proves that if each voter has probability $p > 0.5$ of being correct and errors are independent, the collective majority probability approaches 1 as the ensemble size $B \\to \\infty$.",
      "difficulty": "easy",
      "subtopic": "Condorcet Jury Theorem"
    },
    {
      "id": "cml-l12-q02",
      "type": "single_choice",
      "question": "In standard Bootstrap Aggregation (Bagging) with a training set of size $n$, what is the asymptotic percentage of original training instances that appear in a single bootstrap sample drawn with replacement?",
      "options": [
        {
          "id": "A",
          "text": "50.0%"
        },
        {
          "id": "B",
          "text": "63.2% (approx $1 - 1/e$)"
        },
        {
          "id": "C",
          "text": "36.8% (approx $1/e$)"
        },
        {
          "id": "D",
          "text": "100.0%"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The probability that a specific point is NOT chosen in $n$ draws with replacement is $(1 - 1/n)^n \\to e^{-1} \\approx 0.368$. Hence, the probability of being selected at least once is $1 - e^{-1} \\approx 0.632$ (63.2%).",
      "difficulty": "medium",
      "subtopic": "Bootstrap Sampling & OOB"
    },
    {
      "id": "cml-l12-q03",
      "type": "single_choice",
      "question": "What is the primary benefit of the Out-Of-Bag (OOB) samples in Bagging and Random Forests?",
      "options": [
        {
          "id": "A",
          "text": "They provide an honest validation estimate of generalization error without requiring a separate validation split or $k$-fold cross-validation"
        },
        {
          "id": "B",
          "text": "They speed up the tree construction algorithm by skipping splits"
        },
        {
          "id": "C",
          "text": "They eliminate the need for pruning individual decision trees"
        },
        {
          "id": "D",
          "text": "They guarantee that trees are completely uncorrelated"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Because roughly 36.8% of training points are never seen by each base tree, each sample can be evaluated using only those trees for which it was out-of-bag, providing an unbiased validation metric 'for free'.",
      "difficulty": "easy",
      "subtopic": "OOB Evaluation"
    },
    {
      "id": "cml-l12-q04",
      "type": "single_choice",
      "question": "Consider an ensemble of $B$ trees, each with variance $\\sigma^2$ and pairwise correlation $\\rho$. What is the variance of the ensemble mean prediction?",
      "options": [
        {
          "id": "A",
          "text": "$\\rho \\sigma^2 + \\frac{1 - \\rho}{B} \\sigma^2$"
        },
        {
          "id": "B",
          "text": "$\\frac{\\sigma^2}{B}$"
        },
        {
          "id": "C",
          "text": "$\\rho \\cdot B \\cdot \\sigma^2$"
        },
        {
          "id": "D",
          "text": "$(1 - \\rho) \\sigma^2$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "By the variance formula for correlated variables: $\\text{Var}(\\frac{1}{B}\\sum T_b) = \\rho \\sigma^2 + \\frac{1-\\rho}{B}\\sigma^2$. As $B \\to \\infty$, the second term goes to 0, leaving an asymptotic lower bound of $\\rho \\sigma^2$.",
      "difficulty": "hard",
      "subtopic": "Variance Reduction Math"
    },
    {
      "id": "cml-l12-q05",
      "type": "single_choice",
      "question": "How does Random Forest fundamentally improve upon basic Bagged Decision Trees?",
      "options": [
        {
          "id": "A",
          "text": "By building deeper trees with larger leaf node minimums"
        },
        {
          "id": "B",
          "text": "By forcing trees to split only on a random subset of $m \\approx \\sqrt{p}$ features at each node, de-correlating the trees and reducing $\\rho$"
        },
        {
          "id": "C",
          "text": "By weighting trees inversely to their training errors"
        },
        {
          "id": "D",
          "text": "By training trees sequentially to correct past errors"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "If a few features are dominant, all bagged trees choose them at the root, remaining highly correlated. Random Forests sample $m = \\sqrt{p}$ features at each node split, de-correlating the trees (reducing $\\rho$), which lowers total ensemble variance $\\rho \\sigma^2$.",
      "difficulty": "medium",
      "subtopic": "Random Forest Mechanism"
    },
    {
      "id": "cml-l12-q06",
      "type": "single_choice",
      "question": "What is the fundamental theoretical difference between Bagging and Boosting?",
      "options": [
        {
          "id": "A",
          "text": "Bagging targets bias reduction using sequential weak learners; Boosting targets variance reduction using parallel strong learners"
        },
        {
          "id": "B",
          "text": "Bagging targets variance reduction by averaging independent high-variance models; Boosting targets bias reduction by sequentially fitting models to correct predecessor errors"
        },
        {
          "id": "C",
          "text": "Bagging is only for classification; Boosting is only for regression"
        },
        {
          "id": "D",
          "text": "Bagging uses neural networks, while Boosting uses linear regression"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Bagging trains high-capacity, low-bias models (deep trees) in parallel to reduce variance. Boosting trains low-capacity, high-bias models (stumps/shallow trees) sequentially to reduce bias.",
      "difficulty": "easy",
      "subtopic": "Bagging vs Boosting"
    },
    {
      "id": "cml-l12-q07",
      "type": "single_choice",
      "question": "In the AdaBoost algorithm, what learner weight $\\alpha_t$ is assigned to a weak hypothesis $h_t$ with weighted error rate $\\epsilon_t = 0.1$?",
      "options": [
        {
          "id": "A",
          "text": "$\\frac{1}{2} \\ln(9) \\approx 1.099$"
        },
        {
          "id": "B",
          "text": "$\\ln(0.1) \\approx -2.302$"
        },
        {
          "id": "C",
          "text": "$0.90$"
        },
        {
          "id": "D",
          "text": "$0.5$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "AdaBoost learner weight formula: $\\alpha_t = \\frac{1}{2} \\ln\\left(\\frac{1 - \\epsilon_t}{\\epsilon_t}\\right) = \\frac{1}{2} \\ln\\left(\\frac{0.9}{0.1}\\right) = \\frac{1}{2} \\ln(9) \\approx 1.0986$.",
      "difficulty": "medium",
      "subtopic": "AdaBoost Mathematics"
    },
    {
      "id": "cml-l12-q08",
      "type": "single_choice",
      "question": "How does AdaBoost update the sample distribution weights $w_i^{(t+1)}$ after training weak learner $h_t$ on binary targets $y_i \\in \\{-1, +1\\}$?",
      "options": [
        {
          "id": "A",
          "text": "$w_i^{(t+1)} = w_i^{(t)} \\cdot \\frac{\\exp(-\\alpha_t y_i h_t(\\mathbf{x}_i))}{Z_t}$"
        },
        {
          "id": "B",
          "text": "$w_i^{(t+1)} = w_i^{(t)} + \\alpha_t (y_i - h_t(\\mathbf{x}_i))$"
        },
        {
          "id": "C",
          "text": "$w_i^{(t+1)} = w_i^{(t)} \\cdot (1 - \\epsilon_t)$"
        },
        {
          "id": "D",
          "text": "$w_i^{(t+1)} = \\frac{1}{n}$ resetting weights to uniform"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "If $y_i = h_t(\\mathbf{x}_i)$ (correct), $y_i h_t = 1$, weight multiplied by $e^{-\\alpha_t} < 1$ (downweighted). If misclassified, $y_i h_t = -1$, weight multiplied by $e^{\\alpha_t} > 1$ (upweighted). $Z_t$ is the normalization factor.",
      "difficulty": "hard",
      "subtopic": "AdaBoost Mathematics"
    },
    {
      "id": "cml-l12-q09",
      "type": "single_choice",
      "question": "In Gradient Boosting Machine (GBM) for arbitrary differentiable loss $\\mathcal{L}(y, f(\\mathbf{x}))$, what target value does each subsequent tree $h_m(\\mathbf{x})$ fit against?",
      "options": [
        {
          "id": "A",
          "text": "The ground truth label $y_i$"
        },
        {
          "id": "B",
          "text": "The negative gradient of the loss function evaluated at current predictions: $r_{im} = -\\left[\\frac{\\partial \\mathcal{L}(y_i, f(\\mathbf{x}_i))}{\\partial f(\\mathbf{x}_i)}\\right]_{f = f_{m-1}}$ (pseudo-residuals)"
        },
        {
          "id": "C",
          "text": "The original features transformed by PCA"
        },
        {
          "id": "D",
          "text": "The classification margin $y_i f_{m-1}(\\mathbf{x}_i)$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "GBM performs gradient descent directly in function space. Each new base learner fits the negative gradient (pseudo-residuals) of the loss function with respect to the ensemble's current predictions.",
      "difficulty": "medium",
      "subtopic": "Gradient Boosting Dynamics"
    },
    {
      "id": "cml-l12-q10",
      "type": "single_choice",
      "question": "For Mean Squared Error loss $\\mathcal{L}(y, f(\\mathbf{x})) = \\frac{1}{2}(y - f(\\mathbf{x}))^2$, what are the pseudo-residuals in Gradient Boosting?",
      "options": [
        {
          "id": "A",
          "text": "The exact standard residuals: $r_i = y_i - f(\\mathbf{x}_i)$"
        },
        {
          "id": "B",
          "text": "The absolute differences: $|y_i - f(\\mathbf{x}_i)|$"
        },
        {
          "id": "C",
          "text": "The squared errors: $(y_i - f(\\mathbf{x}_i))^2$"
        },
        {
          "id": "D",
          "text": "The signs of the errors: $\\text{sign}(y_i - f(\\mathbf{x}_i))$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "$-\\frac{\\partial}{\\partial f} \\left[\\frac{1}{2}(y - f)^2\\right] = -(y - f)(-1) = y - f$. For MSE loss, pseudo-residuals coincide exactly with ordinary residuals.",
      "difficulty": "easy",
      "subtopic": "Gradient Boosting Dynamics"
    },
    {
      "id": "cml-l12-q11",
      "type": "single_choice",
      "question": "What key mathematical enhancement does XGBoost introduce over traditional Friedman Gradient Boosting when approximating the objective function?",
      "options": [
        {
          "id": "A",
          "text": "It uses a 2nd-order Taylor expansion incorporating both first-order gradients ($g_i$) and second-order Hessians ($h_i$)"
        },
        {
          "id": "B",
          "text": "It uses cubic spline interpolation"
        },
        {
          "id": "C",
          "text": "It discards gradient evaluation and uses genetic algorithms"
        },
        {
          "id": "D",
          "text": "It replaces trees with kernel SVMs"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "XGBoost approximates the objective via 2nd-order Taylor expansion: $\\mathcal{L}^{(t)} \\approx \\sum [g_i f_t(\\mathbf{x}_i) + \\frac{1}{2} h_i f_t^2(\\mathbf{x}_i)] + \\Omega(f_t)$, allowing closed-form leaf weights and split scoring with curvature information.",
      "difficulty": "hard",
      "subtopic": "XGBoost Architecture"
    },
    {
      "id": "cml-l12-q12",
      "type": "single_choice",
      "question": "In XGBoost, given leaf instance gradients $G_j = \\sum_{i \\in I_j} g_i$, Hessians $H_j = \\sum_{i \\in I_j} h_i$, and L2 leaf regularization $\\lambda$, what is the optimal leaf weight $w_j^*$?",
      "options": [
        {
          "id": "A",
          "text": "$w_j^* = -\\frac{G_j}{H_j + \\lambda}$"
        },
        {
          "id": "B",
          "text": "$w_j^* = -\\frac{H_j}{G_j + \\lambda}$"
        },
        {
          "id": "C",
          "text": "$w_j^* = -\\frac{G_j^2}{2(H_j + \\lambda)}$"
        },
        {
          "id": "D",
          "text": "$w_j^* = \\frac{G_j + \\lambda}{H_j}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Differentiating the leaf objective $G_j w_j + \\frac{1}{2}(H_j + \\lambda)w_j^2$ with respect to $w_j$ yields $G_j + (H_j + \\lambda)w_j = 0 \\implies w_j^* = -\\frac{G_j}{H_j + \\lambda}$.",
      "difficulty": "hard",
      "subtopic": "XGBoost Architecture"
    },
    {
      "id": "cml-l12-q13",
      "type": "multi_choice",
      "question": "Which of the following techniques are used in Random Forests to decorrelate individual trees? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Bootstrap row sampling with replacement (sampling samples)"
        },
        {
          "id": "B",
          "text": "Feature subsampling at each candidate split (evaluating only $m = \\sqrt{p}$ features)"
        },
        {
          "id": "C",
          "text": "Fitting each tree on the residuals of previous trees"
        },
        {
          "id": "D",
          "text": "Growing deep unpruned trees to maintain individual diversity"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Row bagging, column feature subsampling, and deep unpruned growth maximize diversity and decorrelation. Fitting on residuals (C) is Boosting, not Random Forests.",
      "difficulty": "medium",
      "subtopic": "Random Forest Mechanism"
    },
    {
      "id": "cml-l12-q14",
      "type": "multi_choice",
      "question": "What happens when you increase the number of trees ($n\\_estimators$) in a Random Forest? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The model eventually overfits the training data if $n\\_estimators$ exceeds 10,000."
        },
        {
          "id": "B",
          "text": "The test error stabilizes and asymptotes to a constant lower bound $\\rho \\sigma^2$."
        },
        {
          "id": "C",
          "text": "Computational training and inference time scale linearly with $n\\_estimators$."
        },
        {
          "id": "D",
          "text": "Variance decreases monotonically without increasing model bias."
        }
      ],
      "correctOptionIds": [
        "B",
        "C",
        "D"
      ],
      "explanation": "By the Strong Law of Large Numbers, Random Forests DO NOT overfit simply by increasing $n\\_estimators$. The variance approaches its theoretical limit $\\rho \\sigma^2$, bias remains constant, and computation scales linearly.",
      "difficulty": "medium",
      "subtopic": "Ensemble Properties"
    },
    {
      "id": "cml-l12-q15",
      "type": "multi_choice",
      "question": "Which of the following regularizations and hyperparameter controls help prevent overfitting in Gradient Boosted Trees (GBM / XGBoost)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Shrinkage / Learning rate $\\eta < 0.1$ to scale step size"
        },
        {
          "id": "B",
          "text": "Subsample ratio $< 1.0$ (Stochastic Gradient Boosting)"
        },
        {
          "id": "C",
          "text": "Max tree depth limit (e.g., `max_depth` = 3 to 6)"
        },
        {
          "id": "D",
          "text": "Setting `n_estimators` to $\\infty$ without early stopping"
        },
        {
          "id": "E",
          "text": "Minimum split loss threshold $\\gamma$ (complexity control)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "E"
      ],
      "explanation": "Shrinkage (learning rate), stochastic subsampling, shallow depth constraints, and split threshold $\\gamma$ are essential anti-overfitting mechanisms in Boosting. Unlike Random Forests, boosting CAN overfit if `n_estimators` is too large without early stopping.",
      "difficulty": "medium",
      "subtopic": "Boosting Regularization"
    },
    {
      "id": "cml-l12-q16",
      "type": "single_choice",
      "question": "Why is AdaBoost particularly sensitive to label noise and extreme outliers in the dataset?",
      "options": [
        {
          "id": "A",
          "text": "Because its exponential loss function $e^{-y f(\\mathbf{x})}$ heavily penalizes misclassified outliers, causing subsequent learners to focus all their capacity on unlearnable noise"
        },
        {
          "id": "B",
          "text": "Because AdaBoost uses L1 Lasso penalty"
        },
        {
          "id": "C",
          "text": "Because decision stumps cannot split on continuous values"
        },
        {
          "id": "D",
          "text": "Because sample weights are bounded by 1.0"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The exponential loss function grows exponentially for large negative margins $y f(\\mathbf{x}) \\ll 0$. Mislabelled points or outliers receive gigantic sample weights, dominating subsequent rounds.",
      "difficulty": "medium",
      "subtopic": "Loss Functions & Outliers"
    },
    {
      "id": "cml-l12-q17",
      "type": "multi_choice",
      "question": "Which algorithmic innovations explain why LightGBM trains significantly faster than standard XGBoost on large datasets? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Histogram-based binning of continuous features into discrete buckets (e.g., 256 bins)"
        },
        {
          "id": "B",
          "text": "GOSS (Gradient-based One-Side Sampling) retaining instances with large gradients while randomly subsampling instances with small gradients"
        },
        {
          "id": "C",
          "text": "EFB (Exclusive Feature Bundling) combining mutually exclusive sparse features"
        },
        {
          "id": "D",
          "text": "Leaf-wise (best-first) tree growth rather than depth-wise (level-wise) growth"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four are key LightGBM innovations: histogram binning, GOSS, EFB, and leaf-wise splitting allow orders of magnitude faster training than naive exact-greedy split finders.",
      "difficulty": "hard",
      "subtopic": "Modern Boosting Frameworks"
    },
    {
      "id": "cml-l12-q18",
      "type": "single_choice",
      "question": "In Stacking (Stacked Generalization), how is data leakage prevented when generating meta-features for the second-level blender model?",
      "options": [
        {
          "id": "A",
          "text": "By evaluating base models on their own training data"
        },
        {
          "id": "B",
          "text": "By using out-of-fold cross-validation predictions from base models to form the training set for the meta-learner"
        },
        {
          "id": "C",
          "text": "By running PCA on the base model predictions"
        },
        {
          "id": "D",
          "text": "By standardizing the features using MinMaxScaler"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "If base models predict on the data they trained on, meta-features reflect overfitting. Stacking uses $K$-fold cross-validation so each base prediction fed to the meta-model is strictly out-of-fold.",
      "difficulty": "medium",
      "subtopic": "Stacking"
    },
    {
      "id": "cml-l12-q19",
      "type": "single_choice",
      "question": "What is the recommended default number of features to sample at each split in Scikit-Learn's `RandomForestClassifier` for a problem with $p$ features?",
      "options": [
        {
          "id": "A",
          "text": "$p$ (all features)"
        },
        {
          "id": "B",
          "text": "$\\sqrt{p}$"
        },
        {
          "id": "C",
          "text": "$p / 3$"
        },
        {
          "id": "D",
          "text": "$\\log_2(p)$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "For classification, the standard default is $m = \\sqrt{p}$ (`max_features='sqrt'`). For regression, the standard default is typically $p/3$.",
      "difficulty": "easy",
      "subtopic": "Random Forest Hyperparameters"
    },
    {
      "id": "cml-l12-q20",
      "type": "multi_choice",
      "question": "Which of the following statements regarding the convergence and capacity of Ensembles are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Random Forests cannot extrapolate linear upward or downward trends beyond the maximum and minimum targets observed in training data."
        },
        {
          "id": "B",
          "text": "Boosting algorithms can approximate any continuous non-linear mapping given sufficient weak learners and small learning rate."
        },
        {
          "id": "C",
          "text": "A Random Forest can be trained completely in parallel across multiple CPU cores because trees are conditionally independent."
        },
        {
          "id": "D",
          "text": "Gradient Boosting trees must be computed strictly sequentially because each tree depends on the residuals of all previous trees."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four statements are foundational truths: Trees cannot extrapolate beyond training extremes; Boosting is a universal function approximator; Bagging/RF is embarrassingly parallel; Boosting is inherently sequential.",
      "difficulty": "hard",
      "subtopic": "Ensemble Theory"
    }
  ]
}
