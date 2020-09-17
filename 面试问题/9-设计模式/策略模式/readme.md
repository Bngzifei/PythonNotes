```python
class customer:
    customer_name=""
    snd_way=""
    info=""
    phone=""
    email=""
    def setPhone(self,phone):
        self.phone=phone
    def setEmail(self,mail):
        self.email=mail
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email
    def setInfo(self,info):
        self.info=info
    def setName(self,name):
        self.customer_name=name
    def setBrdWay(self,snd_way):
        self.snd_way=snd_way
    def sndMsg(self):
        self.snd_way.send(self.info)
```