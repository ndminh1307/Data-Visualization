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

df_can_t = df_can[years].transpose()
df_can_t.index = map(int, df_can_t.index)
df_can_t.index.name = 'Year'
df_can_t.reset_index(inplace=True)
print(df_can_t.head())

#normalize Brazil data
norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min())/(df_can_t['Brazil'].max() - df_can_t['Brazil'].min())
#normalize Argentina data
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min())/(df_can_t['Argentina'].max() - df_can_t['Argentina'].min())

ax0 = df_can_t.plot(kind='scatter', x='Year', y='Brazil', figsize=(14,8), alpha=0.5, color='green', s = norm_brazil *2000 + 10, xlim=(1975,2015))
ax1 = df_can_t.plot(kind='scatter', x='Year', y='Argentina', alpha=0.5, color='blue', s=norm_argentina * 2000 +10, ax = ax0)
ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina to Canada')
ax0.legend(['Brazil', 'Argentina'], loc = 'upper left')
plt.show()

