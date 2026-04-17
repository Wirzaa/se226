def remove_duplicates(data_list):
    unique_list = list(set(data_list))
    return unique_list

def strip_whitespaces(string_list):
    for i in range(len(string_list)):
        string_list[i] = string_list[i].strip()
    return string_list