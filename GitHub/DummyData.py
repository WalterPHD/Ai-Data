import numpy as np
import matplotlib.pyplot as plt

mean = [-3, 0]  # Mean vector
cov = [[1, 0.8], [0.8, 1]]  # Covariance matrix

np.random.seed(0)
random_points = np.random.multivariate_normal(mean, cov, 500)

# Plot the random points
plt.figure(figsize=(8, 6))
plt.scatter(random_points[:, 0], random_points[:, 1], alpha=0.6, color='blue')
plt.title("500 Random Points from 2D Normal Distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")  
plt.show()

#Problem 2
all_values = random_points.flatten()

# Plot the histogram for all values
plt.figure(figsize=(8, 6))
plt.hist(all_values, bins=30, alpha=0.7, color='blue')
plt.title("Histogram ")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

#Problem 3
#Each Dimension
x_values = random_points[:, 0]  # First dimension
y_values = random_points[:, 1]  # Second dimension

# Plot histograms for both dimensions
plt.figure(figsize=(10, 6))

# Histogram for the X-axis
plt.hist(x_values, bins=30, alpha=0.7, label="(first dimension)")
# Histogram for the Y-axis
plt.hist(y_values, bins=30, alpha=0.7, label="(second dimension)")

plt.title("Histogram of 500 Random Points from 2D Normal Distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

#Problem 4
mean2 = [0, -3]
cov2 = [[1, 0.8], [0.8, 1]]

random_points_2 = np.random.multivariate_normal(mean2, cov2, 500)

plt.figure(figsize=(8, 6))
plt.scatter(random_points[:, 0], random_points[:, 1], alpha=0.6, color='blue', label='Set 1')
plt.scatter(random_points_2[:, 0], random_points_2[:, 1], alpha=0.6, color='orange', label='Set 2')


plt.title("Comparison of Two 2D Normal Distributions")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc="upper left")
plt.grid(True)
plt.axis("equal") 
plt.show()

#Problem 5
#Combining

combined_points=np.vstack((random_points,random_points_2))

plt.figure(figsize=(8, 6))
plt.scatter(combined_points[:, 0], combined_points[:, 1], alpha=0.6, color='green', label='Combined Dataset')

plt.title("Scatter Plot of 1000 Random Points from Two 2D Normal Distributions")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()

#Problem 6
labels_1 = np.zeros((500, 1))  # 500 points with label 0 (Problem 1)
labels_2 = np.ones((500, 1))   # 500 points with label 1 (Problem 4)

data_1_with_labels = np.hstack((random_points, labels_1))  # Combine Problem 1 data with labels
data_2_with_labels = np.hstack((random_points_2, labels_2))  # Combine Problem 4 data with labels

combined_data = np.vstack((data_1_with_labels, data_2_with_labels))

# just to verify
print("Shape of the combined dataset:", combined_data.shape)

#Printing
print("First 100 rows of the combined dataset:")
print(combined_data[:100])#the quantity i want to see i chose 100 to be less stressfull

plt.figure(figsize=(8, 6))
plt.scatter(random_points[:, 0], random_points[:, 1], alpha=0.6, color='blue', label='Problem 1 (Label 0)')
plt.scatter(random_points_2[:, 0], random_points_2[:, 1], alpha=0.6, color='orange', label='Problem 4 (Label 1)')

plt.title("Scatter Plot of Combined Data with Labels [0 and 1]")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis("equal") 
plt.show()





