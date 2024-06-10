import matplotlib.pyplot as plt
import numpy as np

# Problem 1: Create a simple line plot with x-values from 0 to 10 and y-values as their squares.

x = range(11)
y = [i**2 for i in x]

plt.plot(x, y)
plt.show()

# Problem 2: Create a line plot with a title "Square Function".
x = range(11)
y = [i**2 for i in x]
plt.title("Square Function")
plt.plot(x, y)
plt.show()

# Problem 3: Create a line plot with x-axis labeled "X" and y-axis labeled "Y".

x = range(11)
y = [i**2 for i in x]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Problem 4: Create a bar plot with categories A, B, C, and D with values 4, 7, 1, and 8.

categories = ["A", "B", "C", "D"]
values = [4, 7, 1, 8]

plt.bar(categories, values, color="red")
plt.xlabel(categories)
plt.ylabel(values)
plt.title("BarPlot")
plt.show()

# Problem 5: Create a bar plot with the title "Category Values".

fruits = ['Banana', 'Apple', 'Cherry']
prices = [10, 8, 20]

colors = ['yellow', 'green', 'red']
plt.bar(fruits, prices, color=colors)
plt.xlabel('Fruits')
plt.ylabel('MDL')
plt.title('Category Values')
plt.show()

# Problem 6: Create a horizontal bar plot with categories A, B, C, and D with values 4, 7, 1, and 8.

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(values, categories)
plt.show()

# Problem 7: Create a bar plot with x-axis labeled "Categories" and y-axis labeled "Values".

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Problem 8: Create a pie chart with four categories having values 15, 30, 45, and 10.

sizes = [15, 30, 45, 10]

plt.pie(sizes)
plt.show()

# Problem 9: Create a pie chart with categories labeled A, B, C, and D.

sizes = [15, 30, 45, 10]
categories = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=categories)
plt.show()

# Problem 10: Create a pie chart with the title "Distribution".

sizes = [15, 30, 45, 10]
categories = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=categories)
plt.title('Distribution')
plt.show()

# Problem 11: Create a histogram for the list of values [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].

values = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(values)
plt.show()

# Problem 12: Create a histogram with 5 bins for the list of values [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].

values = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(values, bins=5)
plt.show()


# Given list of values
values = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Create a histogram with 5 bins
y, _ = np.histogram(values, bins=5)

# Define the x-axis (bin edges)
x = np.arange(len(y))

# Plot the histogram
plt.bar(x, height=y, tick_label=[f"Bin {i+1}" for i in range(len(y))])
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.title("Histogram with 5 Bins")
plt.show()


# Problem 13: Create a histogram with the title "Value Distribution".

values = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(values, bins=5)
plt.title('Value Distribution')
plt.show()

# Problem 14: Create a line plot with red color.

x_values = [1, 2, 3, 4, 5]
y_values = ['A', 'B', 'C', 'D', 'E']

plt.plot(x_values, y_values, color='red')
plt.show()

# Problem 15: Create a bar plot with blue color.

x_values = [1, 2, 3, 4, 5]
y_values = ['A', 'B', 'C', 'D', 'E']

plt.bar(x_values, y_values, color='blue')
plt.show()

# Problem 16: Create a pie chart with custom colors.

sizes = [15, 30, 20, 50]
categories = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'black', 'green']
plt.pie(sizes, labels=categories, colors=colors)
plt.show()

# Problem 17: Create a line plot with circle markers.

x = range(11)
y = [i**2 for i in x]

plt.plot(x, y, marker='o')
plt.show()

# Problem 18: Create a bar plot with black edge color.

x_values = ['A', 'B', 'C', 'D', 'E']
y_values = [1, 2, 3, 4, 5]

plt.bar(x_values, y_values, edgecolor='black')
plt.show()

# Problem 19: Create a histogram with density set to True.

values = [2, 2, 3, 4, 4, 1, 1]

plt.hist(values, density=True)
plt.show()

# Problem 20: Create a pie chart that displays percentages.

sizes = [15, 30, 20, 50]
categories = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=categories, autopct='%1.1f%%')
plt.show()

# Bonus Problem:
# Solve all the above problems again, but this time use a DICTIONARY to store the data
# Example:
# Instead of:
# x = range(11)
# y = [i**2 for i in x]
# It becomes:
# dic={x:x**2 for x in range(11)}
# Where the dictionary keys are the previous x list and the values are the previous y list
