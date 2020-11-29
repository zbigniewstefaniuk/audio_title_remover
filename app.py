import pyautogui as py
from time import sleep


"""
This program is for removing extra title form filename and properties in audio files.
1. You need to open folder containing files
2. After typing how many signs and song you want to proced you got 3 sec of delay 
"""


def deleting_letters(letters: int):
    for letter in range(letters):
        py.press('backspace')


def click():
    while True:
        try:
            letters_to_delete = int(input('How Many letter you want to delete?: '))
            song_to_proced = int(input('How Many songs you want to proced?: '))
            print('You got 3 second to click on the first song!')
        except ValueError:
            print('Sorry but you typed wrong value :( Try again...')

    sleep(3)

    for click in range(song_to_proced):
        py.press('f2')
        py.press('end')
        deleting_letters(letters_to_delete)
        py.press('enter')
        py.hotkey('alt', 'enter')
        sleep(.5)

        for tab in range(5):
            py.press('tab')

        py.press("right")
        py.press("right")
        py.press('tab')

        for uparrow in range(9):
            py.press('up')

        py.hotkey('ctrl', 'c')
        sleep(.2)
        py.hotkey('ctrl', 'v')
        deleting_letters(letters_to_delete)
        py.press('enter')
        py.press('enter')
        sleep(.2)
        py.press('down')


if __name__ == '__main__':
    auto_clicker = click()
