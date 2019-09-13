from kafka import KafkaConsumer
from json import loads
from cassandra_helper import *
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
import time


consumer = KafkaConsumer(
    'zeek',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

#Configurar a conexão com os nós, o keyspace e a versão protocolo
create_keyspace()
connection.setup(['172.17.0.1', '172.17.0.2'], "packets", protocol_version=3)
sync_table(Connection)
sync_table(SSH)
sync_table(DHCP)
sync_table(HTTP)
sync_table(DNS)
print("Iniciar")

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
