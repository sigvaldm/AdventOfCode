import sys
import re
from copy import copy

tunnels = dict()
rates = dict()

with open(sys.argv[1]) as file:
    for line in file:
        valves = re.findall("[A-Z]{2}", line)
        rate = int(re.findall("\d+", line)[0])
        tunnels[valves[0]] = valves[1:]
        rates[valves[0]] = rate

current = 'AA'

def release(current, rates, min_left):
    open_current = (min_left-1)*rates[current] + release(current

def open_valve(current, rates, min_left):
    min_left -= 1
    result = min_left*rates[current]
    rates = copy(rates)
    rates[current] = 0
    return result + release(current, rates, min_left)

def move(current, next, rates, min_left):
    min

