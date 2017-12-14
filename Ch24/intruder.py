#Marshal Zhang S3C3 Option
# this is my program that simulates the intruder alarm system
def ChooseOption():
    global Option
    print("Press button: 1")
    print("Enter the Pin: 2")
    print("Sensor activated: 3")
    print("Two Minutes past: 4")
    print("End the program:5")
    Option=int(input("Please choose an option:"))
    
def run():
    global Option
    global S
    if S=="System Inactive" and Option==1:
        S="System Active"
    if Option==2:
        S="System Inactive"
    if S=="System Active"and Option==3:
        S="Alert Mode"
    if S=="Alert Mode" and Option==4:
        S="Alarm Bell Ring"
    print(S)

S="System Inactive"
ChooseOption()
while Option !=5:
    run()
    ChooseOption()


    
    

