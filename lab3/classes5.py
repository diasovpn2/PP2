class Account:
    def __init__(self,b,d,w):
        self.b =b
        self.d=d
        self.w=w
    def depo(self):
        print("баланс пополнен",self.b+self.w)
    def withdr(self):
        if self.b-self.w<0:
            print("error")
        else:
            print(self.b-self.w)
q =Account(232,230,233)
q.withdr()