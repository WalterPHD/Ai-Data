import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Loading Iris dataset
df = load_iris()

# Problem 1: Creating the DataFrame
Iris = pd.DataFrame(df['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
print(Iris.head())

Species_Num=pd.DataFrame(df['target'] , columns=['Species'])
print(Species_Num)

# Problem 2: Addind species
Iris['Species'] = df['target']
print(Iris.head())
print('\n')

# Problem 3: Basic Data Exploration
print(Iris.head(4))
print('\n')
print(Iris.info(), 'Info')
print('\n')
print(Iris.describe(), 'Describe')
print('\n')
print(Iris.isnull(), 'IsNull')
print('\n')
print(Iris.sum(), 'Sum')
print('\n')
print(Iris.value_counts(), 'ValueCounts')
print('\n')

# Problem 4: Re-reading the data set and what i can find interesting about it

# Problem 5: Selecting data using loc and iloc
Sepal_withloc = Iris.loc[:, 'Sepal_Width']
Sepal_withiloc = Iris.iloc[:, 1]
print(Sepal_withiloc, '\n', Sepal_withloc, '\n')

print(Iris.loc[50:99, :], '\n')
print(Iris.loc[50:99, 'Petal_Length'], '\n')

# Problem 6: Petal_Width value
Specific_Petal = Iris[Iris['Petal_Width'] == 0.2]
print(Specific_Petal)

# Plotting the distribution of species
species_counts = Iris['Species'].value_counts()
species_names = ['Setosa','Versicolor','Virginica']

# Plot the pie chart for species distribution
plt.figure(figsize=(8, 8))
plt.pie(species_counts, labels=species_names, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Types of Iris')
plt.show()

# List of feature names (columns of Iris DataFrame except 'Species')
features = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']

# Boxplot for each feature by species usinf in
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Species', y=feature, data=Iris)
    plt.title(f'Box Plot of {feature} by Species')
    plt.show()

# Violin plot for each feature by species
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='Species', y=feature, data=Iris)
    plt.title(f'Violin Plot of {feature} by Species')
    plt.show()

#Problem 7: Redo everything but different
# Re-Creating the DataFrame in case of miss loading
Iris = pd.DataFrame(df['data'], columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
Iris['Species'] = df['target']
Iris['Species'] = Iris['Species'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})  # Map species numbers to names

# Scatter plot of all combinations of four feature values, color-coded by species, with all 'o' markers
sns.pairplot(Iris, hue='Species', markers='o') 
plt.show()

# coefficient matrix for the four features using corr()
correlation_matrix = Iris[['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']].corr()
print("Correlation Coefficient Matrix:")
print(correlation_matrix)

# Heatmap of the correlation coefficient matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Coefficient Matrix Heatmap')
plt.show()

#Problem 8
#What i can take from this is that Setosa is easily distinguishable from Versicolor and Virginica,
#  primarily based on the petal dimensions (length and width). Setosa has much smaller petals compared to the other two species.

# Versicolor and Virginica show more similarities in their feature values,
#  particularly in petal dimensions, making them harder to distinguish based purely on those features.
#  However, Sepal Length provides a slight differentiation between the two species.

# The correlation analysis confirms that the petal dimensions (length and width) are highly correlated,
#  and they form the strongest feature pair when distinguishing between the species.

# Sepal Width shows weaker correlations with the other features, especially the petal dimensions,
#  indicating that it is less important for distinguishing between the species.