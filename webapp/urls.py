from django.urls import path
from webapp.views.tasks import add_view, detail_view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('tasks/add/', add_view, name='task_add'),
    path('tasks/', index_view),
    path('tasks/<int:pk>', detail_view, name='task_detail')
]