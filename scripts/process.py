#!/usr/bin/env python3
import requests
import os
import csv

SOURCE_URL = 'http://efele.net/maps/fips-10/data/fips-414.txt'


def retrieve(source_url):
    with open('archive/data.txt', "wb") as file:
        response = requests.get(source_url)
        file.write(response.content)


# The original file formatting is so terrible, e.g.
# UKY9_414_414_county borough_bwrdeistref sirol___Rhondda Cynon Taff [English]; Rhondda Cynon Taf [Welsh]__
# RS82_414_414_autonomous okrug_avtonomnyy okrug___Ust'-Ordynskiy Buryatskiy Avtonomnyy Okrug__
# UKY5_414_414_county borough_bwrdeistref sirol___Neath Port Talbot [English]; Castell-nedd Port Talbot [Welsh]__

# mostly the fields are divided by triple underscore, but sometimes double, but sometimes by only one!
# so don't be scared of my parse function :)

def parse():
    def clean(text):
        return text.strip('_').replace('_', ' ').replace(',', '')

    with open('data/data.csv', 'w') as destination:
        writer = csv.writer(destination)
        writer.writerow(['region code', 'region division', 'region name'])

        with open('archive/data.txt') as source:
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

if __name__ == "__main__":
    # define working directory
    if os.path.exists('process.py'):
        os.chdir('../')

    retrieve(SOURCE_URL)
    parse()
