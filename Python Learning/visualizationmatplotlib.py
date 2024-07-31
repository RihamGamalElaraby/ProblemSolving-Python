import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Line plot
xpoint = [1, 8]
ypoint = [2, 9]

plt.plot(xpoint, ypoint)
plt.show()
##############################################################
# Line plot with markers and grid
xpoint = [1, 8, 9, 15]
ypoint = [2, 9, 11, 6]

plt.plot(xpoint, ypoint, marker="o", linestyle="dotted")
plt.grid()
plt.show()
#############################################################
# Scatter plot
plt.scatter(xpoint, ypoint)
plt.show()
#################################################################
# Bar chart
x = ["apples", "oranges"]
y = [15, 10]
plt.bar(x, y)
plt.show()  # Corrected show function call
###################################################################
# Pie chart
percentages = np.array([35, 15, 50, 46])  # Corrected creation of the percentage array
labels = ["apples", "oranges", "bananas", "cherries"]
plt.pie(percentages, labels=labels)
plt.show()
################################################################

year = [2017 , 2018 , 2019 , 2020 ]
expense= [10000 , 20000 , 12000 , 100000]
profit = [100 , 200 , 300 , 500 ]

startup = {"Year": year, "Expenses": expense, "Profit": profit}

df = pd.DataFrame(startup)
print(df)


plt.plot(df["Year"] , df["Expenses"] , label = "Expenses")
plt.show()

plt.plot(df["Year"]  , df["Profit"] , label = "Profit")
plt.legend(loc = "upper right")
plt.show()
#######################################################