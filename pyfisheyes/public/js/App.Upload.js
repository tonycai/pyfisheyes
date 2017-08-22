App = window.App || {};

App.Upload = (function() {
    var setupForm = function() {
    	
        $("#upload").html("");
        $("#upload").fileUpload({
        	action:'/events/upload',
            submit_label: "upload",
            max_size_error_label: "The file size is too large !",
            success: function() {
        		$('iframe').each(function(index) {
                	$('#ftextile').val($('#ftextile').val() + '\n!' + $(this).contents().find("body").text() + '!\n');
                	$('#flash').text("success");
                  });
                setupForm();
            },
            error: function() {
                $('#flash').text("error");
                setupForm();
            },
            submit_empty_forms: false
        });
    };
    return {
        init: function() {
            setupForm();
            
        }
    };
})();
