#!/usr/bin/python3
'''A module for working with lockboxes
'''


def canUnlockAll(boxes):
    '''Checks if the boxes in a list of list containing the keys(indeces) to
    other boxes can be unlocked give that the first box is unlocked
    '''
    n = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0].difference(set([0]))
    while len(locked_boxes) > 0:
        boxIdx=locked_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in unlocked_boxes:
            locked_boxes=locked_boxes.update(boxes[boxIdx])
            unlocked_boxes.add(boxIdx)
    return n == len(unlocked_boxes)
