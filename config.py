
import pymongo
import certifi
from pymongo.mongo_client import MongoClient
import urllib

usernmae = urllib.parse.quote(".   ")
passwd = urllib.parse.quote(".  ")

uri = "mongodb+srv://%s:%s@bidreg.yl7ag.mongodb.net/?retryWrites=true&w=majority&appName=BidReg&ssl=true&ssl_cert_reqs=CERT_NONE" % (usernmae, passwd)

# Create a new client and connect to the server
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
db = client["BidReg"]
mycollection = db["REGISTER"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
