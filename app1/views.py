from django.shortcuts import render
import requests
from django.http.response import HttpResponse
# Create your views here.


def getVideoObj(url):
    print(url, "downloading now")
    return requests.get(url).content


def download_video(request):
    try:
        url = request.POST.get('url')
        file_name = request.POST.get('file_name')
        no_of_urls = request.POST.get('no_of_urls')
        if url and file_name and no_of_urls:
            content = b"".join(
                [getVideoObj(url.format(x)) for x in range(
                    1, int(no_of_urls)+1)]
            )
            resp = HttpResponse(content, content_type="video/.mp4")
            resp['Content-Disposition'] = 'inline; filename=' + \
                "{}.mp4".format(file_name)
            return resp
        return render(request, "index.html", {"error": "please Fill require Fields"})
    except Exception as exc:
        return render(request, "index.html", {"error": str(exc)})


def renderPage(request):
    return render(request, "index.html")
