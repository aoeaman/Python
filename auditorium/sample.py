import credientials
from bson.objectid import ObjectId
client=credientials.client
db=client.test
q='5bceeae4fe4eb80adc88cc44'
x=db.userdata.find({'_id':ObjectId(q)})
print(x)
