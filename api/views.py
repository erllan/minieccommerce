from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, ProfileSerializer, UpdateUserSerializer

from django.contrib.auth.models import User
from core.models import Profile


from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from core.tokens import account_activation_token


@api_view(['GET'])
def userlist(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
def signup(request):
	serializer = UserSerializer(data=request.data)
	if request.method == 'POST':
			if serializer.is_valid():
				user = serializer.save(is_active=False)
				#user.is_active = False # Deactivate account till it is confirmed
				current_site = get_current_site(request)
				subject = 'Activate Your MySite Account'
				message = render_to_string('emails/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
				})
				user.email_user(subject, message)

				messages.success(request, ('Please Confirm your email to complete registration.'))	
	return Response(serializer.initial_data)


@api_view(['POST'])
def update(request, pk):
	user = User.objects.get(id=pk)
	if request.method == 'POST':
		serializer = UpdateUserSerializer(instance=user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)