import re
import mimetypes

from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404
from django.db.models import Q

from keci.models import Project
from keci.forms import ProjectForm, UploadFileForm
# Create your views here.

def keci_home_view(request):
    form = UploadFileForm()
    document_data = None

    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            document_data = request.FILES['file']
            #re.findall('s', document_data.chunks())
            #f = document_data.chunks()
            text = ""
            for chunk in document_data:
                text += chunk.decode('utf-8')
            print(text[1])
            value = re.findall(r'\\begin{abstract}\n\t(.*?)\n\\end{abstract}', text, flags=re.S)
            #value = re.findall(r"", text)
            print(value)

            #text = ""

            #for chunk in document_data:
            #    chunk = chunk.decode('utf-8')
            #    text += chunk
            #print(text)

            document_data.close()
    context = {'form':form, 'document_data':document_data}
    return render(request, 'keci_home.html', context=context)

def new_project_view(request):
    form = ProjectForm()
    file = "asasasas"

    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        file = request.POST.get('document')
        print(file==None)
    context = {'form':form, 'file':file}
    return render(request, 'new_project.html', context=context)

def keci_search_view(request):
    search_project = request.GET.get('search')

    if search_project:
        projects = Project.objects.filter(Q(title__icontains=search_project))# & Q(abstract__icontains=search_post)
    else:
        projects = Project.objects.all().order_by("-pub_date")

    context = {'projects':projects, 'search_project':search_project}
    return render(request, 'keci_search.html', context=context)

def keci_advanced_search_view(request):
    context = {}
    return render(request, 'keci_advanced_search.html', context=context)

def project_view(request, id):
    project = get_object_or_404(Project, id=id)
    fl_path = 'media/documents/deneme/' + str(id) + '.txt'
    f = open(fl_path, 'r')
    file_content = f.read()
    f.close()
    context = {'project':project, 'file_content':file_content}
    return render(request, 'project.html', context=context)

def help_view(request):
    context = {}
    return render(request, 'help.html', context=context)

def download_pdf(request, id):
    fl_path = 'media/documents/deneme/' + str(id) + '.txt'
    print(fl_path)
    filename = str(id) + ".txt" #str(id)+'.pdf'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    #context = {}
    #return render(request, 'help.html', context=context)