import os
import mimetypes

from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.views import serve
from django.http import HttpResponse

@login_required
def serve_docs(request, path):
    file_path = os.path.join(settings.BASE_DIR, "mkdocs_build", path)
    file_mime = mimetypes.guess_type(file_path)

    with open(file_path, 'r') as file_handle:
        data = file_handle.read()
   
    response = HttpResponse(content_type=file_mime)
    response.write(data)

    return response

    #------

    return HttpResponse(filepath)

    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)

    return serve(request, path, insecure=True)
