from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render


def index(request):
    # return render(request, 'web/index.html')
    return render(request, 'web/index.html')


def coming(request):
    return render(request, 'web/coming.html')


def whitepaper(request):
    # 要下载的文件路径
    filename = './web/static/web/MermaidWhitePaper.pdf'
    response = HttpResponse(readfile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="MermaidWhitePaper"'
    return response


def readfile(filename, chunk_size=512):
    """
    缓冲流下载文件方法
    :param filename:
    :param chunk_size:
    :return:
    """
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
