from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("RDD").config("spark.ui.enabled", "true").getOrCreate()

print(type(spark))

sc = spark.sparkContext
print(sc.uiWebUrl) # uiWebUrl --> returns the url of the spark web ui
print(type(sc))

ls = [1,2,6,7,8,9,10,21,90]

ls_rdd = sc.parallelize(ls) 

print(type(ls_rdd)) # rdd --> Resilient Distributed Dataset
print(ls_rdd)
print(ls_rdd.getNumPartitions()) # getNumPartitions() --> returns the number of partitions in the RDD
print(ls_rdd.collect()) # collect() --> returns the list of elements in the RDD
print(ls_rdd.glom().collect()) # glom() --> returns the list of elements in each partition
print(ls_rdd.map(lambda x: x*2).collect()) # map() --> returns a new RDD by applying a function to each element of the RDD


# text file to rdd
dataRDD = sc.textFile("survey_results_public.csv") # textFile() --> returns an RDD of strings, one string per line of the file
print(dataRDD.getNumPartitions()) 
#print(dataRDD.glom().collect()) 



# RDD Operations

# (Transformations)(Lazy Evaluation)
# 1. map() --> returns a new RDD by applying a function to each element of the RDD
# 2. filter() --> returns a new RDD by applying a function to each element
# 3. flatMap() --> returns a new RDD by applying a function to each element and flattening the result
# 4. distinct() --> returns a new RDD by removing duplicate elements
# 5. union() --> returns a new RDD by combining two RDDs
# 6. intersection() --> returns a new RDD by returning the common elements of two RDDs
# 7. subtract() --> returns a new RDD by removing the elements of one RDD from another RDD
# 8. cartesian() --> returns a new RDD by returning the cartesian product of two RDDs
# 9. groupByKey() --> returns a new RDD by grouping the values of each key in the RDD
# 10. reduceByKey() --> returns a new RDD by reducing the values of each key in the RDD
# 11. sortByKey() --> returns a new RDD by sorting the values of each key in the RDD
# 12. join() --> returns a new RDD by joining two RDDs on a key
# 13. cogroup() --> returns a new RDD by grouping the values of each key in two RDDs
# 14. pipe() --> returns a new RDD by piping the elements of the RDD to a shell command
# 15. aggregate() --> returns a new RDD by aggregating the values of each key in the RDD
# 16. fold() --> returns a new RDD by folding the values of each key in the RDD
# 17. combineByKey() --> returns a new RDD by combining the values of each key in the RDD
# 18. sample() --> returns a new RDD by sampling the elements of the RDD
# 19. randomSplit() --> returns a new RDD by randomly splitting the elements of the RDD into multiple RDDs
# 20. coalesce() --> returns a new RDD by reducing the number of partitions in the RDD
# 21. repartition() --> returns a new RDD by increasing the number of partitions in the RDD

# Triggering Actions
# 1. collect() --> returns a list of all the elements in the RDD
# 2. count() --> returns the number of elements in the RDD
# 3. take(n) --> returns a list of the first n elements in the RDD
# 4. saveAsTextFile(path) --> saves the RDD as a text file in the given path

# It is Lazy Evaluation because it does not compute the result immediately. It only computes the result when an action is called on the RDD. This allows Spark to optimize the execution plan and reduce the amount of data shuffled across the network.
# once an action is called, job is submitted to the cluster.
# one job can have multiple stages and one stage can have multiple tasks. Each task is executed on a single partition of the RDD. 
# The number of tasks in a stage is equal to the number of partitions in the RDD.
# If the Transformation is narrow, then the tasks can be executed in one stage.
# If the Transformation is wide, then another stage is created.

# RDD are immutable, distributed, and fault-tolerant collection of elements that can be processed in parallel. 

ls = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
rdd_ls = sc.parallelize(ls)

def process(x) :
    if x == 17 :
        raise Exception('Fault Tolerence exception') 
    return x**2

fault_tolerence_rdd = rdd_ls.map(process)

try :
    fault_tolerence_rdd.collect()
except Exception as e :
    print(e.__traceback__)

# here although tasks will be failed, but stil it will retry it.

students = [
    (101, "Alice", "D01"),
    (102, "Bob", "D02"),
    (103, "Charlie", "D01"),
    (104, "David", "D03"),
    (105, "Emma", "D02"),
    (106, "Frank", "D04"),
    (107, "Grace", "D01"),
    (108, "Henry", "D03"),
    (109, "Ivy", "D02"),
    (110, "Jack", "D04"),
    (111, "Kevin", "D03"),
    (112, "Lily", "D01"),
    (113, "Mike", "D02"),
    (114, "Nancy", "D03"),
    (115, "Oliver", "D04"),
    (116, "Peter", "D01"),
    (117, "Queen", "D02"),
    (118, "Robert", "D04"),
    (119, "Sophia", "D03"),
    (120, "Tom", "D01")
]

rdd_students = sc.parallelize(students)

print(rdd_students.glom().collect()) # glom() --> returns a list of elements in each partition

# rdd's are type safe. 
# not type safe - i.e the intermediate rdd can have different data type than the original rdd. so we can use type hints to make it type safe.
# but in pyspark, compile-time safety is not enforced due to dynamic typing.
type_safe_rdd = rdd_students.map(lambda x : x[0]-x[1]) # it should give error at runtime, but it will not give error at runtime because rdd's are not type safe. so we can use type hints to make it type safe.

# it will give error at runtime because rdd's are not type safe. so we can use type hints to make it type safe.
time.sleep(1000) # sleep() --> suspends the execution of the current thread for the given number of seconds

spark.stop()

