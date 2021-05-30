from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': '/home/yash/Documents/Ml-dL-Assignments/secure-connect-yash.zip'
}
auth_provider = PlainTextAuthProvider(
    'hCTLhrCrzQLXeUEnxZfCPwd', ' r+4-TauSaejyKnAmrf8l2AdjZoy.vX7LAPJ+t0XsyQxzf0zZon8I+fXaqU6iYcrreHLgJYjQAhp5yMBdXYUk+iZwz51teZAZTZbKKr55N40Yj2N8SCGnAQFMPSxB5GTw')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("create keyspace yash621").one()
# if row:
#     print(row[0])
# else:
#     print("An error occurred.")
# session.execute("")
