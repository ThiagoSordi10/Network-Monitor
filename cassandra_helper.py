from cassandra.cluster import Cluster
from cassandra.cqlengine.columns import *
from cassandra.cqlengine.models import Model
from cassandra.cqlengine.usertype import UserType
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
        # truncate microseconds from timestamps


def insert_connection(data):
        Connection.create(
                 conn = Connection_inherited(
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
                         local_orig = bool(data.get('local_orig')),          
                         local_resp = bool(data.get('local_resp')), 
                         missed_bytes = int(data.get('missed_bytes')),
                         history = str(data.get('history')),
                         orig_pkts = int(data.get('orig_pkts')),
                         orig_ip_bytes = int(data.get('orig_ip_bytes')),
                         resp_pkts = int(data.get('resp_pkts')),
                         resp_ip_bytes = int(data.get('resp_ip_bytes')),
                         orig_l2_addr = str(data.get('orig_l2_addr')),
                         resp_l2_addr = str(data.get('resp_l2_addr'))
                )
         )                     

def insert_ssh(data):
        SSH.create(
                 conn = Connection_inherited(
                                ts = datetime.fromtimestamp(data.get('ts')), 
                                uid = str(data.get('uid')), 
                                orig_h = str(data.get('id.orig_h')),
                                orig_p = int(data.get('id.orig_p')), 
                                resp_h = str(data.get('id.resp_h')), 
                                resp_p = int(data.get('id.resp_p')), 
                                proto = str(data.get('proto'))
                        ),
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
		conn = Connection_inherited(
                                ts = datetime.fromtimestamp(data.get('ts')), 
                                uid = str(data.get('uid')), 
                                orig_h = str(data.get('id.orig_h')),
                                orig_p = int(data.get('id.orig_p')), 
                                resp_h = str(data.get('id.resp_h')), 
                                resp_p = int(data.get('id.resp_p')), 
                                proto = str(data.get('proto'))
                        ),
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
		conn = Connection_inherited(
                                ts = datetime.fromtimestamp(data.get('ts')), 
                                uid = str(data.get('uid')), 
                                orig_h = str(data.get('id.orig_h')),
                                orig_p = int(data.get('id.orig_p')), 
                                resp_h = str(data.get('id.resp_h')), 
                                resp_p = int(data.get('id.resp_p')), 
                                proto = str(data.get('proto'))
                        ),
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
                conn = Connection_inherited(
                                ts = datetime.fromtimestamp(data.get('ts')), 
                                uid = str(data.get('uid')), 
                                orig_h = str(data.get('id.orig_h')),
                                orig_p = int(data.get('id.orig_p')), 
                                resp_h = str(data.get('id.resp_h')), 
                                resp_p = int(data.get('id.resp_p')), 
                                proto = str(data.get('proto'))
                        ),
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
                auth=str(data.get('auth')))
 
#Tabela base de conexão                   
class Connection_inherited(UserType):
        #DateTime.truncate_microseconds = True                
        ts = DateTime(required=True)
        uid = Text(required=True)
        orig_h = Inet(required=True)
        orig_p = Integer(required=True)
        resp_h = Inet(required=True)
        resp_p = Integer(required=True)
        proto = Text(required=True)
        duration = Float(required=False)
        orig_bytes = Integer(required=False)
        resp_bytes = Integer(required=False)
        conn_state = Text(required=False)
        local_orig =  Boolean(required=False)       
        local_resp = Boolean(required=False)
        missed_bytes = Integer(required=False)
        history = Text(required=False)
        orig_pkts = Integer(required=False)
        orig_ip_bytes = Integer(required=False)
        resp_pkts = Integer(required=False)
        resp_ip_bytes = Integer(required=False)
        orig_l2_addr = Text(required=False)
        resp_l2_addr = Text(required=False)

class Connection(Model):
        id = UUID(primary_key=True, default=uuid.uuid4)
        conn = UserDefinedType(Connection_inherited)
        

class SSH(Model):
        id = UUID(primary_key=True, default=uuid.uuid4)
        conn = UserDefinedType(Connection_inherited)
        auth_attempts = Integer(required=False)
        direction = Text(required=False)
        server = Text(required=False)
        cipher_alg = Text(required=False)
        mac_alg = Text(required=False)
        compression_alg = Text(required=False)
        kex_alg = Text(required=False)
        host_key_alg = Text(required=False)
        host_key = Text(required=False)

class DHCP(Model):
        id = UUID(primary_key=True, default=uuid.uuid4)
        conn = UserDefinedType(Connection_inherited)
        client_addr  = Inet(required=False)
        mac  = Text(required=False)
        host_name  = Text(required=False)
        msg_types  = Set(value_type=Text, required=False)
        duration  = Float(required=False)
        assigned_ip = Text(required=False)
        lease_time = Text(required=False)
        trans_id1 = Text(required=False)

class HTTP(Model):
        id = UUID(primary_key=True, default=uuid.uuid4)
        conn = UserDefinedType(Connection_inherited)
        trans_depth  = Text(required=False)
        method = Text(required=False)
        host = Text(required=False)
        uri = Text(required=False)
        referrer = Text(required=False)
        version = Text(required=False)
        user_agent = Text(required=False)
        request_body_len = Text(required=False)
        response_body_len = Text(required=False)
        status_code = Text(required=False)
        status_msg = Text(required=False)
        info_code = Text(required=False)
        info_msg = Text(required=False)
        tags = Text(required=False)
        username = Text(required=False)
        password = Text(required=False)
        proxied = Text(required=False)
        orig_fuids = Text(required=False)
        orig_filenames = Text(required=False)
        orig_mime_types = Text(required=False)
        resp_fuids = Text(required=False)
        resp_filenames = Text(required=False)
        resp_mime_types = Text(required=False)

class DNS(Model):
        id = UUID(primary_key=True, default=uuid.uuid4)
        conn = UserDefinedType(Connection_inherited)
        trans_id  = Integer(required=False)
        rtt = Text(required=False)
        query = Text(required=False)
        qclass = Text(required=False)
        qclass_name = Text(required=False)
        qtype = Text(required=False)
        qtype_name = Text(required=False)
        rcode = Integer(required=False)
        rcode_name = Text(required=False)
        aa = Boolean(required=False)
        tc = Boolean(required=False)
        rd = Boolean(required=False)
        ra = Boolean(required=False)
        z = Integer(required=False)
        answers = Set(Text, required=False)
        ttls = Set(Float, required=False)
        rejected = Boolean(required=False)
        addl = Text(required=False)
        auth = Text(required=False)



#https://docs.datastax.com/en/developer/python-driver/3.19/getting_started/
