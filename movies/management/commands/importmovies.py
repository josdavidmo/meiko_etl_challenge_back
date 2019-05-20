import csv
import glob
import json
import multiprocessing
import os
import subprocess
import time

from django.core.management.base import BaseCommand

from movies.models import Movie


def format(row):
  for key in Movie.HEADERS:
    row[key] = row[key].strip()
    if row[key] == "":
      del row[key]
      continue
  if row.get("genres"):
    row["genres"] = row["genres"].split("|")
  if row.get("plot_keywords"):
    row["plot_keywords"] = row["plot_keywords"].split("|")
  return row


def csv2json(file):
  file_csv = open(file, 'rU')
  reader = csv.DictReader(file_csv, Movie.HEADERS)
  out = json.dumps([{"model": "movies.Movie", "fields": format(row)} for row in
                    reader])
  file_csv.close()
  file_json = open('{}.json'.format(file).replace('data', 'fixtures'), 'w')
  file_json.write(out)
  file_json.close()
  os.remove(file)


class Command(BaseCommand):
  help = 'import data from csv'

  def add_arguments(self, parser):
    parser.add_argument('--file', type=str,
                        help='<file.tar.xz> with file movie_metadata.csv')
    parser.add_argument('-w', '--workers', type=int,
                        default=multiprocessing.cpu_count(),
                        help='number of parallel processes')

  def handle(self, *args, **options):
    start = time.time()
    file = options['file']
    workers = options['workers']
    command = "tar -xf {file} -C data " \
              "&& sed -i '1d;$d' data/movie_metadata.csv " \
              "&& split data/movie_metadata.csv -l 500 " \
              "data/movie_data_part_ " \
              "&& rm data/movie_metadata.csv ".format(file=file)
    subprocess.call(command, stdout=subprocess.PIPE, shell=True)
    files = [f for f in glob.glob("data/movie_data_part_*")]
    pool = multiprocessing.Pool(workers)
    pool.map_async(csv2json, files)
    pool.close()
    pool.join()
    end = time.time()
    self.stdout.write('Successfully creation fixtures: {:.3f}'.format(end -
                                                                      start))
