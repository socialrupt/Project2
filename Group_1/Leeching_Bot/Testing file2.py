import time
from multiprocessing import Pool

def Sum_Square(number):
  s = 0
  for i in range(number):
    s += i * i
  return s
if __name__ == "__main__":
  numbers = range(5)
  p = Pool()
  result = p.map(Sum_Square, numbers)
  # Takes functions and an iterable and gonna map it to the proccessers to our cpu
  p.close
  p.join()