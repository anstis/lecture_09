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

def binary_search(list_of_numbers, number):
    low = 0
    high = len(list_of_numbers) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list_of_numbers[mid] < number:
            low = mid + 1
        elif list_of_numbers[mid] > number:
            high = mid - 1
        else:
            return mid






def main():
    pass


if __name__ == '__main__':
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    search_output_dict = linear_search(unordered_numbers, 5)
    ordered_numbers = [-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120]
    print(binary_search(ordered_numbers, 2))
    print(unordered_numbers)
    print(search_output_dict)
    print(pattern_search('ACCCCTG', 'CCC'))

    main()