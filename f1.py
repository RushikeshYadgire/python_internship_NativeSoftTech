import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = "C:/Users/rushi/OneDrive/Desktop/pyint/world_health_data.csv"
data = pd.read_csv(file_path)
print("Dataset loaded successfully!")

# Step 2: Explore the dataset
print("\nFirst 5 rows of the dataset:")
print(data.head())
print("\nDataset structure:")
data.info()
print("\nStatistical summary:")
print(data.describe())

# Step 3: Add a new column for health-to-life ratio (example calculation)
# Health expenditure as a percentage of life expectancy (if applicable)
data['health_to_life_ratio'] = data['health_exp'] / data['life_expect']
print("\nNew column 'health_to_life_ratio' added!")

# Step 4: Save the processed dataset to a CSV file
data.to_csv('processed_world_health_data.csv', index=False)
print("\nProcessed dataset saved as 'processed_world_health_data.csv'")

# Step 5: Create visualizations
# Scatter plot: Life expectancy vs Health expenditure
sns.scatterplot(data=data, x='health_exp', y='life_expect', hue='country_code', alpha=0.6)
plt.title('Health Expenditure vs Life Expectancy')
plt.savefig('scatter_plot_health_vs_life.png')  # Save the scatter plot as an image
plt.show()

# Histogram: Distribution of life expectancy
sns.histplot(data=data, x='life_expect', kde=True, bins=30)
plt.title('Distribution of Life Expectancy')
plt.savefig('histogram_life_expect.png')  # Save the histogram as an image
plt.show()

# Box plot: Maternal mortality across years
sns.boxplot(data=data, x='year', y='maternal_mortality')
plt.title('Maternal Mortality Across Years')
plt.xticks(rotation=45)
plt.savefig('box_plot_maternal_mortality.png')  # Save the box plot as an image
plt.show()

print("\nAll visualizations saved successfully!")

