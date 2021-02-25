from django.urls import path
from core.views import SignUpView, ProfileView, ActivateAccount, index



urlpatterns = [
	path('', index, name='home'),
   	path('signup/', SignUpView.as_view(), name='signup'),
   	path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
  	#path('update/<int:pk>/', update, name='update_profile'),
	path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

]