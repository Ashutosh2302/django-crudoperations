from django.shortcuts import render, HttpResponseRedirect
from crudApp.models import Crudbase, FilesAdmin
# Create your views here.

def index(request):
    return render(request, 'crudop.html', {'entry': Crudbase.objects.all()})

def add(request):
    if request.method == 'POST':
        Crudbase(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone')).save()
    return HttpResponseRedirect('/')

def delete(request,id):
    if request.method == 'POST':
        Crudbase.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')
  
def edit(request, id):
    if request.method == 'POST':
        obj = Crudbase.objects.filter(id=id)[0]
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.save()
        return HttpResponseRedirect('/')

    return render(request, 'edit.html', {'id':id, 'data':Crudbase.objects.all().filter(id=id)[0]})


def files(request):
    media = {'file': FilesAdmin.objects.all()}
    return render(request,'files.html', media)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/adminupload')
            response['content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404