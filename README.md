# Network Monitor

<h3>1. Images </h3>
Images used in project:

Hbase (two options):
https://github.com/dajobe/hbase-docker

https://hub.docker.com/r/harisekhon/hbase/ <b>(used)</b>

Kafka:
https://hub.docker.com/r/wurstmeister/kafka/

ZooKeepeer:
https://hub.docker.com/r/wurstmeister/zookeeper/

Zeek with connection plugin to Kafka:
https://hub.docker.com/r/thiagosordi/zeek

Python package to use HBase (using ```pip install```):
- happybase (1.1.0)

Python package to use Kafka (using ```pip install```):
- kafka-python (1.4.6)

Spark Streaming (Kafka Consumer):
<link here>

<h3>2. Running containers </h3>
After

```sudo docker-compose up -d``` (in the folder with docker-compose.yml)

With all images installed, now it's just run. 

Running single container:
Ex:
```sudo docker run harisekhon/hbase```

<h3>3. Configuring </h3>
Configure the Zeek container:

```sudo docker exec -ti zeek bash```

Type

```zeekctl```

and 

```deploy```

obs: if deploy gives an error, verify if the network interface is the same (eth0) that is configured, else https://stackoverflow.com/questions/39398773/error-while-starting-bro

<h3>4. Run Spark Streaming </h3>
With all container running, now run the Spark Streaming container:

```sudo docker exec -ti spark-streaming bash```

After:

```/usr/local/spark/bin/spark-submit  --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.0 spark.py```

<h3>5. Using later </h3>
When you want to run everything again, just:

```sudo docker start <container_name>```

<h4>This project is not finished</h4>

