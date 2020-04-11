import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4]
square_values = [x**2 for x in input_values]

fig, ax = plt.subplots()
# The parameter s means size of each dot.
# ax.scatter(input_values, square_values, c='green', s=200)

# Using colormaps
# ax.scatter(input_values, square_values, c=square_values, cmap=plt.cm.Blues, s=200)

# Set title and label axes
ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

# Set range for each axis
ax.axis([0, len(input_values), 0, 16])

plt.show()
# Saving plots instead of just showing it
# plt.savefig('squares.png', bbox_inches='tight')
