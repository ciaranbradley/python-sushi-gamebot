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

#desktop
#x_offset = 156
#y_offset = 313
#laptop
x_offset = 9
y_offset = 80


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

def clickOn(cord, finalwait = 2.5):
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
    menu_toppings = (540, 271)
    t_exit = (585, 345)
    
    t_shrimp = (460, 227)
    t_nori = (460,291)
    t_roe = (543,291)
    t_salmon = (460,345)
    t_unagi = (543,227)

    menu_rice = (540,292)
    buy_rice = (536, 292)
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
    mousePos((87, 210))
    leftClick()
    mousePos((191, 210))
    leftClick()
    mousePos((290, 210))
    leftClick()
    mousePos((392, 210))
    leftClick()
    mousePos((494, 210))
    leftClick()
    mousePos((595, 210))
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
foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}
              


def foldMat():
    mousePos(Cord.mat)
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == "caliroll":
        print "Making a caliroll"
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
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
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
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
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
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

def cr():
    makeFood('caliroll')

def og():
    makeFood('onigiri')

def gk():
    makeFood('gunkan')

def openPhone():
    mousePos(Cord.phone)
    time.sleep(.1)
    leftClick()

def buyItem(item_cord, item_name):
    mousePos(item_cord)
    time.sleep(.5)
    leftClick()
    mousePos(Cord.delivery_norm)
    foodOnHand[item_name] += 10
    time.sleep(.5)
    leftClick()
    time.sleep(.3)

def buyRice():
    buyItem(Cord.buy_rice, 'rice')

def closePhone():
    mousePos(Cord.t_exit)
    leftClick()
    time.sleep(1)

def buyFood(food):
    #Rice has it's own menu
    if food == 'rice':
        openPhone()
        mousePos(Cord.menu_rice)
        time.sleep(.5)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127,127,127):
            print "rice is available"
            buyItem(Cord.buy_rice, 'rice')
        else:
            print 'rice is NOT available'
            closePhone()
            buyFood(food)

    if food == 'nori':
        openPhone()
        mousePos(Cord.menu_toppings)
        time.sleep(.5)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_nori) != (109, 123, 127):
            print 'nori is available'
            buyItem(Cord.t_nori, 'nori')
            
        else:
            print "nori is NOT available"
            closePhone()
            buyFood(food)

    if food == 'roe':
        openPhone()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_roe) != (109, 123, 127):
            print 'roe is available'
            buyItem(Cord.t_roe, 'roe')
        else:
            print "roe is NOT available"
            closePhone()
            buyFood(food)
        
    if food == 'shrimp':
        openPhone()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_shrimp) != (109, 123, 127):
            print 'shrimp is available'
            buyItem(Cord.t_shrimp, 'shrimp')
        else:
            print "shrimp is NOT available"
            closePhone()
            buyFood(food)

    if food == 'salmon':
        openPhone()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_salmon) != (109, 123, 127):
            print 'salmon is available'
            buyItem(Cord.t_salmon,'salmon')
        else:
            print "salmon is NOT available"
            closePhone()
            buyFood(food)

    if food == 'unagi':
        openPhone()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.t_unagi) != (109, 123, 127):
            print 'unagi is available'
            buyItem(Cord.t_unagi,'unagi')
        else:
            print "unagi is NOT available"
            closePhone()
            buyFood(food)


def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)

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

seat_offset = 26

seats = {'seat_1': (seat_offset, 62),
         'seat_2': (seat_offset + 101, 62),
         'seat_3': (seat_offset + 202, 62),
         'seat_4': (seat_offset + 303, 62),
         'seat_5': (seat_offset + 404, 62),
         'seat_6': (seat_offset + 505, 62)}

"""
cr = 2100
gk = 5634
og = 1843
"""

sushiTypes = {1843:'onigiri',
              2100:'caliroll',
              1770:'gunkan'}

class Blank:
    seat_1 = 7204
    seat_2 = 5858
    seat_3 = 10639
    seat_4 = 9838
    seat_5 = 5198
    seat_6 = 6635

def grab_seats():
    for i in seats:
        print "Grabbing " + i
        box = (x_offset + seats[i][0], 
               y_offset + seats[i][1],
               x_offset + seats[i][0] + 55,
               y_offset + seats[i][1] + 16)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        a = array(im.getcolors())
        a = a.sum()
        print a
        im.save(os.getcwd() + '\\'+ i + '__' + str(int(time.time())) + '.png', 'PNG')
        #return a
        

def grab_seat(name, pos_tuple):
    box = (x_offset + pos_tuple[0], 
           y_offset + pos_tuple[1],
           x_offset + pos_tuple[0] + 55,
           y_offset + pos_tuple[1] + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    #im.save(os.getcwd() + '\\'+ name + '__' + str(int(time.time())) + '.png', 'PNG')
    return a
    

def grab():
    box = (x_offset + 1, y_offset + 1,x_offset + 640, y_offset + 480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a


def checkSeat(seat_name):
    
    s = grab_seat(seat_name, seats[seat_name])
    if s != getattr(Blank, seat_name):
        if sushiTypes.has_key(s):
            print '%s is occupied and needs %s' % (seat_name, sushiTypes[s])
            makeFood(sushiTypes[s])
        else:
            print '%s sushi not found!\n sushiType %i' % (seat_name, s)

    else:
        print '%s unoccupied: debug %i' % (seat_name, s)
    

def checkBubs():
    
    checkSeat('seat_1')
    checkSeat('seat_2')
    checkFood()
    checkSeat('seat_3')
    clearTables()
    checkSeat('seat_4')
    checkFood()
    checkSeat('seat_5')
    checkSeat('seat_6')
    checkFood()
    clearTables()
    time.sleep(3)
    
    
    

def main():
    startGame()
    while True:
        checkBubs()

if __name__ == '__main__':
    pass
