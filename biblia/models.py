# -*- coding: utf-8 -*-
from django.db import models

class Testamento(models.Model):
	"""
	Representa o antigo e o novo testamento.
	"""
	id = models.AutoField(primary_key=True, db_column='cd_testamento')
	testamento = models.CharField(max_length=50, null=False, db_column='ds_testamento')
	
	def __unicode__(self):
		return self.testamento
		
	class Meta:
		ordering = ['id']
		db_table = 'tb_testamentos'

class Livro(models.Model):
	id = models.AutoField(primary_key=True,db_column='cd_livro')
	testamento = models.ForeignKey(Testamento, null=False, db_column='cd_testamento', db_index=True)
	livro = models.CharField(max_length=100, null=False, db_column='ds_livro')
	
	def __unicode__(self):
		return self.livro
		
	class Meta:
		ordering = ['testamento', 'id']
		db_table = 'tb_livros'

class Texto(models.Model):
	"""
	Os textos bíblicos (versículos)
	"""
	id = models.AutoField(primary_key=True,db_column='cd_texto')
	livro = models.ForeignKey(Livro, null=False, db_column='cd_livro', db_index=True)
	capitulo = models.IntegerField(null=False, db_column='cd_capitulo', db_index=True)
	versiculo = models.IntegerField(null=False, db_column='cd_versiculo', db_index=True)
	texto = models.TextField(null=False, db_column='ds_texto')
	
	def __unicode__(self):
		return self.texto
		
	class Meta:
		ordering = ['livro', 'capitulo', 'versiculo']
		db_table = 'tb_textos'