# flake8: noqa
from django.conf.urls.defaults import *


urlpatterns = patterns("",
    url(r"^$", "bookmarks.views.bookmarks", name="all_bookmarks"),
    url(r"^your_bookmarks/$", "bookmarks.views.your_bookmarks", name="your_bookmarks"),
    url(r"^add/$", "bookmarks.views.add", name="add_bookmark"),
    url(r"^(\d+)/delete/$", "bookmarks.views.delete", name="delete_bookmark_instance"),
)
