class Bankaccount:
    def __init__(self,name,account):
        """계좌의 입금, 출금 잔액을 표시합니다."""
        self.name=name
        self.account=account
        
        
    def display_info(self):
        """계좌 잔액을 표시합니다."""
        print("woojin님의 계좌 잔액은 %s원 입니다." %(self.account))

   
    def display_deposit(self,deposit):
       """입금액을 표시합니다."""
       if deposit >0:
            self.account+=deposit
            print(f"{deposit}원이 입급되었습니다." )
       else:
          print("금액은 양수여야 합니다.")

    def display_withdraw(self,withdraw):
        """출금액을 표시합니다."""
        if withdraw >0:
            self.account-=withdraw
            print("%d원이 출금되었습니다." %(withdraw))
        elif self.account<0:
         print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.")
    
    
    
self_acount1 = Bankaccount("woojin",1000)

self_acount1.display_info()
self_acount1.display_deposit(500)
self_acount1.display_withdraw(200)






