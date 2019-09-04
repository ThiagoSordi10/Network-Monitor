from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext(appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc,30)

kafkaStream = KafkaUtils.createStream(ssc, '172.21.0.2:2181', 'my-group', {'bro':1})

lines = kafkaStream.map(lambda x: x[1])
lines.pprint()

ssc.start()
ssc.awaitTermination()
