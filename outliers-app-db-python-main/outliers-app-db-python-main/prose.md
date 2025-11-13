### Explanation
$$MSE = \\frac{1}{n} \\sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$$

\$$LASSO = \\frac{1}{n} \\sum_{i=1}^{n} (Y_i - \hat{Y}\_i)^2 + \\lambda \\underbrace{\\sum\_{j=1}^{p} |\\beta_j|}_\\text{penalty}$$

$$Ridge = \\frac{1}{n} \\sum_{i=1}^{n} (Y_i - \hat{Y}\_i)^2 + \\lambda \\underbrace{\\sum\_{j=1}^{p} \\beta_j^2}_\\text{penalty}$$

$$\\lambda \\text{is the regularization strength.}$$
