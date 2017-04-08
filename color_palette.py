from tkinter import Button, mainloop
from tkinter.colorchooser import askcolor


# choose color from color palette
def get_color():
    color = askcolor()
    print('RGB code:', color[0], '\nHEX code:', color[1])
    # Take HEX code without #, this code works in kivy
    set_color = color[1][1:]
    return set_color


Button(text='Select Color', command=get_color).pack()
mainloop()
