FROM alpine:latest

# Environment
ENV SPARK_VERSION 2.4.0
ENV HADOOP_VERSION 2.7
ENV SCALA_VERSION 2.11
ENV SPARK_HOME /usr/local/spark

WORKDIR /spark
COPY requirements.txt /spark

RUN apk update && apk upgrade
RUN apk add --no-cache bash openjdk8-jre python3-dev py-pip gcc musl-dev \
      && pip3 install -r requirements.txt \
      && wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
      && tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local \
      && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

RUN cd /usr/local && ln -s spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# Spark Kafka Streaming
#RUN cd /tmp && \
#    wget http://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10-assembly_${SCALA_VERSION}/${SPARK_VERSION}/spark-streaming-kafka-0-10-#assembly_${SCALA_VERSION}-${SPARK_VERSION}.jar && \
#    mv spark-streaming-kafka-0-10-assembly_${SCALA_VERSION}-${SPARK_VERSION}.jar /usr/local/spark/jars

EXPOSE 8080
EXPOSE 6066
EXPOSE 7077

WORKDIR /spark

#/usr/local/spark/bin/spark-submit  --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.0 spark.py
