# Databricks notebook source
import pandas as pd

# Load wine data
data = pd.read_csv("/dbfs/databricks-datasets/wine-quality/winequality-white.csv", sep=";")

# Remove spaces from column names
data.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

# COMMAND ----------

# MAGIC %run ./featurization

# COMMAND ----------

continousToBinary(data, "pH")

# COMMAND ----------

# Only consider brut and no sulphur added wines

data = data[data['free_sulfur_dioxide'] <= 15]
data = data[data['residual_sugar'] <= 2]


# COMMAND ----------

import seaborn as sns

# COMMAND ----------

# Visualize relationship between high fixed acidity and other wine attributes 
import matplotlib.pyplot as plt

dims = (3, 4)

f, axes = plt.subplots(dims[0], dims[1], figsize=(25, 15))
axis_i, axis_j = 0, 0
for col in data.columns:
  if col == 'binary_fixed_acidity' or col == 'binary_volatile_acidity':
    continue # Box plots cannot be used on indicator variables
  sns.boxplot(x=binary_fixed_acidity, y=data[col], ax=axes[axis_i, axis_j])
  axis_j += 1
  if axis_j == dims[1]:
    axis_i += 1
    axis_j = 0


# COMMAND ----------

# Visualize relationship between high volatile acidity and other wine attributes 
import matplotlib.pyplot as plt

dims = (3, 4)

f, axes = plt.subplots(dims[0], dims[1], figsize=(25, 15))
axis_i, axis_j = 0, 0
for col in data.columns:
  if col == 'binary_fixed_acidity' or col == 'binary_volatile_acidity':
    continue # Box plots cannot be used on indicator variables
  sns.boxplot(x=binary_volatile_acidity, y=data[col], ax=axes[axis_i, axis_j])
  axis_j += 1
  if axis_j == dims[1]:
    axis_i += 1
    axis_j = 0
