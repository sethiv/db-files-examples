# Databricks notebook source
import sys
print("\n".join(sys.path))

# COMMAND ----------

import sys
import os

sys.path.append(os.path.abspath('..'))

# COMMAND ----------

import sys
print("\n".join(sys.path))

# COMMAND ----------

import common.params
print(common.params.get_params())

# COMMAND ----------

from common import params
print(params.get_params())
