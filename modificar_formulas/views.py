from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
#from modificar_formulas.models import Inventario   #import la informacion de la bd
#from modificar_formulas.formulas import Formulas

def mod_formulas(request): #VISTA(view) de inicio o index

		#lista = bd.objects.all() #Obtengo toda la info almacenada en la bd mediante el método objects.all(), lo guardo en lista.
		#return render(request, 'modificar_formulas/mod_formulas.html', {'lista': lista,}) # Devuelvo el objeto HTML (y la lista que va a ser -  
																						  # manejada dentro del código en la página HTML)

def operar(request):

	"""indices = request.GET.getlist('chk_tab')
	lista = Inventario.objects.all()
	opcion = request.GET['radio_formula']				     #con este metodo obtengo la longitud de la lista (o cantidad de filas seleccionada)

	dimension = len(indices)

	if request.GET['radio_formula'] == 'sum':
		#return HttpResponse(Formulas.sumatoria(indices, opcion))
		return render(request, 'modificar_formulas/mod_formulas.html', {'lista': lista, 'result_op': Formulas.sumatoria(indices, opcion),})

	elif request.GET['radio_formula'] == 'prom':
		return render(request, 'modificar_formulas/mod_formulas.html', {'lista': lista, 'result_op': Formulas.promedio(indices, opcion),})

	else:
		return HttpResponse('Fila(s) seleccionada para ACUMULACIO: '+str(dimension)) #una prueba"""

def cargar_tabla(request):
	"""lista = Inventario.objects.filter(id=request.GET['radio_year'])
	return render(request, 'modificar_formulas/mod_formulas.html', {'lista': lista,})"""