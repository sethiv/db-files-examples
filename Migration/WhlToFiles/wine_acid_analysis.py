# Databricks notebook source
# Package your modules as a Python wheel and then install as a cluster library
from modules import continousToBinary
import pandas as pd

# COMMAND ----------

# Load wine data
data = pd.read_csv("/dbfs/databricks-datasets/wine-quality/winequality-white.csv", sep=";")

# Remove spaces from column names
data.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

# COMMAND ----------

continousToBinary(data, "pH")

# COMMAND ----------


