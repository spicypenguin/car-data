import json
import csv


def main():
    processed_data = process_data(load_data())

    print(json.dumps(processed_data, indent=4, sort_keys=True))

    write_data_to_file(processed_data)


def load_data():
    my_file = 'data.json'
    with open(my_file, 'r') as f:
        data = json.load(f)
    
    return data


def process_data(data):
    new_set = []
    for item in data:
        name_components = process_name(item[0])
        new_set.append({
            'year': name_components['year'],
            'make': name_components['make'],
            'model': name_components['model'],
            'price': int(process_price(item[1])),
            'mileage': process_mileage(item[2])
        })
    
    return new_set


def process_name(name):
    components = name.split(' ')
    return {
        'year': int(components[0]),
        'make': components[1],
        'model': ' '.join(components[2:])
    }


def process_price(price):
    return price.replace(',','').replace('$','').split(' ')[0]


def process_mileage(mileage):
    mileage = mileage.replace(',','').replace('$','').split(' ')[0]
    try:
        mileage = int(mileage)
    except:
        mileage = 0
    
    # todo, bucket mileage?
    return mileage


def write_data_to_file(data):
    outfile = 'data.csv'
    with open(outfile, 'w') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    main()
