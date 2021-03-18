# we must use python 3.9 for driver program, as there is a python 3.9 used by spark
import sys
import pyspark

#conf = pyspark.SparkConf()
#conf.setMaster("spark://host.docker.internal:61784")

context = pyspark.SparkContext("local[*]")
txt = context.textFile("data/mnm_dataset.csv")
print(txt.count())