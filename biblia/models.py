# -*- coding: utf-8 -*-
from django.db import models, connection

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
		
	def get_capitulos(self, livro_id):
		cursor = connection.cursor()
		cursor.execute("SELECT DISTINCT cd_capitulo FROM tb_textos WHERE cd_livro = %s ORDER BY cd_capitulo", [livro_id])
		rows = cursor.fetchall()
		lista = []
		if rows:
			for r in rows:
				lista.append(r[0])
		return lista
		
	def get_versiculos(self, livro_id, capitulo_num):
		cursor = connection.cursor()
		cursor.execute("SELECT cd_versiculo FROM tb_textos WHERE cd_livro = %s AND cd_capitulo = %s ORDER BY cd_versiculo", [livro_id, capitulo_num])
		rows = cursor.fetchall()
		lista = []
		if rows:
			for r in rows:
				lista.append(r[0])
		return lista
		
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