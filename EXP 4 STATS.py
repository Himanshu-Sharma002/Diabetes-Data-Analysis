#EXPERIMENT 4

#WORKING ON DIABETES DATASET

import pandas as pd  #IMPORTING LIBRARIES


df = pd.read_csv("diabetes.csv")

#SHAPE (ROWS AND COLUMNS)
print("Shape of dataset (Rows, Columns):")
print(df.shape)

print("\n----------------------------------------------\n")

#COLUMN NAMES
print("\nColumn Names:")
print(df.columns)

print("\n----------------------------------------------\n")

#FIRST 5 ROWS
print("\nFirst 5 Rows (HEAD):")
print(df.head())

print("\n----------------------------------------------\n")

#LAST 5 ROWS
print("\nLast 5 Rows (TAIL):")
print(df.tail())

print("\n----------------------------------------------\n")

#DESCRIBE
print("Describe:")
print(df.describe())

print("\n----------------------------------------------\n")

#MEAN
print("\nMean:")
print(df.mean())

print("\n----------------------------------------------\n")

#MEDIAN
print("\nMedian:")
print(df.median())

print("\n----------------------------------------------\n")

#MODE
print("\nMode:")
print(df.mode().iloc[0])

print("\n----------------------------------------------\n")

#MINIMUM VALUES
print("\nMinimum Values:")
print(df.min())

print("\n----------------------------------------------\n")

#MAXIMUM VALUES
print("\nMaximum Values:")
print(df.max())

print("\n----------------------------------------------\n")

#STANDARD DEVIATION
print("\nStandard Deviation:")
print(df.std())

print("\n----------------------------------------------\n")

#VARIANCE
print("\nVariance:")
print(df.var())

print("\n----------------------------------------------\n")

#MISSING VALUES
print("Missing Values:")
print(df.isnull().sum())

print("\n----------------------------------------------\n")

#UNIQUE VALUES IN EACH COLUMN
print("\nUnique Values Count:")
print(df.nunique())

print("\n----------------------------------------------\n")


