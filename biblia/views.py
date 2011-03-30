# -*- coding: utf-8 -*-
from django_biblia.biblia.models import *
from django.core import serializers
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

def index(request):
	textos = Texto.objects.filter(capitulo=1).filter(livro__id=1)
	return render_to_response('base.html', locals(), context_instance=RequestContext(request))
	
def busca_livro(request):
	busca = request.GET['term']
	livros = Livro.objects.filter(livro__istartswith=busca)
	res = []
	if livros:
		for l in livros:
			dict = {'id':l.id, 'label':l.__unicode__(), 'value':l.__unicode__()}
			res.append(dict)
			
	return HttpResponse(simplejson.dumps(res), mimetype="application/x-javascript")


def busca_capitulos(request):
	livro_id = request.GET['l']  # ID do Livro
	
	livro = Livro()
	lista = livro.get_capitulos(livro_id)
	return HttpResponse(simplejson.dumps(lista), mimetype="application/x-javascript")
	
def busca_versiculos(request):
	livro_id = request.GET['l']  # ID do Livro
	capitulo_num = request.GET['c'] # Cap�tulo
	
	livro = Livro()
	lista = livro.get_versiculos(livro_id, capitulo_num)
	return HttpResponse(simplejson.dumps(lista), mimetype="application/x-javascript")