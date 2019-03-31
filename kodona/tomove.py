def add_search_to_queue(sender, instance, created, **kwargs):
    if (created):
        from img_processor.search_manager import init_search
        init_search.delay(instance.id)

from django.db.models.signals import post_save
post_save.connect(add_search_to_queue, sender=Search)