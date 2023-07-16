#!/usr/bin/env python

from api import runner as api_runner
from server import runner as server_runner
import threading
from logger import Logger
from env import App

if __name__ == '__main__':
    ctx = Logger(name=App.name, log_level=App.log_level)
    try:
        # make threads
        ctx.printable(function=__name__, message='Make Threads')
        thread_1 = threading.Thread(target=server_runner)
        thread_2 = threading.Thread(target=api_runner)
        
        # start threads
        ctx.printable(function=__name__, message='Start Threads')
        thread_1.start()
        thread_2.start()
        
        # join threads
        ctx.printable(function=__name__, message='Join Threads')
        thread_1.join()
        thread_2.join()
        
    except KeyboardInterrupt:
        pass
    except Exception as err:
        ctx.error(__name__, err)