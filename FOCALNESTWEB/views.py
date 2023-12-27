from django.contrib.auth.views import LoginView

class login_page(LoginView):
    template_name = 'admin/login.html'