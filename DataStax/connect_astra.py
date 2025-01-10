# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider

# # Replace with the correct path to your secure connect bundle
# SECURE_CONNECT_BUNDLE_PATH = "path/to/your/secure-connect-database_name.zip"

# def connect_to_astra():
#     try:
#         # Load the Secure Connect Bundle
#         cloud_config = {'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH}
        
#         # Initialize the connection
#         auth_provider = PlainTextAuthProvider('your-clientId', 'your-secret')
#         cluster = Cluster(cloud=cloud_config)
#         session = cluster.connect()
        
#         # Set the keyspace
#         session.set_keyspace('socialmedia')
#         print("✅ Successfully connected to Astra DB!")
#         return session

#     except Exception as e:
#         print(f"❌ Connection Failed: {e}")

# # Test the connection
# session = connect_to_astra()



from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:aDAOsXWbvNqoyJboznZroQQI:35ab71bb70c4cd069b183fb280b6f7f318d0ca0ba5ba0d40d8a08daf47d1a905")
db = client.get_database_by_api_endpoint(
  "https://3ac783e6-8a7b-4370-903a-4ff60f0d822b-us-east1.apps.astra.datastax.com",
    keyspace="socialmedia",
)
      
print(f"Connected to Astra DB: {db.list_collection_names()}")