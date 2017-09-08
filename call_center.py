cd class Call(object):
    def __init__(self,idt,name,phone,time,reason,*args):
        self.idt = idt
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        print "Unique ID:", self.idt
        print "Customer's Name:", self.name
        print "Customer's Phone:", self.phone
        print "Time of Call:", self.time
        print "Reason for call:", self.reason

call1 = Call(100,"Paul Franco","206-538-8558","10:10","prank call").display()

class CallCenter(Call):
    def __init__(self,idt,name,phone,time,reason,queue,calls):
        super(CallCenter,self).__init__(idt,name,phone,time,reason,queue,calls)
        self.queue = queue
        self.calls = []
 
        
print "///"
new_call = CallCenter(2345,"Jesus","206-555-555","9:30","Return Item",10,5).display()

