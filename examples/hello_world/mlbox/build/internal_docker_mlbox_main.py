
# Lint as: python3
import sys
import os
import re

def mlbox_hello(iomap):
  name = iomap["name"]
  greeting = iomap["greeting"]
  return os.system("python3 internal_docker_mlbox_hello_main.py  {}  {} ".format(name, greeting))

def mlbox_goodbye(iomap):
  name = iomap["name"]
  greeting = iomap["greeting"]
  message = iomap["message"]
  return os.system("python3 internal_docker_mlbox_goodbye_main.py  {}  {}  {} ".format(name, greeting, message))



def parse_command_line():
  task = sys.argv[1]

  iomap = {}
  for arg in sys.argv[2:]:
    match = re.match('--([^=]+)=(.+)', arg)
    if not match:
      raise Exception('Invalid argument: {}'.format(arg))
    ioname = match.group(1)
    path = match.group(2)
    iomap[ioname] = path
  return task, iomap


def main():
  print('MLBox starting.')
  task, iomap = parse_command_line()

  if task == "hello":
    if not mlbox_hello(iomap):
      sys.exit(1)
  elif task == "goodbye":
    if not mlbox_goodbye(iomap):
      sys.exit(1)
  else:
    print("No known MLBox task: {}".format(task))
    sys.exit(1)



if __name__ == '__main__':
  main()
