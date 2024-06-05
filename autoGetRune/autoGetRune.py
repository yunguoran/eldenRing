import time
import threading

from pynput import keyboard,mouse

shouldEnd = False
kb = keyboard.Controller()
mo = mouse.Controller()

def main():
    global shouldEnd
    # 键盘监听线程
    kbListener = keyboard.Listener(on_press=pressKeyboard)
    kbListener.daemon = 1

    # 刷卢恩线程
    getRune = threading.Thread(target=autoGetRune)
    getRune.daemon = 1
    kbListener.start()
    getRune.start()

    while True:
        if shouldEnd:
            return

def pressKeyboard(key):
    global shouldEnd
    print('Pressed {0}.'.format(key))
    if key == keyboard.Key.esc:
        shouldEnd = True
        return False

def autoGetRune():
    while True:
        # 初始循环等待时间（卢恩到账时间）
        time.sleep(5)
        kb.press('g')
        time.sleep(1)
        kb.release('g')
        kb.press('f')
        time.sleep(1)
        kb.release('f')
        kb.press('e')
        time.sleep(1)
        kb.release('e')
        # 给操作系统一个反应时间，以防止第二次的按键 e 不生效导致无法传送回赐福
        time.sleep(0.5)
        kb.press('e')
        time.sleep(1)
        kb.release('e')
        # 赐福传送所需要的时间
        time.sleep(5)
        kb.press('r')
        time.sleep(1)
        kb.release('r')
        kb.press('w')
        time.sleep(4.5)
        kb.release('w')
        kb.press('a')
        time.sleep(1)
        kb.release('a')
        kb.press('w')
        time.sleep(2)
        kb.release('w')
        kb.press(keyboard.Key.ctrl_l)
        time.sleep(1)
        kb.release(keyboard.Key.ctrl_l)
        
if __name__ == "__main__":
    main()