# Databricks notebook source
# dbutils.fs.ls("/mnt/bronze/dbo/")
# dbutils.fs.ls("/mnt/bronze/")

# COMMAND ----------

# input_path = "/mnt/bronze/dbo/new_retail_data/new_retail_data.csv"
# df = spark.read.format("csv").option("header", "true").load(input_path)

# COMMAND ----------

# df.show()

# COMMAND ----------



# COMMAND ----------

# from pyspark.sql.functions import from_utc_timestamp, date_format
# from pyspark.sql.types import TimestampType

# df = df.withColumn("Date", date_format(from_utc_timestamp(df['Date'].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))

# COMMAND ----------

# df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Doing transformations for all the Tables

# COMMAND ----------

# create a list of table names

table_name = []

for i in dbutils.fs.ls("/mnt/bronze/dbo/"):
    table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = "/mnt/bronze/dbo/" + i + "/" + i + ".csv"
    df = spark.read.format("csv").option("header", "true").load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))

    output_path = "/mnt/silver/dbo" + i + "/"
    df.write.format('delta').mode("overwrite").option("mergeSchema", "true").save(output_path)

# COMMAND ----------

# df.show()
