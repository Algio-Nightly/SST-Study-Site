QUIZ_L15 = {
  "topicId": "lecture-15",
  "lectureNumber": 15,
  "title": "Unsupervised Learning: K-Means, DBSCAN & Principal Component Analysis (PCA)",
  "description": "20 questions covering K-Means Lloyd's algorithm, K-Means++ initialization, Elbow method, Silhouette analysis, Hierarchical clustering linkages, DBSCAN density reachability, the Curse of Dimensionality, PCA maximum variance derivation, and SVD.",
  "estimatedMinutes": 30,
  "questions": [
    {
      "id": "cml-l15-q01",
      "type": "single_choice",
      "question": "What is the primary characteristic that separates Unsupervised Learning from Supervised Learning?",
      "options": [
        {
          "id": "A",
          "text": "Unsupervised learning operates without any ground-truth target labels $y$, aiming to discover latent structure, clusters, or lower-dimensional manifolds directly from feature matrix $\\mathbf{X}$"
        },
        {
          "id": "B",
          "text": "Unsupervised learning can only be run on GPU clusters"
        },
        {
          "id": "C",
          "text": "Unsupervised learning requires cross-validation with accuracy metrics"
        },
        {
          "id": "D",
          "text": "Unsupervised learning only applies to text data"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Supervised learning guides parameters using ground-truth targets $y$. Unsupervised learning has no target labels; the algorithm models the intrinsic structure, clustering, or density of the input features $\\mathbf{X}$.",
      "difficulty": "easy",
      "subtopic": "Unsupervised Paradigm"
    },
    {
      "id": "cml-l15-q02",
      "type": "single_choice",
      "question": "What is the objective function (Inertia / Within-Cluster Sum of Squares) minimized by the K-Means clustering algorithm?",
      "options": [
        {
          "id": "A",
          "text": "$J = \\sum_{k=1}^K \\sum_{\\mathbf{x}_i \\in C_k} \\|\\mathbf{x}_i - \\boldsymbol{\\mu}_k\\|_2^2$"
        },
        {
          "id": "B",
          "text": "$J = \\sum_{k=1}^K \\|\\boldsymbol{\\mu}_k - \\boldsymbol{\\mu}_{global}\\|_2$"
        },
        {
          "id": "C",
          "text": "$J = -\\sum_{i=1}^n \\log P(\\mathbf{x}_i)$"
        },
        {
          "id": "D",
          "text": "$J = \\sum_{k=1}^K \\sum_{j \\ne k} \\|\\boldsymbol{\\mu}_k - \\boldsymbol{\\mu}_j\\|_2^2$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "K-Means minimizes the within-cluster sum of squared Euclidean distances (WCSS) between each observation $\\mathbf{x}_i$ and its assigned cluster centroid $\\boldsymbol{\\mu}_k$.",
      "difficulty": "easy",
      "subtopic": "K-Means Objective"
    },
    {
      "id": "cml-l15-q03",
      "type": "single_choice",
      "question": "Why is Lloyd's algorithm for K-Means guaranteed to converge in a finite number of iterations?",
      "options": [
        {
          "id": "A",
          "text": "Because both the assignment step and the centroid update step monotonically decrease or maintain the non-negative objective $J$, and there are only a finite number ($K^n$) of possible cluster partitions"
        },
        {
          "id": "B",
          "text": "Because gradient descent has an adaptive learning rate"
        },
        {
          "id": "C",
          "text": "Because the objective function is strictly convex globally"
        },
        {
          "id": "D",
          "text": "Because the Hessian matrix is positive definite everywhere"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Lloyd's algorithm performs alternating coordinate descent on a non-negative energy surface. Since each step strictly decreases or keeps $J$ identical, and the number of partitions of $n$ points into $K$ sets is finite ($K^n$), the sequence must terminate in a local minimum.",
      "difficulty": "medium",
      "subtopic": "Lloyd's Algorithm Convergence"
    },
    {
      "id": "cml-l15-q04",
      "type": "single_choice",
      "question": "How does the K-Means++ initialization algorithm choose subsequent cluster centroids after picking the first centroid $\\mu_1$ uniformly at random?",
      "options": [
        {
          "id": "A",
          "text": "It selects points with probability proportional to the squared distance $D(\\mathbf{x})^2$ to the nearest already chosen centroid: $P(\\mathbf{x}_i) = \\frac{D(\\mathbf{x}_i)^2}{\\sum_j D(\\mathbf{x}_j)^2}$"
        },
        {
          "id": "B",
          "text": "It selects the points with the smallest distance to existing centroids"
        },
        {
          "id": "C",
          "text": "It uses the eigenvectors of the covariance matrix"
        },
        {
          "id": "D",
          "text": "It samples points uniformly at random with replacement"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "K-Means++ samples next centroids with probability proportional to $D(\\mathbf{x})^2$, spreading them far apart across distinct dense clusters and guaranteeing an $\\mathcal{O}(\\log K)$ expected approximation bound.",
      "difficulty": "medium",
      "subtopic": "K-Means++ Initialization"
    },
    {
      "id": "cml-l15-q05",
      "type": "single_choice",
      "question": "In Silhouette Analysis, what does a Silhouette Coefficient value of $s(i) \\approx -1$ indicate for a data point $\\mathbf{x}_i$?",
      "options": [
        {
          "id": "A",
          "text": "The point is well-clustered inside a dense cluster"
        },
        {
          "id": "B",
          "text": "The point lies on the exact decision boundary between two clusters"
        },
        {
          "id": "C",
          "text": "The point is closer to members of a neighboring cluster than to points in its own assigned cluster, indicating a severe misclustering"
        },
        {
          "id": "D",
          "text": "The cluster has zero variance"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "$s(i) = \\frac{b(i) - a(i)}{\\max(a(i), b(i))}$. If $a(i) \\gg b(i)$ (intra-cluster distance is much larger than distance to nearest neighbor cluster), $s(i) \\to -1$, proving the point was placed in the wrong cluster.",
      "difficulty": "medium",
      "subtopic": "Silhouette Analysis"
    },
    {
      "id": "cml-l15-q06",
      "type": "single_choice",
      "question": "Which of the following cluster geometries will K-Means completely FAIL to identify properly?",
      "options": [
        {
          "id": "A",
          "text": "Concentric rings and interleaving half-moon shapes"
        },
        {
          "id": "B",
          "text": "Spherical Gaussian blobs of equal radius"
        },
        {
          "id": "C",
          "text": "Compact linearly separable convex clusters"
        },
        {
          "id": "D",
          "text": "Disjoint isotropic normal distributions"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "K-Means induces linear Voronoi decision boundaries, producing strictly convex polyhedral cells. It cannot separate non-convex geometries like concentric rings or nested spirals.",
      "difficulty": "easy",
      "subtopic": "K-Means Geometric Limitations"
    },
    {
      "id": "cml-l15-q07",
      "type": "single_choice",
      "question": "In Hierarchical Agglomerative Clustering, which linkage criterion merges clusters by minimizing the increase in total within-cluster variance ($\\Delta \\text{WCSS}$)?",
      "options": [
        {
          "id": "A",
          "text": "Single Linkage"
        },
        {
          "id": "B",
          "text": "Complete Linkage"
        },
        {
          "id": "C",
          "text": "Average Linkage"
        },
        {
          "id": "D",
          "text": "Ward's Linkage"
        }
      ],
      "correctOptionIds": [
        "D"
      ],
      "explanation": "Ward's linkage seeks at each step to merge the pair of clusters that minimizes the increase in total within-cluster sum of squares: $\\Delta J = \\frac{|A||B|}{|A|+|B|}\\|\\boldsymbol{\\mu}_A - \\boldsymbol{\\mu}_B\\|^2$.",
      "difficulty": "medium",
      "subtopic": "Hierarchical Linkage Criteria"
    },
    {
      "id": "cml-l15-q08",
      "type": "single_choice",
      "question": "What is the notorious pathology known as the 'Chaining Effect' in Hierarchical Clustering, and which linkage criterion causes it?",
      "options": [
        {
          "id": "A",
          "text": "Complete linkage forcing clusters into chain-like elongated ellipses"
        },
        {
          "id": "B",
          "text": "Single linkage forming long string-like clusters because single intermediate noise points act as bridges between distinct clusters"
        },
        {
          "id": "C",
          "text": "Ward's linkage creating unbalanced single-sample leaves"
        },
        {
          "id": "D",
          "text": "DBSCAN failing to cluster circular points"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Because Single Linkage evaluates minimum distance $\\min \\|\\mathbf{a} - \\mathbf{b}\\|$, a few isolated noise points between two dense clusters will bridge them together into one long spurious cluster.",
      "difficulty": "medium",
      "subtopic": "Hierarchical Linkage Criteria"
    },
    {
      "id": "cml-l15-q09",
      "type": "single_choice",
      "question": "In the DBSCAN algorithm with parameters $\\epsilon$ and $\\text{MinPts} = 4$, when is a point $\\mathbf{p}$ classified as a Core Point?",
      "options": [
        {
          "id": "A",
          "text": "When the $\\epsilon$-neighborhood around $\\mathbf{p}$ contains at least 4 points (including $\\mathbf{p}$ itself)"
        },
        {
          "id": "B",
          "text": "When $\\mathbf{p}$ has the minimum distance to the origin"
        },
        {
          "id": "C",
          "text": "When $\\mathbf{p}$ is connected to at least 4 other Core points"
        },
        {
          "id": "D",
          "text": "When its Silhouette score is greater than 0.5"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "A point is a Core point in DBSCAN if its $\\epsilon$-neighborhood contains at least $\\text{MinPts}$ points: $|N_\\epsilon(\\mathbf{p})| \\ge \\text{MinPts}$.",
      "difficulty": "easy",
      "subtopic": "DBSCAN Point Classification"
    },
    {
      "id": "cml-l15-q10",
      "type": "single_choice",
      "question": "How does DBSCAN classify a point that has fewer than $\\text{MinPts}$ neighbors within radius $\\epsilon$, but lies within the $\\epsilon$-neighborhood of a Core point?",
      "options": [
        {
          "id": "A",
          "text": "Noise / Outlier point (label -1)"
        },
        {
          "id": "B",
          "text": "Border Point"
        },
        {
          "id": "C",
          "text": "Centroid Point"
        },
        {
          "id": "D",
          "text": "Medoid Point"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "A Border point has $|N_\\epsilon(\\mathbf{b})| < \\text{MinPts}$, but falls within radius $\\epsilon$ of an existing Core point. It is assigned to the cluster of that Core point.",
      "difficulty": "easy",
      "subtopic": "DBSCAN Point Classification"
    },
    {
      "id": "cml-l15-q11",
      "type": "single_choice",
      "question": "What is the Distance Concentration phenomenon caused by the Curse of Dimensionality in high-dimensional feature spaces ($d \\to \\infty$)?",
      "options": [
        {
          "id": "A",
          "text": "All points collapse to the origin"
        },
        {
          "id": "B",
          "text": "The relative contrast between the distance to the nearest neighbor and the furthest neighbor vanishes: $\\lim_{d \\to \\infty} \\frac{d_{\\max} - d_{\\min}}{d_{\\min}} \\to 0$"
        },
        {
          "id": "C",
          "text": "All eigenvalues become equal to zero"
        },
        {
          "id": "D",
          "text": "The covariance matrix becomes identity"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In high dimensions, the volume of a hypersphere concentrates almost entirely in a thin outer shell. Every point becomes virtually equidistant from all other points, breaking distance-based metrics.",
      "difficulty": "hard",
      "subtopic": "Curse of Dimensionality"
    },
    {
      "id": "cml-l15-q12",
      "type": "single_choice",
      "question": "In Principal Component Analysis (PCA), what mathematical optimization problem defines the first Principal Component direction $\\mathbf{v}_1$ for zero-centered data with covariance matrix $\\mathbf{\\Sigma}$?",
      "options": [
        {
          "id": "A",
          "text": "$\\max_{\\mathbf{v}_1} \\mathbf{v}_1^T \\mathbf{\\Sigma} \\mathbf{v}_1 \\quad \\text{subject to} \\quad \\|\\mathbf{v}_1\\|_2 = 1$"
        },
        {
          "id": "B",
          "text": "$\\min_{\\mathbf{v}_1} \\|\\mathbf{v}_1\\|_2 \\quad \\text{subject to} \\quad \\mathbf{v}_1^T \\mathbf{\\Sigma} \\mathbf{v}_1 = 0$"
        },
        {
          "id": "C",
          "text": "$\\max_{\\mathbf{v}_1} \\text{Tr}(\\mathbf{\\Sigma}) \\mathbf{v}_1$"
        },
        {
          "id": "D",
          "text": "$\\min_{\\mathbf{v}_1} \\det(\\mathbf{\\Sigma} - \\mathbf{v}_1)$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "PCA seeks the unit vector $\\mathbf{v}_1$ that maximizes the variance of the projected data $\\text{Var}(\\mathbf{X}_c \\mathbf{v}_1) = \\mathbf{v}_1^T \\mathbf{\\Sigma} \\mathbf{v}_1$, constrained by $\\mathbf{v}_1^T \\mathbf{v}_1 = 1$.",
      "difficulty": "medium",
      "subtopic": "PCA Mathematical Derivation"
    },
    {
      "id": "cml-l15-q13",
      "type": "single_choice",
      "question": "Solving the constrained optimization $\\max_{\\mathbf{v}} \\mathbf{v}^T \\mathbf{\\Sigma} \\mathbf{v}$ s.t. $\\mathbf{v}^T \\mathbf{v} = 1$ via Lagrange multipliers leads to which fundamental linear algebra equation?",
      "options": [
        {
          "id": "A",
          "text": "$\\mathbf{\\Sigma} \\mathbf{v} = \\lambda \\mathbf{v}$ (The Eigendecomposition of the Covariance Matrix)"
        },
        {
          "id": "B",
          "text": "$\\mathbf{\\Sigma}^{-1} \\mathbf{v} = \\mathbf{0}$"
        },
        {
          "id": "C",
          "text": "$\\mathbf{X}^T \\mathbf{X} \\mathbf{v} = \\mathbf{y}$"
        },
        {
          "id": "D",
          "text": "$\\nabla f(\\mathbf{v}) = \\mathbf{w}^T \\mathbf{x}$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Differentiating Lagrangian $\\mathcal{L} = \\mathbf{v}^T \\mathbf{\\Sigma} \\mathbf{v} - \\lambda(\\mathbf{v}^T \\mathbf{v} - 1)$ yields $2\\mathbf{\\Sigma} \\mathbf{v} - 2\\lambda \\mathbf{v} = \\mathbf{0} \\implies \\mathbf{\\Sigma}\\mathbf{v} = \\lambda \\mathbf{v}$. The principal directions are the eigenvectors of $\\mathbf{\\Sigma}$.",
      "difficulty": "medium",
      "subtopic": "PCA Mathematical Derivation"
    },
    {
      "id": "cml-l15-q14",
      "type": "single_choice",
      "question": "Given the Singular Value Decomposition (SVD) of centered data $\\mathbf{X}_c = \\mathbf{U} \\mathbf{S} \\mathbf{V}^T$, what is the exact relationship between the singular values $s_j$ and the eigenvalues $\\lambda_j$ of the sample covariance matrix $\\mathbf{\\Sigma} = \\frac{1}{n-1}\\mathbf{X}_c^T \\mathbf{X}_c$?",
      "options": [
        {
          "id": "A",
          "text": "$\\lambda_j = \\frac{s_j^2}{n - 1}$"
        },
        {
          "id": "B",
          "text": "$\\lambda_j = s_j \\cdot (n - 1)$"
        },
        {
          "id": "C",
          "text": "$\\lambda_j = \\sqrt{s_j}$"
        },
        {
          "id": "D",
          "text": "$\\lambda_j = s_j^2$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "$\\mathbf{\\Sigma} = \\frac{1}{n-1} \\mathbf{V} \\mathbf{S}^T \\mathbf{U}^T \\mathbf{U} \\mathbf{S} \\mathbf{V}^T = \\mathbf{V} \\left(\\frac{\\mathbf{S}^2}{n-1}\\right) \\mathbf{V}^T$. Therefore, the eigenvalues equal $\\lambda_j = \\frac{s_j^2}{n-1}$.",
      "difficulty": "hard",
      "subtopic": "PCA and SVD Connection"
    },
    {
      "id": "cml-l15-q15",
      "type": "single_choice",
      "question": "How is the Explained Variance Ratio (EVR) of the $k$-th Principal Component defined?",
      "options": [
        {
          "id": "A",
          "text": "$\\text{EVR}_k = \\frac{\\lambda_k}{\\sum_{j=1}^d \\lambda_j}$"
        },
        {
          "id": "B",
          "text": "$\\text{EVR}_k = \\frac{\\lambda_k}{k}$"
        },
        {
          "id": "C",
          "text": "$\\text{EVR}_k = \\sqrt{\\lambda_k}$"
        },
        {
          "id": "D",
          "text": "$\\text{EVR}_k = 1 - \\lambda_k$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The Explained Variance Ratio is the eigenvalue of the $k$-th component divided by the sum of all eigenvalues (total variance of the dataset).",
      "difficulty": "easy",
      "subtopic": "Explained Variance Ratio"
    },
    {
      "id": "cml-l15-q16",
      "type": "multi_choice",
      "question": "Why is feature scaling (e.g., `StandardScaler`) mandatory before running PCA? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "PCA seeks directions that maximize variance; an unscaled feature with large numeric values will exhibit artificially massive variance and dominate the top principal component."
        },
        {
          "id": "B",
          "text": "Features measured in different units (e.g. Income in dollars vs Age in years) cannot be meaningfully compared by raw variance."
        },
        {
          "id": "C",
          "text": "SVD algorithms crash if features have different standard deviations."
        },
        {
          "id": "D",
          "text": "Standardizing ensures that each feature contributes equally on an unweighted baseline before orthogonal variance maximization."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "PCA is extremely sensitive to relative variance. Without standardization, high-magnitude features dominate the principal axes, even if lower-magnitude features contain vital signals. SVD algorithms do not crash on unscaled data.",
      "difficulty": "medium",
      "subtopic": "PCA Preprocessing"
    },
    {
      "id": "cml-l15-q17",
      "type": "multi_choice",
      "question": "Which of the following are distinct advantages of DBSCAN over K-Means? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The number of clusters $K$ does not need to be specified in advance."
        },
        {
          "id": "B",
          "text": "It can discover clusters of arbitrary, non-convex shapes (such as concentric rings or spirals)."
        },
        {
          "id": "C",
          "text": "It has an explicit notion of noise and is robust to outliers."
        },
        {
          "id": "D",
          "text": "It performs exceptionally well when clusters have drastically different local densities."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are key strengths of DBSCAN. D is a known weakness: because $\\epsilon$ and $\\text{MinPts}$ are global constants, DBSCAN struggles when clusters have varying densities (HDBSCAN addresses this).",
      "difficulty": "medium",
      "subtopic": "DBSCAN Advantages"
    },
    {
      "id": "cml-l15-q18",
      "type": "multi_choice",
      "question": "What is the difference between Feature Selection and Feature Extraction (like PCA)? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Feature Selection preserves the original feature identities by selecting a subset of existing columns (e.g., SelectKBest, Lasso)."
        },
        {
          "id": "B",
          "text": "Feature Extraction constructs new, synthetic composite features as combinations of the original features (e.g., PCA components $\\mathbf{z} = \\mathbf{X}\\mathbf{V}$)."
        },
        {
          "id": "C",
          "text": "Feature Extraction preserves 100% of original domain interpretability."
        },
        {
          "id": "D",
          "text": "Feature Selection discards discarded features completely, whereas PCA blends variance across all features."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "D"
      ],
      "explanation": "Selection chooses existing columns, keeping interpretability. Extraction creates linear combinations of all features, discarding individual column interpretability.",
      "difficulty": "easy",
      "subtopic": "Selection vs Extraction"
    },
    {
      "id": "cml-l15-q19",
      "type": "single_choice",
      "question": "How should PCA be applied in a machine learning pipeline to strictly prevent Information Leakage?",
      "options": [
        {
          "id": "A",
          "text": "Fit PCA on the entire dataset before splitting into train and test sets"
        },
        {
          "id": "B",
          "text": "Fit PCA exclusively on the training set `X_train`, and apply `transform` on both `X_train` and `X_test` using the fitted eigenvectors and mean vector"
        },
        {
          "id": "C",
          "text": "Fit separate PCA models on `X_train` and `X_test` independently"
        },
        {
          "id": "D",
          "text": "Fit PCA on the target variable $y$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "To prevent leakage, the test set must remain completely unseen. Fitting PCA on the entire dataset leaks test set variance and means into the projection subspace.",
      "difficulty": "medium",
      "subtopic": "PCA Pipeline Leakage"
    },
    {
      "id": "cml-l15-q20",
      "type": "multi_choice",
      "question": "Which of the following statements regarding Non-Linear Dimensionality Reduction are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "PCA is a linear transformation and cannot unroll complex non-linear manifolds like the 3D Swiss Roll."
        },
        {
          "id": "B",
          "text": "t-SNE (t-Distributed Stochastic Neighbor Embedding) minimizes the Kullback-Leibler (KL) divergence between high-dimensional and low-dimensional pairwise joint probabilities."
        },
        {
          "id": "C",
          "text": "t-SNE and UMAP are primarily visualization techniques and do not yield an easily reusable parametric projection mapping for new test instances without approximations."
        },
        {
          "id": "D",
          "text": "PCA guarantees preservation of local neighborhood topology better than t-SNE."
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "PCA is strictly linear; t-SNE minimizes KL divergence; t-SNE/UMAP are non-parametric and excel at local neighborhood visualization on training data. PCA focuses on global variance, not local manifolds.",
      "difficulty": "hard",
      "subtopic": "Non-Linear Manifold Learning"
    }
  ]
}
