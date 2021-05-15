import re

def extract(file, section): #section argümanı gerekli değil şimdilik. Yalnızca abstract için kullanılacak.
    section = "abstract"

    f = open(file, encoding = 'utf-8').read()
    value = re.findall(r'\\begin{abstract}\n\t(.*?)\n\\end{abstract}', f, flags=re.S)
    return(value[0])
    
print(extract("Fizik Projesi.tex", "abstract"))

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