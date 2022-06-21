import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
tips = sns.load_dataset('tips')
tips.head()
print(tips)
sns.distplot(tips['total_bill'], kde=False,bins =40)
sns.jointplot(x='total_bill',y='tip',data=tips, kind='kde')
sns.pairplot(tips,hue='sex', palette= 'coolwarm')
sns.rugplot(tips['total_bill'])
plt.show()

#CAREGORICAL PLOTS
sns.barplot(x='sex',y='total_bill',data=tips, estimator=np.std)
plt.show()

sns.boxplot(x='day', y='total_bill', data=tips, hue = 'smoker')
plt.show()

sns.violinplot(x='day', y='total_bill', data = tips, hue='sex', split = True)
plt.show()

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True, hue = 'sex', split=True)
plt.show()

sns.violinplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, color='white')
plt.show()

sns.factorplot(x='day', y='total_bill', data=tips, kind = 'bar')

#MATRIX PLOTS
flights = sns.load_dataset('flights')
flights.head()
tc = tips.corr()
sns.heatmap(tc)
plt.show()

fp = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fp, cmap='magma', linecolor= 'white', linewidths=3)
plt.show()

sns.clustermap(fp, cmap = 'coolwarm', standard_scale=1)

#GRIDS
iris = sns.load_dataset('iris')
iris.head()
#g = sns.PairGrid(iris)
#g.map_diag(sns.distplot)
#g.map_upper(plt.scatter)
#g.map_lower(sns.kdeplot)

g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')
plt.show()


