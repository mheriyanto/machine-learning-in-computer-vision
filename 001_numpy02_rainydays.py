# Link: https://github.com/mheriyanto/Data-Science
# Ref: Python Data Science Handbook (J. Vanderplas. 2018. O'Reilly Media. ISBN-13: 978-1491912058)
# Counting Rainy Days
import matplotlib.pyplot as plt
import pandas as pd
import seaborn
seaborn.set()
# use Pandas to extract data
rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254
inches.shape
plt.hist(inches, 40)
plt.show()
