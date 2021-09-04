
# importing libraries to plot graphs
import matplotlib.pyplot as plt
import math as m

f = [20,50,100,200,500,1000,2000,5000, 20000]
act = [-20.83,
-13.06,
-7.64,
-3.43,
-0.26,
-0.20,
-0.05,
-0.008,
-0.005
]
exp = [-39.67,
-34.39,
-30.4,
-25.8,
-22.02,
-21.23,
-20.86,
-20.33,
-20.42
]
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
font1 = {'family': 'Times New Roman', 'color': 'black', 'size': 16}

# using appropriate background style for better visualization
plt.style.use('seaborn')

# x-label of the plot
plt.xlabel('Frequency (Hz)', fontdict=font)

# y-label of the plot
plt.ylabel('Gain (dB)', fontdict=font)

# plotting the values
plt.plot(f, act, 'b-', label ='Theoretical')
plt.plot(f, exp, 'r-.', label ='Experimental')

# plot legend location
plt.legend(loc = 0)

# plot title
plt.title('Gain of Passive High Pass Filter vs Frequency', fontdict=font1)
# showing the plot
plt.show()
