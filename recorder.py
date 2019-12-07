#!/usr/bin/python3

from pynput import keyboard, mouse
import json
import pickle
import time

'''Any operation should be indicated as a tuple in [(),(),...]'''
'''Turn all Operation Objects to string and save in files, '''
class Recorder:
    '''class Recorder, '''

    pass


def fix(a):
    def f(*b):
        a=b
    return f

class Operation:
    ''' nnnn  '''
    key_op = keyboard.Controller()
    mouse_op = mouse.Controller()
    op = {  
            'pressm': mouse_op.press,
            'releasem': mouse_op.release,
            'click': mouse_op.click,
            'scroll': mouse_op.scroll,
            'move': mouse_op.move,
            'position': mouse_op.position,
            'press': key_op.press,
            'release': key_op.release,
            }
    keys = {}
    for i,j in keyboard.Key.__members__.items():
        keys[i] = j
    button = {}
    for i,j in mouse.Button.__members__.items():
        button[i] = j

    out = []

    def record(self):
#    def __init__(self):
        '''return op object: 2 elements tuple: (action, arguments)'''
        out=[('position', *self.mouse_op.position)]
        def on_press(key):
            try:
                out.append(('press', key.name))
            except AttributeError:
                out.append(('press', key.char))
        def on_release(key):
            if key == keyboard.Key.esc:
                mouse_listener.stop()
                keyboard_listener.stop()
            try:
                out.append(('release', key.name))
            except AttributeError:
                out.append(('release', key.char))
        def on_move(x,y): 
            out.append(('move', x,y))
        def on_click(x,y,button,pressed):
            out.append(('click', button.name))
        def on_scroll(x,y,dx,dy):
            out.append(('scroll',dx,dy))

        keyboard_listener = keyboard.Listener(on_press=on_press,
                on_release=on_release)
        mouse_listener = mouse.Listener(on_move=on_move, 
                on_click=on_click, on_scroll=on_scroll)

        keyboard_listener.start()
        mouse_listener.start()

        self.out = out

    def record_to_json(self, filename='test.json'):
        '''NOT ready for now'''
        with open(filename, 'w') as f:
            json.dump(self.out, f)

    def record_to_pickle(self, filename='test.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.out, f)


    def repeat(self, *args):
        '''execute operations saved in op'''
        
        # if args[0] is "position":
        # I REALY CANNT TELL, WHY 'is' NOT WORK HERE!!!!!
        print('args:', args)
        print('args0: ', args[0])
        print('args1: ', args[1])
        print('*args1: ', *(args[1:]))
        print('if: ', args[0] in self.op.keys())
        if args[0] in 'position':
            self.mouse_op.position = args[1:]
        else:
            try:
                self.op[args[0]](*(args[1:]))
            except (KeyError, AttributeError, ValueError):
                try:
                    self.op[args[0]](self.button[args[1]])
                except KeyError:
                    self.op[args[0]](self.keys[args[1]])

    def repeat_from_pickle(self, filename='test.pkl', l=1):
        with open(filename, 'rb') as f:
            ops = pickle.load(f)
        for item in ops:
            self.repeat(*item)
            time.sleep(l)


