from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName('Wordcount').config("spark.ui.enabled", "true").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile('wordcount.txt')

print(rdd.getNumPartitions())

word_counts = rdd.flatMap(lambda line : line.split()).map(lambda word : (word,1)).reduceByKey(lambda x,y : x+y)

print(word_counts.collect())

print(sc.uiWebUrl) # uiWebUrl --> returns the url of the spark web ui


time.sleep(1000)
spark.stop()
