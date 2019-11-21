import credientials
client=credientials.client
db=client.test
db=db.userdata
for x in db.find():
    print(x['Name'],x['_id'])
input()
