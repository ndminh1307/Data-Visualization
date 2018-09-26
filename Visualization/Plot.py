import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20),skipfooter=2)
years = list(map(str, range(1980, 2014)))

#Delete the columns
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis = 1, inplace = True)

#Rename the columns
df_can.rename(columns = {'OdName':'Country', 'Area':'Continent', 'RegName':'Region'}, inplace = True)

#Ensure that all column label of type string
print(all(isinstance(column,str) for column in df_can.columns)) #return False

df_can.columns = list(map(str, df_can.columns))
print(all(isinstance(column,str) for column in df_can.columns)) #return True

#Set Country as index
df_can.set_index('Country', inplace=True)

#Add 'Total' columns
df_can['Total'] = df_can.sum(axis = 1)

#Sort 'Total'
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

#Get top 5 entries
df_top5 = df_can.head()
#Transpose (chuyen vi) the dataframe
df_top5 = df_top5[years].transpose()
print(df_top5)

#AREA PLOTS
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='area', alpha=0.25, stacked=False, figsize=(20, 10))
plt.title('Immigrantion Trend of Top 5 Country')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

#Histogram of Numpy
df_can['2013'].head()
count, bin_edges = np.histogram(df_can['2013'])
print(count)
print(bin_edges)
df_can['2013'].plot(kind='hist', figsize=(8,5))

plt.title('Histogram of Immigration from 195 countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of Immigrants')

plt.show()

#Bar charts
df_iceland = df_can.loc['Iceland',years]
print(df_iceland.head())
df_iceland.plot(kind='bar', figsize=(10,6))

plt.title('Iceland Immigrants to Canada from 1980 to 2013')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.annotate('', xy=(32,70),xytext=(28,20),xycoords='data',arrowprops=dict(arrowstyle='->', connectionstyle='arc3',color='blue',lw=2))
plt.show()