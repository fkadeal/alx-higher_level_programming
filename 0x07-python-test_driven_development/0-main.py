#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

try:
    print(add_integer(5, int("x")))
except Exception as valueErr:
    print(valueErr)
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer( ' ', -2))
except Exception as u:
    print(u)
try:
    print(add_integer(4j,5) )
except Exception as f:
    print(f)
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)