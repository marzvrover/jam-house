#!/usr/bin/env python
import settings
from os import getenv as env
import RPi.GPIO as GPIO
from relay import Relay
from time import sleep
import sys
from sys import argv as arguments
import warnings

class Jam:
  def __init__(self, arguments):
    GPIO.setmode(GPIO.BCM)

    self.letter_j = Relay(env('RELAY_PIN_1'))
    self.letter_a = Relay(env('RELAY_PIN_2'))
    self.letter_m = Relay(env('RELAY_PIN_3'))

    output = self.command(arguments)
    if output != None:
      print(output)

  def command(self, args):
    for arg in args:
      arg = arg.lower()

    if len(args) == 2:
      self.resolveLetter(args[1]).toggle()
    elif len(args) == 3:
      if (args[1] == 'open'):
        self.resolveLetter(args[2]).open()
      elif (args[1] == 'close'):
        self.resolveLetter(args[2]).close()
      elif (args[1] == 'toggle'):
        self.resolveLetter(args[2]).toggle()
      elif (args[1] == 'status'):
        return self.resolveLetter(args[2]).status()
      elif (args[1] == 'is-open'):
        return self.resolveLetter(args[2]).isOpen()
      elif (args[1] == 'is-close'):
        return self.resolveLetter(args[2]).isClose()
    return


  def resolveLetter(self, letter):
    if letter == 'a':
      return self.letter_a
    elif letter == 'j':
      return self.letter_j
    elif letter == 'm':
      return self.letter_m
    else:
      print "Letter does not exist"
      sys.exit(1)

warnings.filterwarnings("ignore")
Jam(arguments)
