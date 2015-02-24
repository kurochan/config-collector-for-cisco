# -*- coding: utf-8 -*-
from fabric.api import *
from base import BaseTask

class PrintEnvTask(BaseTask):
    """
    print Fabric environment
    """
    name = "print_env"
    def run_task(self, *args, **kwargs):
        print env

print_env = PrintEnvTask()
