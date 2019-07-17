import happybase

class Connect:
	def __init__(self):
		self.connection = happybase.Connection('hbase-docker', 9090) #Conecta ao servidor hbase

		if(b'packets' in self.connection.tables()): #Teste se tabela já existe
			self.table = self.connection.table('packets')
		else:
			families = {
			    'connection': dict(),
			    'dhcp': dict(),
			    'ssh': dict(),
			    'http': dict(),
                            'dns': dict()
			}
			self.connection.create_table('packets', families)
			self.table = self.connection.table('packets')

	def put_data(self, data): #Insere dados	
		try:
			self.table.put(str(data['identification']), {'connection:protocol': data['protocol'], 'connection:ttl': data['time_to_live'], 
					'connection:flags_df': str(data['flags_df']), 'connection:flags_mf': str(data['flags_mf']),
					'connection:flags_rb': str(data['flags_rb']), 'connection:checksum': str(data['checksum']),
					'connection:id': str(data['identification']), 'connection:fragment': str(data['fragment']),
					'connection:header_length': str(data['header_length']), 'connection:size': str(data['size']),
					'connection:src_addr': str(data['src_addr']), 'connection:src_port': str(data['src_port']),
					'connection:dst_addr': str(data['dst_addr']), 'connection:dst_port': str(data['dst_port']),})
			#vai depender do pacote para por nas familias certas
		except ValueError:
			pass
	
	def close(self): #Fecha conexão
		self.connection.close()

	def all_rows(self): #Exibe todos dados salvos
		for k, data in self.table.scan():
			print(k, data)

