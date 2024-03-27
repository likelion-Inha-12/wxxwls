from 실습2 import Bankaccount

class acc(Bankaccount):
    interest=0.05
    def __init__(self,name,acount,inte):
        """계좌의 정보를 표시합니다."""
        super().__init__(name,acount)
        self.inte=inte
    
    def display_int(self):
        """계좌의 이자를 표시합니다"""
        print("%s님의 계좌 잔액은 %d원입니다." %(self.name,self.account))
        print("이자율: %s" %(self.inte))
      
    def display_deposit(self,deposit):
       """입금액을 표시합니다."""
       if deposit >0:
            self.account+=deposit
            print(f"{deposit}원이 입급되었습니다." )
            interest=self.account*self.inte*0.01
            self.account+=interest
            print("%s님의 계좌에 %d원의 이자가 추가되었습니다." %(self.name,interest))

self_acount1 = acc("woojin",1000,5)
self_acount1.display_int()
self_acount1.display_deposit(500)
self_acount1.display_withdraw(200)
self_acount1.display_int()




    

    