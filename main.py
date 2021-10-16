import usb.core
import usb.util

from src import keyboard

k = keyboard.Keyboard()

serial = ""
vendorID = 0x46d
productID = 0xc32b

dev = usb.core.find(idVendor=vendorID, idProduct=productID)

print(dev)

dev.write()