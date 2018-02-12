from csv import DictReader, DictWriter
from os.path import join
from tempfile import gettempdir
from urllib.request import urlretrieve
from config import *

output_fieldnames = []
mapping = []
with open("mapping.txt") as f:
    for line in f:
        line = line.strip()
        if "<=" in line:
            _to, _from = line.replace(" ", "").split("<=")
            mapping.append((_from, _to))
            output_fieldnames.append(_to)
        else:
            output_fieldnames.append(line)

with open(input_path) as input_file:
    reader = DictReader(input_file, delimiter="\t")

    output_file = open(output_path, "w")
    output_writer = DictWriter(output_file, delimiter="\t", fieldnames=output_fieldnames)
    output_writer.writeheader()

    count = 0
    for line in reader:
        count += 1
        line["id"] = count
        line["point"] = "SRID=4326;POINT (" + line['longitude'] + " " + line["latitude"] + ")"
        for inkey, outkey in mapping:
            line[outkey] = line.pop(inkey)

        # trying to handle weird cyrillic city name that's not in 
        # expected encoding and crashing copy by having length > 1000
        if line["name_ascii"].startswith("\302\253\320\241\320\274"):
            line["name_ascii"] = None

        output_writer.writerow(line)

    output_file.close()

print("finishing conforming unum")
