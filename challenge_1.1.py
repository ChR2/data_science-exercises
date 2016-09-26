import csv

with open('9_17_2016_mta_turnstile.csv', 'r') as csvfile:
  data = csv.DictReader(csvfile)

  mta_dict = {}

  for row in data:
    c_a = row['C/A']
    unit = row['UNIT']
    scp = row['SCP']
    station = row['STATION']
    linename = row['LINENAME']
    division = row['DIVISION']
    date = row['DATE']
    time = row['TIME']
    desc = row['DESC']
    entries = row['ENTRIES']
    exits = (row['EXITS                                                               ']).strip()


    touple_mta = (c_a, unit, scp, station)

    if touple_mta not in mta_dict:
      mta_dict[touple_mta]=[[linename, division, date, time, desc, entries, exits]]
    else:
      mta_dict[touple_mta].append([linename, division, date, time, desc, entries, exits])
  print mta_dict






