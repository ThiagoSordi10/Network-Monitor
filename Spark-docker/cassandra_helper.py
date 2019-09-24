from cassandra.cluster import Cluster
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine import connection
import uuid
from datetime import datetime 

def ConnectDB( clusterIPs ):
        # cluster connection, keyspace, and protocol version
        create_keyspace( clusterIPs )
        connection.setup( clusterIPs, "network", protocol_version=3 )
        create_tables()


def create_keyspace( clusterIPs ):
        cluster = Cluster( clusterIPs )
        #This will attempt to connection to a Cassandra instance on your local machine (127.0.0.1). You can also specify a list of IP addresses for nodes in your cluster
        session = cluster.connect()
        session.execute("CREATE KEYSPACE IF NOT EXISTS network WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }");	
        cluster.shutdown() 

def create_tables():
        # https://docs.datastax.com/en/developer/python-driver/3.19/api/cassandra/cqlengine/management/
        sync_table(Connection)
        sync_table(SSH)
        sync_table(DHCP)
        sync_table(HTTP)
        sync_table(DNS)

def insert_connection(data):
 	Connection.create(
                 ts = datetime.fromtimestamp(data.get('ts')),
                 uid = str(data.get('uid')),
                 orig_h = str(data.get('id.orig_h')),
                 orig_p = int(data.get('id.orig_p')),
                 resp_h = str(data.get('id.resp_h')),
                 resp_p = int(data.get('id.resp_p')),
                 proto = str(data.get('proto')),
                 duration = float(0 if data.get('duration') is None else data.get('duration')),                 
                 orig_bytes = int(0 if data.get('orig_bytes') is None else data.get('orig_bytes')),
                 resp_bytes = int(0 if data.get('resp_bytes') is None else data.get('resp_bytes')), 
                 conn_state = str(data.get('conn_state')),
                 #local_orig =   False             
                 # local_resp False
                 missed_bytes = int(data.get('missed_bytes')),
                 history = str(data.get('history')),
                 orig_pkts = int(data.get('orig_pkts')),
                 orig_ip_bytes = int(data.get('orig_ip_bytes')),
                 resp_pkts = int(data.get('resp_pkts')),
                 resp_ip_bytes = int(data.get('resp_ip_bytes')),
                 orig_l2_addr = str(data.get('orig_l2_addr')),
                 resp_l2_addr = str(data.get('resp_l2_addr'))
         )   


def insert_ssh(data):
        SSH.create( 
                ts = datetime.fromtimestamp(data.get('ts')), 
                uid = str(data.get('uid')), 
                orig_h = str(data.get('id.orig_h')),
                orig_p = int(data.get('id.orig_p')), 
                resp_h = str(data.get('id.resp_h')), 
                resp_p = int(data.get('id.resp_p')), 
                proto = str(data.get('proto')),
                auth_attempts = int(data.get('auth_attempts')),
                direction = str(data.get('direction')),
                server = str(data.get('server')),
                cipher_alg = str(data.get('cipher_alg')),
                mac_alg = str(data.get('mac_alg')),
                compression_alg=str(data.get('compression_alg')),
                kex_alg=str(data.get('kex_alg')),
                host_key_alg=str(data.get('host_key_alg')),
                host_key=str(data.get('host_key'))                 
        )

def insert_dhcp(data):
        DHCP.create(
                ts = datetime.fromtimestamp(data.get('ts')), 
                uid = str(data.get('uid')), 
                orig_h = str(data.get('id.orig_h')),
                orig_p = int(data.get('id.orig_p')), 
                resp_h = str(data.get('id.resp_h')), 
                resp_p = int(data.get('id.resp_p')), 
                proto = str(data.get('proto')),
		mac=str(data.get('mac')),
		host_name = str(data.get('host_name')),
		msg_types = list(['',] if data.get('msg_types') is None else data.get('msg_types')),
		duration  = float(data.get('duration')), 
		assigned_ip=str(data.get('assigned_ip')), 
		lease_time=str(data.get('lease_time')), 
		trans_id1=str(data.get('trans_id1'))
	)

def insert_http(data):
        HTTP.create(
                ts = datetime.fromtimestamp(data.get('ts')), 
                uid = str(data.get('uid')), 
                orig_h = str(data.get('id.orig_h')),
                orig_p = int(data.get('id.orig_p')), 
                resp_h = str(data.get('id.resp_h')), 
                resp_p = int(data.get('id.resp_p')), 
                proto = str(data.get('proto')),
		trans_depth=str(data.get('trans_depth')), 
		method=str(data.get('method')), 
		host=str(data.get('host')), 
		uri=str(data.get('uri')), 
		referrer=str(data.get('referrer')), 
		version=str(data.get('version')), 
		user_agent=str(data.get('user_agent')), 
		request_body_len=str(data.get('request_body_len')), 
		response_body_len=str(data.get('response_body_len')), 
		status_code=str(data.get('status_code')), 
		status_msg=str(data.get('status_msg')), 
		info_code=str(data.get('info_code')), 
		info_msg=str(data.get('info_msg')), 
		tags=str(data.get('tags')), 
		username=str(data.get('username')), 
		password=str(data.get('password')), 
		proxied=str(data.get('proxied')), 
		orig_fuids=str(data.get('orig_fuids')), 
		orig_filenames=str(data.get('orig_filenames')), 
		orig_mime_types=str(data.get('orig_mime_types')), 
		resp_fuids=str(data.get('resp_fuids')), 
		resp_filenames=str(data.get('resp_filenames')), 
		resp_mime_types=str(data.get('resp_mime_types'))
	)

def insert_dns(data):
        DNS.create(
                ts = datetime.fromtimestamp(data.get('ts')), 
                uid = str(data.get('uid')), 
                orig_h = str(data.get('id.orig_h')),
                orig_p = int(data.get('id.orig_p')), 
                resp_h = str(data.get('id.resp_h')), 
                resp_p = int(data.get('id.resp_p')), 
                proto = str(data.get('proto')),
                trans_id=int(data.get('trans_id')), 
                rtt=str(data.get('rtt')), 
                query=str(data.get('query')), 
                qclass=str(data.get('qclass')), 
                qclass_name=str(data.get('qclass_name')), 
                qtype=str(data.get('qtype')), 
                qtype_name=str(data.get('qtype_name')), 
                rcode=int(0 if data.get('rcode') is None else data.get('rcode')),
                rcode_name=str(data.get('rcode_name')), 
                aa=bool(data.get('aa')), 
                tc=bool(data.get('tc')), 
                rd=bool(data.get('rd')), 
                ra=bool(data.get('ra')), 
                z=int(0 if data.get('z') is None else data.get('z')), 
                answers=list(['',] if data.get('answers') is None else data.get('answers')), 
                ttls=list([0,] if data.get('TTLs') is None else data.get('TTLs')),
                rejected=bool(data.get('rejected')), 
                addl=str(data.get('addl')),
                auth=str(data.get('auth'))
                )


# super class
class ConnBaseModel(Model):
        __table_name__ = 'connection'
        #columns.DateTime.truncate_microseconds = True          
        id = columns.UUID(primary_key=True, default=uuid.uuid4)
        ts = columns.DateTime( primary_key=True, partition_key=True )
        #
        # CONN / SSH / DHCP / DNS / HTTP
        log_type = columns.Text(discriminator_column=True, index=True)
        # 
        uid = columns.Text(required=True)
        orig_h = columns.Inet(required=True, index=True)
        orig_p = columns.Integer(required=True, index=True)
        resp_h = columns.Inet(required=True, index=True)
        resp_p = columns.Integer(required=True, index=True)
        proto = columns.Text(required=True, index=True)
        duration = columns.Float(required=False)
        orig_bytes = columns.Integer(required=False)
        resp_bytes = columns.Integer(required=False)
        conn_state = columns.Text(required=False)
        #local_orig =   False             
        # local_resp False
        missed_bytes = columns.Integer(required=False)
        history = columns.Text(required=False)
        orig_pkts = columns.Integer(required=False)
        orig_ip_bytes = columns.Integer(required=False)
        resp_pkts = columns.Integer(required=False)
        resp_ip_bytes = columns.Integer(required=False)
        orig_l2_addr = columns.Text(required=False)
        resp_l2_addr = columns.Text(required=False)
        
class Connection(ConnBaseModel):    
        __discriminator_value__ = 'CONN'    

class SSH(ConnBaseModel):
        __discriminator_value__ = 'SSH'            
        auth_attempts = columns.Integer(required=False)
        direction = columns.Text(required=False)
        server = columns.Text(required=False)
        cipher_alg = columns.Text(required=False)
        mac_alg = columns.Text(required=False)
        compression_alg = columns.Text(required=False)
        kex_alg = columns.Text(required=False)
        host_key_alg = columns.Text(required=False)
        host_key = columns.Text(required=False)

class DHCP(ConnBaseModel):
        __discriminator_value__ = 'DHCP'                    
        client_addr  = columns.Inet(required=False)
        mac  = columns.Text(required=False)
        host_name  = columns.Text(required=False)
        msg_types  = columns.Set(value_type=columns.Text, required=False)
        duration  = columns.Float(required=False)
        assigned_ip = columns.Text(required=False)
        lease_time = columns.Text(required=False)
        trans_id1 = columns.Text(required=False)

class HTTP(ConnBaseModel):
        __discriminator_value__ = 'HTTP'                            
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

class DNS(ConnBaseModel):
        __discriminator_value__ = 'DNS'
        trans_id  = columns.Integer(required=False)
        rtt = columns.Text(required=False)
        query = columns.Text(required=False)
        qclass = columns.Text(required=False)
        qclass_name = columns.Text(required=False)
        qtype = columns.Text(required=False)
        qtype_name = columns.Text(required=False)
        rcode = columns.Integer(required=False)
        rcode_name = columns.Text(required=False)
        aa = columns.Boolean(required=False)
        tc = columns.Boolean(required=False)
        rd = columns.Boolean(required=False)
        ra = columns.Boolean(required=False)
        z = columns.Integer(required=False)
        answers = columns.Set(columns.Text, required=False)
        ttls = columns.Set(columns.Float, required=False)
        rejected = columns.Boolean(required=False)
        addl = columns.Text(required=False)
        auth = columns.Text(required=False)
