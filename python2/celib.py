#!/usr/bin/python2
import codecs

"""
This module contains functions for working with the chain encoding.
This encoding uses the unused 8th bit in ASCII to chain multiple bytes together (like a chain).
If the bit is 1, the other 7 bits are chained to the previous byte.
If the bit is 0, a new chain is created.
For more information, visit https://github.com/Deric-W/Chain-Encoding.
"""

__all__ = ["encode","decode","search","int2bytes","bytes2int","is_corrupted"]
__autor__ = "Deric W."
__version__ = 0.3

def decode(bytes_):
    output = []
    for byte in bytes_:
        if byte > 127:      # byte like 1xxxxxxx --> append
            byte = byte & 127   # remove leading 1
            if len(output) > 0:
                output[-1] = (output[-1] << 7)|byte
            else:
                raise ValueError("missing start byte")
        else:                     # new int (chr)
            if len(output) > 0:
                output[-1] = chr(output[-1])
            output.append(byte)
    output[-1] = chr(output[-1])
    return "".join(output), len(bytes_)

def encode(string):
    output = b""
    for char in string:
        char = ord(char)
        buffer = b""          # needed because reversed build order
        while char > 127:     # chain bytes with leading 1
            buffer = bytes([128|(char & 127)]) + buffer
            char = char >> 7
        buffer = bytes([char]) + buffer        # int fits in 1 byte and has leading 0 --> start byte 
        output += buffer
    return output, len(string)
    
def int2bytes(num_list):      # like encode, but with a list of integrers as input
    output = b""
    for num in num_list:
        buffer = b""
        while num > 127:
            buffer = bytes([128|(num & 127)]) + buffer
            num = num >> 7
        buffer = bytes([num]) + buffer
        output += buffer
    return output
    
def bytes2int(bytes_):       # like decode, but with a list of integrers as output
    output = []
    for byte in bytes_:
        if byte > 127:
            byte = byte & 127
            if len(output) > 0:
                output[-1] = (output[-1] << 7)|byte
            else:
                raise ValueError("missing start byte")
        else:
            output.append(byte)
    return output

def is_corrupted(bytes_):     # if start byte is missing
    return bytes_[0] > 127

def search(name):         # is only used for codecs.register
    return codecs.CodecInfo(encode, decode, name="chain")

codecs.register(search)

if __name__ == "__main__":         # print hex of encoded stdin
    from binascii import hexlify
    print hexlify(raw_input().encode("chain")).decode("utf8")
