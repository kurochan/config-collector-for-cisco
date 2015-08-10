# -*- coding: utf-8 -*-
import os
from fabric.api import *
from fabric.state import output
from fabric.colors import *

from base import BaseTask
from helper.print_helper import task_puts

class CollectConfig(BaseTask):
  """
  collect configuration
  """
  name = "collect"
  def run_task(self, *args, **kwargs):
    host_config = env.inventory.get_variables(env.host)
    config = self.get_config(host_config['ssh_host'], host_config['ssh_user'], host_config['ssh_pass'], host_config['exec_pass'])
    # print config

  def get_config(self, hostname, ssh_user, ssh_pass, exec_pass):
    script_name = "dump-config-cisco-ios.sh"
    local(os.path.dirname(os.path.abspath(__file__)) + "/../bin/{0} {1} {2} {3}".format(script_name, ssh_user, hostname, ssh_pass))

collect = CollectConfig()
