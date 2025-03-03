# Parameters
mu <- 5
sigma <- 2
n <- 30
N_sim <- 1000

# Initialize vectors
sample_vars <- numeric(N_sim)
biased_vars <- numeric(N_sim)

# Simulation
set.seed(123)
for (i in 1:N_sim) {
  data <- rnorm(n, mean = mu, sd = sigma)
  sample_vars[i] <- var(data)
  biased_vars[i] <- sum((data - mean(data))^2) / n
}

# Graphical Output
par(mfrow = c(1, 2))

# Histogram of unbiased variances
hist(sample_vars, breaks = 30, col = "lightblue", main = "Unbiased Sample Variance", xlab = "Variance", border = "white")
abline(v = sigma^2, col = "red", lwd = 2)

# Histogram of biased variances
hist(biased_vars, breaks = 30, col = "lightgreen", main = "Biased Sample Variance", xlab = "Variance", border = "white")
abline(v = sigma^2, col = "red", lwd = 2)

# Z-test (if group1 and group2 are defined)
# z_test_result <- z.test(group1, group2, sigma.x = sd(group1), sigma.y = sd(group2))
# print(z_test_result)

# Histograms of groups (if group1 and group2 are defined)
# par(mfrow = c(1, 2))
# hist(group1, breaks = 30, col = "lightblue", main = "Histogram of Group 1", xlab = "Value", border = "white")
# hist(group2, breaks = 30, col = "lightgreen", main = "Histogram of Group 2", xlab = "Value", border