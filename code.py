# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total': 'Total_Medals'},inplace = True)
data.head(10)


# --------------
data["Better_Event"] = np.where(data.Total_Summer> data.Total_Winter,"Summer",
    np.where(data.Total_Summer==data.Total_Winter,"Both","Winter"))
better_event = data["Better_Event"].value_counts().index[0]


# --------------
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]

def top_ten(df, col_name):
    
    country_list= list((df.nlargest(10,col_name)['Country_Name']))
    return country_list

top_10_summer = top_ten(top_countries, "Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter")
top_10 = top_ten(top_countries, "Total_Medals")

print(top_10_summer)
print(top_10_winter)
print(top_10)

common = list()
for col in top_10:
    if col in top_10_summer and col in top_10_winter:
        common.append(col)


# --------------
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.groupby(["Country_Name","Total_Summer"])[["Total_Summer"]].count().plot(kind = "bar")
plt.show()


# --------------
#Code starts 
summer_df['Golden_Ratio'] = data['Gold_Summer']/data['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
print(summer_max_ratio)

summer_country_gold = (summer_df[summer_df.Golden_Ratio == summer_max_ratio].Country_Name).iloc[0]


winter_df['Golden_Ratio'] = data['Gold_Winter']/data['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
print(winter_max_ratio)
winter_country_gold = (winter_df[winter_df.Golden_Ratio == winter_max_ratio].Country_Name).iloc[0]


top_df['Golden_Ratio'] = data['Gold_Total']/data['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = (top_df[top_df.Golden_Ratio == top_max_ratio].Country_Name).iloc[0]



# --------------
#Code starts here
data_1 = data[:-1]




data_1['Total_Points'] = 3*data['Gold_Total'] + 2*data['Silver_Total'] + data['Bronze_Total']

most_points = data_1['Total_Points'].max()
best_country = (data_1[data_1['Total_Points']== most_points].Country_Name).iloc[0]



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar')
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)



