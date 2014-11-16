// Rotinas Javascript

function resetaCombo( el )
{
	$("select[name='"+el+"']").empty();//retira os elementos antigos
	var option = document.createElement('option');
	$( option ).attr( {value : '0'} );
	$( option ).append( '' );
	$("select[name='"+el+"']").append( option );
}

$(function() {
	$( "#livro_capitulo" ).autocomplete({
				// Busca os livros e seus respectivos cap�tulos
				source: "/livros/",
				minLength: 2,
				select: function( event, ui ) {
					//alert(ui.item.value);

					$.getJSON('/get_capitulos/',
							{l:ui.item.id},
							function(data) {
								var option = new Array();
								// Adiciona o ID do livro no campo hidden
								$("#livro_id").val(ui.item.id);

								resetaCombo('capitulo');
								$("select[name='capitulo']").attr("disabled", false);
								$.each(data, function(i, obj) {
									option[i] = document.createElement('option');//criando o option
									$( option[i] ).attr( {value : obj} );//colocando o value no option
									$( option[i] ).append( obj );//colocando o 'label'

									$("select[name='capitulo']").append( option[i] );//jogando um � um os options no pr�ximo combo
								});

								// Traz o texto dos vers�culos do cap�tulo 1 deste livro
								$.ajax({
								  url: '/get_textos_capitulo/?l=' + $("#livro_id").val() + '&c=1',
								  context: document.body,
								  success: function(data){
								    $("#conteudo").html(data);
								  }
								});
							});

				}
			});

	$("#capitulo").change( function() {
		// Preenche o combo de vers�culos
		$.getJSON('/get_versiculos/?l=' + $("#livro_id").val() + '&c=' + $("#capitulo").val(),
				function(data) {
					var option = new Array();

					resetaCombo('versiculo');
					$("select[name='versiculo']").attr("disabled", false);
					$.each(data, function(i, obj) {
						option[i] = document.createElement('option');//criando o option
						$( option[i] ).attr( {value : obj} );//colocando o value no option
						$( option[i] ).append( obj );//colocando o 'label'

						$("select[name='versiculo']").append( option[i] );//jogando um � um os options no pr�ximo combo
					});
				});
		// Traz os vers�culos deste livro e cap�tulo
		$.ajax({
		  url: '/get_textos_capitulo/?l=' + $("#livro_id").val() + '&c=' + $("#capitulo").val(),
		  context: document.body,
		  success: function(data){
		    $("#conteudo").html(data);
		  }
		});
	});

	// Traz o texto do vers�culo
	$("#versiculo").change( function() {
		$.ajax({
		  url: '/get_texto_versiculo/?l=' + $("#livro_id").val() + '&c=' + $("#capitulo").val() + '&v=' + $("#versiculo").val(),
		  context: document.body,
		  success: function(data){
		    $("#conteudo").html(data);
		  }
		});
	});
});