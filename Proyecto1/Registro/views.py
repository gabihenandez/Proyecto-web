from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from Registro.forms import RegisterBusinessForm


# Create your views here.

class RegistrateView(FormView):
    template_name = 'registro.html'

    # GET
    def get(self, request, *args, **kwargs):
        form = RegisterBusinessForm(request.GET or None)
        context = {
        'form_get' : form
        }
        return render(request, self.template_name, context)

    # POST
    def post(self, request, *args, **kwargs):
        form = RegisterBusinessForm(request.POST or None)
        if form.is_valid():
            self.object = form.save(commit = False)
            self.object.set_password(self.object.password)
            self.object.save()
        return redirect('Login:login')