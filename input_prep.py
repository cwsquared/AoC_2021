def file_to_int_list(file_name):
    data = []
    f = open(file_name,'rt')
    input_file = f.readlines()
    for line in input_file:
        data.append(int(line))
    f.close()
    return data


def file_to_str_list(file_name):
    data = []
    f = open(file_name,'rt')
    input_file = f.readlines()
    for line in input_file:
        data.append(line.strip())
    f.close()
    return data


def file_to_tuple_list(file_name):
    data = []
    f = open(file_name,'rt')
    input_file = f.readlines()
    for line in input_file:
        tuple = line.strip().split()
        data.append(tuple)
    f.close()
    return data