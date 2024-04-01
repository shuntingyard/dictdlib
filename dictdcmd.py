import sys

from dictdlib import DictReader

if __name__ == "__main__":
    match len(sys.argv):
        case 2:
            reader = DictReader(sys.argv[1])
            for definition in reader.getdeflist():
                print(definition)
        case 3:
            reader = DictReader(sys.argv[1])
            for entry in reader.getdef(sys.argv[2]):
                print(entry.decode("utf-8"))
        case _:
            print("Usage: dictdcmd BASENAME [DEFINITION]")
