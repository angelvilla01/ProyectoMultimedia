// Evitar comportamiento por defecto al arrastrar sobre el dropzone
document.getElementById('dropzone').addEventListener('dragover', function(e) {
    e.preventDefault();
    e.stopPropagation();
});

// Evitar comportamiento por defecto al soltar en el dropzone
document.getElementById('dropzone').addEventListener('drop', function(e) {
    e.preventDefault();
    e.stopPropagation();

    let file = e.dataTransfer.files[0];
    if (file) {
        document.getElementById('fileInput').files = e.dataTransfer.files;
        document.getElementById('dropzone').innerHTML = "Archivo seleccionado: " + "<b>"+ file.name + "</b>";
        $('#submitBtn').prop('disabled', false);
    }
});

// Evento al hacer clic en el contenedor de arrastrar y soltar
document.getElementById('dropzone').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

// Evento al seleccionar un archivo usando el input de archivos
document.getElementById('fileInput').addEventListener('change', function() {
    if (this.files.length > 0) {
        document.getElementById('dropzone').innerHTML = "Archivo seleccionado: " + "<b>" + this.files[0].name + "</b>";
        $('#submitBtn').prop('disabled', false);
    }
});