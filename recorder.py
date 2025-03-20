#!/usr/bin/python3
# filename: recoder.py
# Author: lufei
# Date: 20191209 21:16:52


from pynput import keyboard, mouse
import pickle, json
import time
import sys

class MouseController(mouse.Controller):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def put(self, *args):
        self.position = args

class Recorder():
    '''recorde user operations'''
    mc = MouseController()
    kc = keyboard.Controller()
    button = {}
    key = {}
    mc_map = {
            'position': mc.put,
            'press': mc.press,
            'release': mc.release,
            'scroll': mc.scroll,
            }
    kc_map = {
            'kpress': kc.press,
            'krelease': kc.release,
            }
    for name,value in mouse.Button.__members__.items():
        button[name] = value

    for name,value in keyboard.Key.__members__.items():
        key[name] = value

    def __init__(self):
        self.out = []

    def record(self):
        out = []
        def on_click(x,y,button,pressed):
            if pressed:
                out.append(('position', x, y))
                out.append(('press', button.name))
            else:
                out.append(('position', x, y))
                out.append(('release', button.name))
        def on_move(x,y):
            #out.append(('position',x,y))
            pass
        def on_scroll(x,y,dx,dy):
            out.append(('position',x,y))
            out.append(('scroll',dx,dy))
        def on_kpress(key):
            try:
                out.append(('kpress', key.name))
            except AttributeError:
                out.append(('kpress', key.char))
        def on_krelease(key):
            try:
                out.append(('krelease', key.name))
            except AttributeError:
                out.append(('krelease', key.char))

            if key is keyboard.Key.esc:
                ml.stop()
                kl.stop()

        kl = keyboard.Listener(on_press=on_kpress, 
                on_release=on_krelease)
        ml = mouse.Listener(on_click=on_click,
                on_move=on_move,
                on_scroll=on_scroll)
        kl.start()
        ml.start()
        while True:
            if kl.running and ml.running:
                time.sleep(1)
                continue
            else:
                break
        self.out = out

    def record_to_pickle(self, filename='test.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.out, f)

    def repeat(self, *args):
        '''e.g: args: press, x, y'''

        if args[0] in self.kc_map.keys():
            caller = self.kc_map[args[0]]
            try:
                caller(*args[1:])
            except Exception as e:
                caller(self.key[args[1]])
        elif args[0] in self.mc_map.keys():
            caller = self.mc_map[args[0]]
            try:
                caller(*args[1:])
            except Exception as e:
                caller(self.button[args[1]])
        else:
            print('Unkonwn operation: ', args[0])
            sys.exit(1)

    def repeat_from_pickle(self, filename='test.pkl', interval=0.5):
        with open(filename, 'rb') as f:
            ops = pickle.load(f)

        for item in ops:
            self.repeat(*item)
            time.sleep(interval)
        
if __name__ == '__main__':
    print('starting to record. ESC to exit')
    recorder = Recorder()
    if sys.argv[1] in "record":
        recorder.record()
        recorder.record_to_pickle()
    elif sys.argv[1] in "repeat":
        recorder.repeat_from_pickle()

