# Lecture 14: Naive Bayes Classification & Probabilistic Generative Models
## Student Notes — SST Classical Machine Learning

---

## 🎯 Learning Objectives

By the end of this lecture, you should be able to:
- Contrast **Generative Classifiers** (modeling joint probability $P(\mathbf{X}, Y)$ via Bayes' Theorem) against **Discriminative Classifiers** (directly modeling posterior $P(Y \mid \mathbf{X})$).
- Formulate **Bayes' Theorem** and dissect its four constituent terms: **Prior**, **Likelihood**, **Evidence (Marginal Probability)**, and **Posterior**.
- Mathematically formulate the **Naive Conditional Independence Assumption**, proving how it shrinks the parameter space from exponential $\mathcal{O}(K \cdot 2^d)$ to linear $\mathcal{O}(K \cdot d)$.
- Derive the **Maximum A Posteriori (MAP)** classification rule and implement the **Log-Space Transformation** to eliminate floating-point numerical underflow.
- Resolve the **Zero Probability Problem** using **Additive Laplace Smoothing ($\alpha = 1$)** and **Lidstone Smoothing ($\alpha < 1$)**.
- Formulate and implement the three primary Naive Bayes paradigms:
  - **Gaussian Naive Bayes** (continuous variables modeled via normal distributions $\mathcal{N}(\mu_{jk}, \sigma_{jk}^2)$).
  - **Multinomial Naive Bayes** (discrete count histograms for NLP and Bag-of-Words).
  - **Bernoulli Naive Bayes** (binary presence/absence indicators).
- Explain why Naive Bayes yields highly accurate classification decisions even when feature independence is violently violated.
- Build a vectorized Naive Bayes classifier from scratch in NumPy.

---

## 1. Generative vs. Discriminative Models

All classification algorithms fall into two broad philosophical paradigms:

```
 Discriminative (Logistic Regression, SVM):         Generative (Naive Bayes, GMM):
 Models P(Y | X) directly:                          Models P(X, Y) = P(X | Y) · P(Y):
 "What is the boundary separating Cats from Dogs?"   "What does a Cat look like? What does a Dog look like?"

       x₂ ▲                                               x₂ ▲
          │      o   o   /   +   +                           │     ╭─────╮           ╭─────╮
          │    o   o    /   +   +                            │    │  o o  │         │  + +  │
          │   o   o    /   +   +                             │     ╰─────╯           ╰─────╯
          │           /                                  │   P(X | Cat)        P(X | Dog)
          └──────────/─────────────►                     └─────────────────────────►
                  Boundary                                   Generates density per class!
```

| Dimension | Discriminative Models | Generative Models |
| :--- | :--- | :--- |
| **Target Distribution** | Directly models $P(Y \mid \mathbf{X})$ | Models joint distribution $P(\mathbf{X}, Y) = P(\mathbf{X} \mid Y) P(Y)$ |
| **Objective** | Find the optimal decision boundary between classes | Model the underlying probability distribution of each class |
| **Examples** | Logistic Regression, SVM, Decision Trees, Neural Networks | Naive Bayes, Gaussian Mixture Models (GMM), Hidden Markov Models |
| **Data Generation** | Cannot generate synthetic data samples | Can generate synthetic observations $\mathbf{x} \sim P(\mathbf{X} \mid Y)$ |
| **Missing Data** | Sensitive to missing feature inputs | Naturally handles missing attributes via marginalization |

---

## 2. Bayes' Theorem in Machine Learning

For a feature vector $\mathbf{x} = [x_1, x_2, \dots, x_d]^T$ and class label $y \in \{1, \dots, K\}$:

$$P(Y = k \mid \mathbf{X} = \mathbf{x}) = \frac{P(\mathbf{X} = \mathbf{x} \mid Y = k) \cdot P(Y = k)}{P(\mathbf{X} = \mathbf{x})}$$

### The Four Components:
1. **Prior Probability $P(Y = k)$**:  
   The baseline probability of encountering class $k$ before observing any features:
   $$\hat{P}(Y = k) = \frac{N_k}{N}$$
2. **Likelihood $P(\mathbf{X} = \mathbf{x} \mid Y = k)$**:  
   The probability that a data point belonging to class $k$ exhibits the exact feature vector $\mathbf{x}$.
3. **Evidence (Marginal Probability) $P(\mathbf{X} = \mathbf{x})$**:  
   The total probability of observing feature vector $\mathbf{x}$ across all classes:
   $$P(\mathbf{X} = \mathbf{x}) = \sum_{j=1}^K P(\mathbf{X} = \mathbf{x} \mid Y = j) \cdot P(Y = j)$$
   *Note: Because $P(\mathbf{X})$ is identical for all classes $k$, it acts as a constant normalizing factor and can be omitted during classification.*
4. **Posterior Probability $P(Y = k \mid \mathbf{X} = \mathbf{x})$**:  
   The updated probability that instance $\mathbf{x}$ belongs to class $k$ after observing the evidence.

---

## 3. The "Naive" Conditional Independence Assumption

Evaluating the full joint likelihood $P(x_1, x_2, \dots, x_d \mid Y = k)$ directly is computationally impossible:
- If each of the $d$ features is binary, the joint distribution requires estimating $2^d - 1$ distinct probabilities **per class**.
- For $d = 50$, $2^{50} \approx 1.12 \times 10^{15}$ parameters! No dataset on Earth could estimate this without catastrophic overfitting.

### The Naive Assumption
Naive Bayes makes the radical assumption that **all features are conditionally independent given the class label**:

$$P(x_1, x_2, \dots, x_d \mid Y = k) = \prod_{j=1}^d P(x_j \mid Y = k)$$

```
 Joint Likelihood (Intractable):        Naive Conditional Independence (O(d) parameters):
 P(x₁, x₂, x₃ | Y) =                    P(x₁, x₂, x₃ | Y) =
 P(x₁|Y) · P(x₂|x₁, Y) · P(x₃|x₁, x₂, Y)   P(x₁|Y) · P(x₂|Y) · P(x₃|Y)
 (Exponential combinations!)               (Simple univariate product!)
```

- **Parameter Reduction**: The number of parameters drops from $\mathcal{O}(K \cdot 2^d)$ to **$\mathcal{O}(K \cdot d)$**.
- The algorithm scales gracefully to millions of features (e.g., text vocabulary or genomic markers).

---

## 4. The Maximum A Posteriori (MAP) Decision Rule

The classifier selects the class $k^*$ that maximizes the posterior probability:

$$\hat{y} = \operatorname{argmax}_{k \in \{1, \dots, K\}} P(Y = k) \prod_{j=1}^d P(x_j \mid Y = k)$$

### 4.1 Numerical Underflow & The Log-Space Transformation
In high-dimensional problems (e.g., $d = 2,000$ words in an email), multiplying thousands of probabilities $p_j \in [0, 1]$ causes the product to underflow double-precision floating-point arithmetic to absolute zero:

$$0.01^{2000} \to 0.0$$

To eliminate underflow, apply the strictly monotonic natural logarithm:

$$\hat{y} = \operatorname{argmax}_{k \in \{1, \dots, K\}} \left[ \ln P(Y = k) + \sum_{j=1}^d \ln P(x_j \mid Y = k) \right]$$

- Products transform into stable, computationally efficient **sums**!

---

## 5. The Zero Probability Problem & Laplace Smoothing

If a specific feature value $x_j$ never appeared alongside class $k$ in the training dataset:

$$\hat{P}(x_j \mid Y = k) = \frac{0}{N_k} = 0$$

Because the decision rule multiplies feature likelihoods together, a **single zero completely annihilates the entire posterior probability**:

$$P(Y = k) \cdot \prod P(x_i \mid Y = k) = P(Y = k) \cdot (0) \cdot (\dots) = 0$$

Even if 99 other features overwhelmingly indicate class $k$, one unseen word (e.g., a typo like *"congrats"*) forces the model to conclude the probability of Spam is zero!

### Laplace (Additive) Smoothing
Add a pseudocount $\alpha > 0$ to the numerator and scale the denominator by $\alpha |V|$ (where $|V|$ is the number of possible values feature $j$ can take, or vocabulary size):

$$\hat{P}(x_j = v \mid Y = k) = \frac{N_{k, v} + \alpha}{N_k + \alpha |V|}$$

- **Laplace Smoothing**: $\alpha = 1.0$.
- **Lidstone Smoothing**: $0 < \alpha < 1.0$ (e.g., $\alpha = 0.1$).
- **Effect**: If $N_{k, v} = 0$, the probability becomes $\frac{\alpha}{N_k + \alpha |V|} > 0$, preventing multiplication by zero while preserving prior dominance.

---

## 6. Taxonomy of Naive Bayes Classifiers

Different data distributions require different models for the likelihood $P(x_j \mid Y = k)$:

```
                                  NAIVE BAYES FAMILY
                                          │
                 ┌────────────────────────┼────────────────────────┐
                 ▼                        ▼                        ▼
       Gaussian Naive Bayes     Multinomial Naive Bayes   Bernoulli Naive Bayes
       (Continuous Features)    (Word Counts / Histograms) (Binary Features)
       x_j ~ 𝒩(μ_jk, σ_jk²)     x_j ∈ {0, 1, 2, ...}       x_j ∈ {0, 1}
```

### 6.1 Gaussian Naive Bayes (Continuous Data)
When features are continuous real numbers $x_j \in \mathbb{R}$, assume the values within each class follow a **Gaussian (Normal) Distribution**:

$$P(x_j \mid Y = k) = \frac{1}{\sqrt{2\pi \sigma_{jk}^2}} \exp\left( -\frac{(x_j - \mu_{jk})^2}{2\sigma_{jk}^2} \right)$$

#### Parameters Estimated from Data:
1. **Class Mean**: $\mu_{jk} = \frac{1}{N_k} \sum_{i: y_i = k} x_{i, j}$
2. **Class Variance**: $\sigma_{jk}^2 = \frac{1}{N_k} \sum_{i: y_i = k} (x_{i, j} - \mu_{jk})^2$

### 6.2 Multinomial Naive Bayes (Count Data / NLP)
Used for text classification and document categorization, where feature vector $\mathbf{x} = [c_1, c_2, \dots, c_d]^T$ represents word token frequencies:

$$P(\mathbf{x} \mid Y = k) = \frac{(\sum c_j)!}{\prod c_j!} \prod_{j=1}^d p_{jk}^{c_j}$$

Where $p_{jk}$ is the probability that word $j$ appears in a document of class $k$:

$$p_{jk} = \frac{\sum_{i \in k} x_{ij} + \alpha}{\sum_{j=1}^d \sum_{i \in k} x_{ij} + \alpha |V|}$$

### 6.3 Bernoulli Naive Bayes (Binary Data)
Used when features are binary flags ($x_j \in \{0, 1\}$) indicating whether a word or attribute is **present or absent**:

$$P(x_j \mid Y = k) = p_{jk}^{x_j} (1 - p_{jk})^{(1 - x_j)}$$

- *Crucial Difference from Multinomial*: Bernoulli explicitly penalizes the absence of words ($x_j = 0$).

---

## 7. The Paradox of Naive Bayes: Why Does It Work So Well?

In almost every real-world application, the conditional independence assumption is **blatantly false** (e.g., in text, *"Hong"* is almost always followed by *"Kong"*).  
Yet Naive Bayes frequently rivals complex neural networks in spam detection and medical triage. Why?

### The Theoretical Explanation (Domingos & Pazzani, 1997)
- **Classification Depends on the Argmax, Not Accurate Probabilities**:  
  To make a correct classification, Naive Bayes does not need accurate posterior probabilities. It only needs the correct class to have the highest relative probability:

  $$\operatorname{argmax}_k \hat{P}(Y = k \mid \mathbf{X}) = \operatorname{argmax}_k P_{\text{true}}(Y = k \mid \mathbf{X})$$

- Violations of the independence assumption can severely distort (calibrate) the posterior probabilities toward $0$ or $1$, but **they rarely shift the location of the optimal decision boundary**.
- **Low Variance**: With only $\mathcal{O}(K \cdot d)$ parameters, Naive Bayes has extremely low variance and is practically immune to overfitting on small datasets.

---

## 8. Complete Python Implementation from Scratch

```python
"""
Gaussian Naive Bayes from Scratch (Pure NumPy)
Implements Maximum Likelihood parameter estimation (mean, variance),
log-space Gaussian likelihood evaluation, and MAP decision rule.
"""

import numpy as np

class GaussianNaiveBayesScratch:
    def __init__(self, eps: float = 1e-9):
        self.eps = eps  # Stability factor added to variance to prevent division by zero
        self.classes = None
        self.mean = {}
        self.var = {}
        self.priors = {}

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)

        for c in self.classes:
            X_c = X[y == c]
            self.mean[c] = np.mean(X_c, axis=0)
            self.var[c] = np.var(X_c, axis=0) + self.eps
            self.priors[c] = X_c.shape[0] / float(n_samples)

        return self

    def _calculate_log_likelihood(self, class_val: int, x: np.ndarray) -> float:
        mean = self.mean[class_val]
        var = self.var[class_val]

        # Log of Gaussian PDF: -0.5 * ln(2π * var) - ((x - mean)² / (2 * var))
        log_prob = -0.5 * np.log(2.0 * np.pi * var) - ((x - mean) ** 2) / (2.0 * var)
        return np.sum(log_prob)

    def _predict_single(self, x: np.ndarray) -> int:
        posteriors = []

        for c in self.classes:
            prior_log = np.log(self.priors[c])
            likelihood_log = self._calculate_log_likelihood(c, x)
            posterior = prior_log + likelihood_log
            posteriors.append((posterior, c))

        # Return class with Maximum A Posteriori (MAP) score
        posteriors.sort(key=lambda item: item[0], reverse=True)
        return posteriors[0][1]

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.array([self._predict_single(x) for x in X])


# Verification on Synthetic Data
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42
    )

    gnb = GaussianNaiveBayesScratch()
    gnb.fit(X_train, y_train)
    predictions = gnb.predict(X_test)
    print(f"Gaussian Naive Bayes Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")
```

---

## 📌 Summary Checklist & Exam Cram Notes

1. **Generative Model**: Models $P(\mathbf{X}, Y) = P(\mathbf{X} \mid Y)P(Y)$; derives posterior via Bayes' Theorem.
2. **Bayes' Theorem**: $P(Y \mid X) = \frac{P(X \mid Y) P(Y)}{P(X)}$. Evidence $P(X)$ is constant across classes and dropped.
3. **Naive Assumption**: Features are conditionally independent given class: $P(\mathbf{X} \mid Y) = \prod_{j=1}^d P(x_j \mid Y)$. Slashes parameter complexity from $\mathcal{O}(2^d)$ to $\mathcal{O}(d)$.
4. **Log-Space Transformation**: Sum log-priors and log-likelihoods to prevent floating-point underflow.
5. **Zero Probability Problem**: Unseen feature-class pairs force posterior to 0; solved by Additive Laplace Smoothing $\frac{N_{kv} + \alpha}{N_k + \alpha |V|}$.
6. **Gaussian NB**: Continuous variables modeled via normal distribution parameters $\mu_{jk}$ and $\sigma_{jk}^2$.
7. **Multinomial NB**: Discrete frequency counts (text classification); models word counts.
8. **Bernoulli NB**: Binary occurrence flags ($x_j \in \{0, 1\}$); explicitly penalizes word absence.
9. **Why It Works**: Accurate classification requires only the correct ranking (argmax), not well-calibrated probabilities.

---

## 🧠 Quick Self-Check Questions

1. A spam filter evaluates two words: "lottery" and "winner". In training, $P(\text{"lottery"} \mid \text{Spam}) = 0.05$ and $P(\text{"winner"} \mid \text{Spam}) = 0.04$. The prior $P(\text{Spam}) = 0.2$. What is the joint likelihood score in log-space?
2. Why is Laplace Smoothing strictly necessary when deploying a Multinomial Naive Bayes model to production text processing?
3. How does Bernoulli Naive Bayes differ mathematically from Multinomial Naive Bayes when classifying a 1,000-word essay?
4. If two features are perfectly correlated ($x_1 = x_2$), how does Naive Bayes react? Does it double-count the evidence?
5. Why are the probability outputs of Naive Bayes typically uncalibrated (pushed toward extreme values of 0.0 or 1.0)?
