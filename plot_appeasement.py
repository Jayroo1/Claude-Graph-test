import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ['Tosu', 'Saga']
appeasement_levels = np.random.randint(1, 5, size=2)  # Random values between 1 and 4

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(countries, appeasement_levels, color=['blue', 'orange'])

# Customize the plot
plt.title('Country Appeasement Level', fontsize=16)
plt.xlabel('Countries', fontsize=12)
plt.ylabel('Appeasement Level', fontsize=12)
plt.ylim(0, 5)  # Set y-axis limit from 0 to 5

# Add value labels on top of each bar
for i, v in enumerate(appeasement_levels):
    plt.text(i, v + 0.1, str(v), ha='center', fontsize=12)

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot
plt.savefig('country_appeasement_level.png')

# Display the plot
plt.show()
