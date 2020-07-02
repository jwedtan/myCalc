from django.conf.urls import url


from . import views
app_name= 'Calc'


urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    # url(r'^history/', views.HistoryView.as_view()),
]