# Chain-encoding
Chain encoding is a simple, (used with numbers less than 128) ASCII-compatible Unicode based encoding that uses the unused 8th bit of an ASCII byte to concatenate multiple bytes (like a chain).
As a result, an infinite number of letters can be stored.

## Syntax
If the bit is 1, the other 7 bits are chained to the previous byte.
If the bit is 0, a new chain is created.

## Examples
### E
**0**1000101 --> new Chain 1000101 --> 1000101 --> 69 --> `E`

### Ä
**0**0000001 **1**1000100 --> new Chain 0000001 + 1000100 --> 00000011000100 --> 196 --> `Ä`

### 漢
**0**0000001 **1**1011110 **1**0100010 --> new Chain 0000001 + 1011110 + 0100010 --> 000000110111100100010 --> 28450 --> `漢`

### Invalid

**1**0100110 **1**0010000 --> missing start of Chain
