#!/usr/bin/env python3
import requests
import csv

SOURCE_URL = 'http://efele.net/maps/fips-10/data/fips-414.txt'


def retrieve(source_url):
    with open('archive/data.txt', "wb") as file:
        response = requests.get(source_url)
        file.write(response.content)

def parse():
    def clean(text):
        return text.strip('_').replace('_', ' ').replace(',', '')

    destination = open('data/data.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(destination)
    writer.writerow(['region_code', 'region_division', 'region_name'])

    source = open('archive/data.txt', encoding='utf-8')
    for line in source:
        line = line.rstrip().strip('_').replace('414', '')
        try:
            code, division, name = line.split('___')
        except ValueError:
            try:
                code, division, name = line.split('__')
            except ValueError:
                code, *division, name = line.split('_')
                division = '_'.join(division)

        writer.writerow([code, clean(division), clean(name)])

    source.close()
    destination.close()

if __name__ == "__main__":
    retrieve(SOURCE_URL)
    parse()
