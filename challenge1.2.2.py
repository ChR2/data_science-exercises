import csv
import dateutil.parser
import numpy as np

with open('9_17_2016_mta_turnstile.csv', 'r') as csvfile:
  data = csv.reader(csvfile)
  next(data, None)

  mta_dict = {}
  for row in data:
    row[-1]=row[-1].strip()
    mta_dict.setdefault(tuple(row[:4]),[]).append([dateutil.parser.parse(row[6] + ' ' + row[7]), row[9]])
  #print mta_dict.items()[0][1][0][0]

  #count = 0
  diff_dict = {}
  for k, v in mta_dict.items():
    for i in range(len(v)):
      if i == 0:
        count = 0
      else:
        count = int(v[i][1]) - int(v[i-1][1])
        if count < 0:
          count = np.NaN
      diff_dict.setdefault(k,[]).append([v[i][0], count])
  print diff_dict.items()[4]


  #print mta_dict.items()