from django.contrib.auth.models import User

from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import *
from .forms import UserRegisterform
from .models import Articulo, Seccion
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from django.contrib.auth.decorators import permission_required

# Create your views here.

from django.shortcuts import render, redirect
from .carro import Carro
from inicio.models import Articulo  



def agregar_producto(request, producto_id):
    carro= Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.agregar(producto= producto)
    return redirect("inicio:carrito") 

def eliminar_producto(request, producto_id):
    carro= Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.eliminar(producto = producto)
    return redirect("inicio:carrito") 

def restar_producto(request, producto_id):
    carro= Carro(request)
    producto=Articulo.objects.get(id=producto_id)
    carro.restar_producto(producto = producto)
    return redirect("inicio:carrito") 

def limpiar_carro(request):
    carro= Carro(request)
    carro.limpiar_carro()
    return redirect("inicio:carrito") 

def index(request):
    if "leer_mas_tarde" not in request.session:
        request.session["leer_mas_tarde"] = []
    return render(request,"blog/index.html", {
        "lista_articulos": Articulo.objects.all().order_by('fecha_publicacion')[:10],
        "lista_articulos2": Articulo.objects.all(),
        "lista_secciones": Seccion.objects.all(),
        "leer_mas_tarde": request.session["leer_mas_tarde"],
    })
   
def carrito(request):         
    return render(request, "blog/carrito.html")

def acerca_de(request):         
    return render(request, "blog/acerca_de.html")

def contacto(request):         
    return render(request, "blog/contacto.html")
    


def articulo(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    return render(request, "blog/articulo.html", {
        "articulo": un_articulo
    })

def articulo_alta(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormArticulo(request.POST, request.FILES, instance=Articulo(imagen=request.FILES['imagen'], publicador=user))      
        if form.is_valid():
            form.save()
           
            return redirect("inicio:index")          
    else:
        form = FormArticulo(initial={'fecha_publicacion':timezone.now()})
        return render(request, "blog/articulo_nuevo.html", {
            "form": form
        })

def articulo_editar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == "POST":  
        user = User.objects.get(username=request.user)   
        un_articulo.publicador = user
        form = FormArticulo(data=request.POST, files=request.FILES, instance=un_articulo)
        if form.is_valid():
            form.save()
            return redirect("inicio:index")
    else:
        form = FormArticulo(instance = un_articulo)
        return render(request, 'blog/articulo_edicion.html', {
            "articulo": un_articulo,
            "form": form
        })

def articulo_eliminar(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    un_articulo.delete()
    return redirect("inicio:index")

def filtro_secciones(request, seccion_id):
    una_seccion = get_object_or_404(Seccion, id=seccion_id)
    queryset = Articulo.objects.all()
    queryset = queryset.filter(seccion=una_seccion)
    return render(request,"blog/index.html", {
        "lista_articulos": queryset,
        "lista_secciones": Seccion.objects.all(),
        "seccion_seleccionada": una_seccion
    })

@login_required
def leer_mas_tarde(request, articulo_id):
    un_articulo = get_object_or_404(Articulo, id=articulo_id)
    for id in request.session["leer_mas_tarde"]:
        if id == articulo_id:
            #existe el articulo
            return HttpResponseRedirect(reverse("sitio:articulo", args=(un_articulo.id,)))            
    request.session["leer_mas_tarde"] += [articulo_id]
    return HttpResponseRedirect(reverse("inicio:articulo", args=(un_articulo.id,)))   

    
def registro(request):
    if request.method == 'POST':
        form =  UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario: {username} creado')
           
            return redirect("inicio:index")
    else: 
        form = UserRegisterform()
    context = {'form' : form}
    return render(request,"registration/registro.html", context )

