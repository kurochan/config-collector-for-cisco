# -*- coding: utf-8 -*-
from fabric.api import env, run, sudo, task, execute, settings, hide
from fabric.tasks import Task
from fabric.colors import red, green
from fabric.state import output
from helper.print_helper import task_puts

env.parallel = True
env. pool_size = 5
env.skip_bad_hosts = True
env.abort_exception = Exception
output['running'] = False
output['output'] = False

import inspect
class BaseTask(Task):
    """
    base tesk
    """
    name = "task"
    def run(self, *args, **kwargs):
        try:
            env.task_name = task_name = self.__module__.split(".")[-1] + "." + self.name
            # task_puts(self.name + " start")
            task_puts("start")

            self.before_run_task(self, *args, **kwargs)
            self.run_task(self, *args, **kwargs)
            self.after_run_task(self, *args, **kwargs)
            env.task_name = task_name

            task_puts(green("OK"))
        except Exception as e:
            if "fail" not in env or not env.fail:
                env.fail = True
                task_puts(red("ERROR:") + " " + str(type(e)))
                task_puts(red("ERROR:") + " " + str(e))
            task_puts(red("NG"))
            raise

    def before_run_task(self, *args, **kwargs):
        pass

    def run_task(self, *args, **kwargs):
        pass

    def after_run_task(self, *args, **kwargs):
        pass
