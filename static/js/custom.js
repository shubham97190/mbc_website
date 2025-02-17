jQuery(document).ready(function($) {

    $('#myTab li a').on('click',function(event) {

        event.preventDefault();
        var href_id = $(this).attr('href');        
        var image_height = $('#myTabContent').find(href_id).find('img').parent();
        console.log(image_height.innerHeight(true));
    });

});