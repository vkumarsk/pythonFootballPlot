import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('football.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
     x.append(str(row[0]))
     y.append(int(row[7]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph for number of wins by team')
plt.legend()
plt.show()

