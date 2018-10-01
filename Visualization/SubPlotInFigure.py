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

df_CI = df_can.loc[['China', 'India'], years].transpose()
print(df_CI.head())

fig = plt.figure()
ax0 = fig.add_subplot(1,2,1) #fig.add_subplot(nrows, ncolumns, plot_number)
ax1 = fig.add_subplot(1,2,2)
#box plot - subplot 1
df_CI.plot(kind='box', color='blue', vert=False, ax = ax0)
ax0.set_title('Box plot of Chinese and Indians Immigrants from 1980 to 2013')
ax0.set_xlabel('Number of immigrants')
ax0.set_ylabel('Countries')

#line plot - subplot 2
df_CI.plot(kind='line', figsize=(20,6), ax = ax1)
ax1.set_title('Line plots of Immigrants from China and India to Canada 1980-2013')
ax0.set_xlabel('Number of immigrants')
ax0.set_ylabel('Countries')

plt.show()


