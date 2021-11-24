from django.contrib                 import admin
from django.urls                    import path
from authAppExample                 import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from django.conf                    import settings
from django.conf.urls.static        import static
from django.conf.urls               import url,include 
from django.contrib                 import admin

urlpatterns = [
    path('admin/',                     admin.site.urls),  # use defaul Djando Admin
    path('login/',                     TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                   TokenRefreshView.as_view()), # generate new access token
    path('user/',                      authAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',             authAppViews.UserDetailView.as_view()), # check info for an specific user based on id(pk)
    path('persona/create/',            authAppViews.PersonaCreateView.as_view()),
    path('persona/view/',              authAppViews.PersonaGetAllView.as_view()), 
    path('pais/create/',               authAppViews.PaisCreateView.as_view()),
    path('pais/view/',                 authAppViews.PaisGetAll.as_view()),
    path('prueba/create/',             authAppViews.PruebaCreateView.as_view()),
    path('prueba/view/',               authAppViews.PruebaGetAllView.as_view()),
    path('prueba/views/<int:pk>/',     authAppViews.PruebaDetailView.as_view()),
    path('prueba/delete/<int:pk>/',    authAppViews.PruebaDeleteView.as_view()),
    path('prueba/update/<int:pk>/',    authAppViews.PruebaUpdateView.as_view()),
    
]
