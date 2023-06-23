from django.shortcuts import render
from .models import Tipo_solicitud, Subir
from .forms import Tipo_solicitud_Form


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
    if request.method != "POST":
        tipo_solicitud = Tipo_solicitud.objects.all()
        context = {"tipo_solicitud":tipo_solicitud}
        return render(request,'paginaweb/pag_inicio/subir.html',context)
    else:
        nombre = request.POST["nombre"]
        tipo_solicitud = request.POST["tipo_solicitud"] 
        mensaje = request.POST["mensaje"]
        fecha = request.POST["fecha"]
        telefono = request.POST["telefono"]
        categorias = request.POST["categorias"]
        seleccionar = request.POST["seleccionar"]

        objtipo_solicitud= Tipo_solicitud.objects.get(id_tipo_solicitud = tipo_solicitud)
        obj = Subir.objects.create(
            nombre = nombre,
            id_tipo_solicitud = objtipo_solicitud,
            mensaje = mensaje,
            fecha = fecha,
            telefono = telefono,
            categorias = categorias,
            seleccionar = seleccionar )
        
        obj.save()
        context={'mensaje': "ok,mensaje enviado"}
        return render(request,'paginaweb/index2.html',context)



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

def crud(request):
    subir= Subir.objects.all()
    context={"subir":subir}
    return render(request,'paginaweb/mens_list.html',context)

def borrarmens(request,pk):
    context={}
    try:
        subir = Subir.objects.get(id_subir = pk)
        subir.delete()
        mensaje = "bien, mensaje eliminado"
        subirs = Subir.objects.all()
        context = {'subir':subir, 'mensaje':mensaje}
        return render(request,'paginaweb/mens_list.html',context)
    except:
        mensaje = "Error, mensaje no exixste"
        subirs = Subir.objects.all()
        context = {'subir':subir, 'mensaje':mensaje}
        return render(request,'paginaweb/mens_list.html',context)


def editarmens(request,pk):

    if pk != "":
        subir = Subir.objects.get(id_subir = pk)
        tipo_solicitud = Tipo_solicitud.objects.all()
    
        print(type(subir.id_tipo_solicitud.tipo_solicitud))

        context={'subir': subir, 'tipo_solicitud':tipo_solicitud}
        if subir:
            return render(request,'paginaweb/pag_inicio/subir2.html',context)
        else:
            context = {'mensaje':"Error, mensaje no existe"}
            return render(request,'paginaweb/mens_list.html',context)


def subirUpdate(request):

    if request.method == "POST":
        nombre = request.POST["nombre"]
        tipo_solicitud = request.POST["tipo_solicitud"] 
        mensaje = request.POST["mensaje"]
        fecha = request.POST["fecha"]
        telefono = request.POST["telefono"]
        categorias = request.POST["categorias"]
        seleccionar = request.POST["seleccionar"]

        objtipo_solicitud= Tipo_solicitud.objects.get(id_tipo_solicitud = tipo_solicitud)

        subir = Subir()
        subir.nombre = nombre
        subir.id_tipo_solicitud = objtipo_solicitud
        subir.mensaje= mensaje
        subir.fecha= fecha
        subir.telefono= telefono
        subir.categorias= categorias
        subir.seleccionar= seleccionar
        subir.save()

        tipos = Tipo_solicitud.objects.all()
        context = {'mensaje': "OK, mensaje actualizado",'tipos':tipos, 'subir':subir }
        return render(request, 'paginaweb/index2.html',context)
    else:
        subir = Subir.objects.all()
        context = {'subir':subir}
        return render(request,'paginaweb/mens_list.html',context)
    

def subir2(request):
    context = {}
    return render(request,'paginaweb/pag_inicio/subir2.html',context)


def crud_tipo_solicitud(request):
    tipo_solicitud = Tipo_solicitud.objects.all()
    context = {'tipo_solicitud':tipo_solicitud}
    print("enviando datos tipo_solicitud_list")
    return render(request,"paginaweb/tipo_solicitud_list.html",context)


def tipo_solicitudAdd(request):
    print("estoy en controlador tipo_solicitudAdd ")
    context={}

    if request.method == "POST":
        print("controlador de un POST")
        form = Tipo_solicitud_Form(request.POST)
        if form.is_valid:
            print("estoy en agregar ta bien")
            form.save()

            form = Tipo_solicitud_Form()
            context = {'mensaje':"datos grabados ", "form":form}
            return render(request,"paginaweb/tipo_solicitudAdd.html",context)
    else:
        form = Tipo_solicitud_Form()
        context= {'form':form}
        return render(request,"paginaweb/tipo_solicitudAdd.html",context)

