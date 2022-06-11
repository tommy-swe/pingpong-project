## Author
## Date

## Main script for run code
from LED_control import RGBLEDcontroller
import time


COLOR = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]

def main():
    controller = RGBLEDcontroller()
    controller.setup()
    try:
        while True:
            for color in COLOR:
                controller.setColor(color)
                time.sleep(0.5)
    except KeyboardInterrupt:
        controller.stop()

if __name__ == '__main__':
    main()





