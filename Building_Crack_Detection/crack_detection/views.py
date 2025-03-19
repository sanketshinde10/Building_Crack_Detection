from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ImageUploadForm
from .detection import predict_crack

def index(request):
    result = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            result = predict_crack(image.image.path)
    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {'form': form, 'result': result})