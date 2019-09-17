from kafka import KafkaConsumer
from json import loads
from cassandra_helper import *
import time
import docker


consumer = KafkaConsumer(
    'zeek',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = docker.APIClient(base_url='unix://var/run/docker.sock')
container = client.containers(filters={'name': "cassandra_node_1"}) #colocar pela imagem pra pegar os containers
clusterIPs = []
clusterIPs.append(client.inspect_container(container[0])['NetworkSettings']['Networks']['testedosistema_default']['IPAddress'])

ConnectDB( clusterIPs )
print("Starting ...")

for message in consumer:
        message = message.value
        print(message)
        if 'conn' in message:
                message['conn'].update(identification = time.time())
                insert_connection(message['conn'])
        elif 'dns' in message:
                message['dns'].update(identification = time.time())
                insert_dns(message['dns'])
        elif 'dhcp' in message:
                message['dhcp'].update(identification = time.time())
                insert_dhcp(message['dhcp'])
        elif 'ssh' in message:
                message['ssh'].update(identification = time.time())
                insert_ssh(message['ssh'])
        elif 'http' in message:
                message['http'].update(identification = time.time())
                insert_http(message['http'])

