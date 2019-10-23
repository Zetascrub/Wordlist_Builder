import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f1', metavar="", help='File1')
parser.add_argument('-f2', metavar="", help='File2')
parser.add_argument('-F', metavar="", help='Folder')
parser.add_argument('-O', metavar="", help='Output')
args = parser.parse_args()

list1 = []

if __name__ == "__main__":

    # Reading Files
    if args.F:
        files = os.listdir(str(args.F))
        for file in files:
            if file.endswith(".txt"):
                try:
                    with open(file, 'r') as f:
                        lines = f.read().splitlines()
                        for line in lines:
                            list1.append(line)
                except Exception as e:
                    print(e.args)
    elif args.f1:
        with open(args.F1, 'r') as file:
            lines = file.read().splitlines()
            for line in lines:
                list1.append(line)
        if args.F2:
            with open(args.F2, 'r') as file:
                lines = file.read().splitlines()
                for line in lines:
                    list1.append(line)
    else:
        parser.print_help()

    if args.F or args.f1:
        # Unique Files
        unique = set(list1)
        unique_sorted = sorted(unique)

        x = len(list1)
        y = len(unique)
        print("Count Before: {}".format(x))
        print("Count Before: {}".format(y))
        print("Reduced by: {}".format(x - y))

        # Save file
        if args.O:
            with open(args.O, 'w') as file:
                for word in unique_sorted:
                    file.write("{}\n".format(word))
        else:
            with open("WordList.txt", 'w') as file:
                for word in unique_sorted:
                    file.write("{}\n".format(word))
