import os
import json
import numpy as np

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

def pattern_search(sequence, pattern):
    positions = []
    for index in range(len(sequence)-len(pattern)+1):
        subsequence = sequence[index:(index+len(pattern))]
        same = True
        for letter_subsequence, letter_pattern in zip(subsequence, pattern):
            if letter_subsequence != letter_pattern:
                same = False
                break
        if same:
            positions.append(index)
    return positions








def main():
    pass


if __name__ == '__main__':
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    search_output_dict = linear_search(unordered_numbers, 5)
    print(unordered_numbers)
    print(search_output_dict)
    print(pattern_search('ACCCCTG', 'CCC'))

    main()