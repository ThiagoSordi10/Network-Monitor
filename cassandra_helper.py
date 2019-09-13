from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid

#https://docs.datastax.com/en/developer/python-driver/3.19/getting_started/

'''class Connect_db:
        def __init__(self):
                cluster = Cluster(['172.17.0.1', '172.17.0.2']) #This will attempt to connection to a Cassandra instance on your local machine (127.0.0.1). You can also specify a list of IP addresses for nodes in your cluster
                self.session = cluster.connect()
                print(self.session)
                self.session.execute("CREATE KEYSPACE IF NOT EXISTS packets WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 }");
                #self.session.execute("CREATE COLUMNFAMILY IF NOT EXISTS conn (id )");
                #self.session.execute("CREATE KEYSPACE IF NOT EXISTS packets WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 }");
                #self.session.execute("CREATE KEYSPACE IF NOT EXISTS packets WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 }");
                #self.session.execute("CREATE KEYSPACE IF NOT EXISTS packets WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 }");
                #self.session.execute("CREATE KEYSPACE IF NOT EXISTS packets WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 }");
                self.session.set_keyspace('packets')

        def close(self): #Fecha conexão
                self.session.close()
        
        #def put_data_conn(self, data): #Insere dados'''

def create_keyspace():
	cluster = Cluster(['172.22.0.2', '172.22.0.3', '172.22.0.4']) #This will attempt to connection to a Cassandra instance on your local machine (127.0.0.1). You can also specify a list of IP addresses for nodes in your cluster
        session = cluster.connect()
        session.execute("CREATE KEYSPACE IF NOT EXISTS packets WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }");	
	cluster.shutdown() 

def insert_connection(data):
	Connection.create(service=str(data.get('service')), duration=str(data.get('duration')), orig_bytes=str(data.get('orig_bytes')), resp_bytes=str(data.get('resp_bytes')), conn_state=str(data.get('conn_state')), local_orig=str(data.get('local_orig')), local_resp=str(data.get('local_resp')), missed_bytes=str(data.get('missed_bytes')), history=str(data.get('history')), orig_pkts=str(data.get('orig_pkts')), orig_ip_bytes=str(data.get('orig_ip_bytes')), resp_pkts=str(data.get('resp_pkts')), resp_ip_bytes=str(data.get('resp_ip_bytes')), tunnel_parents=str(data.get('tunnel_parents')), vlan=str(data.get('vlan')), inner_vlan=str(data.get('inner_vlan')), orig_l2_addr=str(data.get('orig_l2_addr')), resp_l2_addr=str(data.get('resp_l2_addr')))

def insert_ssh(data):
	SSH.create(version_1=str(data.get('version_1')), auth_success=str(data.get('auth_success')), auth_attempts=str(data.get('auth_attempts')), direction=str(data.get('direction')), client=str(data.get('client')), server=str(data.get('server')), cipher_alg=str(data.get('cipher_alg')), mac_alg=str(data.get('mac_alg')), compression_alg=str(data.get('compression_alg')), kex_alg=str(data.get('kex_alg')), host_key_alg=str(data.get('host_key_alg')), host_key=str(data.get('host_key')))

def insert_dhcp(data):
	DHCP.create(mac=str(data.get('mac')), assigned_ip=str(data.get('assigned_ip')), lease_time=str(data.get('lease_time')), trans_id1=str(data.get('trans_id1')))

def insert_http(data):
	HTTP.create(trans_depth=str(data.get('trans_depth')), method=str(data.get('method')), host=str(data.get('host')), uri=str(data.get('uri')), referrer=str(data.get('referrer')), version=str(data.get('version')), user_agent=str(data.get('user_agent')), request_body_len=str(data.get('request_body_len')), response_body_len=str(data.get('response_body_len')), status_code=str(data.get('status_code')), status_msg=str(data.get('status_msg')), info_code=str(data.get('info_code')), info_msg=str(data.get('info_msg')), tags=str(data.get('tags')), username=str(data.get('username')), password=str(data.get('password')), proxied=str(data.get('proxied')), orig_fuids=str(data.get('orig_fuids')), orig_filenames=str(data.get('orig_filenames')), orig_mime_types=str(data.get('orig_mime_types')), resp_fuids=str(data.get('resp_fuids')), resp_filenames=str(data.get('resp_filenames')), resp_mime_types=str(data.get('resp_mime_types')))

def insert_dns(data):
	DNS.create(trans_id=str(data.get('trans_id')), rtt=str(data.get('rtt')), query=str(data.get('query')), qclass=str(data.get('qclass')), qclass_name=str(data.get('qclass_name')), qtype=str(data.get('qtype')), qtype_name=str(data.get('qtype_name')), rcode=str(data.get('rcode')), rcode_name=str(data.get('rcode_name')), aa=str(data.get('aa')), tc=str(data.get('tc')), rd=str(data.get('rd')), ra=str(data.get('ra')), z=str(data.get('z')), answers=str(data.get('answers')), ttls=str(data.get('ttls')), rejected=str(data.get('rejected')), addl=str(data.get('addl')), auth=str(data.get('auth')))
                       
class Connection(Model):
        id = columns.UUID(primary_key=True, default=uuid.uuid4)
        service = columns.Text(required=False)
        duration = columns.Text(required=False)
        orig_bytes = columns.Text(required=False)
        resp_bytes = columns.Text(required=False)
        conn_state = columns.Text(required=False)
        local_orig = columns.Text(required=False)
        local_resp = columns.Text(required=False)
        missed_bytes = columns.Text(required=False)
        history = columns.Text(required=False)
        orig_pkts = columns.Text(required=False)
        orig_ip_bytes = columns.Text(required=False)
        resp_pkts = columns.Text(required=False)
        resp_ip_bytes = columns.Text(required=False)
        tunnel_parents = columns.Text(required=False)
        vlan = columns.Text(required=False)
        inner_vlan = columns.Text(required=False)
        orig_l2_addr = columns.Text(required=False)
        resp_l2_addr = columns.Text(required=False)

class SSH(Model):
        id = columns.UUID(primary_key=True, default=uuid.uuid4)
        version_1  = columns.Text(required=False)
        auth_success = columns.Text(required=False)
        auth_attempts = columns.Text(required=False)
        direction = columns.Text(required=False)
        client = columns.Text(required=False)
        server = columns.Text(required=False)
        cipher_alg = columns.Text(required=False)
        mac_alg = columns.Text(required=False)
        compression_alg = columns.Text(required=False)
        kex_alg = columns.Text(required=False)
        host_key_alg = columns.Text(required=False)
        host_key = columns.Text(required=False)

class DHCP(Model):
        id = columns.UUID(primary_key=True, default=uuid.uuid4)
        mac  = columns.Text(required=False)
        assigned_ip = columns.Text(required=False)
        lease_time = columns.Text(required=False)
        trans_id1 = columns.Text(required=False)

class HTTP(Model):
        id = columns.UUID(primary_key=True, default=uuid.uuid4)
        trans_depth  = columns.Text(required=False)
        method = columns.Text(required=False)
        host = columns.Text(required=False)
        uri = columns.Text(required=False)
        referrer = columns.Text(required=False)
        version = columns.Text(required=False)
        user_agent = columns.Text(required=False)
        request_body_len = columns.Text(required=False)
        response_body_len = columns.Text(required=False)
        status_code = columns.Text(required=False)
        status_msg = columns.Text(required=False)
        info_code = columns.Text(required=False)
        info_msg = columns.Text(required=False)
        tags = columns.Text(required=False)
        username = columns.Text(required=False)
        password = columns.Text(required=False)
        proxied = columns.Text(required=False)
        orig_fuids = columns.Text(required=False)
        orig_filenames = columns.Text(required=False)
        orig_mime_types = columns.Text(required=False)
        resp_fuids = columns.Text(required=False)
        resp_filenames = columns.Text(required=False)
        resp_mime_types = columns.Text(required=False)

class DNS(Model):
        id = columns.UUID(primary_key=True, default=uuid.uuid4)
        trans_id  = columns.Text(required=False)
        rtt = columns.Text(required=False)
        query = columns.Text(required=False)
        qclass = columns.Text(required=False)
        qclass_name = columns.Text(required=False)
        qtype = columns.Text(required=False)
        qtype_name = columns.Text(required=False)
        rcode = columns.Text(required=False)
        rcode_name = columns.Text(required=False)
        aa = columns.Text(required=False)
        tc = columns.Text(required=False)
        rd = columns.Text(required=False)
        ra = columns.Text(required=False)
        z = columns.Text(required=False)
        answers = columns.Text(required=False)
        ttls = columns.Text(required=False)
        rejected = columns.Text(required=False)
        addl = columns.Text(required=False)
        auth = columns.Text(required=False)



'''
rows = session.execute('SELECT name, age, email FROM users')
for row in rows:
    print row.name, row.age, row.email

session.execute(
    """
    INSERT INTO users (name, credits, user_id, username)
    VALUES (%(name)s, %(credits)s, %(user_id)s, %(name)s)
    """,
    {'name': "John O'Reilly", 'credits': 42, 'user_id': uuid.uuid1()}
)'''
