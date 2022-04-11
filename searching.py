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
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]

def linear_search(sequence, searched_number):
    slovnik = {"positions": [], "count": 0}

    for index, value in enumerate(sequence):

        if value == searched_number:
            slovnik["positions"].append(index)
            slovnik["count"] += 1

    return slovnik


def pattern_search(sequence, pattern):
    positions = set()
    index = 0
    while index < len(sequence) - len(pattern):
        idx = 0
        for letter in sequence[index:index + len(pattern)]:
            if letter != pattern[idx]:
                break
            else:
                idx += 1
        if idx == len(pattern):                                 #nebo "else:" - dalsi podminky se provedou v pripade, ze cyklus probehl cely
            positions.add(index)
        index += 1
    return positions



def main():
    #sequential_data = read_data("sequential.json", "unordered_numbers")
    sequential_data = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    results = linear_search(sequential_data, 0)
    #print(results)
    search = pattern_search(sequential_data, "ATA")
    print(search)


if __name__ == '__main__':
    main()

#def pattern_search(sequence, pattern)
    #positions = set()
    #index = 0
    #while index < len(sequence) - len(pattern):
        #if sequenxe[index:index + len(pattern)] == pattern:
            #positions.add(index)
        #index += 1
    #return positions