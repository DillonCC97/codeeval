#!/usr/bin/env python

import sys

def main():
  with open(sys.argv[1], 'r') as input_file:
    lines = [line.split() for line in input_file]
    input_file.close()

  for line in range(0, len(lines[0])):
    output_string = ''
    div1 = int(lines[line][0])
    div2 = int(lines[line][1])
    for num in range(1, int(lines[line][2]) + 1):
        if num % div1 == 0 and num % div2 == 0:
            output_string += 'FB '
        elif num % div1 == 0:
            output_string += 'F '
        elif num % div2 == 0:
            output_string += 'B '
        else:
            output_string += str(num) + ' '
    print(output_string)
main()
