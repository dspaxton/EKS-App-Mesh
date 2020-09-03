#!/usr/bin/env python3
import os, os.path
import json
import pymongo


import cherrypy
import random
import string

import cherrypy
from bson import json_util, ObjectId




class dbquery(object):
	@cherrypy.expose
	def index(self):
		from bson.json_util import loads,dumps
		## Create a MongoDB client, open a connection to Amazon DocumentDB as a replica set and specify the read preference as secondary preferred
		docdbendpoint = "working-docdb.cluster-cig0c7mgb1nk.eu-west-1.docdb.amazonaws.com"
		docdbuser = "mongoadmin"
		docdbpass = "demoadminpass"
		# uristring = "mongodb://" + docdbuser + ":" + docdbpass + "@" + docdbendpoint ":27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false"
		uristring = "mongodb://{0}:{1}@{2}:27017/".format(docdbuser,docdbpass,docdbendpoint)
		print(uristring)
		client = pymongo.MongoClient(uristring)
		##Specify the database to be used
		db = client.products
		##Specify the collection to be used
		col = db.items
		#get count of items
		count = col.count()
		print(count)
		ran = random.randint(0, count)
		print(ran)
		##Find the document that was previously written
		output = col.find_one({'id': ran })
		json_str = dumps(output)
		newjson = loads(json_str)
		print(json_str)
		##Print the result to the screen
		print(output)
		#print(type(output))
		##Close the connection
		client.close()
		values = { "Product" : newjson["product"], "Price" : newjson["price"] }
		#return dumps(newjson["product"]["price"])
		return dumps(values)
		# return count


if __name__ == '__main__':
	cherrypy.quickstart(dbquery())

