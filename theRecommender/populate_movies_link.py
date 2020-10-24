import os
from django.conf import settings
import urllib.request
import django
import datetime
import decimal
from tqdm import tqdm
from surprise import Reader
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theRecommender.settings')

django.setup()

from movieRecom.models import links


def create_link(movieid, imbdid, tmdbid):

    link = links(movieid=movieid, imbdid=imbdid, tmdbid=tmdbid)
    link.save()
    return link

def delete_db():
    print('truncate db')
    links.objects.all().delete()
    print('finished truncate db')


def populate():

    delete_db()

    # links = download_ratings()

    # for rating in tqdm(ratings.split(sep="\n")):
    #     r = rating.split(sep="::")
    #     if len(r) == 4:
    #         create_rating(r[0], r[1], r[2], r[3])
    linksPath = os.path.join(settings.BASE_DIR, 'movieRecom/mlModels/ml-latest-small/links.csv')
    reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

    with open(linksPath, newline='', encoding='ISO-8859-1') as csvfile:
            movieReader = csv.reader(csvfile)
            next(movieReader)  #Skip header line
            for row in tqdm(movieReader):
                movieID = int(row[0])
                imbdid = int(row[1])
                tmdbid =  1 if len(row[2]) == 0 else int(row[2])
                create_link(movieID, imbdid, tmdbid)


if __name__ == '__main__':
    print("Starting...")
    populate()