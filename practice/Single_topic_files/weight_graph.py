import matplotlib.pyplot as plt
x = [151.6, 151.8, 150.2, 148.4, 147.2, 146.6, 146.0, 145.2, 145.8, 144.2, 143.8, 143.8, 143.2, 143.0]
y = ['3/30', '3/31', '4/1', '4/3', '4/4', '4/6', '4/8', '4/10', '4/12', '4/13', '4/15', '4/18', '4/19', '4/20']

plt.plot(y,x)

plt.xlabel('Weight')
plt.ylabel('Date')

plt.show()