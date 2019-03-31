import os

from kodona import celeryapp
from . import ImageProcessor
from . import util
from cloud_storage.storage import upload_output



@celeryapp.task
def test(n):
    for i in range(n):
        print(i)


@celeryapp.task
def start_search(search_id):
    from searches.models import Search

    search = Search.objects.get(id=search_id)
    search.status = Search.IN_PROGRESS
    search.save()

    searchee_id = search.searchee.id
    images = list(search.searchee.samples.all().values_list('image_url', flat=True))
    video = search.video_url

    print('\n [INFO] Starting Search - {}. This will take a while...'.format(search_id))

    processor = ImageProcessor()
    processor.add_searchee([searchee_id], [images])
    result = processor.find_searchee(video)

    write_results(search, result)


def write_results(search, results):
    from searches.models import Search, SearchResult
    
    for r in results:
        searchee_id = r['searchee_id']
        confidence = r['confidence']
        timestamp = r['timestamp']
        image = r['image']
        x1 = r['x1']
        x2 = r['x2']
        y1 = r['y1']
        y2 = r['y2']

        url = upload_output(image)
        util.rm(image)  # delete file after uploading inorder to optimise space

        result = SearchResult(
            search=search,
            timestamp_sec=timestamp,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            image_url=url,
            confidence=confidence
        )
        result.save()
    
    search.status = Search.COMPLETED
    search.save()