QUIZ_L11 = {
  "topicId": "lecture-11",
  "lectureNumber": 11,
  "title": "Decision Trees: Recursive Space Partitioning & Impurity Metrics",
  "description": "20 questions covering recursive binary splitting, Shannon Entropy, Information Gain, Gini Impurity, CART vs ID3 vs C4.5, regression trees with variance reduction, cost-complexity post-pruning, and MDI feature importance.",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml-l11-q01",
      "type": "single_choice",
      "question": "What is the primary geometric nature of the decision boundaries constructed by standard Decision Trees (CART/ID3)?",
      "options": [
        {
          "id": "A",
          "text": "Smooth non-linear polynomial hypersurfaces"
        },
        {
          "id": "B",
          "text": "Axis-aligned, orthogonal hyperplanes partitioning the feature space into hyper-rectangles"
        },
        {
          "id": "C",
          "text": "Spherical Voronoi tessellations centered at support vectors"
        },
        {
          "id": "D",
          "text": "Arbitrary oblique hyperplanes maximizing geometric margin"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Standard decision trees split on a single feature at a time ($x_j \\le s$), which geometrically produces orthogonal, axis-aligned splits partitioning the $d$-dimensional space into hyper-rectangles.",
      "difficulty": "easy",
      "subtopic": "Geometric Partitioning"
    },
    {
      "id": "cml-l11-q02",
      "type": "single_choice",
      "question": "A binary classification node contains 30 positive samples and 10 negative samples. What is the Gini Impurity of this node?",
      "options": [
        {
          "id": "A",
          "text": "0.375"
        },
        {
          "id": "B",
          "text": "0.500"
        },
        {
          "id": "C",
          "text": "0.1875"
        },
        {
          "id": "D",
          "text": "0.811"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "$p_1 = 30/40 = 0.75$, $p_2 = 10/40 = 0.25$. Gini Impurity $G = 1 - (p_1^2 + p_2^2) = 1 - (0.5625 + 0.0625) = 1 - 0.625 = 0.375$.",
      "difficulty": "medium",
      "subtopic": "Gini Impurity"
    },
    {
      "id": "cml-l11-q03",
      "type": "single_choice",
      "question": "For a node with $K$ classes, what is the theoretical maximum possible value of Gini Impurity, and when is it achieved?",
      "options": [
        {
          "id": "A",
          "text": "1.0, achieved when all samples belong to a single class"
        },
        {
          "id": "B",
          "text": "$\\log_2(K)$, achieved when classes are uniformly distributed"
        },
        {
          "id": "C",
          "text": "$1 - \\frac{1}{K}$, achieved under a uniform distribution where each class has probability $p_k = 1/K$"
        },
        {
          "id": "D",
          "text": "0.5, regardless of the number of classes $K$"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "When all $K$ classes are uniformly distributed, $p_k = 1/K$. Then $G = 1 - \\sum_{k=1}^K (1/K)^2 = 1 - K(1/K^2) = 1 - 1/K$. For binary classification ($K=2$), the maximum is $0.5$.",
      "difficulty": "medium",
      "subtopic": "Gini Impurity"
    },
    {
      "id": "cml-l11-q04",
      "type": "single_choice",
      "question": "Why did Quinlan introduce Gain Ratio in C4.5 to replace raw Information Gain in ID3?",
      "options": [
        {
          "id": "A",
          "text": "Information Gain cannot be computed for continuous features"
        },
        {
          "id": "B",
          "text": "Information Gain is strongly biased toward features with many distinct categorical levels (e.g., ID numbers), creating pure but useless single-sample leaves"
        },
        {
          "id": "C",
          "text": "Information Gain requires computing natural logarithms instead of base 2"
        },
        {
          "id": "D",
          "text": "Gain Ratio eliminates the need for recursive tree splitting"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Raw Information Gain maximizes the reduction in entropy, which artificially favors features with high cardinality (e.g., CustomerID), creating leaves with 1 point and zero entropy. Gain Ratio penalizes high-branching features by dividing by the Split Information (intrinsic entropy of the split).",
      "difficulty": "medium",
      "subtopic": "Gain Ratio"
    },
    {
      "id": "cml-l11-q05",
      "type": "single_choice",
      "question": "In CART regression trees, what prediction is assigned to any test instance falling into a terminal leaf region $R_m$?",
      "options": [
        {
          "id": "A",
          "text": "The median of all training targets in $R_m$"
        },
        {
          "id": "B",
          "text": "The arithmetic mean $\\bar{y}_{R_m} = \\frac{1}{N_m} \\sum_{i \\in R_m} y_i$ of the training targets in that leaf"
        },
        {
          "id": "C",
          "text": "The linear OLS regression prediction fitted solely on points in $R_m$"
        },
        {
          "id": "D",
          "text": "The mode of the target distribution in $R_m$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Standard CART regression trees minimize squared error loss $\\sum (y_i - c_m)^2$. Setting the derivative with respect to $c_m$ to zero yields the arithmetic mean $\\hat{c}_m = \\bar{y}_{R_m}$.",
      "difficulty": "easy",
      "subtopic": "Regression Trees"
    },
    {
      "id": "cml-l11-q06",
      "type": "single_choice",
      "question": "In Cost-Complexity Post-Pruning (Minimal Cost-Complexity Pruning), what is the objective function being minimized over subtrees $T \\subseteq T_0$?",
      "options": [
        {
          "id": "A",
          "text": "$R_\\alpha(T) = R(T) + \\alpha |T|$, where $R(T)$ is training error, $|T|$ is the number of terminal leaves, and $\\alpha \\ge 0$ is the complexity penalty"
        },
        {
          "id": "B",
          "text": "$R_\\alpha(T) = R(T) \\times \\alpha^{|T|}$"
        },
        {
          "id": "C",
          "text": "$R_\\alpha(T) = \\frac{R(T)}{\\alpha |T|}$"
        },
        {
          "id": "D",
          "text": "$R_\\alpha(T) = R(T) + \\frac{1}{\\alpha} \\sum_{j} w_j^2$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Cost-complexity pruning uses the regularized cost function $R_\\alpha(T) = R(T) + \\alpha |T|$. When $\\alpha = 0$, the full tree $T_0$ is chosen; as $\\alpha \\to \\infty$, the tree collapses to the single root node.",
      "difficulty": "hard",
      "subtopic": "Cost-Complexity Pruning"
    },
    {
      "id": "cml-l11-q07",
      "type": "single_choice",
      "question": "What is the computational time complexity for evaluating all candidate binary split thresholds on a single continuous feature with $n$ training instances?",
      "options": [
        {
          "id": "A",
          "text": "$\\mathcal{O}(n^2)$ using brute-force search"
        },
        {
          "id": "B",
          "text": "$\\mathcal{O}(n \\log n)$ by sorting the feature once and updating impurity running counts in $\\mathcal{O}(n)$"
        },
        {
          "id": "C",
          "text": "$\\mathcal{O}(1)$ independent of dataset size"
        },
        {
          "id": "D",
          "text": "$\\mathcal{O}(2^n)$ because all subsets must be evaluated"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Sorting the $n$ continuous values takes $\\mathcal{O}(n \\log n)$. Once sorted, we scan adjacent pairs in linear $\\mathcal{O}(n)$ time by maintaining cumulative class frequency histograms, giving total time $\\mathcal{O}(n \\log n)$.",
      "difficulty": "medium",
      "subtopic": "Continuous Splitting Algorithm"
    },
    {
      "id": "cml-l11-q08",
      "type": "single_choice",
      "question": "How is the Mean Decrease in Impurity (MDI) feature importance calculated for a feature $X_j$ in a Decision Tree?",
      "options": [
        {
          "id": "A",
          "text": "By counting how many leaves classify instances using feature $X_j$"
        },
        {
          "id": "B",
          "text": "By summing the impurity reductions $\\Delta I(t) = I(t) - \\frac{N_L}{N_t}I(t_L) - \\frac{N_R}{N_t}I(t_R)$ weighted by node sample proportions across all internal nodes where $X_j$ was used as the splitting attribute"
        },
        {
          "id": "C",
          "text": "By measuring the correlation between $X_j$ and the target $y$"
        },
        {
          "id": "D",
          "text": "By shuffling feature $X_j$ and computing the degradation in test accuracy"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "MDI (Gini Importance) sums the impurity decrease across all nodes $t$ split on $X_j$, weighted by the fraction of training samples passing through $t$: $Importance(X_j) = \\sum_{t \\text{ splits on } X_j} \\frac{N_t}{N} \\Delta I(t)$.",
      "difficulty": "hard",
      "subtopic": "Feature Importance (MDI)"
    },
    {
      "id": "cml-l11-q09",
      "type": "single_choice",
      "question": "Why are unpruned Decision Trees notorious for having high variance (overfitting)?",
      "options": [
        {
          "id": "A",
          "text": "Because they cannot model non-linear boundaries"
        },
        {
          "id": "B",
          "text": "Because recursive splitting can continue until every training sample is isolated into its own pure leaf, capturing idiosyncratic noise"
        },
        {
          "id": "C",
          "text": "Because they require strict feature normalization"
        },
        {
          "id": "D",
          "text": "Because gradient descent diverges on piecewise constant step functions"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Without constraints, a tree can grow until $H(T) = 0$ with 1 sample per leaf, achieving 100% training accuracy but massive generalization error due to extreme variance.",
      "difficulty": "easy",
      "subtopic": "Tree Overfitting"
    },
    {
      "id": "cml-l11-q10",
      "type": "single_choice",
      "question": "Which of the following preprocessing steps is completely UNNECESSARY when training a standard CART Decision Tree?",
      "options": [
        {
          "id": "A",
          "text": "Monotonic feature scaling or normalization (e.g., StandardScaler or MinMaxScaler)"
        },
        {
          "id": "B",
          "text": "Handling missing target values"
        },
        {
          "id": "C",
          "text": "Limiting maximum depth to prevent overfitting"
        },
        {
          "id": "D",
          "text": "Selecting an impurity criterion"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Decision trees split based on monotonic order ($x_j \\le s$), making them completely invariant to strictly monotonic feature scaling. Scaling features by multiplying by 1000 or taking logs does not change split ordering.",
      "difficulty": "easy",
      "subtopic": "Scale Invariance"
    },
    {
      "id": "cml-l11-q11",
      "type": "multi_choice",
      "question": "Which of the following are valid Pre-Pruning (early stopping) hyperparameter controls in Scikit-Learn's `DecisionTreeClassifier`? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "`max_depth` (limiting maximum tree depth)"
        },
        {
          "id": "B",
          "text": "`min_samples_split` (minimum samples required to split an internal node)"
        },
        {
          "id": "C",
          "text": "`min_samples_leaf` (minimum samples required at a leaf node)"
        },
        {
          "id": "D",
          "text": "`max_leaf_nodes` (grow tree in best-first fashion up to a leaf budget)"
        },
        {
          "id": "E",
          "text": "`learning_rate` (shrinking individual leaf predictions)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "A, B, C, and D are all pre-pruning stopping hyperparameters for a single decision tree. `learning_rate` belongs to Gradient Boosted Trees, not a standalone DecisionTreeClassifier.",
      "difficulty": "medium",
      "subtopic": "Pre-Pruning Hyperparameters"
    },
    {
      "id": "cml-l11-q12",
      "type": "multi_choice",
      "question": "Which statements correctly compare Shannon Entropy and Gini Impurity? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Both metrics equal 0 when a node is 100% pure (all samples belong to one class)."
        },
        {
          "id": "B",
          "text": "Gini Impurity is computationally faster to calculate because it avoids logarithmic evaluations ($\\log_2$)."
        },
        {
          "id": "C",
          "text": "Shannon Entropy penalizes mixed states slightly more heavily than Gini Impurity."
        },
        {
          "id": "D",
          "text": "Entropy can produce negative values, whereas Gini Impurity is always positive."
        },
        {
          "id": "E",
          "text": "In practice, both metrics lead to virtually identical tree topologies in over 98% of splits."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "E"
      ],
      "explanation": "Both equal 0 at pure nodes. Gini requires only multiplications and additions ($1 - \\sum p_k^2$), avoiding costly log calls. Both are strictly non-negative for probability distributions ($p_k \\le 1 \\implies -p_k \\log_2 p_k \\ge 0$). They yield nearly identical trees in empirical studies.",
      "difficulty": "hard",
      "subtopic": "Entropy vs Gini"
    },
    {
      "id": "cml-l11-q13",
      "type": "multi_choice",
      "question": "Why is a Decision Tree highly sensitive to small perturbations in the training data (high structural instability)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "A tiny change near the root split changes which samples travel to left vs right subtrees."
        },
        {
          "id": "B",
          "text": "Hierarchical greediness: Errors and sub-optimal splits cascade and propagate down the entire tree hierarchy."
        },
        {
          "id": "C",
          "text": "Gradient descent step sizes oscillate near local saddle points."
        },
        {
          "id": "D",
          "text": "The tree cannot backtrack on a suboptimal split made earlier."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Decision trees use greedy top-down recursive partitioning without backtracking. Changing a few points can flip the top-level split, causing radically different subtrees downstream. Decision trees do not use gradient descent.",
      "difficulty": "medium",
      "subtopic": "Structural Instability"
    },
    {
      "id": "cml-l11-q14",
      "type": "multi_choice",
      "question": "Which of the following are known drawbacks or vulnerabilities of Mean Decrease in Impurity (MDI / Gini Importance)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "MDI is computed exclusively on the training set, so it inflates the importance of features that the tree overfitted on."
        },
        {
          "id": "B",
          "text": "MDI strongly biases toward high-cardinality features (e.g., continuous variables or categories with many unique levels) because they offer more split opportunities."
        },
        {
          "id": "C",
          "text": "When two features are perfectly collinear, MDI splits their importance arbitrarily between them."
        },
        {
          "id": "D",
          "text": "MDI cannot be computed for classification problems."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "MDI's major flaws are: (1) in-sample evaluation reflecting overfitting, (2) severe bias towards high-cardinality continuous features, and (3) dilution over collinear pairs. Permutation Feature Importance is preferred to overcome these flaws.",
      "difficulty": "hard",
      "subtopic": "Feature Importance (MDI)"
    },
    {
      "id": "cml-l11-q15",
      "type": "multi_choice",
      "question": "How does the CART algorithm handle continuous-valued attributes when finding the optimal split? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "It sorts the distinct continuous values in ascending order: $v_1 < v_2 < \\dots < v_m$."
        },
        {
          "id": "B",
          "text": "Candidate split thresholds are evaluated at midpoints $s_i = \\frac{v_i + v_{i+1}}{2}$."
        },
        {
          "id": "C",
          "text": "It converts continuous values to Fourier frequency harmonics."
        },
        {
          "id": "D",
          "text": "It selects the threshold $s^*$ that maximizes the weighted impurity reduction (Information Gain or Gini Gain)."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "CART sorts values, tests midpoints between adjacent distinct values, and picks the split threshold that maximizes impurity reduction.",
      "difficulty": "medium",
      "subtopic": "Continuous Splitting Algorithm"
    },
    {
      "id": "cml-l11-q16",
      "type": "single_choice",
      "question": "What is the entropy $H(S)$ of a node where all 50 samples belong to Class A?",
      "options": [
        {
          "id": "A",
          "text": "1.0 bit"
        },
        {
          "id": "B",
          "text": "0.0 bits"
        },
        {
          "id": "C",
          "text": "0.5 bits"
        },
        {
          "id": "D",
          "text": "Undefined due to $\\log_2(0)$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "$p_A = 1.0, p_{\\text{other}} = 0$. $H(S) = -1 \\log_2(1) = 0$. By mathematical convention, $0 \\log_2(0) = 0$. Zero entropy signifies complete certainty/purity.",
      "difficulty": "easy",
      "subtopic": "Shannon Entropy"
    },
    {
      "id": "cml-l11-q17",
      "type": "single_choice",
      "question": "A parent node has entropy $H(D) = 1.0$. A split divides 100 samples into Left (60 samples, $H(D_L) = 0.4$) and Right (40 samples, $H(D_R) = 0.8$). What is the Information Gain of this split?",
      "options": [
        {
          "id": "A",
          "text": "0.44 bits"
        },
        {
          "id": "B",
          "text": "0.56 bits"
        },
        {
          "id": "C",
          "text": "0.20 bits"
        },
        {
          "id": "D",
          "text": "0.60 bits"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Weighted child entropy $= \\frac{60}{100}(0.4) + \\frac{40}{100}(0.8) = 0.24 + 0.32 = 0.56$. Information Gain $= 1.0 - 0.56 = 0.44$ bits.",
      "difficulty": "medium",
      "subtopic": "Information Gain"
    },
    {
      "id": "cml-l11-q18",
      "type": "multi_choice",
      "question": "Which of the following are inherent strengths of Decision Trees compared to Linear Regression or Support Vector Machines? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "White-box interpretability: Decisions can be easily visualized and converted into human-readable IF-THEN rules."
        },
        {
          "id": "B",
          "text": "Natural handling of non-linear relationships without needing explicit polynomial feature transformations or kernels."
        },
        {
          "id": "C",
          "text": "Total immunity to feature scale; no feature normalization or standardization is required."
        },
        {
          "id": "D",
          "text": "Smooth and accurate extrapolation far outside the bounding box of training feature ranges."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are classic advantages of Decision Trees. D is false: decision trees predict piecewise constant values and completely fail to extrapolate trends outside the training feature domain.",
      "difficulty": "medium",
      "subtopic": "Decision Tree Characteristics"
    },
    {
      "id": "cml-l11-q19",
      "type": "single_choice",
      "question": "In Regression Trees, what metric is typically minimized when choosing split points?",
      "options": [
        {
          "id": "A",
          "text": "Cross-Entropy"
        },
        {
          "id": "B",
          "text": "Gini Impurity"
        },
        {
          "id": "C",
          "text": "Variance Reduction (or Sum of Squared Errors: $\\sum (y_i - \\bar{y}_L)^2 + \\sum (y_i - \\bar{y}_R)^2$)"
        },
        {
          "id": "D",
          "text": "ROC-AUC Score"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "Regression trees use variance reduction (or mean squared error reduction), seeking splits that minimize the sum of squared deviations from the leaf means.",
      "difficulty": "easy",
      "subtopic": "Regression Trees"
    },
    {
      "id": "cml-l11-q20",
      "type": "multi_choice",
      "question": "Which algorithmic differences distinguish CART from ID3? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "CART builds strictly binary trees (each node has exactly 2 branches), whereas ID3 can create multi-way branches for categorical attributes."
        },
        {
          "id": "B",
          "text": "CART supports regression as well as classification; ID3 supports only classification."
        },
        {
          "id": "C",
          "text": "CART natively handles continuous numeric attributes; original ID3 supports only discrete categorical features."
        },
        {
          "id": "D",
          "text": "CART uses Gini Impurity by default; ID3 uses Shannon Entropy / Information Gain."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C",
        "D"
      ],
      "explanation": "All four statements accurately describe the architectural advancements of Breiman's CART (1984) over Quinlan's original ID3 (1986).",
      "difficulty": "hard",
      "subtopic": "CART vs ID3"
    }
  ]
}
