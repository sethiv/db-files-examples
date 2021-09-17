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
