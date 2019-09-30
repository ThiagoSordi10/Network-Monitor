from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from cassandra_helper import *
import docker
import json

clusterIPs = ["172.24.0.2"]

def sendPartition(iter):
    # ConnectionPool is a static, lazily initialized pool of connections
    #connection = ConnectionPool.getConnection()
    ConnectDB( clusterIPs )
    print("Starting ...")
    for record in iter:
        #connection.send(record)
        print(record)
	record = json.loads(record)
        if 'conn' in record:
                #record['conn'].update(identification = time.time())
                insert_connection(record['conn'])
        elif 'dns' in record:
                #record['dns'].update(identification = time.time())
                insert_dns(record['dns'])
        elif 'dhcp' in record:
                #record['dhcp'].update(identification = time.time())
                insert_dhcp(record['dhcp'])
        elif 'ssh' in record:
                #record['ssh'].update(identification = time.time())
                insert_ssh(record['ssh'])
        elif 'http' in record:
                #record['http'].update(identification = time.time())
                insert_http(record['http'])
    # return to the pool for future reuse
    #ConnectionPool.returnConnection(connection)
#dstream.foreachRDD(lambda rdd: rdd.foreachPartition(sendPartition))

# get docker containers from cassandra
client = docker.from_env()


'''
print(client.containers.list())
for container in client.containers.list(filters={'name': "cassandra"}):
        cnet = next(iter(vars(container)["attrs"]["NetworkSettings"]["Networks"].values()))
        print('Found cassandra node ' + container.name)
        clusterIPs.append(cnet['IPAddress'])'''



sc = SparkContext("local[2]", appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc,30)

kafkaStream = KafkaUtils.createStream(ssc, 'zookeeper:2181', 'my-group', {'zeek':1})

lines = kafkaStream.map(lambda x: x[1])
lines.pprint()
lines.foreachRDD(lambda rdd: rdd.foreachPartition(sendPartition))

ssc.start()
ssc.awaitTermination()


