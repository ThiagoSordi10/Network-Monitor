from kafka import KafkaConsumer
from json import loads
#import sys
#from ipaddress import IPv4Network
#from typing import List
from hbase_helper import Connect
import time


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
	if 'conn' in message:
		message['conn'].update(identification = time.time())
		connect.put_data_conn(message['conn'])
	elif 'dns' in message:
		message['dns'].update(identification = time.time())
		connect.put_data_dns(message['dns'])
	elif 'dhcp' in message:
		message['dhcp'].update(identification = time.time())
		connect.put_data_dhcp(message['dhcp'])
	elif 'ssh' in message:
		message['ssh'].update(identification = time.time())
		connect.put_data_ssh(message['ssh'])
	elif 'http' in message:
		message['http'].update(identification = time.time())
		connect.put_data_http(message['http'])
	#connect.put_data(message) #Para cada mensagem no consumidor, salvar no hbase

connect.close()
