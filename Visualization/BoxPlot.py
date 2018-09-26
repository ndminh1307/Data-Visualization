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

#BOX PLOT
#get dataframe, place extra square bracket around 'Japan'
df_japan = df_can.loc[['Japan'], years].transpose()

df_japan.plot(kind='box', figsize=(8,6))
plt.title('Box plot of Japanese Immigrants')
plt.ylabel('Number of Immigrants')

plt.show()
