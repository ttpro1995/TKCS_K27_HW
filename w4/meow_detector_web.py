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
import urllib.request

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

    def detect_from_url(self, url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
            hex_list = ["{:02x}".format(c) for c in html]
            sig = hex_list[0]+hex_list[1]
            filetype = self.signature_dict[sig]
            return filetype

def simple_test():
    meow = MeowDetector()
    print("test")
    print(meow.detect_from_url("https://znews-photo-td.zadn.vn/w660/Uploaded/znguhv/2017_10_11/zing_con_meo_hong_kong.jpg"))

if __name__ == "__main__":
    if (len(sys.argv)>1):
        try:
            url = sys.argv[1]
            meow = MeowDetector()
            print(meow.detect_from_url(url))
        except:
            print("please try again")
    else:
        simple_test()
