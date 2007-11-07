from django.conf.urls import url 
from . import views

app_name= 'modificar_formulas'
urlpatterns = [
	url(r'^$', views.mod_formulas, name ='mod_formulas'), # configuración de la url para la VISTA (view) de inicio o index
	url(r'^operar/$', views.operar, name = 'operar'),	  # url invocada cuando se presiona el botón ENVIAR de la sección FORMULAS
	url(r'^generando_tabla/$', views.cargar_tabla, name = "cargar_tabla"),	#se invoca esta url cuando el usuario selecciona un año
]