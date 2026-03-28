#EXPERIMENT 4
#GRAPHS OF DIABETES DATASET

import pandas as pd   #IMPORTING ALL LIBRARIES
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv("diabetes.csv")

#--------------------------------------------------------------------
#BAR CHART (Pregnancies)

preg_counts = df["Pregnancies"].value_counts().sort_index()

plt.figure()
plt.bar(preg_counts.index, preg_counts.values)
plt.xlabel("Pregnancies")
plt.ylabel("Frequency")
plt.title("Bar Chart - Pregnancies")
plt.show()

#--------------------------------------------------------------------

#HORIZONTAL BAR (Glucose)

glucose_counts = df["Glucose"].value_counts().sort_index()

plt.figure()
plt.barh(glucose_counts.index, glucose_counts.values)
plt.xlabel("Frequency")
plt.ylabel("Glucose")
plt.title("Horizontal Bar Chart - Glucose")
plt.show()


#--------------------------------------------------------------------
#PARETO CHART (BloodPressure)

bp_counts = df["BloodPressure"].value_counts().sort_values(ascending=False)
cumulative = bp_counts.cumsum() / bp_counts.sum() * 100

fig, ax1 = plt.subplots()
ax1.bar(bp_counts.index, bp_counts.values)
ax1.set_ylabel("Frequency")
plt.xticks(rotation=90)

ax2 = ax1.twinx()
ax2.plot(bp_counts.index, cumulative)
ax2.set_ylabel("Cumulative %")

plt.title("Pareto Chart - BloodPressure")
plt.show()

#--------------------------------------------------------------------

#HISTOGRAM (SkinThickness)

plt.figure()
plt.hist(df["SkinThickness"], bins=10)
plt.xlabel("SkinThickness")
plt.ylabel("Frequency")
plt.title("Histogram - SkinThickness")
plt.show()



#FREQUENCY POLYGON (Insulin)

counts_ins, bins_ins = np.histogram(df["Insulin"], bins=10)
mid_points = (bins_ins[:-1] + bins_ins[1:]) / 2

plt.figure()
plt.plot(mid_points, counts_ins)
plt.xlabel("Insulin")
plt.ylabel("Frequency")
plt.title("Frequency Polygon - Insulin")
plt.show()



#OGIVE CURVE (BMI)

counts_bmi, bins_bmi = np.histogram(df["BMI"], bins=10)
cumulative_bmi = np.cumsum(counts_bmi)

plt.figure()
plt.plot(bins_bmi[:-1], cumulative_bmi)
plt.xlabel("BMI")
plt.ylabel("Cumulative Frequency")
plt.title("Ogive Curve - BMI")
plt.show()


#--------------------------------------------------------------------
#SEABORN HISTOGRAM (Age)

plt.figure()
sns.histplot(df["Age"], bins=10, kde=True)
plt.title("Seaborn Histogram - Age")
plt.show()

#--------------------------------------------------------------------

#HISTOGRAM (DiabetesPedigreeFunction)

plt.figure()
plt.hist(df["DiabetesPedigreeFunction"], bins=10)
plt.xlabel("DiabetesPedigreeFunction")
plt.ylabel("Frequency")
plt.title("Histogram - DiabetesPedigreeFunction")
plt.show()

#--------------------------------------------------------------------

# PIE CHART (Outcome)

outcome_counts = df["Outcome"].value_counts()

plt.figure()
plt.pie(outcome_counts.values, labels=["No Diabetes","Diabetes"], autopct="%1.1f%%")
plt.title("Pie Chart - Outcome")
plt.show()

# Heatmap (Correlation Matrix)

plt.figure(figsize=(10,8))
corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Box Plot for Glucose

plt.figure()
sns.boxplot(y=df['Glucose'])
plt.title("Box Plot of Glucose")
plt.show()
