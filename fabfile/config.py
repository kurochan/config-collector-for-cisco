# -*- coding: utf-8 -*-
import os
import util
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
    hostname = host_config['ssh_host']

    if not util.tcping(hostname, 22, 1):
      task_puts("host {0} does not exist. skip...".format(hostname))
      return

    config = self.get_config(hostname, host_config['ssh_user'], host_config['ssh_pass'], host_config['exec_pass'])
    self.write_config(env.host, config)
    # print config

  def get_config(self, hostname, ssh_user, ssh_pass, exec_pass):
    script_name = "dump-config-cisco-ios.sh"
    config = local(os.path.dirname(os.path.abspath(__file__)) + "/../bin/{0} {1} {2} {3}".format(script_name, ssh_user, hostname, ssh_pass), capture = True)
    return config

  def write_config(self, hostname, config):
    output_dir = os.path.dirname(os.path.abspath(__file__)) + "/../tmp/config"
    local("mkdir -p {0}".format(output_dir))
    file = open("{0}/{1}.txt".format(output_dir, hostname), 'w')
    file.write(str(config))
    file.close()

collect = CollectConfig()
