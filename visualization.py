# healthcare-data-visualization
Healthcare data visualization task-2 
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv('cleaned_healthcare_data.csv')

# 1. Disease Distribution
plt.figure(figsize=(8,5))
df['DISEASE'].value_counts().plot(kind='bar', color=['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4'])
plt.title('Patients by Disease')
plt.ylabel('Count')
plt.savefig('disease_distribution.png')
plt.show()

# 2. Gender Ratio
plt.figure(figsize=(6,6))
df['GENDER'].value_counts().plot(kind='pie', autopct='%1.1f%%', labels=['Male','Female'])
plt.title('Patients by Gender')
plt.savefig('gender_ratio.png')
plt.show()

# 3. Age Distribution
plt.figure(figsize=(8,5))
plt.hist(df['AGE'], bins=5, color='#45B7D1', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution.png')
plt.show()

# 4. Medication Usage
plt.figure(figsize=(6,6))
df['MEDICATION'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Medication Usage')
plt.savefig('medication_usage.png')
plt.show()

print("All visualizations created successfully!")
