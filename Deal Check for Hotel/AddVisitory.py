import Credentials
import datetime
client = Credentials.client
db = client.Bookingwebsite
    
def addVisitor(X):
    x=db.Registration.find_one({'User':X[1]})
    if x == None:
                result=db.Registration.insert_one({'Name':X[0],'User':X[1],'Email':X[2],'Phone':X[3],'Password':X[4],
                                                   'date':datetime.datetime.utcnow()})
                return True
    else:
                return False
    
