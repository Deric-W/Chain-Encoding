#This Module can write and read Files encoded in chain encoding.
#For help, type libce.help()

if __name__ == "__main__":
    print("This is a Module, import it before using")

def read(path):
    output = []
    buffer = 0                                  #buffers bytes for numbers > 127
    file = open(path,"rb")
    byte = file.read(1)
    while byte:
        number = int.from_bytes(byte,"big")
        if number <= 127:                       #first byte = 0
            buffer = (buffer << 7) | number     #merge
            output.append(buffer)
            buffer = 0
        else:                                   #first byte = 1
            number = 0b01111111 & number        #first byte --> 0
            buffer = (buffer << 7) | number     #merge
        byte = file.read(1)                     #next byte
    file.close()
    return output

def write(path,List):

    for number in List: #raises Error if not int
        number + 1

    file = open(path,"wb")
    for number in List:
        length = number.bit_length()
        byte_buffer = []
        byte_buffer.append(bytes([0b00000000 | (0b01111111 & number)])) #last byte
        while length > 0:
            number = number >> 7                                        #del written bits
            byte_buffer.append(bytes([0b10000000 | (0b01111111 & number)])) #next byte
            length = length - 7
        byte_buffer.reverse()                                           #because last byte is appended first,etc.
        if byte_buffer[0] == bytes([0b10000000]):
            byte_buffer = byte_buffer[1:]                                   #remove useless 10000000 byte from start
        for byte in byte_buffer:
            file.write(byte)
    file.close()

def help():
    print("This module can do 2 things:\n\tRead a file encoded in chain encoding and return a list with the numbers encoded in the file --> .read(path)\n\tWrite a list of numbers to a file in chain encoding --> .write(path,list)")
