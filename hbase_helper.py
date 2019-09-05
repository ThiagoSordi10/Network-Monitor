import happybase

class Connect:
	def __init__(self):
		self.connection = happybase.Connection('hbase-docker', 9090) #Conecta ao servidor hbase

		if(b'packets' in self.connection.tables()): #Teste se tabela já existe
			self.table = self.connection.table('packets')
		else:
			families = {
			    'conn': dict(),
			    'dhcp': dict(),
			    'ssh': dict(),
			    'http': dict(),
			    'dns': dict()
			}
			self.connection.create_table('packets', families)
			self.table = self.connection.table('packets')
	#NA VERDADE DEVE-SE JUNTAR TODOS CADA TIPO DE CONEXÃO NA MESMA ROW DA CONN ENTAÕ EM CADA UM DEVE SER CHAMADO O put_data_conn
	def put_data_conn(self, data): #Insere dados	
		try:
			self.table.put(str(data['identification']), {'conn:service': str(data.get('service')), 'conn:duration': str(data.get('duration')), 
					'conn:orig_bytes': str(data.get('orig_bytes')), 'conn:resp_bytes': str(data.get('resp_bytes')),
					'conn:conn_state': str(data.get('conn_state')), 'conn:local_orig': str(data.get('local_orig')),
					'conn:local_resp': str(data.get('local_resp')), 'conn:missed_bytes': str(data.get('missed_bytes')),
					'conn:history': str(data.get('history')), 'conn:orig_pkts': str(data.get('orig_pkts')),
					'conn:orig_ip_bytes': str(data.get('orig_ip_bytes')), 'conn:resp_pkts': str(data.get('resp_pkts')),
					'conn:resp_ip_bytes': str(data.get('resp_ip_bytes')), 'conn:tunnel_parents': str(data.get('tunnel_parents')),
					'conn:vlan': str(data.get('vlan')), 'conn:inner_vlan': str(data.get('inner_vlan')),
					'conn:orig_l2_addr': str(data.get('orig_l2_addr')), 'conn:resp_l2_addr': str(data.get('resp_l2_addr'))})
			#vai depender do pacote para por nas familias certas

		except ValueError:
			pass

	def put_data_ssh(self, data): #Insere dados	
		try:
			self.table.put(str(data['identification']), {'ssh:version1': str(data.get('version1')), 'ssh:auth_success': str(data.get('auth_success')), 
					'ssh:auth_attempts': str(data.get('auth_attempts')), 'ssh:direction': str(data.get('direction')),
					'ssh:client': str(data.get('client')), 'ssh:server': str(data.get('server')),
					'ssh:cipher_alg': str(data.get('cipher_alg')), 'ssh:mac_alg': str(data.get('mac_alg')),
					'ssh:compression_alg': str(data.get('compression_alg')), 'ssh:kex_alg': str(data.get('kex_alg')),
					'ssh:host_key_alg': str(data.get('host_key_alg')), 'ssh:host_key': str(data.get('host_key'))})
			#vai depender do pacote para por nas familias certas

		except ValueError:
			pass

	def put_data_dhcp(self, data): #Insere dados	
		try:
			self.table.put(str(data['identification']), {'dhcp:mac': str(data.get('mac')), 'dhcp:assigned_ip': str(data.get('assigned_ip')), 
					'dhcp:lease_time': str(data.get('lease_time')), 'dhcp:trans_id1': str(data.get('trans_id1'))})
			#vai depender do pacote para por nas familias certas

		except ValueError:
			pass

	def put_data_http(self, data): #Insere dados	
		try:
			self.table.put(str(data['identification']), {'http:trans_depth': str(data.get('trans_depth')), 'http:method': str(data.get('method')), 
					'http:host': str(data.get('host')), 'http:uri': str(data.get('uri')),
					'http:referrer': str(data.get('referrer')), 'http:version': str(data.get('version')),
					'http:user_agent': str(data.get('user_agent')), 'http:request_body_len': str(data.get('request_body_len')),
					'http:response_body_len': str(data.get('response_body_len')), 'http:status_code': str(data.get('status_code')),
					'http:status_msg': str(data.get('status_msg')), 'http:info_code': str(data.get('info_code')),
					'http:info_msg': str(data.get('info_msg')), 'http:tags': str(data.get('tags')),
					'http:username': str(data.get('username')), 'http:password': str(data.get('password')),
					'http:proxied': str(data.get('proxied')), 'http:orig_fuids': str(data.get('orig_fuids')),
					'http:orig_filenames': str(data.get('orig_filenames')), 'http:orig_mime_types': str(data.get('orig_mime_types')),
					'http:resp_fuids': str(data.get('resp_fuids')), 'http:resp_filenames': str(data.get('resp_filenames')),
					'http:resp_mime_types': str(data.get('resp_mime_types'))})
			#vai depender do pacote para por nas familias certas

		except ValueError:
			pass
	
	def put_data_dns(self, data): #Insere dados	
		try:
			self.table.put(str(data['identification']), {'dns:trans_id': str(data.get('trans_id')), 'dns:rtt': str(data.get('rtt')), 
					'dns:query': str(data.get('query')), 'dns:qclass': str(data.get('qclass')),
					'dns:qclass_name': str(data.get('qclass_name')), 'dns:qtype': str(data.get('qtype')),
					'dns:qtype_name': str(data.get('qtype_name')), 'dns:rcode': str(data.get('rcode')),
					'dns:rcode_name': str(data.get('rcode_name')), 'dns:aa': str(data.get('aa')),
					'dns:tc': str(data.get('tc')), 'dns:rd': str(data.get('rd')),
					'dns:ra': str(data.get('ra')), 'dns:z': str(data.get('z')),
					'dns:answers': str(data.get('answers')), 'dns:ttls': str(data.get('ttls')),
					'dns:rejected': str(data.get('rejected')), 'dns:addl': str(data.get('addl')),
					'dns:auth': str(data.get('auth'))})
			#vai depender do pacote para por nas familias certas

		except ValueError:
			pass

	def close(self): #Fecha conexão
		self.connection.close()

	def all_rows(self): #Exibe todos dados salvos
		for k, data in self.table.scan():
			print(k, data)


