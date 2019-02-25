{% if django_version < "2" %}from django.conf.urls import url{% endif %}
{% if django_version >= "2" %}from django.urls import path{% endif %}
from {{ project_name }} import views


urlpatterns = [{% if django_version >= "2" %}
    path("<str:path>", views.static_view),
{% else %}
    url(r"^(.*)$", views.static_view),
{% endif %}]
