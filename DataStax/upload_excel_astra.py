import pandas as pd
from astrapy import DataAPIClient

# Step 1: Initialize Astra Client
client = DataAPIClient("AstraCS:UZZIyPEGhsrGuDtGYpxvYtvK:01f4749ba4278649f6c9a17a798ddf13f6eee38181898fea3dc8d43e0c72d814")

# Connect to the database and keyspace
db = client.get_database_by_api_endpoint(
    "https://3ac783e6-8a7b-4370-903a-4ff60f0d822b-us-east1.apps.astra.datastax.com",
    keyspace="socialmedia",
)

print(f"✅ Connected to Astra DB. Available Collections: {db.list_collection_names()}")

# Step 2: Load the Excel Data
excel_file_path = r"C:\Users\91809\Documents\extended_social_media_engagement.xlsx"  # Provide the correct path
df = pd.read_excel(excel_file_path)

# Step 3: Convert DataFrame Rows to a List of Dictionaries
data_to_insert = df.to_dict(orient="records")

# Step 4: Insert Data into Astra DB
collection = db.get_collection("media")  # Ensure the collection exists
for row in data_to_insert:
    # Convert the column names and insert the data
    collection.insert_one({
        "post_id": int(row["Post ID"]),
        "post_type": row["Post Type"],
        "likes": int(row["Likes"]),
        "comments": int(row["Comments"]),
        "shares": int(row["Shares"])
    })

print("✅ Data successfully uploaded to Astra DB!")


#C:\Users\91809\Documents\extended_social_media_engagement.xlsx

#c:\Users\91809\Documents\social_media_datasets1.csv

#AstraCS_UZZIyPEGhsrGuDtGYpxvYtvK_01f4749ba4278649f6c9a17a798ddf13f6eee38181898fea3dc8d43e0c72d814