import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode='r') as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]


def linear_search(unordered_numbers, to_find_number):
    positions = []
    count = 0
    for position, number in enumerate(unordered_numbers):
        if number == to_find_number:
            positions.append(position)
            count += 1
    output = dict()
    output['positions'] = positions
    output['count'] = count
    return output



def main():
    pass


if __name__ == '__main__':
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    search_output_dict = linear_search(unordered_numbers, 5)
    print(unordered_numbers)
    print(search_output_dict)

    main()