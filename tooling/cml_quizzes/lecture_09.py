QUIZ_L09 = {
  "topicId": "lecture-09",
  "lectureNumber": 9,
  "title": "Instance-Based Learning: K-Nearest Neighbors",
  "description": "25 questions covering K-Nearest Neighbors (k-NN) mechanics, Euclidean, Manhattan, and Minkowski distance metrics, feature scaling imperatives, selection of hyperparameter k, curse of dimensionality, and KD-Tree / Ball Tree acceleration.",
  "estimatedMinutes": 35,
  "questions": [
    {
      "id": "cml-l09-q01",
      "type": "single_choice",
      "question": "Why is the K-Nearest Neighbors (k-NN) algorithm formally classified as a 'lazy learner' (instance-based learning)?",
      "options": [
        {
          "id": "A",
          "text": "Because it runs slowly even on small datasets"
        },
        {
          "id": "B",
          "text": "Because it performs no explicit mathematical model training or parameter estimation during the training phase, simply storing the training instances in memory until prediction time"
        },
        {
          "id": "C",
          "text": "Because it does not calculate gradients"
        },
        {
          "id": "D",
          "text": "Because it requires human labeling for every test sample"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Lazy learners do not generalize or build an explicit parameterized hypothesis during training ($O(1)$ training time). Instead, all computation (distance calculation, neighbor sorting, and voting) is deferred to test/query time ($O(n \\cdot p)$ inference time for brute-force).",
      "difficulty": "easy",
      "subtopic": "Lazy Learning Concept"
    },
    {
      "id": "cml-l09-q02",
      "type": "single_choice",
      "question": "What is the general mathematical formula for the Minkowski distance of order $p$ between two $d$-dimensional feature vectors $u$ and $v$?",
      "options": [
        {
          "id": "A",
          "text": "$D(u, v) = \\left( \\sum_{i=1}^d |u_i - v_i|^p \\right)^{1/p}$"
        },
        {
          "id": "B",
          "text": "$D(u, v) = \\sum_{i=1}^d (u_i - v_i)^p$"
        },
        {
          "id": "C",
          "text": "$D(u, v) = \\max_i |u_i - v_i|^p$"
        },
        {
          "id": "D",
          "text": "$D(u, v) = \\frac{u \\cdot v}{\\|u\\| \\|v\\|}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Minkowski distance is the $L_p$ metric: $D(u, v) = (\\sum |u_i - v_i|^p)^{1/p}$. When $p = 1$, it yields Manhattan distance; when $p = 2$, it yields Euclidean distance; as $p \\to \\infty$, it converges to Chebyshev distance.",
      "difficulty": "easy",
      "subtopic": "Minkowski Distance"
    },
    {
      "id": "cml-l09-q03",
      "type": "single_choice",
      "question": "What happens if you run a 5-NN classifier on a dataset containing Feature 1 ('Age' ranging from 18 to 80) and Feature 2 ('Annual Income' ranging from $20,000 to $500,000) WITHOUT feature standardization?",
      "options": [
        {
          "id": "A",
          "text": "Both features contribute equally to the distance computation"
        },
        {
          "id": "B",
          "text": "Annual Income completely dominates the Euclidean distance calculation, rendering Age virtually irrelevant"
        },
        {
          "id": "C",
          "text": "The algorithm fails to converge"
        },
        {
          "id": "D",
          "text": "The decision boundary becomes purely linear"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Euclidean distance is $\\sqrt{(\\Delta \\text{Age})^2 + (\\Delta \\text{Income})^2}$. An Age difference of 50 squared is 2,500, whereas an Income difference of $10,000 squared is $100,000,000$. Without scaling, the high-magnitude feature dictates neighbor selection completely.",
      "difficulty": "easy",
      "subtopic": "Need for Scaling"
    },
    {
      "id": "cml-l09-q04",
      "type": "single_choice",
      "question": "What are the bias, variance, and decision boundary characteristics of a 1-Nearest Neighbor ($k = 1$) classifier?",
      "options": [
        {
          "id": "A",
          "text": "High bias, low variance, extremely smooth decision boundary"
        },
        {
          "id": "B",
          "text": "Low bias, high variance, highly complex and jagged decision boundary perfectly memorizing training noise"
        },
        {
          "id": "C",
          "text": "Zero training error and guaranteed zero test error"
        },
        {
          "id": "D",
          "text": "Underfitting across all datasets"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "When $k=1$, each training sample creates its own Voronoi cell. The training accuracy is 100% (zero training error / low bias), but the boundary is intricate and highly sensitive to individual noisy points (high variance / overfitting).",
      "difficulty": "easy",
      "subtopic": "Extreme k=1 Behavior"
    },
    {
      "id": "cml-l09-q05",
      "type": "single_choice",
      "question": "What occurs when the hyperparameter $k$ in a k-NN classifier is set to the total number of training samples $N$ ($k = N$)?",
      "options": [
        {
          "id": "A",
          "text": "The classifier predicts the majority class of the entire training dataset for every test point, resulting in high bias (underfitting)"
        },
        {
          "id": "B",
          "text": "The model achieves maximum possible complexity and overfits violently"
        },
        {
          "id": "C",
          "text": "The inference time drops to $O(1)$"
        },
        {
          "id": "D",
          "text": "The decision boundary becomes an exact circle"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "When $k = N$, every single test point queries all $N$ training samples. The plurality vote is always identical to the global majority class, ignoring query features entirely (maximal bias / extreme underfitting).",
      "difficulty": "easy",
      "subtopic": "Extreme k=N Behavior"
    },
    {
      "id": "cml-l09-q06",
      "type": "single_choice",
      "question": "Why is an odd value of $k$ (e.g. $k = 3, 5, 7$) strongly recommended when using k-NN for binary classification?",
      "options": [
        {
          "id": "A",
          "text": "Odd numbers make distance computations run twice as fast"
        },
        {
          "id": "B",
          "text": "To prevent 50-50 tie votes when counting neighbor class labels"
        },
        {
          "id": "C",
          "text": "Because Scikit-Learn throws a ValueError for even values of $k$"
        },
        {
          "id": "D",
          "text": "To guarantee that the decision boundary remains convex"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In a 2-class problem, an even $k$ (e.g., $k=4$) can result in a 2-2 tie vote, requiring arbitrary tie-breaking. An odd $k$ guarantees a strict majority.",
      "difficulty": "easy",
      "subtopic": "Tie-Breaking with Odd k"
    },
    {
      "id": "cml-l09-q07",
      "type": "single_choice",
      "question": "In distance-weighted k-NN (`weights='distance'`), how is each neighbor's vote weighted during classification or regression?",
      "options": [
        {
          "id": "A",
          "text": "Proportional to distance: $w_i = d(x, x_i)$"
        },
        {
          "id": "B",
          "text": "Inversely proportional to distance: $w_i = \\frac{1}{d(x, x_i)}$ (closer neighbors have much greater influence)"
        },
        {
          "id": "C",
          "text": "Uniformly: $w_i = \\frac{1}{k}$ regardless of distance"
        },
        {
          "id": "D",
          "text": "Exponentially proportional to the index of the neighbor in the dataset"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Distance weighting assigns weights inversely proportional to distance (typically $w_i = 1/d_i$ or $1/d_i^2$). A neighbor right next to the query point exerts much stronger influence than a neighbor near the outer boundary of the $k$-neighborhood.",
      "difficulty": "easy",
      "subtopic": "Distance-Weighted k-NN"
    },
    {
      "id": "cml-l09-q08",
      "type": "single_choice",
      "question": "What mathematical phenomenon regarding distances occurs in high-dimensional spaces, severely degrading the performance of k-NN (Curse of Dimensionality)?",
      "options": [
        {
          "id": "A",
          "text": "Distances between all pairs of points become zero"
        },
        {
          "id": "B",
          "text": "The distance to the nearest neighbor approaches the distance to the farthest neighbor: $\\lim_{d \\to \\infty} \\frac{\\text{dist}_\\text{max} - \\text{dist}_\\text{min}}{\\text{dist}_\\text{min}} = 0$, rendering proximity meaningless"
        },
        {
          "id": "C",
          "text": "All points collapse onto a single 1D line"
        },
        {
          "id": "D",
          "text": "Euclidean distance evaluates to negative values"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Beyer et al. (1999) proved that under broad data distributions, as dimensionality $d \\to \\infty$, the relative variance of pairwise distances vanishes. Every point becomes roughly equidistant from every other point, destroying the concept of 'nearest' neighbor.",
      "difficulty": "hard",
      "subtopic": "Curse of Dimensionality"
    },
    {
      "id": "cml-l09-q09",
      "type": "single_choice",
      "question": "What is the Mahalanobis distance between two vectors $u$ and $v$ with covariance matrix $\\Sigma$, and why is it superior to Euclidean distance for correlated features with unequal variances?",
      "options": [
        {
          "id": "A",
          "text": "$D_M(u, v) = \\sqrt{(u - v)^T \\Sigma^{-1} (u - v)}$; it accounts for feature variance and inter-feature correlations by standardizing space along principal axes"
        },
        {
          "id": "B",
          "text": "$D_M(u, v) = (u - v)^T \\Sigma (u - v)$"
        },
        {
          "id": "C",
          "text": "$D_M(u, v) = \\|u - v\\|_1$"
        },
        {
          "id": "D",
          "text": "$D_M(u, v) = \\det(\\Sigma) \\|u - v\\|$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The Mahalanobis distance measures distance in terms of standard deviations from the distribution mean while rotating coordinates to account for feature covariance (via $\\Sigma^{-1}$). If $\\Sigma = I$, it reduces to Euclidean distance.",
      "difficulty": "hard",
      "subtopic": "Mahalanobis Distance"
    },
    {
      "id": "cml-l09-q10",
      "type": "single_choice",
      "question": "Which spatial partitioning data structure partitions training data using axis-aligned hyperplanes to accelerate k-NN nearest-neighbor queries from $O(n)$ to $O(\\log n)$ in low dimensions?",
      "options": [
        {
          "id": "A",
          "text": "Hash Table"
        },
        {
          "id": "B",
          "text": "KD-Tree (k-dimensional tree)"
        },
        {
          "id": "C",
          "text": "Red-Black Tree"
        },
        {
          "id": "D",
          "text": "Trie"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A KD-Tree is a binary tree where each node splits data along one specific dimension at the median, cycling through dimensions across tree levels, enabling fast geometric pruning during neighbor search.",
      "difficulty": "medium",
      "subtopic": "KD-Tree Acceleration"
    },
    {
      "id": "cml-l09-q11",
      "type": "single_choice",
      "question": "Why does a KD-Tree's query time performance degrade back to brute-force $O(n)$ when the feature dimensionality $p$ is moderately large (e.g. $p > 20$)?",
      "options": [
        {
          "id": "A",
          "text": "Because the tree cannot store floating point values"
        },
        {
          "id": "B",
          "text": "Because the query hypersphere overlaps almost all bounding hyper-rectangles, requiring the algorithm to backtrack and search virtually every branch"
        },
        {
          "id": "C",
          "text": "Because the tree depth exceeds $2^{64}$"
        },
        {
          "id": "D",
          "text": "Because Python's recursion limit is exceeded"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In high dimensions, an $\\epsilon$-ball around the query point inevitably intersects the boundary of nearly every partitioned hyper-rectangle in the tree. Backtracking cannot prune any subtree, forcing inspection of almost all $n$ points.",
      "difficulty": "hard",
      "subtopic": "KD-Tree Dimensionality Limit"
    },
    {
      "id": "cml-l09-q12",
      "type": "single_choice",
      "question": "How does a Ball Tree differ from a KD-Tree, and why is it preferred for higher-dimensional spaces or arbitrary metric spaces?",
      "options": [
        {
          "id": "A",
          "text": "A Ball Tree partitions points into nested hyperspheres (balls) rather than axis-aligned hyper-rectangles, using the triangle inequality to prune distant balls efficiently"
        },
        {
          "id": "B",
          "text": "A Ball Tree converts continuous numbers into binary integers"
        },
        {
          "id": "C",
          "text": "A Ball Tree requires only 1 MB of memory for any dataset"
        },
        {
          "id": "D",
          "text": "A Ball Tree works only with Manhattan distance"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Ball trees group data into nested hyper-spheres defined by a center and radius. By the triangle inequality, if the distance from query point to sphere center exceeds query radius + sphere radius, the entire nested cluster can be pruned instantly.",
      "difficulty": "medium",
      "subtopic": "Ball Tree vs KD-Tree"
    },
    {
      "id": "cml-l09-q13",
      "type": "single_choice",
      "question": "For high-dimensional embeddings (e.g., 768-dimensional text embeddings from BERT across 10 million vectors), which class of algorithms is used in production systems (like FAISS or Pinecone) instead of exact k-NN?",
      "options": [
        {
          "id": "A",
          "text": "Ordinary Least Squares"
        },
        {
          "id": "B",
          "text": "Approximate Nearest Neighbors (ANN) such as HNSW (Hierarchical Navigable Small World) or Inverted File Index (IVF)"
        },
        {
          "id": "C",
          "text": "Polynomial regression with degree 768"
        },
        {
          "id": "D",
          "text": "Bubble sort on cosine similarities"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Exact brute force across millions of high-dim vectors takes seconds per query. Approximate Nearest Neighbors (ANN) algorithms (e.g. HNSW, ScaNN, FAISS) trade off a tiny fraction of recall (e.g. 98% accuracy) for sub-millisecond retrieval speeds.",
      "difficulty": "medium",
      "subtopic": "Approximate Nearest Neighbors (ANN)"
    },
    {
      "id": "cml-l09-q14",
      "type": "single_choice",
      "question": "In Cover and Hart's famous 1967 theorem on nearest neighbor classification, what is the theoretical upper bound on the asymptotic error rate $R$ of the 1-NN rule relative to the optimal Bayes error rate $R^*$ as $N \\to \\infty$?",
      "options": [
        {
          "id": "A",
          "text": "$R \\le R^*$ (1-NN beats Bayes optimal)"
        },
        {
          "id": "B",
          "text": "$R^* \\le R \\le 2 R^* (1 - R^*) \\le 2 R^*$ (1-NN error is at most twice the Bayes error rate)"
        },
        {
          "id": "C",
          "text": "$R = 1.0$"
        },
        {
          "id": "D",
          "text": "$R = \\frac{1}{2}$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Cover & Hart (1967) proved that as $n \\to \\infty$, the risk of 1-NN is bounded by $R^* \\le R \\le 2 R^*(1 - R^*) \\le 2 R^*$. Thus, with infinite data, 1-NN never has more than double the error of the theoretically best possible classifier.",
      "difficulty": "hard",
      "subtopic": "Cover-Hart Theorem"
    },
    {
      "id": "cml-l09-q15",
      "type": "single_choice",
      "question": "How does k-NN perform regression on a query point $x$ given its $k$ nearest neighbors $\\{x_1, \\dots, x_k\\}$ with target values $\\{y_1, \\dots, y_k\\}$?",
      "options": [
        {
          "id": "A",
          "text": "By calculating the mean of the neighbor targets: $\\hat{y} = \\frac{1}{k} \\sum_{i=1}^k y_i$ (or a distance-weighted average)"
        },
        {
          "id": "B",
          "text": "By taking the maximum value $\\max(y_i)$"
        },
        {
          "id": "C",
          "text": "By computing the dot product of $x$ and $y$"
        },
        {
          "id": "D",
          "text": "By fitting an $n$-degree polynomial"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "In k-NN regression (`KNeighborsRegressor`), predictions are the mean (or inverse-distance-weighted mean) of the $k$ nearest continuous target values.",
      "difficulty": "easy",
      "subtopic": "k-NN Regression"
    },
    {
      "id": "cml-l09-q16",
      "type": "single_choice",
      "question": "Which distance metric is most appropriate for comparing text documents represented as sparse TF-IDF word frequency vectors of varying lengths?",
      "options": [
        {
          "id": "A",
          "text": "Euclidean Distance ($L_2$ norm)"
        },
        {
          "id": "B",
          "text": "Cosine Distance ($1 - \\frac{u \\cdot v}{\\|u\\| \\|v\\|}$) because it evaluates the angle between vectors and is invariant to document length"
        },
        {
          "id": "C",
          "text": "Chebyshev Distance ($L_\\infty$ norm)"
        },
        {
          "id": "D",
          "text": "Hamming Distance"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Cosine similarity measures directional alignment rather than vector magnitude, preventing a long article and a short summary on the same topic from appearing artificially distant due to word count alone.",
      "difficulty": "easy",
      "subtopic": "Cosine Distance"
    },
    {
      "id": "cml-l09-q17",
      "type": "single_choice",
      "question": "What is the Hamming distance between two binary bitstrings `1011101` and `1001001`?",
      "options": [
        {
          "id": "A",
          "text": "0"
        },
        {
          "id": "B",
          "text": "2 (they differ at the 3rd and 5th bits)"
        },
        {
          "id": "C",
          "text": "5"
        },
        {
          "id": "D",
          "text": "7"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Comparing bit-by-bit: position 3 ('1' vs '0') and position 5 ('1' vs '0') differ. Exactly 2 bit flips are required, so the Hamming distance is 2.",
      "difficulty": "easy",
      "subtopic": "Hamming Distance"
    },
    {
      "id": "cml-l09-q18",
      "type": "single_choice",
      "question": "In Scikit-Learn's `KNeighborsClassifier`, what does setting `algorithm='auto'` do?",
      "options": [
        {
          "id": "A",
          "text": "It automatically tunes the optimal value of $k$"
        },
        {
          "id": "B",
          "text": "It automatically attempts to determine the most efficient search algorithm (`'ball_tree'`, `'kd_tree'`, or `'brute'`) based on dataset size, sparsity, and number of features"
        },
        {
          "id": "C",
          "text": "It automatically standardizes all input features"
        },
        {
          "id": "D",
          "text": "It automatically converts multi-class problems into binary problems"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "`algorithm='auto'` inspects the input data matrix (sample count $n$, feature dimension $p$, sparsity) and selects between `BallTree`, `KDTree`, and brute-force computation for fastest execution.",
      "difficulty": "easy",
      "subtopic": "Scikit-Learn k-NN Parameters"
    },
    {
      "id": "cml-l09-q19",
      "type": "multi_choice",
      "question": "Which of the following properties are TRUE of the K-Nearest Neighbors (k-NN) algorithm? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "It is a non-parametric model (makes no strong structural assumptions about the underlying distribution of data)"
        },
        {
          "id": "B",
          "text": "Its training time complexity for brute force is $O(1)$ (just storing data)"
        },
        {
          "id": "C",
          "text": "Its inference time complexity for brute-force search over $n$ training instances with $p$ features is $O(n \\cdot p)$"
        },
        {
          "id": "D",
          "text": "It automatically prunes noisy or irrelevant features from the dataset without preprocessing"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are defining attributes of instance-based lazy learning. D is FALSE: k-NN is exceptionally vulnerable to irrelevant noisy features because they pollute distance calculations.",
      "difficulty": "medium",
      "subtopic": "k-NN Complexity & Architecture"
    },
    {
      "id": "cml-l09-q20",
      "type": "multi_choice",
      "question": "Which of the following statements about the effect of the hyperparameter $k$ on model behavior are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Small values of $k$ (e.g. $k=1$) correspond to high model capacity, low bias, and high variance (overfitting)"
        },
        {
          "id": "B",
          "text": "Large values of $k$ (e.g. $k=100$) smooth the decision boundary, reducing variance but increasing bias (underfitting)"
        },
        {
          "id": "C",
          "text": "The optimal $k$ is typically selected by cross-validation via Grid Search"
        },
        {
          "id": "D",
          "text": "Increasing $k$ to infinity always guarantees 100% test accuracy"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C accurately outline the bias-variance trade-off governed by $k$. D is false; setting $k$ too high collapses predictions to the global majority class.",
      "difficulty": "easy",
      "subtopic": "Tuning k"
    },
    {
      "id": "cml-l09-q21",
      "type": "multi_choice",
      "question": "Which of the following distance metrics satisfy the formal mathematical axioms of a metric (Non-negativity, Identity of Indiscernibles, Symmetry, and Triangle Inequality)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Euclidean Distance ($L_2$)"
        },
        {
          "id": "B",
          "text": "Manhattan Distance ($L_1$)"
        },
        {
          "id": "C",
          "text": "Cosine Distance ($1 - \\cos(\\theta)$)"
        },
        {
          "id": "D",
          "text": "Chebyshev Distance ($L_\\infty$)"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Euclidean, Manhattan, and Chebyshev are valid $L_p$ norms and satisfy all metric axioms (including the triangle inequality). Standard Cosine Distance ($1 - \\cos$) is technically a pseudo-metric and does NOT satisfy the triangle inequality (though Angular Distance does).",
      "difficulty": "hard",
      "subtopic": "Formal Metric Axioms"
    },
    {
      "id": "cml-l09-q22",
      "type": "multi_choice",
      "question": "Which of the following techniques are effective in mitigating the Curse of Dimensionality for k-NN? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Dimensionality reduction using Principal Component Analysis (PCA)"
        },
        {
          "id": "B",
          "text": "Feature selection using Lasso ($L_1$) or mutual information to discard uninformative features"
        },
        {
          "id": "C",
          "text": "Adding random Gaussian noise features to increase diversity"
        },
        {
          "id": "D",
          "text": "Metric learning to optimize a Mahalanobis distance metric tailored to the classification task"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "A reduces dimension to dense principal components; B discards noisy features that distort distance; D learns a metric focusing on class separation. C worsens the curse of dimensionality.",
      "difficulty": "medium",
      "subtopic": "Mitigating High Dimensionality"
    },
    {
      "id": "cml-l09-q23",
      "type": "multi_choice",
      "question": "What are the primary disadvantages of the basic k-NN algorithm in real-world software applications? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "High inference latency for large datasets ($O(N \\cdot p)$ per test query)"
        },
        {
          "id": "B",
          "text": "High memory/RAM footprint (must keep the entire training dataset in memory)"
        },
        {
          "id": "C",
          "text": "Extreme vulnerability to irrelevant, redundant, or unscaled features"
        },
        {
          "id": "D",
          "text": "Inability to learn non-linear decision boundaries"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are major engineering drawbacks of k-NN. D is FALSE: k-NN naturally forms highly non-linear, arbitrary decision boundaries.",
      "difficulty": "medium",
      "subtopic": "k-NN Drawbacks"
    },
    {
      "id": "cml-l09-q24",
      "type": "multi_choice",
      "question": "Suppose you are building a Scikit-Learn pipeline for k-NN classification on tabular data with missing values and continuous features. Which components should be included? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "`SimpleImputer(strategy='median')` to handle missing numeric values"
        },
        {
          "id": "B",
          "text": "`StandardScaler()` or `RobustScaler()` to ensure all feature scales are normalized"
        },
        {
          "id": "C",
          "text": "`KNeighborsClassifier()` as the final estimator"
        },
        {
          "id": "D",
          "text": "Fitting the scaler on the test set before passing it to the pipeline"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A handles missingness; B equalizes scales; C makes predictions. D represents data leakage and must never be done.",
      "difficulty": "easy",
      "subtopic": "k-NN Pipeline Architecture"
    },
    {
      "id": "cml-l09-q25",
      "type": "multi_choice",
      "question": "Which of the following statements about the geometry of Voronoi tessellations produced by 1-NN are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Each training point lies inside a convex Voronoi cell where every point inside the cell is closer to that training point than to any other"
        },
        {
          "id": "B",
          "text": "The boundary between two Voronoi cells is a segment of the perpendicular bisector between the two training points"
        },
        {
          "id": "C",
          "text": "The union of all Voronoi cells tiles the entire feature space with zero gaps or overlaps"
        },
        {
          "id": "D",
          "text": "The Voronoi diagram requires features to be non-negative"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are fundamental geometric properties of Voronoi diagrams (and their dual Delaunay triangulations). D is false; Voronoi diagrams are defined over all $\\mathbb{R}^d$.",
      "difficulty": "hard",
      "subtopic": "Voronoi Geometry"
    }
  ]
}
