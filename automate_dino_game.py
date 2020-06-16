import pyautogui
from PIL import Image,ImageGrab
import time
#from numpy import asarray
pyautogui.FAILSAFE = False
def press(key):
    pyautogui.press(key)


def isCollide(data):

    day = True
    for i in range(550,560):
        for j in range(800,810):
            if data[i,j]<100:
                day = False
                break
        if not day:
            break
        
    # Cactus
    for i in range(315,630):
        for j in range(580,688):
            if day:
                if data[i,j] < 100:
                    press('up')
                    return
            else:
                if data[i,j] > 100:
                    press('up')
                    return
                     

def show(image,data):
    #Draw the rectangle for day
    for i in range(550,560):
        for j in range(800,810):
            data[i,j] = 171
    # Draw the rectangle for cactus
    for i in range(315,630):
        for j in range(580,688):
            data[i,j] = 100
    
    image.show()

if __name__=='__main__':
    print('Hey.. Dino game is about to start in 3 seconds')
    time.sleep(3)
    press('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        #print(asarray(image))
        #show(image,data)
        #break
        




