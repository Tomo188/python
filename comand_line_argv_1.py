import sys
if len(sys.argv) < 2:
    sys.exit("enter argument")
elif len(sys.argv) > 2:
    sys.exit("to many arguments")

print("my name is", sys.argv[1])

print(sys.argv)
for line in sys.stdin:
    print(len("liverpool"))
    print(len(line))
    print("liverpool" == line.rstrip())
    for i in line:
        print(i)
    if line.rstrip() == "liverpool   ".rstrip():
        break
print("exit")
