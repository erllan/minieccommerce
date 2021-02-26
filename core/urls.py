from django.urls import path
from core.views import SignUpView, ActivateAccount, index, edit, ProfileView



urlpatterns = [
	path('', index, name='home'),
   	path('signup/', SignUpView.as_view(), name='signup'),
   	
   	#frontend edit
   	path('edit/<int:pk>/', edit, name='profile_edit' ),
   	
   	path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
	path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

]