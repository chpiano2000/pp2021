import sys
import os
import subprocess

while True:
    try:
        cmd = input('>')
        command = cmd.split(" ")
        subprocess.run(command)
    except KeyboardInterrupt:
        print('\nKeyboard Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    
    except Exception as E:
        print("Command not valid")