# -*- coding: utf-8 -*-
import os
from fabric.api import *
from fabric.state import output
from fabric.colors import *

from base import BaseTask
from helper.print_helper import task_puts

from datetime import datetime

class PushGit(BaseTask):
  """
  git push
  """
  name = "push"
  def run_task(self, *args, **kwargs):
    output_dir = os.path.dirname(os.path.abspath(__file__)) + "/../tmp/config"

    if self.git_repo_exists(output_dir):
      with lcd(output_dir):
        with settings(warn_only=True):
          task_puts("commit config")
          local("git add -A")
          local("git commit -m \"{0}\"".format(datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
          task_puts("push config")
          local("git push origin master")
    else:
      task_puts("Nothing to push")

  def git_repo_exists(self, base_path):
    return os.path.exists("{0}/.git".format(base_path))

push = PushGit()
