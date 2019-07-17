from kafka import KafkaConsumer
from json import loads
import sys
from ipaddress import IPv4Network
from typing import List
from hbase_helper import Connect


consumer = KafkaConsumer(
    'bro',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

connect = Connect() #Instancia um objeto de conexão

for message in consumer:
	message = message.value
	print(message)
	'''if 'dns' in message:
		message = loads(message['dns'])
	elif 'dhcp' in message:
		message = loads(message['dhcp'])
	elif 'ssh' in message:
		message = loads(message['ssh'])
	elif 'http' in message:
		message = loads(message['http'])
	print(message)'''
	connect.put_data(message) #Para cada mensagem no consumidor, salvar no hbase

connect.close()
