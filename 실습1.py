import math

def math(a,b,c):
    if b^2-4*a*c>=0: 
        print("근은 %d와 %d입니다." %(-b+math.sqrt(b^2)-4*a*c,-b-math.sqrt(b^2)-4*a*c))
    elif b^2-4*a*c==0:
        print("%d" %(-b/2*a))
        print("중근을 갖습니다.")
    else:
        print("근이 존재하지 않습니다.")

math(2,3,5)
    

