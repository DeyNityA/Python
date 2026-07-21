from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("Broadcast").config("spark.ui.enabled", "true").getOrCreate()
sc = spark.sparkContext

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

departments = {
    "D01": "Computer Science",
    "D02": "Mechanical",
    "D03": "Electronics",
    "D04": "Civil"
}

# first approach -- will create RDD of both and then will join both
students_rdd = sc.parallelize(students)
departments_rdd = sc.parallelize(departments.items())

students_by_departments_rdd = students_rdd.map( lambda x : (x[2],(x[0],x[1])))

final_rdd = students_by_departments_rdd.join(departments_rdd)

print(final_rdd.collect())

#shuffle operation is performed in join operation which is costly operation. so we can use broadcast variable to avoid shuffle operation.
#we can also use small dataset as python object and serialize it for each task. but it will be costly operation 
# as serialization and deserialization is costly operation. so we can use broadcast variable to avoid serialization and deserialization.

broadcast_departments = sc.broadcast(departments) # broadcast variable is a read-only variable which is cached on each machine rather than shipping a copy of it with tasks. 
#it is used to avoid shuffle operation and serialization and deserialization.

final_rdd2 = students_by_departments_rdd.map(lambda x : (broadcast_departments.value[x[0]],x[1]))
print(final_rdd2.collect())
time.sleep(1000)

spark.stop()

