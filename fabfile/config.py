# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.state import output
from fabric.colors import *

from base import BaseTask
from helper.print_helper import task_puts

import pexpect

class CollectConfig(BaseTask):
    """
    collect configuration
    """
    name = "collect"
    def run_task(self, *args, **kwargs):
      host_config = env.inventory.get_variables(env.host)
      config = self.get_config(env.host, host_config['ssh_user'], host_config['ssh_pass'], host_config['exec_pass'])
      # config = self.get_config(host_config['ssh_host'], host_config['ssh_user'], host_config['ssh_pass'], host_config['exec_pass'])
      # print '\r\n'.join(config)

    def get_config(self, hostname, ssh_user, ssh_pass, exec_pass):
      child = pexpect.spawn("ssh {0}@{1}".format(ssh_user,hostname))
      child.expect('Password:*')
      child.sendline(ssh_pass)

      child.expect('>$')
      child.sendline('enable')
      child.expect('Password:*')
      child.sendline(exec_pass)

      child.expect('#$')
      child.sendline('terminal length 0')
      child.expect('#$')

      child.sendline('show running-config')
      child.expect('bytes')
      child.before
      child.expect('\r\nend\r\n')
      child.close()
      return [line for line in child.before.splitlines() if len(line) > 0]

collect = CollectConfig()
