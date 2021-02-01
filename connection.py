from pymongo import MongoClient
import datetime

client = MongoClient('mongodb+srv://mongoDBuser:mongoDBP%40%24%24W0RD@bigdataintegrationclust.rkeh2.mongodb.net/gettingStarted?retryWrites=true&w=majority')
db = client.test
people = db.people


personDocument = {
  "name": { "first": "mohamad", "last": "said" },
  "birth": datetime.datetime(1990, 11, 21),
  "contribs": [ "driver"],
  "views": 125
}

people.insert_one(personDocument)
people.find_one({ "name.last": "said" })
