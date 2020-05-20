import sys

print("Recived input:")

if sys.stdin != None:
    for line in sys.stdin:
        print(line)
else:
    print("None.")



