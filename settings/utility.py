# конвертирует список ,с p[(5,)(8,),...] к [5,8,...]
def convert(list_convert):
    return [itm[0].lower() for itm in list_convert]


def download_catalog_coordinates_bd(catalog_file, delimiter):
    dict_catalog = {}
    with open(catalog_file, 'r', ) as file_out:
        data_catalog = file_out.readlines()
        for line in data_catalog:
            data = line.split(delimiter)
            dict_catalog[data[0]] = {
                'x_coordinate': data[1],
                'y_coordinate': data[2],
                'h_coordinate': data[3].replace('\n', ''),
            }
    return dict_catalog


def data_verification(data):
    flag = False
    for p in data:
        print(p)
        for coord in data[p]:
            try:
                f = float(data[p][coord])
                flag = True
            except:
                flag = False
                continue
        print(flag)
    return flag
