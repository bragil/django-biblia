# -*- coding: utf-8 -*-
from django_biblia.biblia.models import *
from django.core import serializers
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from django.core.cache import cache


def index(request):
	"""
	Página inicial, traz os versículos de Gênesis 1
	"""
	textos = Texto.objects.filter(capitulo=1).filter(livro__id=1)
	return render_to_response('base.html', locals(), context_instance=RequestContext(request))
	

def busca_livro(request):
	"""
	Retorna os livros da Bíblia para serem exibidos no autocomplete do campo de busca, de acordo com a busca feita, via JSON.
	"""
	busca = request.GET['term']
	# Busca lista no cache
	cache_key = 'livros-iniciados-em-' + busca
	livros = cache.get(cache_key)
	if livros is None:
		livros = Livro.objects.filter(livro__istartswith=busca)
		cache.set(cache_key, livros)
	else:
		print 'Obtido do cache: ' + cache_key

	res = [ dict(id=l.id, label=l.__unicode__(), value=l.__unicode__()) for l in livros ]
			
	return HttpResponse(simplejson.dumps(res), mimetype="application/x-javascript")


def busca_capitulos(request):
	"""
	Retorna os números referentes aos capítulos de um determinado livro, via JSON.
	"""
	livro_id = request.GET['l']  # ID do Livro
	# Busca lista no cache
	cache_key = 'capitulos-do-livro-' + livro_id
	lista = cache.get(cache_key)
	if lista is None:
		livro = Livro()
		lista = livro.get_capitulos(livro_id)
		cache.set(cache_key, lista)
	else:
		print 'Obtido do cache: ' + cache_key

	return HttpResponse(simplejson.dumps(lista), mimetype="application/x-javascript")
	

def busca_versiculos(request):
	"""
	Retorna os números referentes aos versículos de um determinado capítulo, via JSON.
	"""
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Capítulo
	# Busca lista no cache
	cache_key = 'versiculos-do-capitulo-' + capitulo_num + '-do-livro-' + livro_id
	lista = cache.get(cache_key)
	if lista is None:
		livro = Livro()
		lista = livro.get_versiculos(livro_id, capitulo_num)
		cache.set(cache_key, lista)
	else:
		print 'Obtido do cache: ' + cache_key

	return HttpResponse(simplejson.dumps(lista), mimetype="application/x-javascript")
	

def busca_textos_capitulo(request):
	"""
	Retorna os textos de um determinado capítulo.
	"""
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Capítulo
	# Busca lista no cache
	cache_key = 'textos-do-capitulo-' + capitulo_num + '-do-livro-' + livro_id
	textos = cache.get(cache_key)
	if textos is None:
		textos = Texto.objects.filter(livro__id = livro_id).filter(capitulo = capitulo_num)
		cache.set(cache_key, textos)
	else:
		print 'Obtido do cache: ' + cache_key
			
	txt = ''
	if textos:
		for t in textos:
			txt = txt + '<p class="texto"><span class="num_versiculo">' + str(t.capitulo) + ':' + str(t.versiculo) + '</span>\n' + t.texto + '</p>'
	return HttpResponse(txt)
	

def busca_texto_versiculo(request):
	"""
	Retorna o texto de um determinado versículo.
	"""
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Capítulo
	verso_num = request.GET['v'] # Versículo
	# Busca lista no cache
	cache_key = 'texto-do-versiculo-' + verso_num + '-do-capitulo-' + capitulo_num + '-do-livro-' + livro_id
	textos = cache.get(cache_key)
	if textos is None:
		textos = Texto.objects.filter(livro__id = livro_id).filter(capitulo = capitulo_num).filter(versiculo = verso_num)
		cache.set(cache_key, textos)
	else:
		print 'Obtido do cache: ' + cache_key

	txt = ''
	if textos:
		for t in textos:
			txt = txt + '<p class="texto"><span class="num_versiculo">' + str(t.capitulo) + ':' + str(t.versiculo) + '</span>\n' + t.texto + '</p>'
	return HttpResponse(txt)