import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)



def pretty_print_json(data):
    print(json.dumps(data, indent = 4, ensure_ascii = False))



if __name__ == '__main__':
    if len (sys.argv) == 1:
        filepath = input('Enter file path > ')
    else:
        if len (sys.argv) > 2:
            print ("Error: too many parameters are transferred")
            sys.exit (1)

        filepath = sys.argv[1]
    
    pretty_print_json(load_data(filepath))
