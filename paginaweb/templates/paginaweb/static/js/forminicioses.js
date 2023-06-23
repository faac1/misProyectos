function validar() {
    var nombre = document.getElementById("nombre").value;
    var tipo_registro = document.getElementById("tipo_registro").value;
    var registro = document.getElementById("registro").value;
    var password = document.getElementById("password").value;
    var confirmar_password = document.getElementById("confirmar_password").value;
  
    if (nombre === "" || tipo_registro === "" || registro === "" || password === "" || confirmar_password === "") {
      alert("Por favor, rellena todos los campos.");
      return false;
    }
  
    if (tipo_registro === "email") {
        // Expresión regular para validar el campo de correo electrónico
        var email = /^[\w-\.]+@(duocuc|profesor.duoc|gmail|yahoo)\.(com|cl)$/;
        if (!email.test(registro)) {
            alert("Por favor, introduce un correo electrónico válido (duocuc, yahoo, gmail o profesor.duoc, terminado en .com o .cl).");
            return false;
        }
    } else if (tipo_registro === "rut") {
        // Expresión regular para validar el campo de RUT
        var rut = /^[0-9]{7,8}-([0-9]{1}|[k]{1})$/;
        if (!rut.test(registro)) {
            alert("Por favor, introduce un RUT válido (formato: 12345678-9 o k).");
            return false;
        }
    }
  
    if (password !== confirmar_password) {
      alert("Las contraseñas no coinciden. Por favor, vuelve a escribirlas.");
      return false;
    }
  
    if (nombre !== "" || tipo_registro !== "" || registro !== "" || password !== "" || confirmar_password !== "") {
        alert("todo correcto.");
        window.location.href = "index2"
    }
    return false;
}
  

function validar1() {
    var tipo_registro = document.getElementById("tipo_registro").value;
    var registro = document.getElementById("registro").value;
    var password = document.getElementById("password").value;
  
    if (tipo_registro === "" || registro === "" || password === "" ) {
      alert("Por favor, rellena todos los campos.");
      return false;
    }
  
    if (tipo_registro === "email") {
        // Expresión regular para validar el campo de correo electrónico
        var email = /^[\w-\.]+@(duocuc|profesor.duoc|gmail|yahoo)\.(com|cl)$/;
        if (!email.test(registro)) {
            alert("Por favor, introduce un correo electrónico válido (duocuc, yahoo, gmail o profesor.duoc, terminado en .com o .cl).");
            return false;
        }
    } else if (tipo_registro === "rut") {
        // Expresión regular para validar el campo de RUT
        var rut = /^[0-9]{7,8}-([0-9]{1}|[k]{1})$/;
        if (!rut.test(registro)) {
            alert("Por favor, introduce un RUT válido (formato: 12345678-9 o k).");
            return false;
        }
    }

  
    if (tipo_registro !== "" || registro !== "" || password !== "") {
        alert("todo correcto.");
         window.location.href = "index2"
    }
    return false;
}
  

  //subir 
$("#formulario_subir").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 2,
            maxlength: 30
        },
        tipo_solicitud: {
            required: true
        },
        mensaje: {
            required: true,
            minlength: 10,
            maxlength: 1000
        },
        fecha: {
            required: true,
            date: true
        },
        telefono: {
            required: true,
            number: true
        },
        categorias: {
            required: true,
            minlength:1,
            maxlength:5
            
        },
        seleccionar: {
            required: true
            
        }
    },
    messages: {
        nombre: {
            required: "Por favor, escribe tu nombre.",
            minlength: "El nombre debe tener al menos 2 caracteres y maximo 30."
        },
        tipo_solicitud: {
            required: "Por favor, selecciona una opción."
        },
        mensaje: {
            required: "Por favor, escribe un mensaje.",
            minlength: "El mensaje debe tener al menos 10 caracteres."
        },
        fecha: {
            required: "Por favor, selecciona una fecha.",
            date: "Por favor, introduce una fecha válida."
        },
        telefono: {
            required: "Por favor, escribe un número de teléfono.",
            number: "Por favor, introduce un número válido."
        },
        categorias: {
            required: "Por favor, selecciona al menos una categoría."
        },
        seleccionar: {
            required: "Por favor, selecciona una opción."
        }
    }
})


$("#enviar").click(function(){
  if($("#formulario_subir").valid()){
    alert("mensaje enviado");
    window.location.href = "index2"
}

})


$("#actualizar").click(function(){
  if($("#formulario_subir").valid()){
    alert("mensaje actualizado");
    window.location.href = "index2"
}

})
