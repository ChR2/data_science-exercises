import csv

with open('9_17_2016_mta_turnstile.csv', 'r') as csvfile:
  data = csv.reader(csvfile)
  next(data, None)

  mta_dict = {}

  for row in data:
    row[-1]=row[-1].strip()
    #tuple_mta = tuple(row[:4])
    mta_dict.setdefault(tuple(row[:4]),[]).append(row[4:])

    # if tuple_mta not in mta_dict:
    #   mta_dict[tuple_mta]=[row[4:]]
    # else:
    #   mta_dict[tuple_mta].append(row[4:])
  print mta_dict.items()[0:5]

