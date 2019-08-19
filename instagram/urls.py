from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static #static 로드할 떄 꼭 필요
from django.conf import settings # settings 로드할 떄 필요
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'profile', )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form':form,
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('insta.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)