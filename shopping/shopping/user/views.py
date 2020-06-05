from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.

#루트 경로 
def index(request):
    return render(request, 'index.html', { 'email':request.session.get('user') })
    # 세선 안에 있는 유저를 가져오게 { 'email':request.session.get('user') }) 추가

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/' # 등록성공하면 root page로

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    #유효성 검사가 끝났을때 = 로그인이 정상적으로 되었을때
    def form_valid(self, form):
        self.request.session['user'] = form.email
        return super().form_valid(form)