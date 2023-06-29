#!/bin/python
# Copied from https://forum.flirc.tv/index.php?/topic/11418-any-way-to-get-the-json-for-device/&do=findComment&comment=29427
# Author: Jason Kotzin
import csv
import re
import sys 
import json

skipbr = {}
skipbr['header'] = {}
skipbr['header']['version'] = '2.0'

skipbr['types'] = ['devices.tv.a' , 'devices.box' , 'devices.audio' , 'devices.av' , 'devices.games' , 'devices.pc' , 'devices.home' , 'devices.misc']
skipbr['brand'] = 'BRAND (REPLACE ME)'
skipbr['model'] = 'MODEL (REPLACE ME)'

skipbr['signals'] = []

if (len(sys.argv) != 2):
    print("Error: specify text file")
    sys.exit(0)

def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", ',', s)

    return s

def count():
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
    return line_count

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        signal = {
            "label": row[0],
            "protocol": "PRONTO",
            "code": row[1].lstrip()
        }
        skipbr['signals'].append(signal)

print(json.dumps(skipbr, indent=4)) 
