import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    result = []
    with open(neo_csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            pdes = row['pdes'] if row['pdes'] else None
            name = row['name'] if row['name'] else None
            diameter = float(
                row['diameter']) if row['diameter'] else float('nan')
            pha = True if row['pha'] == 'Y' else False

            result.append(NearEarthObject(pdes, name, diameter, pha))

    return result


def load_approaches(cad_json_path):
    result = []
    with open(cad_json_path, mode='r') as json_file:
        approaches_dict = json.load(json_file)
        for row in approaches_dict['data']:
            designation = row[0]
            time = row[3]
            distance = float(row[4])
            velocity = float(row[7])
            result.append(CloseApproach(time, distance, velocity, designation))
    return result
