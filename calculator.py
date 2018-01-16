def add():
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    result=num1+num2
    print(result)

def sub():
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    result=num1-num2
    print(result)

def multiply():
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    result=num1*num2
    print(result)

def divide():
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    if num1==0 or num2==0:
        print("Error")
        return
    result=num1/num2
    print(result)

def mok():
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    if num1==0 or num2==0:
        print("Error")
        return
    result=num1//num2
    print(result)

def namuji():
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    if num1==0 or num2==0:
        print("Error")
        return
    result=num1%num2
    print(result)

while True:
    print(" Menu ")
    print("------")
    print("1:덧셈")
    print("2:뺄셈")
    print("3:곱셈")
    print("4:나눗셈")
    print("5:나눗셈 몫")
    print("6:나눗셈 나머지")
    print("7:나가기")
    sel=int(input("선택하시오: "))

    if(sel==1):
        add()
    elif(sel==2):
        sub()
    elif(sel==3):
        multiply()
    elif(sel==4):
        divide()
    elif(sel==5):
        mok()
    elif(sel==6):
        namuji()
    elif(sel==7):
        break
    else:
        print("바르지 못한 입력값입니다. 다시 입력하여 주십시오.")
