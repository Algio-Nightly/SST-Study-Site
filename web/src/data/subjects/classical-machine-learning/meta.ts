import type { SubjectMetadata } from '../types';

export const classicalMachineLearningMeta: SubjectMetadata = {
  id: 'classical-machine-learning',
  title: 'Classical Machine Learning',
  code: 'CML-101',
  term: 'Term 5',
  shortDescription: 'Statistical learning theory, OLS normal equations, gradient descent dynamics, bias-variance tradeoffs, and regularized classification.',
  detailedDescription: 'Rigorous applied machine learning notes covering Mitchell\'s ETP framework, leakage-free pipelines, LINE assumption diagnostics, VIF, Ridge/Lasso regularization, logistic regression odds ratios, and the curse of dimensionality.',
  iconName: 'Brain',
  accentColor: 'indigo',
  status: 'active',
  lecturesCount: 10,
  questionsCount: 255,
  featuredTopics: [
    'Mitchell\'s ETP Framework & Problem Formulation',
    'Data Leakage Taxonomy & ColumnTransformer Pipelines',
    'Ordinary Least Squares & Normal Equation Projection',
    'LINE Assumptions, Residual Diagnostics & VIF',
    'Vectorized Gradient Descent & Loss Curves',
    'Bias–Variance Decomposition & Occam\'s Razor',
    'Ridge (L2), Lasso (L1) & ElasticNet Regularization',
    'Log-Loss, ROC-AUC, PR Curves & Threshold Tuning',
    'K-Nearest Neighbours & Curse of Dimensionality',
    'Industrial Churn Lab & Asymmetric Cost Matrices'
  ],
  instructors: ['Chitwan Manchanda', 'SST CML Faculty']
};
