$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(this);
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
            url: '/compresor_video',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                // Acciones a realizar cuando la carga y procesamiento estén completos
                $('#progressBar').css('width', '100%').delay(500).fadeOut();
                
                $('#downloadButton').show().click(function() {
                    window.location.href = response.fileUrl;
                });
            }
        });
    });
});