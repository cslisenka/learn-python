import shutil
# we must use python 3.9 for driver program, as there is a python 3.9 used by spark
# RDD documentation
# http://spark.apache.org/docs/latest/rdd-programming-guide.html
import pyspark

# TODO investigate how to connect to spark cluster on local machine
from pyspark.storagelevel import StorageLevel

conf = pyspark.SparkConf()
conf.setAppName("my-app")
# http://spark.apache.org/docs/latest/submitting-applications.html#master-urls
conf.setMaster("local[*]")

# TODO configure spark in standalone mode
# http://spark.apache.org/docs/latest/spark-standalone.html
# conf.setMaster("spark://host.docker.internal:61784")
# TODO configure spark in k*s

# create context
context = pyspark.SparkContext(conf=conf)

# create RDD from collection with 2 partitions (if not specified Spark automatically chooses number of partitions)
data = [1, 2, 3, 4, 5]
data_rdd = context.parallelize(data, 2)
print(type(data_rdd))
# action - returns value to the driver program
print(data_rdd.count())

# transformation - transforms the data set and returns new data set object
# map - works independently for each partition
# this RDD will be cached and other transformations will not start from the beginning
data_rdd = data_rdd.map(lambda s: s * 10).persist(StorageLevel.MEMORY_ONLY)

# save to file -> file is saved in parts, each part is one partition
shutil.rmtree("data/output.txt")
data_rdd.saveAsTextFile("data/output.txt")

# aggregates all elements and returns result to the driver program
data_sum = data_rdd.reduce(lambda a, b: a + b)
print(data_sum)

# create RDD from data in file system
# this file path needs to be accessible on worker nodes (copy or NFS)
# we may specify path to folder, wildcards or *.gz files
csv_rdd = context.textFile("data/mnm_dataset.csv")
print(type(csv_rdd))
# all execution happens when we execute any action
print(csv_rdd.count())