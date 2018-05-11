"""
PNG     89 50 4E 47 0D 0A 1A 0A
JPG     FF D8 FF E0 ?? ?? 4A 46 49 46 00 01
GIF     47 49 46 38 37 61
        47 49 46 38 39 61
BMP     42 4D
"""
# Thai Thien
# 17c 12 031
from collections import defaultdict
import sys

class MeowDetector:
    def __init__(self):
        self.signature_dict = defaultdict()
        self.signature_dict["8950"] = "PNG"
        self.signature_dict["ffd8"] = "JPG"
        self.signature_dict["4749"] = "GIF"
        self.signature_dict["424d"] = "BMP"



    def read_file_to_hex(self, path):
        """
        Read file to hex
        :param path: path to file
        :return: list of hex
        """
        with open(path, 'rb') as fp:
            hex_list = ["{:02x}".format(c) for c in fp.read()]
            return hex_list

    def detect(self, path):
        """
        detect file type
        :param path:
        :return:
        """

        hex = self.read_file_to_hex(path)
        sig = hex[0]+hex[1]
        filetype = self.signature_dict[sig]
        return filetype

def simple_test():
    meow = MeowDetector()
    print("test")
    print(meow.detect("Britishblue.jpg"))
    print(meow.detect("11-2-cat-png.png"))
    print(meow.detect("catnail.gif"))
    print(meow.detect("cat.bmp"))

if __name__ == "__main__":
    if (len(sys.argv)>1):
        try:
            filepath = sys.argv[1]
            meow = MeowDetector()
            print(meow.detect(filepath))
        except:
            print("please try again")
    else:
        simple_test()
