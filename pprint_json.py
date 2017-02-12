import json


def load_data(filepath):
    myfile = open(filepath, mode = 'r', encoding ='cp1251')
    return json.load(myfile)


def pretty_print_json(data):
    print(json.dumps(data, indent = 3, sort_keys=True))   

if __name__ == '__main__':
    pretty_print_json(load_data(input("filepath = ")))