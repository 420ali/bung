from django.shortcuts import render


def home(request):
    # URL'den bungalov adını almak
    bungalow = request.path.strip('/').split('/')[0]  # "asibungalov", "dogabungalov", "yildizbungalov"
    
    # Bungalov URL'lerine göre veri işleme (gerekirse)
    context = {
        'bungalow': bungalow
    }
    
    return render(request, 'home.html', context)

def asibungalov(request):
    return render(request, 'asi.html', {'bungalov': 'Asi'})

def dogabungalov(request):
    return render(request, 'doga.html', {'bungalov': 'Doğa'})

def yildizbungalov(request):
    return render(request, 'yildiz.html', {'bungalov': 'Yıldız'})