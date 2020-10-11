import threading
varDownInput =[ 0, 0, 0, 0, 0, 0, 0, 0]
varUpInput = [0, 0, 0, 0, 0, 0, 0, 0]
varDestination=[0, 0, 0, 0, 0, 0, 0, 0]
varStopPoint = [0, 0, 0, 0, 0, 0, 0, 0]
current = 0
upFlag = False
downFlag = False
stopFlag = True  # when upFlag||downFlag!=True
forTestOut=[1,0,0,0,0,0,0,0]
finish=False
timer=False
openDoor=False
def getCurrent():
    global forTestOut,current
    for i in range(8):
        if forTestOut[i]==1:
            current=i
    pass
def getInput():
    global varUpInput,varDownInput,varDestination,openDoor
    o=input("ENTER to next / O to open /ANY OTHER KEY to input: ").strip() 
    while o!= '' and o!='o':
        varInput=input("u/d/D(up/down/Destination),1~8(where are you) (eg:u,6):").strip()
        i,j=varInput.split(',')
        if i=='u':
            varUpInput[int(j)-1]=1
        elif i=='d':
            varDownInput[int(j)-1]=1
        elif i=='D':
            varDestination[int(j)-1]=1
        o=input("ENTER to next / ANY OTHER KEY to input: ").strip() 
    if o == 'o':
        openDoor=True
def openTheDoor():
    global openDoor
    if True:#未达限位
        print("the door has been opened!")
    else:
        openDoor=False
def motor(upStopDown):
    global forTestOut,current,upFlag,downFlag,stopFlag,finish,openDoor
    if upStopDown==0:
        if not finish:
            openTheDoor()
            getTimer()
            closeTheDoor()
    elif upStopDown==1:
        forTestOut[current]=0
        forTestOut[(current+1) if current<7 else 7]=1
    else:
        forTestOut[current]=0
        forTestOut[(current-1) if current>0 else 0]=1
    print(forTestOut,("UP" if upFlag else ("DOWN" if downFlag else "STOP")),current+1)
    pass

def setStopPoint():
    global upFlag,downFlag,varStopPoint,current,stopFlag
    if upFlag:
        for i in range(8-current):
            if varUpInput[current+i]==1:
                varStopPoint[current+i]=1
                varUpInput[current+i]=0
            if varDestination[current+i]==1:
                varStopPoint[current+i]=1
                varDestination[current+i]=0
    elif downFlag:
        for i in range(current+1):
            if varDownInput[current-i]==1:
                varStopPoint[current-i]=1
                varDownInput[current-i]=0
            if varDestination[current-i]==1:
                varStopPoint[current-i]=1
                varDestination[current-i]=0
    elif stopFlag:
        for i in range(8):
            if varDownInput[i]==1:
                varStopPoint[i]=1
                varDownInput[i]=0
            if varDestination[i]==1:
                varStopPoint[i]=1
                varDestination[i]=0
            if varUpInput[i]==1:
                varStopPoint[i]=1
                varUpInput[i]=0
    if finish:
        varStopPoint[current]=0
    pass
def run():
    global varStopPoint,current,stopFlag,finish,openDoor
    if varStopPoint[current] == 1 or stopFlag:
        motor(0)  # stop:0
    elif upFlag:
        finish=False
        motor(1)  # up:1
    elif downFlag:
        finish=False
        motor(-1)  # down:-1
    pass
def closeTheDoor():
    global finish,timer,openDoor
    while input("close the door ? (y/n)").strip()!="y" and timer :
        pass
    if not openDoor:
        finish=True
        print("door closed!")
    else:
        openTheDoor()
    pass
def getTimer():
    global timer,finish
    if not timer:
        timer=True
        threading.Timer(5,cleanTimer).start()
    elif not finish:
        timer=True
    else:
        timer=False
def cleanTimer():
    global timer
    timer=False
def setFlag():
    global stopFlag,current,downFlag,upFlag
    if stopFlag:
        if current < 4:
           flag = True
           i = 0
           while flag and i < 8-current:
                if current-i >= 0:
                    if varStopPoint[current-i] == 1:
                        downFlag = True
                        stopFlag = False
                        flag = False
                if varStopPoint[current+i]==1:
                    upFlag=True
                    stopFlag=False
                    flag=False
                i=i+1
        else:
           flag=True
           i=0
           while flag and i<=current:
               if current+i<8:
                    if varStopPoint[current+i]==1:
                        upFlag=True
                        stopFlag=False
                        flag=False
               if varStopPoint[current-i]==1:
                        downFlag=True
                        stopFlag=False
                        flag=False
               i=i+1
    else:
        if downFlag:
            flag=True
            i=1
            while flag and current-i>=0:
                if varStopPoint[current-i]==1:
                    downFlag=True
                    upFlag=False
                    flag=False
                i=i+1
            if flag:
                stopFlag=True
                downFlag=False
                upFlag=False
                pass
        else:
            flag=True
            i=1
            while flag and current+i<8:
                if varStopPoint[current+i]==1:
                    upFlag=True
                    downFlag=False
                    flag=False
                i=i+1
            if flag:
                stopFlag=True
                downFlag=False
                upFlag=False
                pass
            
if __name__ == "__main__":
    while True:
        getCurrent()
        getInput()
        setStopPoint()
        setFlag()
        run()
    pass