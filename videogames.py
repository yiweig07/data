import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')
genres= df.Genre.value_counts()
gen = df['Genre']
gen = gen.drop_duplicates(keep = 'first', inplace = False).reset_index(drop=True)
i = 0
genre_sale = []
g_error = []
while i < len(gen):
    g1= df.loc[df['Genre'].isin([str(gen[i])])]
    g1_sale = g1['Global_Sales'].sum()
    g_error.append(np.std(g1['Global_Sales']))
    genre_sale.append(g1_sale)
    i += 1

yearrelease = df['Year_of_Release'].dropna().apply(np.int64)
year = yearrelease.sort_values(ascending = True, inplace = False, kind = 'quicksort')
year = year.drop_duplicates(keep = 'first', inplace = False).reset_index(drop=True)
i = 0
year_sale = []
y_error = []
while i < len(year):
    y = df.loc[df['Year_of_Release'].isin([str(year[i])])]
    y_sale = y['Global_Sales'].sum()
    y_error.append(np.std(y['Global_Sales']))
    year_sale.append(y_sale)
    i += 1

plt.rcdefaults()
fig, ax = plt.subplots()
x = gen
y_pos = np.arange(len(gen))
error = g_error

ax.barh(y_pos, genre_sale, xerr = error, align = 'center')
ax.set_yticks(y_pos)
ax.set_yticklabels(gen)
ax.invert_yaxis()
ax.set_xlabel('Global_Sales')
ax.set_ylabel('Genres')
ax.set_title('Global Sales for Game Genres')
plt.show()

##
x= np.arange(len(year))
width = 0.35
fig,ax = plt.subplots()
ax.bar(x, year_sale, width)
ax.set_ylabel('Global_Sales')
ax.set_xlabel('Year')
ax.set_title('Global_Sales vs Year')
ax.set_xticks(x)
ax.set_xticklabels(year)
for label in plt.gca().xaxis.get_ticklabels()[::2]:
                label.set_visible(False)
plt.show()
