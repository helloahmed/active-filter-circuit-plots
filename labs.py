
# importing libraries to plot graphs
import matplotlib.pyplot as plt
import math as m

f = [1000, 3000, 5000]
a = [52.9, 158.7, 264.5]
t = [50, 148, 256]
# adding values of f from 1k ro 11k
# for i in range(11):
#     f.append(1000 * (i + 1))



# adding values of impedance in an array
# for i in range(11):
#     a.append((2 * m.pi * f[i] * 0.0033))

# t = [18.2,
# 32.6,
# 48.8,
# 72.2,
# 86.1,
# 100,
# 118.8,
# 138,
# 155,
# 176,
# 191
# ]

# choosing appropriate font style for better visualization
font = {'family': 'Times New Roman', 'color': 'black', 'size': 14}

# using appropriate background style for better visualization
plt.style.use('seaborn')

# x-label of the plot
plt.xlabel('Resistances', fontdict=font)

# y-label of the plot
plt.ylabel('Time for RC Series Circuit (us)', fontdict=font)

# plotting the values
plt.plot(f, a, 'b-', label ='Theoretical')
plt.plot(f, t, 'r-.', label ='Experimental')
plt.legend(loc = 0)

# showing the plot

plt.show()
