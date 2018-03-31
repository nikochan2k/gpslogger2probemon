import sqlite3
import csv

from datetime import datetime, timezone
from contextlib import closing

with closing(sqlite3.connect('probemon.db')) as conn:
  c = conn.cursor()
  try:
    c.execute('ALTER TABLE probemon ADD COLUMN lat float')
    c.execute('ALTER TABLE probemon ADD COLUMN lon float')
  except:
    pass
  with open('./20180330.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    begin = None
    end = None
    for row in reader:
      time = datetime.strptime(row['time'],  '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()
      end = time + 9 * 60 * 60
      if begin is None:
        param = (row['lat'], row['lon'], end, )
        c.execute('UPDATE probemon SET lat = ?, lon = ? WHERE date < ?', param)
      else:
        param = (row['lat'], row['lon'], begin, end, )
        c.execute('UPDATE probemon SET lat = ?, lon = ? WHERE ? <= date AND date < ?', param)
      begin = end
    param = (row['lat'], row['lon'], begin, )
    c.execute('UPDATE probemon SET lat = ?, lon = ? WHERE ? <= date', paraｍ)
    conn.commit()
 
 