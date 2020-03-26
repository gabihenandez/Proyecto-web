from django.shortcuts import render 
from django.views.generic import View
from django.contrib.auth import authenticate
from django.shortcuts import redirect
 	#LLEGA A LA VISTA Y LA EJECUTA
#  def Index (request):
#      return render(request,'index.html',{})

#  def Landing (request):
#     return render(request,'Landing.html',{})

class LoginClass(View):

    templates = 'login/index.html'
    template_ok = 'Landing/Landing.html'
    def get(self, request , *args , **kwargs):

        return render(request,self.templates, {})
    def post(self,request,*args,**kwargs):

        user_post = request.POST['user'] #Extraer lo que tiene la vista .POST
        password_post = request.POST['password']

        user_session = authenticate(username = user_post , password = password_post)
        #metodo de autentificacion
        if user_session is not None:
            return redirect ('Login:Dashboard')
        else:
            self.message = 'usuario o contraseña incorrecto'

        return render(request, self.templates, self.get_context())

    def get_context(self):
        return {
            'error':self.message,
        }
    
class LandingClass(View):
    template_ok = 'Landing/Landing.html'
    def get(self, request, * args, ** kwargs):
        return render(request,self.template_ok,{})

class DashboardClass(View):
    template_ok= 'Dashboard/dashboard.html'
    def get(self,request, * args, ** kwargs):
        return render(request,self.template_ok,{})


