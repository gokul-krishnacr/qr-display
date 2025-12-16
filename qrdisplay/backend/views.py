from django.shortcuts import render,redirect
from django.http import HttpResponse
import qrcode
from .forms import Qrform
from .models import QrCodeModel
from io import BytesIO
# Create your views here.

def show(request):
    return HttpResponse("backend is working")

"""def home(request):

    return render(request , 'backend/index.html')"""

from io import BytesIO
import qrcode
from .models import QrCodeModel

def home(request):
    qr_image_url = None

    if request.method == 'POST':
        form = Qrform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            # Generate QR code
            qr = qrcode.QRCode(box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save image to buffer
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)  # 🔥 IMPORTANT

            # Save to database (ALL required fields)
            qr_obj = QrCodeModel.objects.create(
                data=url,
                url=url
            )

            qr_obj.qr_image.save(f"{url}.png", buffer, save=True)

            qr_image_url = qr_obj.qr_image.url
             # ✅ redirect after POST
            #return redirect('home')  # name your url pattern

    else:
        form = Qrform()

    return render(
        request,
        'backend/index.html',
        {'form': form, 'qr_image_url': qr_image_url}
    )
