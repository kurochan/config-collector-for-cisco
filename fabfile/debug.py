# -*- coding: utf-8 -*-
from fabric.state import output
from fabric.colors import *

from base import BaseTask
from helper.print_helper import task_puts

class DebugTask(BaseTask):
    """
    enable debug output
    """
    name = "debug"
    def run_task(self, *args, **kwargs):
        output['running'] = True
        output['output'] = True
        task_puts(green("enable debug output"))

debug = DebugTask()
