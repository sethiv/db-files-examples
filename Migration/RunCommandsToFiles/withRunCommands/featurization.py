# Databricks notebook source
# adds a binary label to the input dataframe based on the same average of the column
def continousToBinary(data, column_name):
  average = data[column_name].mean()
  binary_column_name = "binary_"+column_name
  binary_column =(data[column_name] >= average).astype(int)
  data[binary_column_name] = binary_column
  return data
    
  

# COMMAND ----------


