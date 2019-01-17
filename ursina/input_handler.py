import sys
from collections import defaultdict


control = False
left_control = False
right_control = False

shift = False
left_shift = False
right_shift = False

alt = False
left_alt = False
right_alt = False

held_keys = defaultdict(lambda: 0)
rebinds = dict()


def bind(alternative_key, original_key):
    rebinds[original_key] = alternative_key

def unbind(key):
    if key in rebinds:
        del rebinds[key]
    else:
        rebinds[key] = 'none'

def rebind(from_key, to_key):
    unbind(to_key)
    bind(to_key, from_key)


def input(key):
    if key == 'arrow up':
        held_keys[key] = 1
        return
    elif key == 'arrow up up':
        held_keys['arrow up'] = 0
        return

    if key.endswith('up'):
        held_keys[key[:-3]] = 0
    else:
        held_keys[key] = 1
