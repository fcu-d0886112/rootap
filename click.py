import pyautogui
import pygetwindow as gw
import time
import threading

x_plant_2 = 828
stop_event = threading.Event()
pyautogui.PAUSE = 1
leftWindow_position=[
    [828,455],
    [828,530],
    [220,128],
    [240,233]
]
leftWindow_position_a=[
    [810,72],
    [264,530],
    [678,168],
    [746,168],
    [883,463],
    [796,499],
    [46,81],
    [139,222],
    [111,347],
]

def plant_seed(x_plant):
    y_plant_1 = 455
    y_plant_2 = 530
    pyautogui.moveTo(x=x_plant, y=y_plant_1, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(x=x_plant, y=y_plant_2, duration=0.25)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(x=x_plant, y=y_plant_1, duration=0.25)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
   
def apply_p(w:int):
    seq=[0,1,7,8,3,4,5,2,4,5,6]
    if w==1:
        for i in seq:
            pyautogui.moveTo(*leftWindow_position_a[i], duration=0.5)
            pyautogui.click()
            '''
    if w==2:
        for i in seq:
            pyautogui.moveTo(*rightWindow_position_a[i], duration=0.5)
            pyautogui.click()
'''
def background(limit_time: float):
    start_time = time.time()
    
    limit_count=int(8400/limit_time)+1
    count = limit_count-1
    while not stop_event.is_set():
        elapse_time = time.time()-start_time
        if int(elapse_time) == limit_time or int(elapse_time) == 0:
            count=count+1
            start_time = time.time()
            pyautogui.moveTo(*leftWindow_position[2], duration=0.5)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            plant_seed(x_plant_2)
            pyautogui.moveTo(*leftWindow_position[3], duration=0.5)
            time.sleep(0.5)
            pyautogui.click(*leftWindow_position[3])
            plant_seed(x_plant_2)
            time.sleep(2)
            print(count)
        if count==limit_count:
            apply_p(1)
            apply_p(2)
            count=0

def monitor():
    while True:
        user_input = input("輸入'q'結束主程式:")
        if user_input == 'q':
            print('結束')
            stop_event.set()
            return


fullscreenWidth, fullscreenHeight=pyautogui.size()
newWidth=int(fullscreenWidth//2)
windows=gw.getWindowsWithTitle('RO仙境傳說：愛如初見')
for i, win in enumerate(windows):
    width , height = win.size
    newHeight=int(height/width * newWidth)
    position_x=-8+i*(+newWidth)
   # print(position_x)
    win.resizeTo( 976, 588)
    time.sleep(1)
    win.moveTo(position_x,0)

print("先選擇種子")
inputtime = 0.0
while True:     
    ini_input = input("輸入種植東西的時長(min):")
    if ini_input.isdigit():
        inputtime = int(ini_input)*60.0
        if inputtime < 0:
            continue
        break
    else:
        print('請輸入整數')

    
bg_thread = threading.Thread(target=background, args=(inputtime,))
bg_thread.start()

monitor()

bg_thread.join()
