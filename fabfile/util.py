# -*- coding: utf-8 -*-
from fabric.api import *
from base import BaseTask
import socket

def tcping(server, port, timeout = 10):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((server, port))
    s.close()
    return True
  except socket.error:
    return False

class PrintEnvTask(BaseTask):
    """
    print Fabric environment
    """
    name = "print_env"
    def run_task(self, *args, **kwargs):
        print env

print_env = PrintEnvTask()
