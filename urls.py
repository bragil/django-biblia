from django.conf import settings
from django.conf.urls.defaults import *
from django_biblia import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^statics/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^$', 'django_biblia.biblia.views.index'),
	(r'^livros/$', 'django_biblia.biblia.views.busca_livro'),
	(r'^get_capitulos/$', 'django_biblia.biblia.views.busca_capitulos'),
	(r'^get_versiculos/$', 'django_biblia.biblia.views.busca_versiculos'),
	(r'^get_textos_capitulo/$', 'django_biblia.biblia.views.busca_textos_capitulo'),
	(r'^get_texto_versiculo/$', 'django_biblia.biblia.views.busca_texto_versiculo'),
	# Example:
	# (r'^django_biblia/', include('django_biblia.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
