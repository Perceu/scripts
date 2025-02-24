import argparse
import pyautogui as gui
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument(
    "--clicks", type=int, help="Envia o numero de clicks que deseja fazer"
)
parser.add_argument(
    "--capture-position",
    action="store_true",
    help="use para capturar a posição do mouse",
)
parser.add_argument("--position", help="Posição que deseja clicar")

args = parser.parse_args()

default_position = dict(x=10, y=10)

if args.capture_position:
    while True:
        sleep(1)
        position = gui.position()
        print(position)

elif args.position:
    positions = args.position.split(",")
    print(positions)

    for i in range(args.clicks):
        gui.click(x=int(positions[0]), y=int(positions[1]))

elif args.clicks:
    for i in range(args.clicks):
        gui.click(**default_position)

else:
    print("peca ajuda para os parametros -h")
