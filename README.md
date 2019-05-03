# Chain-encoding
Chain encoding is a simple, (used with numbers less than 128) ASCII-compatible encoding that uses the unused 8th bit of an ASCII byte to concatenate multiple bytes (like a chain).
As a result, an infinite number of letter variants can be stored.
(Warning: this encoding was conceived just for fun, mistakes can happen with high probability!)

An example:

Number of letter = 1000 = 1111101000 as binary

1.: The binary number is divided into 7-bit parts beginning from the end (the last one is padded with zeros)
    **0000**111 + 1101000
    
2.: From left to right, all 7 bit parts (except the last one) get a 1 bit in front, which means that the next byte belongs to the
    same number.
    Instead, the last part gets a 0 bit in front, which means that the next byte does not belong to the same number anymore.
    If only one part was created at step one, the part gets a 0 bit up front.
    **1**0000111 + **0**1101000
    
3.: Finally, the resulting bytes are written together in a file (or you do something else with them).
    1000011101101000
    
4.: This procedure is repeated with each letter, which can be written by the 0 bit at the beginning of the last byte without a
    separator next to each other.
    
To read, you just go the other way around and hang all the bytes to the next byte until there is a 0 bit at the beginning, but you
always have to remove the first bit.
