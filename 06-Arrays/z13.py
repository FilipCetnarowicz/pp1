import matplotlib.pyplot as plt

# Data
commute_modes = ['Car', 'Public Transport', 'Bike', 'Foot']
employees = [25, 19, 32, 7]

# Create bar chart
plt.bar(commute_modes, employees, color=['blue', 'green', 'red', 'cyan'])

# Add title and labels
plt.title('Commute Modes of Company Employees')
plt.xlabel('Commute Mode')
plt.ylabel('Number of Employees')

# Show the chart
plt.show()