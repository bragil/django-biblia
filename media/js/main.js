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
								//data = eval(data);
								//list = eval('[' + data + ']');
								var option = new Array();
								$("#livro_id").val(ui.item.id);
								
								resetaCombo('capitulo');
								$("select[name='capitulo']").attr("disabled", false);
								$.each(data, function(i, obj) {
									option[i] = document.createElement('option');//criando o option
									$( option[i] ).attr( {value : obj} );//colocando o value no option
									$( option[i] ).append( obj );//colocando o 'label'
			 
									$("select[name='capitulo']").append( option[i] );//jogando um � um os options no pr�ximo combo
								});
							});
				}
			});
	
	$("#capitulo").change( function() {
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
	});
});