# the anscombe dataset can be found in the seaborn library
import seaborn as sns
anscombe = sns.load_dataset("anscombe")
print(anscombe)

import matplotlib.pyplot as plt

# create a subset of the data
# contains only dataset 1 from anscombe
dataset_1 = anscombe[anscombe['dataset'] == 'I']

plt.plot(dataset_1['x'], dataset_1['y'])

plt.plot(dataset_1['x'], dataset_1['y'], 'o')

# create subsets of the anscombe data
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

# create the entire figure where our subplots will go
fig = plt.figure()

# tell the figure how the subplots should be laid out
# in the example below we will have
# 2 row of plots, each row will have 2 plots

# subplot has 2 rows and 2 columns, plot location 1
axes1 = fig.add_subplot(2, 2, 1)

# subplot has 2 rows and 2 columns, plot location 2
axes2 = fig.add_subplot(2, 2, 2)

# subplot has 2 rows and 2 columns, plot location 3
axes3 = fig.add_subplot(2, 2, 3)

# subplot has 2 rows and 2 columns, plot location 4
axes4 = fig.add_subplot(2, 2, 4)

# add a plot to each of the axes created above
axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

fig.savefig('ch-0300-intro_plotting/figures/anscombe_mpl')

# add a small title to each subplot
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

# add a title for the entire figure
fig.suptitle("Anscombe Data")

fig.savefig('ch-0300-intro_plotting/figures/anscombe_mpl_labeled')




#########
# Seaborn
#########

import seaborn as sns

tips = sns.load_dataset("tips")

hist = sns.distplot(tips['total_bill'])
hist.set_title('Total Bill Histogram with Density Plot')

hist = sns.distplot(tips['total_bill'], kde=False)
hist.set_title('Total Bill Histogram')
hist.set_xlabel('Total Bill')
hist.set_ylabel('Frequency')

den = sns.distplot(tips['total_bill'], hist=False)
den.set_title('Total Bill Density')
den.set_xlabel('Total Bill')
den.set_ylabel('Unit Probability')

hist_den_rug = sns.distplot(tips['total_bill'], rug=True)
hist_den_rug.set_title('Total Bill Histogram with Density and Rug Plot')
hist_den_rug.set_xlabel('Total Bill')

count = sns.countplot('day', data=tips)
count.set_title('Count of days')
count.set_xlabel('Day of the Week')
count.set_ylabel('Frequency')

scatter = sns.regplot(x='total_bill', y='tip', data=tips)
scatter.set_title('Scatterplot of Total Bill and Tip')
scatter.set_xlabel('Total Bill')
scatter.set_ylabel('Tip')

sns.lmplot(x='total_bill', y='tip', data=tips)

scatter = sns.jointplot(x='total_bill', y='tip', data=tips)
scatter.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
# add a title, set font size, and move the text above the total bill axes
scatter.fig.suptitle('Joint plot of Total Bill and Tip',
                     fontsize=20, y=1.03)

hex = sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
hex.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hex.fig.suptitle('Hexbin Joint plot of Total Bill and Tip',
                 fontsize=20, y=1.03)

kde = sns.kdeplot(data=tips['total_bill'],
                  data2=tips['tip'],
		  shade=True) # shade will fill in the contours
kde.set_title('Kernel Density Plot of Total Bill and Tip')
kde.set_xlabel('Total Bill')
kde.set_ylabel('Tip')

kde_joint = sns.jointplot(x='total_bill', y='tip',
                          data=tips,
			  kind='kde')

bar = sns.barplot(x='time', y='total_bill', data=tips)
bar.set_title('Barplot of average total bill for time of day')
bar.set_xlabel('Time of day')
bar.set_ylabel('Average total bill')

box = sns.boxplot(x='time', y='total_bill', data=tips)
box.set_title('Box plot of total bill by time of day')
box.set_xlabel('Time of day')
box.set_ylabel('Total Bill')

violin = sns.violinplot(x='time', y='total_bill', data=tips)
violin.set_title('Violin plot of total bill by time of day')
violin.set_xlabel('Time of day')
violin.set_ylabel('Total Bill')

sns.pairplot(tips)

pair_grid = sns.PairGrid(tips)
# can also use plt.scatter instead of sns.regplot
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug=True)

violin = sns.violinplot(x='time', y='total_bill',
                        hue='sex', data=tips,
			split=True)

# note I'm using lmplot instead of regplot here
scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False)

sns.pairplot(tips, hue='sex')

scatter = sns.lmplot(x='total_bill', y='tip', data=tips,
                     fit_reg=False,
                     hue='sex',
                     scatter_kws={'s': tips['size']*10})

scatter = sns.lmplot(x='total_bill', y='tip', data=tips,
                     fit_reg=False, hue='sex', markers=['o', 'x'],
		                 scatter_kws={'s': tips['size']*10})

anscombe = sns.lmplot(x='x', y='y', data=anscombe, fit_reg=False,
                      col='dataset', col_wrap=2)

# create the FacetGrid
facet = sns.FacetGrid(tips, col='time')
# for each value in time, plot a histogram of total bill
facet.map(sns.distplot, 'total_bill', rug=True)

facet = sns.FacetGrid(tips, col='day', hue='sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()

sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False,
           hue='sex', col='day')

facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet.map(plt.scatter, 'total_bill', 'tip')

sns.factorplot(x='day', y='total_bill', hue='sex', data=tips,
               row='smoker', col='time', kind='violin')
