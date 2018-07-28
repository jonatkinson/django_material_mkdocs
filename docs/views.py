import os

from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.views import serve
from django.http import HttpResponse

@login_required
def serve_docs(request, path):
    filepath = os.path.join(settings.BASE_DIR, "mkdocs_build", path)

    return HttpResponse(filepath)

    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)

    return serve(request, path, insecure=True)
