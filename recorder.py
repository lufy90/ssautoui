#!/usr/bin/python3

from pynput import keyboard, mouse
import json



'''Any operation should be indicated as a tuple in [(),(),...]'''
class Recorder:
    '''class Recorder, '''

    pass


class Operation:
    ''' nnnn  '''
    def record(self):
        '''return op object: 2 elements tuple: (action, arguments)'''
        out=[]
        key_op = keyboard.Controller()
        mouse_op = mouse.Controller()
        def on_press(key):
            out.append((key_op.press, key))
        def on_release(key):
            if key == keyboard.Key.esc:
                mouse_listener.stop()
                keyboard_listener.stop()
            out.append((key_op.release, key))
        def on_move(x,y): 
            out.append((mouse_op.move, (x,y)))
        def on_click(x,y,button,pressed):
            out.append((mouse_op.click, button))
        def on_scroll(x,y,dx,dy):
            out.append((mouse_op.scroll,(dx,dy)))

        keyboard_listener = keyboard.Listener(on_press=on_press,
                on_release=on_release)
        mouse_listener = mouse.Listener(on_move=on_move, 
                on_click=on_click, on_scroll=on_scroll)

        keyboard_listener.start()
        mouse_listener.start()

        return out

    def record_to_json(self, filename='test.json'):
        with open(filename, 'w') as f:
            json.dump(self.record(), f)


    def repeat(self, op):
        '''execute operations saved in op'''
        pass

