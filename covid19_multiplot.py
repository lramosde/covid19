import pandas as pd
import math as m
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

#source = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"
# new data source. The data tracking stopped on December 14th, 2020
source = "https://covid.ourworldindata.org/data/owid-covid-data.xlsx"
data = pd.read_excel(source)
data = data.sort_values(by=['date'])

# select the country (in English), e.g. United_States_of_America
countries = ['Italy', 'Greece', 'Portugal', 'Spain', 'France', 'United Kingdom', 'Ireland', 
             'Belgium', 'Netherlands', 'Switzerland', 'Austria', 'Germany', 
             'Denmark', 'Sweden', 'Brazil', 'Peru', 'United States', 
             'Turkey', 'Russia', 'India', 'China',  'South Korea', 
             'Japan', 'Australia', 'New Zealand'    ]

num_rows = int( m.ceil( m.sqrt( len(countries) )         ) ) 
num_cols = int( m.ceil(         len(countries) / num_rows) ) 
if num_rows * num_cols < len(countries)  : 
   num_cols = num_cols +1

fig = plt.figure()

plt.suptitle('Covid19 - daily cases (red) / deaths (blue) per million - 2020-01-01 - ' + str(date.today()))
count = 1
for country in countries:
  selected_data = data[data['location']==country]
  selected_data['deaths']            = 1.0e6 * selected_data['new_deaths'] / selected_data['population']
  selected_data['total_per_million'] = 1.0e6 * selected_data['new_cases'].cumsum() / selected_data['population']
  selected_data['cases']             = 1.0e6 * selected_data['new_cases']          / selected_data['population']
  chart = country
  ax = fig.add_subplot(num_rows,num_cols,count)
#  ax.set_aspect('equal')
#  ax.xaxis.set_major_locator(plt.MaxNLocator(4))
#  ax.yaxis.set_major_locator(plt.MaxNLocator(4))
  selected_data.plot(kind='line',
#                     x='total_cases', y=['cases','deaths'],
                      x='total_per_million', y=['cases','deaths'],
                     color=['red','blue'], 
                     title=chart, 
                     fontsize=8, 
                     logx=True, logy=True,
#                     logx=False, logy=True,
                     ax = ax,
                     xlim=(1.0e-3,1.0e5),ylim=(1.0e-3,5.0e3))
#                     xlim=(1e-10,1e-4),ylim=(1e-8,1e-4))
  count = count +1
#  if count > 2 :
  ax.legend().remove()
  fig.subplots_adjust(hspace=0.9)
#  fig.tight_layout()
plt.show()