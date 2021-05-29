import re
import mimetypes
from django.core import paginator
from django.forms.forms import Form

from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404
from django.utils.translation import templatize
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.core.paginator import Paginator

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from keci.models import Project, Author
from keci.forms import ProjectForm, UploadFileForm
# Create your views here.

def keci_home_view(request):
    projects = ""

    if request.user.is_authenticated:
        projects = Project.objects.filter(created_by__username=request.user.username).order_by('-pub_date')
        print(projects)
        print(type(projects))
    else:
        print(False)

    context = {'projects':projects}
    return render(request, 'keci/keci_home.html', context=context)

#def keci_home_view(request):
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
    return render(request, 'keci/keci_home.html', context=context)

def keci_search_view(request):
    query = request.GET.get('query')#id ile alıyoruz
    field = request.GET.get('field')
    size = request.GET.get('size')
    order = request.GET.get('order')

    if order == None:
        order = "-pub_date"

    if size == None:
        size = 25

    if query:
        if field == 'all':
            projects = Project.objects.filter(Q(title__icontains=query)|Q(abstract__icontains=query)|Q(created_by__username__icontains=query)).order_by(order)
        elif field == 'title':
            projects = Project.objects.filter(Q(title__icontains=query)).order_by(order)
        elif field == 'abstract':
            projects = Project.objects.filter(Q(abstract__icontains=query)).order_by(order)
        elif field == 'author':
            projects = Project.objects.filter(Q(created_by__username__icontains=query)).order_by(order)
        else:
            projects = Project.objects.filter(Q(created_by__username__icontains=query)).order_by(order)
    else:
        projects = Project.objects.all().order_by(order)
        query = ""

    size = 1

    paginator = Paginator(projects, size)

    page = request.GET.get('page')

    if page == None:
        page = 1
    
    projects = paginator.get_page(page)

    context = {'projects':projects, 'query_term':query, 'size_term':size, 'order_term':order}
    return render(request, 'keci/keci_search.html', context=context)

def keci_advanced_search_view(request):
    context = {}
    return render(request, 'keci/keci_advanced_search.html', context=context)

class new_project_view(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title','abstract','language','current_stage','branches','authors','document']
    template_name = 'keci/new_project.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

def project_view(request, id):
    project = get_object_or_404(Project, id=id)
    fl_path = 'media/documents/deneme/' + str(id) + '.txt'
    f = open(fl_path, 'r')
    file_content = f.read()
    f.close()
    context = {'project':project, 'file_content':file_content}
    return render(request, 'keci/project.html', context=context)

def help_view(request):
    context = {}
    return render(request, 'keci/help.html', context=context)

def download_pdf(request, id):
    fl_path = 'media/documents/deneme/' + str(id) + '.pdf'
    print(fl_path)
    filename = str(id) + ".pdf" #str(id)+'.pdf'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    #context = {}
    #return render(request, '*.html', context=context)