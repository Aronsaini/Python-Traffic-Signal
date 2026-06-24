import time
def countdown():
    for sec in range(30,-1,-1):
            print(f"\rTimer : {sec:02}",end="")
            time.sleep(1)
    print()        
def P1_Tsig():
    print("\n")
    print(" Path 1 : 🟢 : < ^ > ")
    print("\n")
    print(" Path 2 : 🔴")
    print(" Path 3 : 🔴")
    print(" Path 4 : 🔴")
    print("\n")

def P2_Tsig():
    print("\n")
    print(" Path 2 : 🟢 : < ^ > ")
    print("\n")
    print(" Path 1 : 🔴")
    print(" Path 3 : 🔴")
    print(" Path 4 : 🔴")
    print("\n")

def P3_Tsig():
    print("\n")
    print(" Path 3 : 🟢 : < ^ > ")
    print("\n")
    print(" Path 1 : 🔴")
    print(" Path 2 : 🔴")
    print(" Path 4 : 🔴")
    print("\n")

def P4_Tsig():
    print("\n")
    print(" Path 4 : 🟢 : < ^ > ")
    print("\n")
    print(" Path 1 : 🔴")
    print(" Path 2 : 🔴")
    print(" Path 3 : 🔴")
    print("\n")

def T_sig_normal():
    while True:
        P1_Tsig()
        countdown()
        P2_Tsig()
        countdown()
        P3_Tsig()
        countdown()
        P4_Tsig()
        countdown()
        terminate=input("Do you want to Terminate the Signal (Y/N) :")
        if terminate=="Y":
            break
def T_sig_spcl():
    Td={"P1_Tsig":"Blinking Orange","P2_Tsig":"Blinking Orange","P3_Tsig":"Blinking Orange","P4_Tsig":"Blinking Orange"}
    for i in Td:
        print(i,":",Td[i])
        print("\n")
    print("!!! Drive Safely !!!")    
print("******************************")
print("\n")
print("\n")
print("***Time Required***")
print("If Time is 12:00am to 5:00am Enter 1")
print("If Time is 5:01am to 11:59pm Enter 2")
print("\n")
while True:
    try:
        T=int(input("Enter Option :"))
        break
    except ValueError:
            print("Invalid Input :- Please Enter Number")
            
print("\n")
while True:
    if T==1:
       T_sig_spcl()
    elif T==2:
        T_sig_normal()
    else:
        print("***Invalide Time Choice***")
    break    
    