import usb.core
import usb.util


class Keyboard (object):
    def __init__(self):
        vendorID = 0x46d
        productID = 0xc32b
        self.__dev = usb.core.find(idVendor=vendorID, idProduct=productID)