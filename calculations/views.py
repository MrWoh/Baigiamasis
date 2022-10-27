from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.views.decorators.csrf import csrf_protect


def calculations(request):

    return render(request, 'calculations.html')
