# documentation is here: http://spark.apache.org/docs/latest/api/python/getting_started/quickstart.html
from datetime import date, datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import Row

spark = SparkSession.builder.getOrCreate()

# DataFrame is the API on top of RDD
df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')

# to avoid out of memory error, just take 1 value and display
result = df.take(1)
print(result)

# requires installing of pandas library
pandas = df.toPandas()
print(pandas)