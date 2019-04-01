from subprocess import Popen, CREATE_NEW_CONSOLE
import time
from pathlib import Path
from sys import executable

__author__ = 'Fleece Johnson a.k.a Booty Warrior'

dir = Path('D:').exists()
dir = False


while True:
    if Path('D:').exists():
        dir = True
        def bup_start():
            Popen([executable, 'actual_bup.py'], creationflags=CREATE_NEW_CONSOLE)
        bup_start()
        time.sleep(2)
    if dir is True:
        quit()
    else:
        time.sleep(2)
