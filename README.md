# Network Monitor

<h3>1. Images </h3>
Images used in project:

Cassandra:
https://hub.docker.com/_/cassandra

Kafka:
https://hub.docker.com/r/wurstmeister/kafka/

ZooKeepeer:
https://hub.docker.com/r/wurstmeister/zookeeper/

Zeek with connection plugin to Kafka:
https://hub.docker.com/r/thiagosordi/zeek

Spark Streaming (Kafka Consumer):
https://hub.docker.com/r/thiagosordi/spark-streaming

They are auto installed in Spark Streaming image, but:

Python package to use Spark (using ```pip install```):
- pyspark (2.4.4)

Python package to use Kafka (using ```pip install```):
- kafka-python (1.4.6)

Python package to use Cassandra-driver (using ```pip install```):
- cassandra-driver (3.19.0)(not updated  in image yet)

<h3>2. Running containers </h3>

```sudo docker-compose up -d``` (in the folder with docker-compose.yml)

With all images installed, now it's just run. 

Running single container:
Ex:
```sudo docker run thiagosordi/zeek```

<h3>3. (Probably) Configuring Error Zeek Container </h3>

If running Zeek container gives an error, verify if the network interface is the same that is configured in ```node.cfg```, else change the interface in this file.

<h3>4. (Optional) Manual Consumer</h3>
Running cassandra_helper.py and consumer.py in your machine to get some results:

```sudo python3 consumer.py```

Obs: The Zeek and Hbase container are running as containers too.

<h3>5. Run Spark Streaming </h3>
With all container running, now run the Spark Streaming container:

```sudo docker exec -ti spark-streaming bash```

After:

```/usr/local/spark/bin/spark-submit  --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.0 spark.py```

<h3>6. Using later </h3>
When you want to run everything again, just:

```sudo docker start <container_name>```

<h4>This project is not finished</h4>

