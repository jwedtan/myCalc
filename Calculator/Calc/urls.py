from django.conf.urls import url


from . import views
app_name= 'Calc'


urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
]