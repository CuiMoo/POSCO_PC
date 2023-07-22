import pyautogui
import time

#-Fail Safe Activated-#
pyautogui.FAILSAFE = True

currentMouseX, currentMouseY = pyautogui.position()  
print("X Cordinate is: ", currentMouseX)  
print("Y Cordinate is: ", currentMouseY)
pyautogui.FAILSAFE = True

yStartPoint = 662 

#---INPUT HOW MANY OF YOUR ODERS HERE---#
HowMany = 3  
#--------------------------------------#

def autoBot():
    t1 = time.time()

    i=0
    global yStartPoint
    
    while i<HowMany:
        try:
            pyautogui.moveTo(904,yStartPoint,duration=2)    # Move to title
            pyautogui.click(904,yStartPoint,1,0.1,'left')   # Click at title
            pyautogui.moveTo(1471,155,duration=2)           # Move at the approve button
            time.sleep(1.5)                                 #Wait seconds 
            pyautogui.click(1471,155,1,0.1,'left')          #click at the approve button
            pyautogui.moveTo(905,519,duration=1)            #Move to the confimed button
            pyautogui.click(905,519,1,0.1,'left')           #click at the confirmed button
            time.sleep(1.5)                                 #wait seconds
            print(f'The order no.{i+1} has been approved')              
            #yStartPoint=yStartPoint -24
            i+=1
            
        except BaseException:
            print('Sequence suspended ')
            break
    t2 = time.time()      
    print(f'Done, Usage time: {(t2-t1):.2f}s.')
           
autoBot()
