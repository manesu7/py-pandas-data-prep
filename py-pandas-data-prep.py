import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pandas project 1: Flights, loading data


df = pd.read_csv('flights.csv')
print(df.head(10))

print(df.info())

print(df.isnull().sum())

print(df.describe())
print(df.describe().round(2))
print(df['Origin'].value_counts())

print(df['Origin'].unique())
print(df['Origin'].nunique())

