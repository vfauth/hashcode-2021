ex = {
    'IT0': [('IDR0', 1), ('IDR1', 1), ('IDR2', 1), ('IDR3', 1), ('IDR4', 1)],
    'IT1': [('IDR0', 1), ('IDR1', 1), ('IDR2', 1), ('IDR3', 1), ('IDR4', 1)],
    'IT2': [('IDR0', 1), ('IDR1', 1), ('IDR2', 1), ('IDR3', 1), ('IDR4', 1)]
}


def output(dict_data):
    f = open('output.txt', 'w+')
    nb_keys = len(dict_data.keys())
    out = str(nb_keys) + '\n'
    for iterationID in dict_data.keys():
        out += iterationID + '\n'
        nb_road_for_intersection = len(dict_data[iterationID])
        out += str(nb_road_for_intersection) + '\n'
        for street in dict_data[iterationID]:
            out += str(street[0]) + ' '  # street name
            out += str(street[1]) + ' '  # street name
            out += '\n'
    f.write(out)
    f.close()

    return out


print(output(ex))
