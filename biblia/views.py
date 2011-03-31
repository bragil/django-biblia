# -*- coding: utf-8 -*-
from django_biblia.biblia.models import *
from django.core import serializers
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

def index(request):
	"""
	Página inicial, traz os versículos de Gênesis 1
	"""
	textos = Texto.objects.filter(capitulo=1).filter(livro__id=1)
	return render_to_response('base.html', locals(), context_instance=RequestContext(request))
	
def busca_livro(request):
	"""
	Retorna os livros da Bíblia para serem exibidos no autocomplete do campo de busca, de acordo com a busca feita.
	"""
	busca = request.GET['term']
	livros = Livro.objects.filter(livro__istartswith=busca)
	res = [ dict(id=l.id, label=l.__unicode__(), value=l.__unicode__()) for l in livros ]
			
	return HttpResponse(simplejson.dumps(res), mimetype="application/x-javascript")


def busca_capitulos(request):
	livro_id = request.GET['l']  # ID do Livro
	
	livro = Livro()
	lista = livro.get_capitulos(livro_id)
	return HttpResponse(simplejson.dumps(lista), mimetype="application/x-javascript")
	
def busca_versiculos(request):
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Capítulo
	
	livro = Livro()
	lista = livro.get_versiculos(livro_id, capitulo_num)
	return HttpResponse(simplejson.dumps(lista), mimetype="application/x-javascript")
	
def busca_textos_capitulo(request):
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Capítulo
	
	textos = Texto.objects.filter(livro__id = livro_id).filter(capitulo = capitulo_num)
	txt = ''
	if textos:
		for t in textos:
			txt = txt + '<p class="texto"><span class="num_versiculo">' + str(t.capitulo) + ':' + str(t.versiculo) + '</span>' + t.texto + '</p>'
	return HttpResponse(txt)
	
def busca_texto_versiculo(request):
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Capítulo
	verso_num = request.GET['v'] # Versículo
	
	textos = Texto.objects.filter(livro__id = livro_id).filter(capitulo = capitulo_num).filter(versiculo = verso_num)
	txt = ''
	if textos:
		for t in textos:
			txt = txt + '<p class="texto"><span class="num_versiculo">' + str(t.capitulo) + ':' + str(t.versiculo) + '</span>' + t.texto + '</p>'
	return HttpResponse(txt)