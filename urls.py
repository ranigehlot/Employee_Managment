from django.urls import path,include
from.import views

urlpatterns = [
    path('add',views.add,name='add'),
    path('insert',views.insert,name='insert'),
    path('show',views.show,name='show'),
    path('edit/<int:eid>',views.edit,name='edit'),
    path('update/<int:eid>',views.update,name='update'),
    path('delete/<int:eid>',views.delete,name='delete')
]



