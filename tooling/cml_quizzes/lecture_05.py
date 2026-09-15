QUIZ_L05 = {
  "topicId": "lecture-05",
  "lectureNumber": 5,
  "title": "Optimization: Gradient Descent & Modern Variants",
  "description": "25 questions covering Mean Squared Error convexity, vectorized gradient derivation, learning rate dynamics, Batch vs SGD vs Mini-Batch, feature scaling impact, and convergence criteria.",
  "estimatedMinutes": 35,
  "questions": [
    {
      "id": "cml-l05-q01",
      "type": "single_choice",
      "question": "For a linear regression model with $m$ samples and design matrix $X \\in \\mathbb{R}^{m \\times (p+1)}$, what is the exact vectorized formula for the gradient $\\nabla_{\\theta} J(\\theta)$ of the MSE loss $J(\\theta) = \\frac{1}{2m} \\|X\\theta - y\\|^2$?",
      "options": [
        {
          "id": "A",
          "text": "$\\nabla_{\\theta} J(\\theta) = \\frac{1}{m} X (X\\theta - y)$"
        },
        {
          "id": "B",
          "text": "$\\nabla_{\\theta} J(\\theta) = \\frac{1}{m} X^T (X\\theta - y)$"
        },
        {
          "id": "C",
          "text": "$\\nabla_{\\theta} J(\\theta) = \\frac{1}{2m} (X\\theta - y)^T X$"
        },
        {
          "id": "D",
          "text": "$\\nabla_{\\theta} J(\\theta) = \\frac{1}{m} (X^T X \\theta + y)$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Expanding the squared norm gives $J(\\theta) = \\frac{1}{2m}(\\theta^TX^TX\\theta - 2y^TX\\theta + y^Ty)$. Differentiating with respect to $\\theta$ yields $\\nabla_{\\theta} J(\\theta) = \\frac{1}{m} (X^TX\\theta - X^Ty) = \\frac{1}{m} X^T(X\\theta - y)$.",
      "difficulty": "medium",
      "subtopic": "Vectorized Gradient"
    },
    {
      "id": "cml-l05-q02",
      "type": "single_choice",
      "question": "Why is the factor $\\frac{1}{2}$ conventionally included in the definition of the Mean Squared Error cost function $J(\\theta) = \\frac{1}{2m} \\sum_{i=1}^m (h_\\theta(x^{(i)}) - y^{(i)})^2$?",
      "options": [
        {
          "id": "A",
          "text": "To ensure the cost function evaluates strictly between 0 and 1"
        },
        {
          "id": "B",
          "text": "To cancel out the factor of 2 produced by applying the chain rule when taking the derivative"
        },
        {
          "id": "C",
          "text": "To double the effective learning rate during parameter updates"
        },
        {
          "id": "D",
          "text": "To make the cost function strictly convex"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The derivative of $(u)^2$ is $2u$. Multiplying by $\\frac{1}{2}$ algebraically cancels this 2 ($\\\\frac{d}{du}[\\frac{1}{2}u^2] = u$), leaving clean gradient expressions without stray constants.",
      "difficulty": "easy",
      "subtopic": "Cost Function Conventions"
    },
    {
      "id": "cml-l05-q03",
      "type": "single_choice",
      "question": "What is the mathematical definition of the Hessian matrix $H$ for the linear regression MSE cost function $J(\\theta) = \\frac{1}{2m} \\|X\\theta - y\\|^2$, and what does it imply about local minima?",
      "options": [
        {
          "id": "A",
          "text": "$H = \\frac{1}{m} X^TX$; since $X^TX$ is positive semi-definite, $J(\\theta)$ is convex and any local minimum is a global minimum"
        },
        {
          "id": "B",
          "text": "$H = \\frac{1}{m} X$; since it is rectangular, multiple suboptimal local minima exist"
        },
        {
          "id": "C",
          "text": "$H = -\\frac{1}{m} X^TX$; because it is negative definite, gradient descent finds maximum error"
        },
        {
          "id": "D",
          "text": "$H = \\mathbf{0}$; linear regression has no curvature"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "The second derivative of $J(\\theta)$ is $H = \\nabla^2 J(\\theta) = \\frac{1}{m} X^TX$. For any non-zero vector $z$, $z^T(X^TX)z = (Xz)^T(Xz) = \\|Xz\\|^2 \\ge 0$. Since $H \\succeq 0$ (positive semi-definite), the MSE surface is globally convex, guaranteeing every stationary point is a global minimum.",
      "difficulty": "hard",
      "subtopic": "Convexity & Hessian"
    },
    {
      "id": "cml-l05-q04",
      "type": "single_choice",
      "question": "During training of a linear regression model with Gradient Descent, the loss $J(\\theta)$ oscillates violently and increases exponentially toward infinity across iterations. What is the root cause?",
      "options": [
        {
          "id": "A",
          "text": "The learning rate $\\alpha$ is set too small"
        },
        {
          "id": "B",
          "text": "The learning rate $\\alpha$ is too large, causing the updates to overshoot the valley and diverge"
        },
        {
          "id": "C",
          "text": "The design matrix contains an intercept column of all ones"
        },
        {
          "id": "D",
          "text": "The training set has too few samples ($m < p$)"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "When $\\alpha > \\frac{2}{\\lambda_{\\max}(H)}$, gradient descent steps overshoot the valley bottom farther on each step than the previous iteration, causing exponential divergence toward infinity.",
      "difficulty": "easy",
      "subtopic": "Learning Rate Dynamics"
    },
    {
      "id": "cml-l05-q05",
      "type": "single_choice",
      "question": "How does unscaled data (e.g., Feature 1 ranging in $[0, 1]$ and Feature 2 ranging in $[0, 1{,}000{,}000]$) affect the geometry of the MSE loss surface and gradient descent updates?",
      "options": [
        {
          "id": "A",
          "text": "It converts the convex surface into a non-convex surface with multiple saddle points"
        },
        {
          "id": "B",
          "text": "It creates highly elongated elliptical contours where gradients point almost perpendicularly to the minimum, causing inefficient zigzag oscillations"
        },
        {
          "id": "C",
          "text": "It forces the gradient to evaluate to zero immediately at the initialization point"
        },
        {
          "id": "D",
          "text": "It eliminates the need for computing the learning rate $\\alpha$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Unscaled features create high condition numbers in $X^TX$, turning circular spherical loss contours into severe ellipses. The gradient vector is orthogonal to contour lines, pointing sideways rather than directly at the minimum, forcing slow zigzag convergence.",
      "difficulty": "medium",
      "subtopic": "Feature Scaling Impact"
    },
    {
      "id": "cml-l05-q06",
      "type": "single_choice",
      "question": "In Batch Gradient Descent (BGD), how many training samples are evaluated to perform a SINGLE weight update step $\\theta := \\theta - \\alpha \\nabla J$?",
      "options": [
        {
          "id": "A",
          "text": "Exactly 1 randomly chosen sample"
        },
        {
          "id": "B",
          "text": "A small mini-batch of typically 32 to 128 samples"
        },
        {
          "id": "C",
          "text": "All $m$ samples in the entire training dataset"
        },
        {
          "id": "D",
          "text": "Only the samples that have non-zero residual error"
        }
      ],
      "correctOptionIds": [
        "C"
      ],
      "explanation": "Batch Gradient Descent computes the exact gradient by summing across all $m$ training instances for every single parameter update step.",
      "difficulty": "easy",
      "subtopic": "Batch Gradient Descent"
    },
    {
      "id": "cml-l05-q07",
      "type": "single_choice",
      "question": "What is the primary computational advantage of Stochastic Gradient Descent (SGD) over Batch Gradient Descent (BGD) on massive datasets with billions of samples?",
      "options": [
        {
          "id": "A",
          "text": "SGD guarantees exact convergence to the true global minimum with a fixed learning rate"
        },
        {
          "id": "B",
          "text": "SGD updates weights immediately after inspecting each individual sample, enabling rapid online learning and fitting into limited RAM"
        },
        {
          "id": "C",
          "text": "SGD strictly prevents overfitting without requiring regularization"
        },
        {
          "id": "D",
          "text": "SGD requires computing the matrix inverse $(X^TX)^{-1}$ only once"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "SGD updates parameters after every single sample ($O(1)$ cost per update instead of $O(m)$), enabling immediate progress, memory-mapped streaming, and very fast initial convergence on huge datasets.",
      "difficulty": "easy",
      "subtopic": "Stochastic Gradient Descent"
    },
    {
      "id": "cml-l05-q08",
      "type": "single_choice",
      "question": "Why does pure Stochastic Gradient Descent (SGD) with a constant learning rate $\\alpha$ fail to settle precisely at the exact global minimum $\\theta^*$?",
      "options": [
        {
          "id": "A",
          "text": "Because the gradient at an individual sample does not vanish at $\\theta^*$, causing continuous noisy fluctuations around the minimum"
        },
        {
          "id": "B",
          "text": "Because the Hessian matrix becomes negative definite near $\\theta^*$"
        },
        {
          "id": "C",
          "text": "Because the cost function becomes non-convex within an $\\epsilon$-ball of $\\theta^*$"
        },
        {
          "id": "D",
          "text": "Because single-sample gradients always point in the direction opposite to the true gradient"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "At the true minimum $\\theta^*$, the sum of all gradients is zero, but individual sample gradients $g_i(\\theta^*) = (x^{(i)}\\theta^* - y^{(i)})x^{(i)} \\neq 0$. Therefore, SGD continues to bounce around the minimum unless $\\alpha$ is decayed to 0.",
      "difficulty": "medium",
      "subtopic": "SGD Noise & Fluctuation"
    },
    {
      "id": "cml-l05-q09",
      "type": "single_choice",
      "question": "What is the standard condition on a learning rate schedule $\\alpha_t$ (known as the Robbins-Monro conditions) to guarantee almost sure convergence of SGD to the minimum?",
      "options": [
        {
          "id": "A",
          "text": "$\\sum_{t=1}^\\infty \\alpha_t < \\infty$ and $\\sum_{t=1}^\\infty \\alpha_t^2 < \\infty$"
        },
        {
          "id": "B",
          "text": "$\\sum_{t=1}^\\infty \\alpha_t = \\infty$ and $\\sum_{t=1}^\\infty \\alpha_t^2 < \\infty$"
        },
        {
          "id": "C",
          "text": "$\\alpha_t = \\alpha_0$ for all $t$"
        },
        {
          "id": "D",
          "text": "$\\lim_{t \\to \\infty} \\alpha_t = 1$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "The Robbins-Monro conditions require $\\sum \\alpha_t = \\infty$ (sufficient learning capacity to reach arbitrarily distant minima from any initialization) and $\\sum \\alpha_t^2 < \\infty$ (decay fast enough to suppress stochastic variance and settle at the minimum).",
      "difficulty": "hard",
      "subtopic": "Robbins-Monro Conditions"
    },
    {
      "id": "cml-l05-q10",
      "type": "single_choice",
      "question": "In Mini-Batch Gradient Descent, why is the mini-batch size $B$ commonly chosen as a power of 2 (e.g., 32, 64, 128, 256)?",
      "options": [
        {
          "id": "A",
          "text": "Powers of 2 guarantee the Hessian matrix is invertible"
        },
        {
          "id": "B",
          "text": "To optimize memory alignment and parallel execution efficiency on modern CPU cache lines and GPU SIMD warps"
        },
        {
          "id": "C",
          "text": "Because odd numbers cause mathematical instability in the gradient formula"
        },
        {
          "id": "D",
          "text": "To prevent the learning rate from decaying to zero"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Hardware memory architectures (cache hierarchies, SIMD vector registers, GPU thread warps of 32 threads) are designed around binary powers, maximizing parallel matrix-matrix multiplication throughput.",
      "difficulty": "easy",
      "subtopic": "Mini-Batch Hardware Alignment"
    },
    {
      "id": "cml-l05-q11",
      "type": "single_choice",
      "question": "If you plot the Cost $J(\\theta)$ against the number of iterations for Batch Gradient Descent, what shape should the curve exhibit if the implementation and learning rate are correct?",
      "options": [
        {
          "id": "A",
          "text": "A jagged saw-tooth curve bouncing up and down"
        },
        {
          "id": "B",
          "text": "A strictly monotonic decrease asymptotically flattening out toward a minimum"
        },
        {
          "id": "C",
          "text": "A strictly increasing linear line"
        },
        {
          "id": "D",
          "text": "A parabolic curve dipping and then rising back up"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In Batch Gradient Descent, every step computes the true full gradient. If $\\alpha$ is sufficiently small, $J(\\theta)$ is guaranteed to decrease monotonically at every single iteration until convergence.",
      "difficulty": "easy",
      "subtopic": "Loss Curve Diagnostics"
    },
    {
      "id": "cml-l05-q12",
      "type": "single_choice",
      "question": "What is the role of Polyak Momentum in gradient descent optimization ($v_t := \\gamma v_{t-1} + \\alpha \\nabla J(\\theta_t)$, $\\theta_{t+1} := \\theta_t - v_t$)?",
      "options": [
        {
          "id": "A",
          "text": "It dampens oscillations in high-curvature directions and accelerates progress along flat ravines"
        },
        {
          "id": "B",
          "text": "It guarantees that the gradient never evaluates to zero"
        },
        {
          "id": "C",
          "text": "It computes the analytical matrix inverse $(X^TX)^{-1}$ incrementally"
        },
        {
          "id": "D",
          "text": "It automatically eliminates the need for feature scaling"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "Momentum accumulates an exponentially decaying moving average of past gradients ($v_t$), canceling out oscillating orthogonal components while reinforcing consistent downhill trajectories.",
      "difficulty": "medium",
      "subtopic": "Momentum Optimization"
    },
    {
      "id": "cml-l05-q13",
      "type": "single_choice",
      "question": "What is a standard early stopping convergence criterion commonly employed in iterative Gradient Descent algorithms?",
      "options": [
        {
          "id": "A",
          "text": "Stop when the norm of the gradient vector $\\|\\nabla J(\\theta)\\|_2 < \\epsilon$ for a small threshold $\\epsilon$"
        },
        {
          "id": "B",
          "text": "Stop when all parameters $\\theta_j$ become strictly equal to each other"
        },
        {
          "id": "C",
          "text": "Stop when the learning rate $\\alpha$ reaches 1.0"
        },
        {
          "id": "D",
          "text": "Stop when the condition number of the design matrix exceeds $10^5$"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "At a local or global minimum, the gradient $\\nabla J(\\theta^*) = \\mathbf{0}$. Therefore, checking whether $\\|\\nabla J(\\theta)\\| < \\epsilon$ (or $|J_t - J_{t-1}| < \\tau$) is the standard stopping condition.",
      "difficulty": "easy",
      "subtopic": "Convergence Criteria"
    },
    {
      "id": "cml-l05-q14",
      "type": "single_choice",
      "question": "Suppose an algorithm uses the Lipschitz continuous gradient condition with constant $L = \\lambda_{\\max}(H)$. What is the theoretical upper bound on learning rate $\\alpha$ to ensure Batch Gradient Descent does not diverge on a quadratic loss?",
      "options": [
        {
          "id": "A",
          "text": "$\\alpha < \\frac{1}{L}$"
        },
        {
          "id": "B",
          "text": "$\\alpha < \\frac{2}{L}$"
        },
        {
          "id": "C",
          "text": "$\\alpha > 2L$"
        },
        {
          "id": "D",
          "text": "$\\alpha = \\infty$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "In convex quadratic optimization, the step contraction factor is $|1 - \\alpha \\lambda_i| < 1$. This yields $-1 < 1 - \\alpha \\lambda_{\\max} < 1$, which strictly requires $\\alpha < \\frac{2}{\\lambda_{\\max}} = \\frac{2}{L}$. For guaranteed monotonic descent, $\\alpha \\le \\frac{1}{L}$.",
      "difficulty": "hard",
      "subtopic": "Lipschitz Smoothness & Step Size"
    },
    {
      "id": "cml-l05-q15",
      "type": "single_choice",
      "question": "In Scikit-Learn, which class implements linear regression fitted via iterative Stochastic Gradient Descent instead of the analytical closed-form Normal Equation?",
      "options": [
        {
          "id": "A",
          "text": "`sklearn.linear_model.LinearRegression`"
        },
        {
          "id": "B",
          "text": "`sklearn.linear_model.SGDRegressor`"
        },
        {
          "id": "C",
          "text": "`sklearn.cluster.KMeans`"
        },
        {
          "id": "D",
          "text": "`sklearn.decomposition.PCA`"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "`SGDRegressor` implements first-order stochastic gradient descent with customizable loss (squared error, Huber, epsilon-insensitive) and penalties (L1, L2, ElasticNet). `LinearRegression` uses LAPACK SVD.",
      "difficulty": "easy",
      "subtopic": "Scikit-Learn SGD"
    },
    {
      "id": "cml-l05-q16",
      "type": "single_choice",
      "question": "Why is zero-initialization (setting $\\theta = \\mathbf{0}$) perfectly acceptable for Linear Regression with Gradient Descent, whereas it causes symmetry-breaking issues in deep neural networks?",
      "options": [
        {
          "id": "A",
          "text": "Because Linear Regression has no hidden layers with symmetric neurons; the MSE cost is globally convex, so gradient updates for each feature depend directly on distinct input values $x_j$"
        },
        {
          "id": "B",
          "text": "Because Linear Regression has no bias/intercept parameter"
        },
        {
          "id": "C",
          "text": "Because the learning rate in Linear Regression dynamically adjusts to zero inputs"
        },
        {
          "id": "D",
          "text": "Because the Normal Equation prevents zero-initialization from being used"
        }
      ],
      "correctOptionIds": [
        "A"
      ],
      "explanation": "In linear models, each parameter $\\theta_j$ updates as $-\\alpha \\frac{1}{m}\\sum e^{(i)} x_j^{(i)}$, which depends on feature values $x_j^{(i)}$, breaking symmetry naturally without hidden layers.",
      "difficulty": "medium",
      "subtopic": "Parameter Initialization"
    },
    {
      "id": "cml-l05-q17",
      "type": "single_choice",
      "question": "What is 'gradient clipping', and why is it occasionally introduced in gradient-based optimization pipelines?",
      "options": [
        {
          "id": "A",
          "text": "Setting negative weights to zero to enforce non-negative coefficients"
        },
        {
          "id": "B",
          "text": "Rescaling or capping the norm/value of the gradient if it exceeds a predetermined threshold to prevent exploding gradients"
        },
        {
          "id": "C",
          "text": "Dropping the gradients of uninformative features after each epoch"
        },
        {
          "id": "D",
          "text": "Clipping the target variable $y$ to lie within $[0, 1]$"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "Gradient clipping caps the gradient magnitude (either element-wise or by Euclidean norm: $g := g \\cdot \\min(1, c / \\|g\\|)$) to avoid numeric overflow and exploding updates.",
      "difficulty": "medium",
      "subtopic": "Optimization Tricks"
    },
    {
      "id": "cml-l05-q18",
      "type": "single_choice",
      "question": "What happens if the learning rate $\\alpha$ is chosen to be extremely small (e.g., $\\alpha = 10^{-12}$)?",
      "options": [
        {
          "id": "A",
          "text": "The model diverges instantly toward infinity"
        },
        {
          "id": "B",
          "text": "The algorithm takes infinitesimally tiny steps, requiring millions of epochs to reach the minimum and possibly stopping prematurely due to numerical underflow"
        },
        {
          "id": "C",
          "text": "The loss function changes from convex to concave"
        },
        {
          "id": "D",
          "text": "The model perfectly memorizes all training noise and overfits"
        }
      ],
      "correctOptionIds": [
        "B"
      ],
      "explanation": "An overly small learning rate guarantees safe convergence theoretically, but practically crawls at a glacial pace, taking prohibitively long and risking premature termination by max-epochs or underflow.",
      "difficulty": "easy",
      "subtopic": "Learning Rate Extremes"
    },
    {
      "id": "cml-l05-q19",
      "type": "multi_choice",
      "question": "Which of the following statements comparing Batch Gradient Descent (BGD), Stochastic Gradient Descent (SGD), and Mini-Batch Gradient Descent (MBGD) are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "BGD produces a completely deterministic, smooth, monotonically decreasing loss trajectory per iteration"
        },
        {
          "id": "B",
          "text": "SGD trajectories are noisy and stochastic, with loss fluctuating up and down between steps"
        },
        {
          "id": "C",
          "text": "MBGD combines the computational efficiency of vectorized matrix multiplication with the variance-reduction benefits of small batches"
        },
        {
          "id": "D",
          "text": "BGD is computationally superior to SGD when training on 10 billion streaming samples"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C accurately characterize the three paradigms. D is FALSE: evaluating 10 billion samples for a single parameter update makes BGD completely infeasible for large-scale streaming data.",
      "difficulty": "medium",
      "subtopic": "Comparison of GD Variants"
    },
    {
      "id": "cml-l05-q20",
      "type": "multi_choice",
      "question": "Which of the following techniques can help accelerate or stabilize gradient descent convergence when the loss surface is poorly conditioned? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Feature standardization (Z-score scaling: $\\frac{x - \\mu}{\\sigma}$)"
        },
        {
          "id": "B",
          "text": "Using momentum to dampen oscillations in steep dimensions"
        },
        {
          "id": "C",
          "text": "Employing an adaptive learning rate schedule (such as step decay or cosine annealing)"
        },
        {
          "id": "D",
          "text": "Multiplying the feature values by arbitrary random numbers at each epoch"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A rounds out the contours; B accelerates through flat areas while suppressing oscillation; C refines step sizes over time. D injects arbitrary destructive noise into features.",
      "difficulty": "easy",
      "subtopic": "Stabilization Techniques"
    },
    {
      "id": "cml-l05-q21",
      "type": "multi_choice",
      "question": "Which of the following are mathematically valid reasons why the Mean Squared Error (MSE) surface of linear regression is convex? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "The affine function $f(\\theta) = X\\theta - y$ preserves convexity under the composition with the convex squared L2 norm $\\|u\\|^2$"
        },
        {
          "id": "B",
          "text": "The Hessian matrix $\\nabla^2 J(\\theta) = \\frac{1}{m} X^TX$ is positive semi-definite for any real matrix $X$"
        },
        {
          "id": "C",
          "text": "The second directional derivative $v^T H v = \\frac{1}{m} \\|Xv\\|^2 \\ge 0$ for all vectors $v$"
        },
        {
          "id": "D",
          "text": "Because all features in $X$ are bounded between $-1$ and $+1$"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are mathematically rigorous justifications for convexity. D has nothing to do with convexity; convexity holds regardless of feature values or bounds.",
      "difficulty": "hard",
      "subtopic": "Mathematical Convexity"
    },
    {
      "id": "cml-l05-q22",
      "type": "multi_choice",
      "question": "When debugging a custom Gradient Descent implementation in Python/NumPy, which of the following signs indicate that the learning rate $\\alpha$ is likely too high? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Cost values return `np.nan` or `np.inf` during iteration"
        },
        {
          "id": "B",
          "text": "The cost curve increases after the initial iterations"
        },
        {
          "id": "C",
          "text": "Parameter values explode in magnitude exponentially toward machine limits"
        },
        {
          "id": "D",
          "text": "The cost function decreases slowly and smoothly over 100,000 epochs without converging"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are symptoms of divergence due to an oversized learning rate. D is the signature symptom of an overly small learning rate.",
      "difficulty": "easy",
      "subtopic": "Debugging Gradient Descent"
    },
    {
      "id": "cml-l05-q23",
      "type": "multi_choice",
      "question": "Which of the following statements about learning rate schedules are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Time-based decay updates $\\alpha_t = \\frac{\\alpha_0}{1 + k t}$, gradually shrinking steps as training progresses"
        },
        {
          "id": "B",
          "text": "Step decay reduces $\\alpha$ by a multiplicative factor (e.g. 0.5 or 0.1) every fixed number of epochs"
        },
        {
          "id": "C",
          "text": "Decaying $\\alpha$ helps Stochastic Gradient Descent settle into a compact neighborhood around the true minimum instead of wandering indefinitely"
        },
        {
          "id": "D",
          "text": "Increasing $\\alpha$ exponentially as training progresses is necessary to ensure convergence"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C describe standard decay schedules and their purpose. D is false; increasing $\\alpha$ later in training causes immediate divergence.",
      "difficulty": "medium",
      "subtopic": "Learning Schedules"
    },
    {
      "id": "cml-l05-q24",
      "type": "multi_choice",
      "question": "In comparing the Normal Equation $\\theta = (X^TX)^{-1}X^Ty$ with Gradient Descent for linear regression, which statements are TRUE? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "Normal Equation does not require choosing a learning rate $\\alpha$ or iterating over epochs"
        },
        {
          "id": "B",
          "text": "Normal Equation becomes prohibitively slow when the number of features $p > 100{,}000$ due to $O(p^3)$ matrix inversion cost"
        },
        {
          "id": "C",
          "text": "Gradient Descent scales efficiently to massive feature dimensions ($p > 1{,}000{,}000$) where closed-form inversion runs out of memory"
        },
        {
          "id": "D",
          "text": "Feature scaling is mandatory for the Normal Equation but completely unnecessary for Gradient Descent"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "A, B, and C are exact architectural tradeoffs. D is reversed: feature scaling is essential for Gradient Descent to prevent slow zigzagging, but the Normal Equation is scale-invariant (scaling $X$ simply scales the resulting $\\theta$ without affecting closed-form solvability).",
      "difficulty": "medium",
      "subtopic": "Normal Equation vs Gradient Descent"
    },
    {
      "id": "cml-l05-q25",
      "type": "multi_choice",
      "question": "Which of the following optimization algorithms compute adaptive learning rates tailored per-parameter based on historical gradient moments? (Select ALL that apply)",
      "options": [
        {
          "id": "A",
          "text": "AdaGrad (accumulates sum of squared historical gradients)"
        },
        {
          "id": "B",
          "text": "RMSprop (exponentially decaying average of squared gradients)"
        },
        {
          "id": "C",
          "text": "Adam (combines first moment exponential averaging with second raw moment RMSprop)"
        },
        {
          "id": "D",
          "text": "Standard Vanilla Batch Gradient Descent with fixed step size"
        }
      ],
      "correctOptionIds": [
        "A",
        "B",
        "C"
      ],
      "explanation": "AdaGrad, RMSprop, and Adam are classic adaptive learning rate optimizers that maintain per-parameter scaling. Standard Vanilla BGD uses a single shared constant scalar $\\alpha$ for all parameters.",
      "difficulty": "medium",
      "subtopic": "Adaptive Optimizers"
    }
  ]
}
