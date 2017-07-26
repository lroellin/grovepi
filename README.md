# grovepi

## How the display works

You have a display of 128x64 (columns x rows) pixels. For each pixel, you can turn it on (`0b1`) or off (`0b0`).

I recommend using a font with characters like this:

```python
char = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
```

With that, you have 16 columns and 8 rows. This means, these characters are 8x8 pixels.

## How these fonts work (in hexadecimal)

On the individual character level, you're operating in an 8x8 pixel grid. Each character is comprised of 8 bytes.

Let's take one of those bytes, e.g. `0xF0`. Each byte here represents a *column*.

* The *upper* part in the byte, `F` in this example, specifies the physically *lower* part.
* The *lower* part in the byte, `0` in this example, specifies the physically *upper* part.

Let's focus on only half that byte, half a byte is called a *nibble*. One hex character is a nibble.

Here's a little table for hex to decimal to individual bits:

| Hex (0x) | Dec  | Bin (0b) |
| -------- | ---- | -------: |
| 0        | 0    |        0 |
| 1        | 1    |        1 |
| 2        | 2    |       10 |
| 3        | 3    |       11 |
| 4        | 4    |      100 |
| 5        | 5    |      101 |
| 6        | 6    |      110 |
| 7        | 7    |      111 |
| 8        | 8    |     1000 |
| 9        | 9    |     1001 |
| A        | 10   |     1010 |
| B        | 11   |     1011 |
| C        | 12   |     1100 |
| D        | 13   |     1101 |
| E        | 14   |     1110 |
| F        | 15   |     1111 |

And that, is how the pixels are turned on. 

* The byte `0xFF` is a complete line, from top to bottom
* The byte `0x0F`  is half a line, from top to the middle
* The byte `0x02` is a little dot, on the second row
* The byte `0x03` are two little dots on the first and the second row

In a nibble, we have four bits. We also have half a column, which is 4 pixels. Each pixel is either on or off, depending on how its bit is set.

## Designing pixel stuff: going down to the bits

If you wanna design your own character, start with a 8x8 pixel grid. Then, draw it.

When you're done, you'll have 8 columns. Now for *each column*, you have to figure out which pixels are lit (`1`) and which are off (`0`)

Start with this template: `0b00000000`. That is 8 bits.

Start from the top of your column and go from *right-to-left* in your bits. When a pixel should be on, change that bit to `1`.

When you're done, you have one column, e.g. `0b00000011`. That is a column with two lit pixels at the top and nothing else. 

If you want, you can convert these bits to a hex number for easier reading.