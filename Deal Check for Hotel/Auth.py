import Credentials
client = Credentials.client
db = client.Bookingwebsite

def main(X,Y):
    result1=db.Registration.find_one({'User':X})
    result2=db.Registration.find_one({'Password':Y})
       
    if result1 != result2:
        return False
    elif(result1==None) or (result2==None):
        return False
    else:
        return True
