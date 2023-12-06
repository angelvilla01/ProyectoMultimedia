$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(this);
        var url_1 = $('#urlField').val();

        $.ajax({
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener("progress", function(evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = evt.loaded / evt.total;
                        percentComplete = parseInt(percentComplete * 100);
                        $('#progressBar').css('width', percentComplete + '%');
                        $('#progressBar').attr('aria-valuenow', percentComplete);
                    }
                }, false);
                return xhr;
            },
            type: 'POST',
            url: url_1,
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                $('#progressBar').css('width', '100%');
                
                $('#downloadButton').show().click(function() {
                    window.location.href = response.fileUrl;
                });
                
                $('#downloadButton')
                    .show()
                    .prop('disabled', false)
                    .click(function() {
                        window.location.href = response.fileUrl;

                        //Tienes 15 segundos para la descarga y luego hacemos reset
                        setTimeout(function() {
                            $('#progressBar').css('width', '0%').attr('aria-valuenow', 0);
                            $('#downloadButton').prop('disabled', true);
                            $('#fileInput').val("");
                            document.getElementById('dropzone').innerHTML = "<b>Arrastra el fichero o haz click aquí</b>";
                        }, 15000);
                    });
            }
        });
    });
});