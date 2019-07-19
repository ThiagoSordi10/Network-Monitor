# Network Monitor

<h3>1. Downloads requirements </h3>
First, you must download (docker push) the necessary images:

Hbase (two options):
https://github.com/dajobe/hbase-docker

https://hub.docker.com/r/harisekhon/hbase/ <b>(used)</b>

Kafka:
https://hub.docker.com/r/wurstmeister/kafka/

ZooKeepeer:
https://hub.docker.com/r/wurstmeister/zookeeper/

Zeek with connection plugin to Kafka:
https://cloud.docker.com/u/thiagosordi/repository/docker/thiagosordi/bro

<h3>2. Running containers </h3>
After
```sudo docker-compose up -d``` (in the folder with docker-compose.yml)

With all images installed, now it's just run. Running the container images;

obs: the wurstmeister's container, after docker-compose, will automatically begin. The thiagosordi's container too.

```sudo docker run harisekhon/hbase```

<h3>3. Configuring </h3>
Configure the Zeek container:

```sudo docker exec -ti zeek bash```

```nano $ZEEK_HOME/share/zeek/site/local.zeek```

and insert this lines in the beggining of the file:

```
@load /usr/local/zeek/lib/zeek/plugins/APACHE_KAFKA/scripts/Apache/Kafka/logs-to-kafka.bro
    redef Kafka::kafka_conf = table(
        ["metadata.broker.list"] = "localhost:9092",
        ["client.id"] = "bro"
    );
    redef Kafka::topic_name = "bro";
    redef Kafka::logs_to_send = set(Conn::LOG, DNS::LOG, SSH::LOG, Notice::LOG);
    redef Kafka::tag_json = T;
```

Save and close. After type

```broctl```

and 

```deploy```

obs: if deploy gives an error, verify if the network interface is the same (eth0) that is configured, else https://stackoverflow.com/questions/39398773/error-while-starting-bro

<h3>4. Run consumer Kafka </h3>
With all container running, now run the Python application, Kafka consumer:

```sudo python3 <consumer_name>.py```

<h3>5. Using later </h3>
When you want to run everything again, just:

```sudo docker start <container_name>```

<h4>This project is not finished, next step is save in HBase each connection's service and integrate Spark</h4>

