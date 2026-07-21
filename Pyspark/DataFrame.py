# Datasets and DataFrames both handle structured data or semi-structured data. They both need to have a schema. 
# The main difference between the two is that Datasets are type-safe, 
# while DataFrames are not. Datasets provide compile-time type safety, which means that the compiler can catch errors at compile time, while DataFrames do not provide this feature.


'''Q1. Are DataFrames and Datasets different underlying engines in Spark?
--> No, They are unified, in Spark 2.0+, Dataframe is an alias for Dataset[Row].
    So, DataFrames are just a special case of Datasets where the type is Row. The core execution engine is the same for both,
    The difference lies in whether spark directly operates on raw binary bites(Row/UnsafeRow) or deserializes those bytes into
    strongly typed on JVM objects (Dataset[UserDefinedType]). Encoders are used to convert between JVM objects and Spark's internal binary format.

Q2. Does Pyspark have Datasets?
--> No, Pyspark does not have Datasets. Python is a dynamically typed language, so it does not have compile-time type safety.
Under the hood, Pyspark DataFrames interface directly with directly with Scala's Dataset<Row>.

'''








from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col


spark = SparkSession.builder.appName("RDD").config("spark.ui.enabled", "true").getOrCreate()

data = [
    (101, "Alice", 50000),
    (102, "Bob", 60000),
    (103, "Charlie", 70000),
    (104,"John", 90000),
    (105,"Khoka",87998)
]

schema = ['id', 'name', 'salary']

df = spark.createDataFrame(data, schema)

df.printSchema()

#df to rdd
rdd = df.rdd
print(rdd.collect())

df.show()

#dataframes are not type safe. 
type_safe_df = df.filter(df.salary > "Bob") # it should give error at runtime, but it will not give error at runtime because dataframes are not type safe. so we can use type hints to make it type safe.

try :
    type_safe_df.show() # it will give error at runtime because dataframes are not type safe. so we can use type hints to make it type safe.
except Exception as e :
    print('type saftey runtime error') 


df2 = df.withColumn(
    "salary",
    when(col("name") == "Bob", 45900.78).otherwise(col("salary"))
)

df2.show()
df2.printSchema()

# DataSets are type safe. 

print(df2.take(2)) 

#now we will see spark data types

