from GameEngine import Engine
from GameEngine import Canvas

def start():
    print("starting...")
    pass

def draw():
    print("looping...")
    pass

def stop():
    print("stopping...")
    pass

def main() -> None:
    engine = Engine( start, draw, stop, frameRate=25)
    canvas = Canvas(90, 40)
    engine.startEngine(canvas)
    pass

if __name__ == "__main__":
    main()