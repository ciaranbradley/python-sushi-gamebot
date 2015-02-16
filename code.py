import ImageGrab
import os
import time
import win32api, win32con
import ImageOps
from numpy import *

"""
 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""
x_offset = 156
y_offset = 313

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."

def leftDown():
    win32api.mouse_event(win32com.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'

def mousePos(cord):
    win32api.SetCursorPos((x_offset + cord[0], y_offset + cord[1]))

def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_offset
    y = y - y_offset
    print x,y

def clickOn(cord, finalwait = 1.5)
    mousePos(cord)
    time.sleep(.1)
    leftClick()
    time.sleep(finalwait)

class Cord:
    f_shrimp = (41,335)
    f_rice = (98,337)
    f_nori = (35, 389)
    f_roe = (96, 400)
    f_salmon = (36, 448)
    f_unagi = (95,445)

    phone = (564, 385)
    mat = (133, 406)
    menu_toppings = (540, 276)
    

    t_shrimp = (496, 228)
    t_nori = (489,273)
    t_roe = (577,282)
    t_salmon = (493,334)
    t_unagi = (577,233)

    menu_rice = (531,294)
    buy_rice = (546, 299)
    menu_sake = (528,314)
    buy_sake = (543,288)
    delivery_norm = (484,299)
    delivery_express = (575,300)

"""
Plate cords
    91, 208
    193, 209
    298, 212
    394, 212
    495, 212
    604, 213

"""



def clearTables():
    mousePos((91, 208))
    leftClick()
    mousePos((193, 208))
    leftClick()
    mousePos((298, 212))
    leftClick()
    mousePos((394, 212))
    leftClick()
    mousePos((495, 212))
    leftClick()
    mousePos((604, 212))
    leftClick()
    time.sleep(1)

"""
Recipies

    onigiri
        2 rice, 1 nori

    caliroll:
        1 rice, 1 nori, 1 roe

    gunkan:
        1 rice, 1 nori, 2 roe
"""

def foldMat():
    mousePos(Cord.mat)
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == "caliroll":
        print "Making a caliroll"
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'onigiri':
        print "Making onigiri"
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

    elif food == 'gunkan': 
        print "Making gunkan"
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)


def buyFood(food):

    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_nori) != (33, 30, 11)
            print 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print "nori is NOT available'
            mou
        
    
    mousePos(Cord.phone)
    mousePos(Cord.menu_toppings)
    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)

    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)

    mousePos(Cord.delivery_norm)


def startGame():
    #Start Button Click
    mousePos((310, 200))
    leftClick()
    time.sleep(.1)

    #Continue button
    mousePos((310, 395))
    leftClick()
    time.sleep(.1)

    #Skip button
    mousePos((580, 455))
    leftClick()
    time.sleep(.1)

    #Todays Goal Continue button
    mousePos((310, 380))
    leftClick()
    time.sleep(.1)

    
def screenGrab():
    box = (x_offset + 1, y_offset + 1,x_offset + 640, y_offset + 480)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def main():
    screenGrab()

if __name__ == '__main__':
    pass
