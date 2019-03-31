from kodona.celery import celery
from searches.models import Search, SearchResult
from .image_processor import ImageProcessor
from cloud_storage.storage import upload_output


@celery.task
def init_search(search_id):
    search = Search.objects.get(id=search_id)
    update_status(search, Search.IN_PROGRESS)

    searchee_id = search.searchee.id
    images = list(search.searchee.samples.all(
    ).values_list('image', flat=True))
    video = search.video

    print('\n [INFO] Received search request for Searchee<{}>'.format(searchee_id))
    result = start_search(search_id, images, video)

    write_results(result)


def update_status(search, status):
    search.status = status
    search.save()


def start_search(searchee_id, images, video):
    processor = ImageProcessor()
    print('\n [INFO] Starting search. This will take a while...')

    processor.add_searchee([searchee_id], [images])
    return processor.find_searchee(video)


#
# searchee_id=id,
# confidence=confidence,
# timestamp=timestamp,
# image=snap_path
#
def write_results(search, results):
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

        result = SearchResult(
            search=search,
            timestamp_sec=timestamp,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            image=url,
            confidence=confidence
        )
        result.save()
    
    search.status = Search.COMPLETED
    search.save()