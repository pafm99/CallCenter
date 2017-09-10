from datetime import datetime

class Call(object):
    def __init__(self,name,phone,reason,id):
        num_of_calls = 0
        self.name = name
        self.phone = phone
        self.reason = reason
        self.id = id
        self.time = datetime.now().time() 
        


    def display(self):
        print "Call ID:", self.id
        print "Time of Call:", self.time
        print "Customer's Name:", self.name
        print "Customer's Phone:", self.phone
        print "Reason for call:", self.reason
        

class Call_Center(object):
    def __init__(self):
        self.calls = [] #Empty List
        self.next_id = 1
        
    def add_call(self,name,phone,reason): #This is what we are passing to Call(object)
        new_call = Call(name,phone,reason,self.next_id)
        self.next_id += 1
        self.calls.append(new_call) #Appends new calls to List
        #print "working"

    def remove_call(self):
        del self.calls[1]
        return self
        print self.calls

    def queue_size(self):
        print "There are ", len(self.calls), "calls left"
        return len(self.calls)
        
    def info(self):
        print "There are ", len(self.calls), "calls left"
        for caller in self.calls:
            print caller.name, caller.phone

    def filter(self,phone): #filter by phone number
        temp = []
        for caller in self.calls:
            if caller.phone == phone:
                temp.append(caller)                
                print "this is in temp",caller.name
        return self
        
        
        
        


newuser = Call_Center() #newuser is a database 
newuser.add_call("Jesus Franco","206-555-5555","test")
newuser.add_call("Paul Franco","235-333-333","test")
#newuser.queue_size()
#newuser.calls[1].display()
#newuser.remove_call()
#newuser.queue_size()
#newuser.queue_size()
#newuser.filter("206-538-8558")
newuser.info()


