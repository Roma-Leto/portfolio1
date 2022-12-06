from django.urls import path

from .views import bbs, BbDetailView, comments

urlpatterns = [
    path('bbs/<int:pk>/comments/', comments),
    path('bbs/<int:pk>/', BbDetailView.as_view()),
    path('bbs/', bbs),
]

# TODO: Добавить ттекстовые файлы свящанные с комментариями.
# TODO: Не отображаются последние 10объявлений наглавной.
# TODO: Кнопка регистрции не пропадает после входа.
