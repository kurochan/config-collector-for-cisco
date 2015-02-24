# -*- coding: utf-8 -*-
import os
from fabric.api import *
import ansible.inventory

from base import BaseTask
from helper.print_helper import task_puts

class RoleTask(BaseTask):
    """
    select role
    """
    name = "role"
    def run_task(self, *args, **kwargs):
        name = args[1]
        inventory = ansible.inventory.Inventory(os.path.dirname(os.path.abspath(__file__)) + "/../hosts")
        env.inventory = inventory
        env.hosts = inventory.groups_list()[name]
        task_puts("loading role " + name)

role = RoleTask()
