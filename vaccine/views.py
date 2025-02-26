from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from vaccine.forms import VaccineForm
from vaccine.models import Vaccine


@method_decorator(login_required, name="dispatch")
class VaccineList(View):
    def get(self, request):
        vaccine_list = Vaccine.objects.all().order_by('name')
        paginator_obj = Paginator(vaccine_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator_obj.get_page(page_number)
        context = {
            'page_obj': page_obj
        }
        return render(request, 'vaccine/vaccine-list.html', context)


@method_decorator(login_required, name="dispatch")
class VaccineDetail(View):
    def get(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404('Vaccine does not exist')
        
        context = {
            'object': vaccine
        }
        return render(request, 'vaccine/vaccine-detail.html', context)
    

@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("vaccine.add_vaccine", raise_exception=True), name="dispatch")
class VaccineCreate(View):
    form_class = VaccineForm
    template_name = 'vaccine/create-vaccine.html'

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaccine created successfully')
            return HttpResponseRedirect(reverse('vaccine:list'))
        messages.error(request, 'Please enter valid data')
        return render(request, self.template_name, {'form': form})
    

@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("vaccine.change_vaccine", raise_exception=True), name="dispatch")
class VaccineUpdate(View):
    form_class = VaccineForm
    template_name = 'vaccine/update-vaccine.html'

    def get(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404('Vaccine does not exist')
        
        context = {
            'form': self.form_class(instance=vaccine)
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404('Vaccine does not exist')
        
        form = self.form_class(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaccine updated successfully')
            return HttpResponseRedirect(reverse('vaccine:detail', kwargs={'id': vaccine.id}))
        messages.error(request, 'Please enter valid data')
        return render(request, self.template_name, {'form': form})
    

@method_decorator(login_required, name="dispatch")
@method_decorator(permission_required("vaccine.delete_vaccine", raise_exception=True), name="dispatch")
class VaccineDelete(View):
    template_name = 'vaccine/delete-vaccine.html'

    def get(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404('Vaccine does not exist')
        
        context = {
            'object': vaccine
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404('Vaccine does not exist')
        
        vaccine.delete()
        messages.success(request, 'Vaccine deleted successfully')
        return HttpResponseRedirect(reverse('vaccine:list'))