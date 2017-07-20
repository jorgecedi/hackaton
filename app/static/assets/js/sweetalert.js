(function ($) {
	
	$('body').on('click', '.borrar_noticia', function () {
		swal({ 
			title: "Esta seguro de borrar la noticia?", 
			text: "No podra recuperarla una vez borrada", 
			type: "warning", 
			showCancelButton: true, 
			confirmButtonColor: "#039BE5", 
			confirmButtonText: "Si, borrarla", 
			cancelButtonText: "No, cancelar por favor!", 
			closeOnConfirm: false, 
			closeOnCancel: false 
		}, function (isConfirm) {
			if (isConfirm) { 
				swal({
					title: "Eliminada!", 
					text: "Su accion ha sido llevada a cabo.", 
					type:"success", 
					confirmButtonColor: "#039BE5"
				});
			} 
			else {
				swal({ 
					title: "Cancelado", 
					text: "Se ha cancelado la accion.", 
					type: "error", 
					confirmButtonColor: "#039BE5" 
				});
			} 
		});
	});



	$('body').on('click', '.borrar_usuario', function () {
		swal({ 
			title: "Esta seguro de borrar el usuario?", 
			text: "No podra recuperarla una vez borrada", 
			type: "warning", 
			showCancelButton: true, 
			confirmButtonColor: "#039BE5", 
			confirmButtonText: "Si, borrarla", 
			cancelButtonText: "No, cancelar por favor!", 
			closeOnConfirm: false, 
			closeOnCancel: false 
		}, function (isConfirm) {
			if (isConfirm) { 
				swal({
					title: "Eliminada!", 
					text: "Su accion ha sido llevada a cabo.", 
					type:"success", 
					confirmButtonColor: "#039BE5"
				});
			} 
			else {
				swal({ 
					title: "Cancelado", 
					text: "Se ha cancelado la accion.", 
					type: "error", 
					confirmButtonColor: "#039BE5" 
				});
			} 
		});
	});

	$('body').on('click', '.borrar_pedido', function () {
		swal({ 
			title: "Esta seguro de borrar el pedido?", 
			text: "No podra recuperarla una vez borrada", 
			type: "warning", 
			showCancelButton: true, 
			confirmButtonColor: "#039BE5", 
			confirmButtonText: "Si, borrarla", 
			cancelButtonText: "No, cancelar por favor!", 
			closeOnConfirm: false, 
			closeOnCancel: false 
		}, function (isConfirm) {
			if (isConfirm) { 
				swal({
					title: "Eliminada!", 
					text: "Su accion ha sido llevada a cabo.", 
					type:"success", 
					confirmButtonColor: "#039BE5"
				});
			} 
			else {
				swal({ 
					title: "Cancelado", 
					text: "Se ha cancelado la accion.", 
					type: "error", 
					confirmButtonColor: "#039BE5" 
				});
			} 
		});
	});

}(jQuery));