#!/usr/bin/env python

import argparse

def main():
  parser = argparse.ArgumentParser() # create an ArgumentParser to parse the command-line arguments
  parser.add_argument("filename") # the only argument will be a file name
  args = parser.parse_args()

  with open(args.filename, "r") as file: # open the input file to begin reading it as text
    for line in file: # for each line in the input file
      args = line.split()
      output_string = ''
      div1 = int(args[0])
      div2 = int(args[1])
      digits = int(args[2]) + 1

      for num in range(1, digits):
        found = False

        if num % div1 == 0:
          output_string += 'F'
          found = True

        if num % div2 == 0:
          output_string += 'B'
          found = True

        if found == False:
          output_string += str(num)

        output_string += ' '

      output_string.rstrip(" ")
      print(output_string)

if __name__ == '__main__':
  main()
