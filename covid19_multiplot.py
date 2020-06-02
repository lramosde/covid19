import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

source = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"
data = pd.read_excel(source)
data = data.sort_values(by=['dateRep'])

# select the country (in English), e.g. United_States_of_America
countries = ['Italy', 'Greece', 'Portugal', 'Spain', 'France', 'United_Kingdom', 'Ireland', 
             'Belgium', 'Netherlands', 'Switzerland', 'Austria', 'Germany', 
             'Denmark', 'Sweden', 'Brazil', 'Ecuador', 'United_States_of_America', 
             'Turkey', 'Russia', 'India', 'China',  'South_Korea', 
             'Japan', 'Australia', 'New_Zealand'    ]

num_rows = int( m.ceil( m.sqrt( len(countries) )         ) ) 
num_cols = int( m.ceil(         len(countries) / num_rows) ) 
if num_rows * num_cols < len(countries)  : 
   num_cols = num_cols +1

fig = plt.figure()

plt.suptitle('Covid19 - daily cases (red) / deaths (blue) - 2019-12-31 - ' + str(date.today()))
count = 1
for country in countries:
  selected_data = data[data['countriesAndTerritories']==country]
  selected_data['total_cases'] = selected_data['cases'].cumsum()
#   selected_data['per_hundred_thousand'] = 1.0e5 * selected_data['cases'].cumsum() / selected_data['popData2018']
#  chart = country + ' - covid19 - daily cases (red) / deaths (blue) - 2019-12-31 - ' + str(date.today())
  chart = country
  ax = fig.add_subplot(num_rows,num_cols,count)
  ax.set_aspect('equal')
  plt.subplots_adjust(hspace=1)
  selected_data.plot(kind='line',
                     x='total_cases', y=['cases','deaths'],
#                      x='per_hundred_thousand', y=['cases','deaths'],
                     color=['red','blue'], 
                     title=chart, 
#                     fontsize=8, 
                     logx=True, logy=True,
#                     logx=False, logy=True,
                     ax = ax, 
                     xlim=(1,10000000),ylim=(1,10000000))
  count = count +1
#  if count > 2 :
  ax.legend().remove()
# fig.tight_layout()
plt.show()
