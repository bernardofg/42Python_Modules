
import sys

data = {}

for arg in sys.argv[1:]:
    colon_pos = arg.find(":")
    key = arg[:colon_pos]
    value = int(arg[colon_pos+1:])
    data[key] = value

print(key)
print(value)
