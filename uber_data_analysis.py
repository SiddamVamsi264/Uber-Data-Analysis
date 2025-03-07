#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
import os

#Loading DataSet

df = pd.read_csv("C:/Users/Sidda/OneDrive/Desktop/Python EDA/UberDataset.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.dtypes)
print(df.info())

# Data Preprocessing

#dropping rows
df.drop(df[df['END_DATE'].isnull()].index, inplace=True)
print(df.isnull().sum())
print(df.info())


#Filling Null Values with key word
df['PURPOSE'].fillna("NOT")


#Checking Duplicates
#print(df[df.duplicated()])
df.drop(df[df.duplicated()].index,axis=0,inplace=True)
print(df[df.duplicated()])
print(df.head())

#converting datetime
df['START_DATE'] = pd.to_datetime(df['START_DATE'], errors='coerce', dayfirst=True)
df['END_DATE'] = pd.to_datetime(df['END_DATE'], errors='coerce', dayfirst=True)

print(df.dtypes)
from datetime import datetime

df['date'] = pd.DatetimeIndex(df['START_DATE']).date
df['time'] = pd.DatetimeIndex(df['START_DATE']).hour

#changing into categories of day and night
df['day-night'] = pd.cut(x=df['time'],
                              bins = [0,10,15,19,24],
                              labels = ['Morning','Afternoon','Evening','Night'])

print(df.head())




#Data Exploration




plt.figure(figsize=(10, 5))

# Subplot 1: CATEGORY (y-axis)
plt.subplot(1, 2, 1)
sns.countplot(y=df['CATEGORY'])  # Use y instead of x
plt.yticks(rotation=0)  # Rotate y-axis labels (optional)
plt.show()

# # Subplot 2: PURPOSE (y-axis)
plt.subplot(1, 2, 2)
sns.countplot(y=df['PURPOSE'])  # Use y instead of x
plt.yticks(rotation=0)  # Rotate y-axis labels (optional)
plt.show()

# # Countplot for day-night (y-axis)
sns.countplot(y=df['day-night'])  # Use y instead of x
plt.yticks(rotation=0)  # Rotate y-axis labels (optional)
plt.show()

plt.figure(figsize=(15, 5))
sns.countplot(data=df, x='PURPOSE', hue='CATEGORY')
plt.xticks(rotation=90)
plt.show()



(df['CATEGORY'].unique())
df[["CATEGORY","MILES"]].groupby(["CATEGORY"]).agg(NO_OF_MILES=("MILES","sum"))

plt.figure()
df[["CATEGORY","MILES"]].groupby(["CATEGORY"]).agg(NO_OF_MILES=("MILES","sum")).plot(kind='bar')
plt.xlabel('Categories')
plt.ylabel('Number of MILES')
plt.title('Categories vs. Number of MILES')
plt.show()
# Checking for unique values
print(len(df['START'].unique()))

# Checking Top 10 start points
plt.figure()
df["START"].value_counts(ascending=False)[:10].plot(kind='barh')
plt.xlabel("Pickup Count")
plt.ylabel("Places")
plt.title("Top 10 Pickup Places")
plt.show()
print(len(df["STOP"].unique()))
#
plt.figure()
df["STOP"].value_counts(ascending=False)[:10].plot(kind='barh')
plt.xlabel("Drop Count")
plt.ylabel("Places")
plt.title("Top 10 Dropped Places")
plt.show()

print((df[df["STOP"]=="Unknown Location"]['STOP'].value_counts()))

print(df.describe().T)

df.groupby(['START','STOP'])['MILES'].sum().sort_values(ascending=False)[1:11]

def is_roundtrip(df):
    if df["START"] == df["STOP"]:
        return 'YES'
    else:
        return 'NO'
df["Round_Trip"] = df.apply(is_roundtrip, axis=1)
sns.countplot(x="Round_Trip", data=df,order = df["Round_Trip"].value_counts().index)
plt.show()