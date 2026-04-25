import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,25]


## LINE / PLOT GRAPH
# plt.plot(x,y) # default blue color graph
# plt.plot(x,y,color="red")
# plt.plot(x,y,color="orange",linestyle="--",marker="o")
plt.plot(x,y,color="orange",linestyle=":",marker="x")
"""
linestyle:
> "-", "--", ":"
marker:
> "o", "x", "*"
"""
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot")

plt.show()


## BAR GRAPH
x = ["std1", "std2", "std3", "std4", "std5"]
y = [60, 70, 80, 90, 100]
# plt.bar(x,y)
# plt.barh(x,y)
bars = plt.bar(x,y,color=['red','green','blue'],width=0.5,edgecolor='black')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height()+2, bar.get_height(), ha="center", va="center")
plt.title("Bar chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


## PIE CHART / GRAPH

subjects = ["Math", "Science", "English", "Computer"]
marks = [80, 90, 70, 95]
colors=["gold", "lightblue", "lightgreen", "orange"]
explode = [0,0.2,0,0.1]
plt.pie(marks,
        labels=subjects,
        colors=colors,
        autopct="%1.2f%%",
        explode=explode,
        shadow=True,
        textprops={'fontsize':10, 'color': 'blue'},
        wedgeprops={'edgecolor':'red','linewidth':2},
        startangle=90)
plt.title("Students Marks Distribution")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


## Histoplot
marks=[45,50,55,60,62,65,67,70,72,75,78,80,82,85,88,90,92,95,97,100]

# max = 100
# min = 45
# diff = 55
# bins = 55 / 5 = 11
# bin1 = 45 - 56 = 3 (45 included, 56 excluded)
# bin2 = 56 - 67 = 3 (56 included, 67 excluded)
# bin3 = 67 - 78 = 4 (67 included, 78 excluded)
# bin4 = 78 - 89 = 5 (78 included, 89 excluded)
# bin5 = 89 - 100 = 5 (89 included, 100 included)

plt.figure(figsize=(8,6))
plt.hist(marks,
         bins=5,
         color='skyblue',
         edgecolor='black')
plt.title("Students Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Fequency")
plt.show()


# Scatter plot (Graphs in school)
hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 50, 60, 70, 85]
plt.figure(figsize=(8,6))
plt.scatter(hours,
            marks,
            s=200,
            color='red',
            marker='o',
            edgecolors='black',
            alpha=0.7)
plt.grid(True)
plt.title("Students ku kais haula banana")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()


## Area graph

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 200, 180, 250]

plt.fill_between(months, sales)

plt.title("Monthly Sales Area Graph")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()



## combining multiple graphs

# Graph 1
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
x = [1,2,3,4]
y = [10,20,30,40]
plt.plot(x,y)

# Graph 2
plt.subplot(2,2,2)
plt.bar(x,y)

# Graph 3
plt.subplot(2,2,3)
marks=[45,50,55,60,62,65,67,70,72,75,78,80,82,85,88,90,92,95,97,100]
plt.hist(marks,
         bins=5,
         color='skyblue',
         edgecolor='black')

# Graph 4
plt.subplot(2,2,4)
hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 50, 60, 70, 85]
plt.scatter(hours,
            marks,
            s=200,
            color='red',
            marker='o',
            edgecolors='black',
            alpha=0.7)

plt.show()



