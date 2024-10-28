# Databricks notebook source
# dbutils.fs.ls("/mnt/silver/")

# COMMAND ----------

# dbutils.fs.ls("/mnt/gold/")

# COMMAND ----------

# input_path = "/mnt/silver/dbonew_retail_data/"

# COMMAND ----------

# df = spark.read.format("delta").load(input_path)
# df.show(1)

# COMMAND ----------

# # For one table transofrmation

# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, regexp_replace

# #get the column's name
# column_names = df.columns

# for old_col_name in column_names:
#     # Pascal Case formatting: conver the column name from ColumnName to Column_Name format 
#     new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

#     # Change the column name using withColumnRenamed and regexp_replace
#     df = df.withColumnRenamed(old_col_name, new_col_name)

# COMMAND ----------

# display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Let's do this tranformation for all the Tables

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls("/mnt/silver/"):
    table_name.append(i.name.split("/")[0])
table_name    

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

for name in table_name:
    path = "/mnt/silver/" + name
    print(path)

    df = spark.read.format("delta").load(path)

    #get the column's name
    column_names = df.columns

    for old_col_name in column_names:
        # Pascal Case formatting: conver the column name from ColumnName to Column_Name format 
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

        # Change the column name using withColumnRenamed and regexp_replace
        df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = "/mnt/gold/" + name + "/"
    df.write.format("delta").mode("overwrite").option("mergeSchema", "true").save(output_path)


# COMMAND ----------

# display(df)

# COMMAND ----------


