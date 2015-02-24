# -*- coding: utf-8 -*-
from fabric.api import env
from fabric.utils import puts
from fabric.colors import *

def task_puts(msg = "", task = None):
    if task is None and "task_name" in env:
        task = env.task_name
    line = "[{0}] {1}".format(cyan(task), msg)
    puts(line)
