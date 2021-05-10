# Databricks notebook source
# MAGIC %md Current working directotory in Repos is incluced in the Path

# COMMAND ----------

import sys
print("\n".join(sys.path))

# COMMAND ----------

# MAGIC %md Modules in this directory can be imported

# COMMAND ----------



# COMMAND ----------

# MAGIC %md To import modules in other directories add them to the Path

# COMMAND ----------

import sys
import os

sys.path.append(os.path.abspath('..'))

# COMMAND ----------

from sample import hmm
