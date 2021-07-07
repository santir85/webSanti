from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView

app_name = "inicio"
urlpatterns = [
    
    path('', views.index, name="index"),
    path('filtro_secciones/<int:seccion_id>', views.filtro_secciones, name="filtro_secciones"),
    path('<int:articulo_id>', views.articulo, name="articulo"),
    path('articulo_alta', views.articulo_alta, name="articulo_alta"),
    path('articulo_editar/<int:articulo_id>', views.articulo_editar, name="articulo_editar"),
    path('articulo_eliminar/<int:articulo_id>', views.articulo_eliminar, name="articulo_eliminar"),
    path('leer_mas_tarde/<int:articulo_id>', views.leer_mas_tarde, name="leer_mas_tarde"),
    path('login/',LoginView.as_view( template_name = 'registrtion/login.html') , name="login"),
    path('logout/',LogoutView.as_view( template_name = 'registration/logged_out.html') , name="logout"),
    path('registro/', views.registro, name="registro"),
     path("agregar_producto/<int:producto_id>/", views.agregar_producto, name="agregar_producto"),
     path('carrito/', views.carrito, name="carrito"),
     path("eliminar_producto/<int:producto_id>/", views.eliminar_producto, name="eliminar_producto"),
      path("restar_producto/<int:producto_id>/", views.restar_producto, name="restar_producto"),
    path("limpiar_carro/", views.limpiar_carro, name="limpiar_carro"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    path('contacto/', views.contacto, name="contacto"),
   
    
    
    
]