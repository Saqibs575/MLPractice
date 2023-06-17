from typing import List
import seaborn , pandas
from matplotlib import pyplot
df = pandas.read_csv('/config/workspace/notebooks/data/Diamond.csv')
seaborn.histplot(data = df , x = 'z' , kde = True)
pyplot.show()
