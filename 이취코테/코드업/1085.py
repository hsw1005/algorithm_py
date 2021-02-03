h, b, c, s = map(int, input().split())

bit = h * b * c * s

byte = bit // 8
kb = byte // 1024
mb = byte // 1024
print(bit)
print(byte)
print(kb)
print(mb)

print(round(mb, 2), "MB")

"""
44100 16 2 10
"""