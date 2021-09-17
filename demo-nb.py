# Databricks notebook source
# MAGIC %md
# MAGIC This notebook should be used with Files on Repos onboarding documentation

# COMMAND ----------

# MAGIC %md 
# MAGIC #### Working with Python modules

# COMMAND ----------

from sample import hmm

# COMMAND ----------

hmm()

# COMMAND ----------

# MAGIC %md ****Managing Python paths****

# COMMAND ----------

# MAGIC %md Refer to /db-files-examples/path-example/path-demo-nb

# COMMAND ----------

# MAGIC %md
# MAGIC #### 4/ Working with data files

# COMMAND ----------

# MAGIC %md  ****Reads****

# COMMAND ----------

import csv
with open('data/winequality-red.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# COMMAND ----------

import pandas as pd
df= pd.read_csv("data/winequality-red.csv")
display(df)


# COMMAND ----------

# MAGIC %md
# MAGIC Installation from requirements.txt

# COMMAND ----------

pip install -r requirements.txt

# COMMAND ----------

# MAGIC %md
# MAGIC File reads via Pyspark are now allowed

# COMMAND ----------

df=spark.read.csv("file:/Workspace/Repos/vaibhav.sethi@databricks.com/db-files-examples/data/winequality-red.csv")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Limitations

# COMMAND ----------

# MAGIC %md
# MAGIC Cannot write to the data file from the notebook

# COMMAND ----------

import csv
list=[6,0.31,0.47,3.6,0.067,18,42,0.99549,3.39,0.66,11,6]
with open('data/winequality-red.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(list)

# COMMAND ----------

import os
os.getcwd()

# COMMAND ----------

import databricks.koalas as ks

df= ks.read_csv("file:/Workspace/Repos/vaibhav.sethi@databricks.com/db-files-examples/data/winequality-red.csv")
display(df)



# COMMAND ----------


