import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')

df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20),skipfooter=2)
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df_can.rename(columns = {'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)
years = list(map(str, range(1980,2014)))

#Create df_countries dataframe
df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
#Create df_total by summing across 3 countries for each year
df_total = pd.DataFrame(df_countries.sum(axis=1))

#reset index in place
df_total.reset_index(inplace=True)
#rename columns
df_total.columns = ['year', 'total']

#change column year from str to int
df_total['year'] = df_total['year'].astype(int)
#df.loc[index, column_name]
x = df_total['year']
y = df_total['total']
fit = np.polyfit(x,y, deg=1)

df_total.plot(kind='scatter', x='year', y='total', figsize=(10,6), color='darkblue')
plt.title('Total immigration to Canada by Denmark, Norway and Sweden from 1980 to 2013')
plt.xlabel('Year')
plt.ylabel('Number of immigrants')

plt.plot(x, fit[0]*x+fit[1],color='red')
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000,150000))
plt.show()