# temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
# temperatures_adjusted = [15, 49, 46, 13, 21, 38, 32, 51]
# temperatures_adjusted2 = [temp + 20 for temp in temperatures]
# print(temperatures_adjusted2)
# temperatures_fah = [(9.0 / 5.0) * temp + 32 for temp in temperatures]
# print(temperatures_fah)

# import matplotlib.pyplot as plt

# rainfall_1 = [153, 156, 147, 149, 151]
# rainfall_2 = [159, 156, 160, 161, 148]

# x_values_1 = [x * 2 for x in range(5)]
# x_values_2 = [x * 2 + 0.8 for x in range(5)]
# x_values_midpoints = [(x1 + x2)/2.0 for (x1, x2) in zip(x_values_1, x_values_2)]
# print(x_values_midpoints)

# y_values_1 = [amount - 140 for amount in rainfall_1]
# y_values_2 = [amount - 140 for amount in rainfall_2]

# plt.bar(x_values_1, y_values_1, 0.8, 0)
# plt.bar(x_values_2, y_values_2, 0.8, 0)
# plt.show()


xy = [[1, 3], [2, 4], [3, 3], [4, 2]]
z = [x * y for (x, y) in xy]
print(z)

