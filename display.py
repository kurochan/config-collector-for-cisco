'''

@author: Takashi.K

'''
# -*- coding: utf-8 -*-
import sys
import commands
import os
import re
import time

showInitial = 'ls -1t | head -1 | xargs cat'
#showSecond = 'ls -1t | head -2 | tail -1 | xargs cat'
showHead = 'ls -1t | head -1'
showSecond = 'ls -1t | head -2 | tail -1'

show = commands.getoutput(showInitial)
print show
def display(cmd1,cmd2):
    while True:
        show1 = commands.getoutput(cmd1)
        show2 = commands.getoutput(cmd2)
        showDiff = "diff " + show1 + " "+ show2
        resultDiff = commands.getoutput(showDiff)
        print resultDiff
        time.sleep(10)

display(showHead,showSecond)