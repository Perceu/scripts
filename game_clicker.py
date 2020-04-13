import argparse
import pyautogui as gui
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument('--clicks', type=int)
parser.add_argument('--capture-position', action='store_true')
parser.add_argument('--position')

args = parser.parse_args()

if args.capture_position:
    while True:
        print(gui.position())
elif args.position:
    positions = args.position.split(",")
    print(positions)
    for i in range(args.clicks):
        gui.click(x=int(positions[0]), y=int(positions[1]))
else:
    for i in range(args.clicks):
        gui.click(x=3222, y=413)

