import firebase_admin
import pandas as pd
import json

# Step 1: Open xlsx and convert to JSON
df = pd.read_excel("example_input.xlsx")
results = df.to_json("results.json", orient="records")

# Step 2: Connect to Firebase and Reference the root
cred_obj = firebase_admin.credentials.Certificate('....path to file') ## UPDATE
default_app = firebase_admin.initialize_app(cred_object, {'databaseURL':databaseURL}) ## UPDATE
db = firebase_admin.db
ref = db.reference("/")

# Step 3: Upload JSON to firebase

# Load the JSON
with open("results.json", "r") as f:
	file_contents = json.load(f)

# Set the context of the DB
ref = db.reference("/Items") ## UPDATE ##

# Start adding items into firebase
for key, value in file_contents.items():
	ref.push().set(value)
