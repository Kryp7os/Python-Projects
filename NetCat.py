import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
  cmd = cmd.strip()
  if not cmd:
    return
output = 
subprocess.check_output(shlex.split(cmd),
                        
stderr=subprocess.STDOUT)
  return output.decode()

if __name__=='__main__':
  parser =
argparse.ArgumentParser(description='My Net Tool',

formatter_class=argparse.RawDescriptionHelpFormatter,

epilog=textwrap.dedent('''Example: ''')
                        
  parser.add_argument('-c', '--command', action='store_true', help='command shell')
  parser.add_argument('-e', '--execute', help='execute specified command')
  parser.add_argument('-l', '--listen' action='store_true', help='listen')
  parser.add_argument('-p', '--port' type=int, default=5555, help='specified port')                          
    if args.listen:
        buffer= ''
    else:
        buffer = sys.stdin.read()
                        
    nc = NetCat(args, buffer.encode())
          nc.run()                        
