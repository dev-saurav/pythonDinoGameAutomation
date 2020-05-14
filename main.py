import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(250, 300):
        for j in range(360, 380):
            if data[i, j] > 150:
                return True
    return False            

if __name__ == "__main__":
    print('Hey! dino game is to start in 5 sec.')
    time.sleep(2)
    pyautogui.keyDown('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        # for i in range(250, 300):
        #     for j in range(360, 380):
        #         data[i, j] = 255
        # image.show()
        # break    
        
    


