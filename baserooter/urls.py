from django.urls import path,include
from baserooter import views as bviews
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

app_name = 'baserooter'

urlpatterns = [

    # users views
    path('register',bviews.createUserView.as_view(), name='register'),
    path('token/',obtain_jwt_token ),
    path('token/refresh/',refresh_jwt_token),
    path('login',bviews.loginUserView.as_view(), name= 'login'),
    path('password/update',bviews.updatePasswordView.as_view(), name= 'password-update'),
    path('logout',bviews.logoutView.as_view(), name= 'logout'),
    path('all-users',bviews.getAllusers.as_view(), name= 'all-users'),

    # environment views
    path('get-environments',bviews.environmentView.as_view(),name='get-environments'),

    # application types view
    path('get-application-types',bviews.applicationTypeView.as_view(),name='get-application-types'),
    
    # applications views
    path('get-applications',bviews.getApplications.as_view(),name="get-application"), 
    path('get-app-data',bviews.getAppdataView.as_view(),name="get-app-data"),
    path('get-program-data',bviews.getProgramDataView.as_view(),name="get-program-data"),
    path('update-program-version',bviews.updateProgramVersion.as_view(),name="get-program-data"),

    # normal requests view
    path('create-normal-request',bviews.createNormalRequest.as_view(), name='create-normal-requests'),
    path('get-normal-request',bviews.retrieveNormalRequest.as_view(),name='get-normal-requests'),
    path('update-normal-request',bviews.updateNormalRequest.as_view(),name='update-normal-requests'),

    # deployment requests view
    path('create-deployment-request',bviews.createDeploymentRequest.as_view(),name='create-deployment-requests'),
    path('get-deployment-request',bviews.getDeploymentRequest.as_view(),name='get-deployment-requests'),  
    path('update-deployment-request',bviews.updateDeploymentRequest.as_view(),name='update-deployment-requests'),  

    # chat logs view
    path('get-chat-logs', bviews.getChatView.as_view(),name='get-chat-logs'),
    path('create-chat-logs', bviews.createChatView.as_view(),name='create-chat-logs'),
    
    
]