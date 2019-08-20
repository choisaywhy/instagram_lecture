from django.shortcuts import render, redirect
from django.conf.urls.static import static # 개발환경에서 static과 media 파일을 서빙하기 위해 필요합니다
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

# 현재 Django가 사용하는 유저 클래스를 반환하는 함수입니다
User = get_user_model()

# UserCreationForm이라는 기존의 유저생성폼을 상속받아
# 필요한 필드만 사용할 수 있도록 구현했습니다
class UserCreationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'profile', )

# 회원가입을 위한 함수입니다
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

    # views.py를 만들지 않고 view 함수를 urls.py에 구현했습니다
    path('signup/', signup, name='signup'), 

    # 기존의 로그인과 로그아웃 CBV를 사용하기 위한 코드입니다
    # 필요한 CBV가 있는 views.py 를 임포트하여 재사용 합니다
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include('insta.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)