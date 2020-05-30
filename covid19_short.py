import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

source = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx"
#source = "/home/lramos/Downloads/COVID-19-geographic-disbtribution-worldwide.xlsx"


data = pd.read_excel(source)

country = "Switzerland"
selected_data = data.sort_values(by=['dateRep'])
selected_data = selected_data[selected_data['countriesAndTerritories']==country]
selected_data['total_cases'] = selected_data['cases'].cumsum()
chart = country + ' - covid19 - daily cases / deaths - 2019-12-31 - ' + str(date.today())
selected_data.plot(kind='line',x='total_cases',y=['cases','deaths'],color=['red','blue'], \
                   title=chart, logx=True, logy=True)
plt.show()