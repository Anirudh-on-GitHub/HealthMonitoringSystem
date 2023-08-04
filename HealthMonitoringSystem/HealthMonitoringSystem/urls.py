from django.urls import re_path
import health.views

urlpatterns = [
    re_path(r'^$', health.views.display_data, name='display_data'),
]
