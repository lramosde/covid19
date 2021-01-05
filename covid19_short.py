import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

#source = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"
#source = "/home/lramos/Downloads/COVID-19-geographic-disbtribution-worldwide.xlsx"
source = "https://covid.ourworldindata.org/data/owid-covid-data.xlsx"

data = pd.read_excel(source)

country = "United States"
selected_data = data.sort_values(by=['date'])
selected_data = selected_data[selected_data['location']==country]
selected_data['deaths']            = 1.0e6 * selected_data['new_deaths']         / selected_data['population']
selected_data['total_per_million'] = 1.0e6 * selected_data['new_cases'].cumsum() / selected_data['population']
selected_data['cases']             = 1.0e6 * selected_data['new_cases']          / selected_data['population']
chart = country + ' - covid19 - daily cases / deaths - 2020-01-01 - ' + str(date.today())
selected_data.plot(kind='line',x='total_per_million',y=['cases','deaths'],color=['red','blue'], \
                   title=chart, logx=True, logy=True)
plt.show()