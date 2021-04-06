"""
author: weiwei
date: 202010406
"""

import copy

def find_all(a_string, pattern):
    return [i for i in range(len(a_string)) if a_string.startswith(pattern, i)]

if __name__ == '__main__':

    original_file = "revision.txt"
    output_file = "output.txt"
    keyword = "rev"

    file_object = open(original_file, 'r')
    file_data = file_object.read()
    rev_pairs = []
    rev_start_list = find_all(file_data, "\\"+keyword+"{")
    for rev_start in rev_start_list:
        rev_end = rev_start+5
        newstart_counter = 0
        for element in file_data[rev_start+5::]:
            if element == '{':
                newstart_counter += 1
            if element == '}' and newstart_counter == 0:
                print(rev_start, rev_end+1)
                print(file_data[rev_start:rev_end+1])
                rev_pairs.append((rev_start, rev_end))
                break
            elif element == '}':
                newstart_counter -= 1
            rev_end += 1
    new_file_data = copy.deepcopy(file_data)
    start = 0
    for revp in rev_pairs:
        print(revp)
        new_file_data = ''.join((new_file_data[:revp[0]], chr(177)*5, new_file_data[revp[0]+5:]))
        new_file_data = ''.join((new_file_data[:revp[1]], chr(177), new_file_data[revp[1]+1:]))
    new_file_data = new_file_data.replace(chr(177), '')
    new_file_object = open(output_file, "w")
    new_file_object.write(new_file_data)
    new_file_object.close()