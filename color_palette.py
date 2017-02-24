from tkinter import Button, mainloop
from tkinter.colorchooser import askcolor


# choose color from color palette
def get_color():
    color = askcolor()
    print('RGB code:',color[0],'\nHEX code:',color[1])

    # save color code in txt file
    try:
        with open('colordata.txt', mode='a', encoding='utf-8') as color_file:

            # from color code choose hex color, saved in text file in new line
            color_file.write(str(color[1]))
            color_file.write('\n')
            color_file.close()
            if color_file.closed == True:
                print('color code saved in text file')
    except:
        print('Error with text file')
        pass


Button(text='Select Color', command=get_color).pack()
mainloop()
