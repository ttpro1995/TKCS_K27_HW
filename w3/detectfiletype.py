
outputfile = open("output.txt", "w")

with open('Britishblue.jpg', 'rb') as fp:
    hex_list = ["{:02x}".format(c) for c in fp.read()]
    outputfile.write(str(hex_list))
    outputfile.close()