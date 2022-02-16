print("----- EXERCISE01 -----")

import argparse

if __name__ == "__main__":
    print("__name__ = __main__")
    parser = argparse.ArgumentParser(description="Exercise 01")
    parser.add_argument("name",help="Name of the exercise")
    parser.add_argument("-o","--optional",default="default",help="This is an optional argument with the name Optional with a default being default")
    args = parser.parse_args()

    name = args.name
    optional = args.optional
    print("value in name arg: ",name)
    print("value in optional arg: ",optional)

print("----- END -----")