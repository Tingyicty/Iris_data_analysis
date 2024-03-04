import matplotlib.pyplot as plt
import numpy as np

# Setting constants
iris_dict = {'setosa': [[], [], [], []], 'versicolor': [[], [], [], []],
             'virginica': [[], [], [], []]}
data_order = ('Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width')
iris_name = ('setosa', 'versicolor', 'virginica')
colors = ('blue', 'orange', 'green')

# Reading and storing the data
fobj = open('iris_data.txt', 'r')
for line in fobj:
    line = line.strip('\n')
    line_list = line.split(',')
    for iris in iris_dict:
        if line_list[-1].endswith(iris):
            for i in range(4):
                iris_dict[iris][i].append(float(line_list[i]))
fobj.close()





# Creating a plot with 4 * 4 subplots
figure, axis = plt.subplots(4, 4)
for i in range(4):
    for j in range(4):
        if i == j:
            axis[i, j].text(0.1, 0.45, data_order[i], fontsize = 10)
        else:
            for key in iris_dict:
                axis[i, j].scatter(iris_dict[key][j], iris_dict[key][i], s = 3)

plt.show()





for i in range(4):
    box_data = []
    for key in iris_dict:
        box_data.append(iris_dict[key][i])
    bplot = plt.boxplot(box_data, widths = 0.8, patch_artist = True)
    plt.xticks([1, 2, 3], iris_name)
    plt.xlabel('Iris Species')
    plt.ylabel(data_order[i])
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    plt.show()





# Helper function for linear regression
def betas(x, y):
    n = len(x)
    x_sum = sum(x)
    y_sum = sum(y)
    xy_sum = 0
    x_sqr_sum = 0
    x_mean = x_sum / n
    y_mean = y_sum / n
    for i in range(n):
        xy_sum += x[i] * y[i]
        x_sqr_sum += (x[i]) ** 2
    beta1 = (xy_sum - (y_sum * x_sum) / n) / (x_sqr_sum - ((x_sum) ** 2) / n)
    beta0 = y_mean - beta1 * x_mean
    return(beta0, beta1)

def linear_regression_function(x, beta0, beta1):
    y = []
    for i in range(len(x)):
        y.append(beta0 + beta1 * x[i])
    return y

# Create the scatter plots and the legend
for key in iris_dict:
    x = iris_dict[key][3]
    y = iris_dict[key][2]
    plt.scatter(x, y, s=15)
plt.legend(iris_name)

# Two empty list to store the overall data
all_petal_width = []
all_petal_length = []

# Add the linear regression lines to the scatter plots
for key in iris_dict:
    x = iris_dict[key][3]
    y = iris_dict[key][2]
    all_petal_width += x
    all_petal_length += y
    beta0, beta1 = betas(x, y)
    regression_y = linear_regression_function(x, beta0, beta1)
    plt.plot(x, regression_y)

# Create the overall regression line
beta0, beta1 = betas(all_petal_width, all_petal_length) # 1.0906, 2.2259
regression_y = linear_regression_function(all_petal_width, beta0, beta1)
plt.plot(all_petal_width, regression_y, c = 'black')

plt.xlabel(data_order[3])
plt.ylabel(data_order[2])
plt.title('Petal Width vs. Petal Length')
plt.show()


# Storing the overall width and length, no matter the type of iris
all_width_length = [[], [], [], []]
for key in iris_dict:
    for i in range(4):
        all_width_length[i].append(iris_dict[key][i])
all_width_length_dict = dict(zip(data_order, all_width_length))





# Output of the descriptive statistics
i = 0
for key in all_width_length_dict:
    data = all_width_length_dict[key]
    name = data_order[i]
    Min = np.min(data)
    q1 = np.percentile(data, 25)
    median = np.median(data)
    mean = np.mean(data)
    q3 = np.percentile(data, 75)
    Max = np.max(data)
    print("%s\nMin %13.3f\n1st Qu %10.3f\nMedian %10.3f\nMean %12.3f\n3rd Qu %10.3f\nMax %13.3f\n"
          % (name, Min, q1, median, mean, q3, Max))
    i += 1

