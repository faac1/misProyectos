from django.shortcuts import render


def index(request):
    context={}
    return render(request,'paginaweb/index.html',context)

def index2(request):
    context={}
    return render(request,'paginaweb/index2.html',context)

def crearcuenta(request):
    context={}
    return render(request,'paginaweb/Isession/crearcuenta.html',context)

def iniciosession(request):
    context={}
    return render(request,'paginaweb/Isession/iniciosession.html',context)

def rw(request):
    context={}
    return render(request,'paginaweb/pag_artista/r.w.html',context)

def perro(request):
    context={}
    return render(request,'paginaweb/pag_escultura/perro.html',context)

def perro2(request):
    context={}
    return render(request,'paginaweb/pag_escultura/perro2.html',context)

def artistas(request):
    context={}
    return render(request,'paginaweb/pag_inicio/artistas.html',context)

def esculturas(request):
    context={}
    return render(request,'paginaweb/pag_inicio/esculturas.html',context)

def obras(request):
    context={}
    return render(request,'paginaweb/pag_inicio/obras.html',context)

def orfebreria(request):
    context={}
    return render(request,'paginaweb/pag_inicio/orfebreria.html',context)

def pinturas(request):
    context={}
    return render(request,'paginaweb/pag_inicio/pinturas.html',context)

def subir(request):
    context={}
    return render(request,'paginaweb/pag_inicio/subir.html',context)

def tejidos(request):
    context={}
    return render(request,'paginaweb/pag_inicio/tejidos.html',context)

def aros(request):
    context={}
    return render(request,'paginaweb/pag_orfabreria/aros.html',context)

def collar(request):
    context={}
    return render(request,'paginaweb/pag_orfabreria/collar.html',context)

def elbebedor(request):
    context={}
    return render(request,'paginaweb/pag_pinturas/elBebedor.html',context)

def elviolinista(request):
    context={}
    return render(request,'paginaweb/pag_pinturas/elVioliista.html',context)

def mujerrumana(request):
    context={}
    return render(request,'paginaweb/pag_pinturas/mujer_ruma.html',context)

def tejidohuaso(request):
    context={}
    return render(request,'paginaweb/pag_tejidos/tejidohauso.html',context)

def tejidomapuche(request):
    context={}
    return render(request,'paginaweb/pag_tejidos/tejidomapuche.html',context)
