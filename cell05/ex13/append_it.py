import sys

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        word = sys.argv[i]

        if not word.endswith("ism"):
            print(word + "ism")