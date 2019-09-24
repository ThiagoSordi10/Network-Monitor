from pyspark import SparkContext
from pyspark.sql import SQLContext


def load_and_get_table_df(keys_space_name, table_name):
    table_df = sqlContext.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keys_space_name)\
        .load()
    return table_df

sc = SparkContext(appName="PythonSparkStreamingKafka")
sqlContext = SQLContext(sc)
#sc.setLogLevel("OFF")
sc.setLogLevel("WARN")

df = load_and_get_table_df( "network", "connection" )
#df.show()

df2 = df.groupBy(["orig_h", "resp_h", "resp_p", "proto"]).count().orderBy('count', ascending=False).cache()

df2.show()
#df2.count()
#df2.registerTempTable("conn_by_ip_total")
df2.write\
    .format("org.apache.spark.sql.cassandra")\
    .options(table="conn_by_ip_total", keyspace="testing")\
    .mode("append")\
    .save()
