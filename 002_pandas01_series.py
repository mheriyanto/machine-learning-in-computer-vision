# Link: https://github.com/mheriyanto/Data-Science
# Ref: Python Data Science Handbook (J. Vanderplas. 2018. O'Reilly Media. ISBN-13: 978-1491912058)
# Series

import pandas as pd
# simple data
data1 = pd.Series([0.25, 0.5, 0.75, 1.0])
data2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# buat librari populasi
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)
# buat librari area
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
# menggabungkan populasi dan area
states = pd.DataFrame({'population': population,
                       'area': area})

print(states)

