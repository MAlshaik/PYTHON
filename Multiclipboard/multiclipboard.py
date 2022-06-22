import sys 
import clipboard
import json

def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)



if len(sys.argv) == 2:
    command = sys.argv[1]

    #perhaps use switch instead 
    if command == 'save':
        print('save')
    elif command == 'load':
        print(load)
    elif command == 'list':
        print('list')
    else:
        print('Unknown command')
else:
    print("Please pass exactly one command.")