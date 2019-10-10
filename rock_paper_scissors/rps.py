#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  arr = []
  moves = ['rock', 'paper', 'scissors']
  if n <= 0:
    return 0
  if n >= 1:
    for i in range(0, len(moves) - 1):
      arr[i].append(moves[i])

    rock_paper_scissors(n-1)
  return arr



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')