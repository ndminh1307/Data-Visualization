import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')

df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20),skipfooter=2)
#clean up dataset and remove unnecessary columns
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
#rename columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
#make all column labels of type str
df_can.columns = list(map(str, df_can.columns))
#set country as index
df_can.set_index('Country', inplace=True)
#add total column
df_can['Total'] = df_can.sum(axis=1)
#years
years = list(map(str, range(1980,2014)))

#PIE CHARTS
#groupby method to summarize the immigration data by 'Continent'
df_continents = df_can.groupby('Continent', axis=0).sum()

#plot
colors_list = ['gold', 'yellowgreen','lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]
df_continents['Total'].plot(kind='pie', figsize=(15,6), autopct='%1.1f%%', startangle=90, shadow=True, labels=None, pctdistance=1.12, colors=colors_list, explode=explode_list)

plt.title('Immigration to Canada by Continent 1980-2013',y=1.12)
plt.axis('equal') #set pie chart to look like circle
plt.legend(labels=df_continents.index, loc='upper left')

plt.show()