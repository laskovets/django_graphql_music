from celery import shared_task
from music.models import Track


@shared_task()
def print_track_count():
    count = Track.objects.count()
    print(count)
    return str(count)
