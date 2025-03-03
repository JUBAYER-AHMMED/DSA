# Create a 2x2 contingency table
data <- matrix(c(10, 5, 2, 8), nrow = 2, byrow = TRUE)
rownames(data) <- c("Group A", "Group B")
colnames(data) <- c("Success", "Failure")

# Perform Fisher's exact test
fisher_test_result <- fisher.test(data)

# Output
print(data)
print(fisher_test_result)

# Graphical Output
par(mfrow = c(1, 2))

# Barplot of the contingency table
barplot(data, beside = TRUE, col = c("lightblue", "lightgreen"), main = "2x2 Contingency Table", xlab = "Outcome", ylab = "Frequency")
legend("topright", legend = rownames(data), fill = c("lightblue", "lightgreen"))

# Mosaic plot
mosaicplot(data, main = "Mosaic Plot", color = TRUE)