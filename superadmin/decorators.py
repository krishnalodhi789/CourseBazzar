from django.shortcuts import render, redirect
from django.contrib import messages

def check_superadmin_decorator(view_func):
    def valid_superadmin(request, *args, **kwargs):
        # Your custom logic goes here before the view is executed
        if not request.user.username == "superadmin":
            messages.error(request, "You are not Super Admin..")
            return redirect('superadmin_loginform')

        # Call the original view function
        return view_func(request, *args, **kwargs)

    return valid_superadmin
