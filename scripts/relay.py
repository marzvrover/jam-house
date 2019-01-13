import RPi.GPIO as GPIO

class Relay:
  def __init__(self, pin):
    self.pin = int(pin)
    GPIO.setup(self.pin, GPIO.OUT)

  def close(self):
    GPIO.output(self.pin, GPIO.LOW)
    return

  def open(self):
    GPIO.output(self.pin, GPIO.HIGH)
    return

  def status(self):
    return bool(GPIO.input(self.pin))

  def isClose(self):
    return not self.status()

  def isOpen(self):
    return self.status()

  def toggle(self):
    if self.isOpen():
      self.close()
    elif self.isClose():
      self.open()
    return

  def cleanup(self):
    GPIO.cleanup(self.pin)
    return
