jQuery(document).ready(function($) {
    $('#myTab li a').on('click',function(event) {
        event.preventDefault();
        var href_id = $(this).attr('href');        
        var image_height = $('#myTabContent').find(href_id).find('img').parent();
        console.log(image_height.innerHeight(true));
    });
    updatePhone();
});

function addImagePopup(count){
   $('#imagepreview').attr('src', $('#imageresource'+count).attr('src')); // here asign the image to the modal when the user click the enlarge link
   $('#imagemodal').modal('show'); // imagemodal is the id attribute assigned to the bootstrap modal, then i use the show function
}

function fetchDetails($event){
  var value = $event.value
  var link = $('div[name="tournament_term_condition"]');
  fetch('tournament_details', '/tournament-details/', value)
  if(value != '' && value != undefined){
    link.attr('id','tournament_term_condition');
  }else{
    link.attr('id','');
  }
}

//function fetchTnc(){
//  var value = $('#id_tournament').find(":selected").val()
//  if(value != '' && value != undefined){
//    fetch('tournament_term_condition_content', '/tournament-tnc/', value)
//     $('#tournament_term_condition').on('hidden.bs.modal', function (e) {
//          $('#tournament_term_condition_content').html('')
//     })
//  }
//}

function showData(id){
    $('#tnc_body').html($('#'+id).data('body'));
    $('#tnc_title').html($('#'+id).data('title'));
    $('#tournament_term_condition').on('hidden.bs.modal', function (e) {
         $('#tnc_body').html('')
         $('#tnc_title').html('')
    })
}

function fetch(element_id, api_url, value){
  var ref = $('#'+element_id)
  ref.html('');
  if(value !=''){
     axios
      .get(api_url+`${value}`+'/')
      .then(function (response) {
        if (response.status === 200) {
         ref.html(response.data);
        }
      })
      .catch((error) => {
         ref.html('');
         console.error(error);
      });
  }
}

function updatePhone(){
  const phoneInputField = document.querySelector("#id_mobile");
   const phoneInput = window.intlTelInput(phoneInputField, {'onlyCountries': ["CA"],
     utilsScript:
       "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
   });
 }

 function formatMobile(){
     var number =  $('input[id="id_mobile"]').val();
     var classf = $(".iti__selected-flag > div").attr("class");
     var flag = classf.slice(-2);
     var formattedNumber = intlTelInputUtils.formatNumber(number, flag, intlTelInputUtils.numberFormat.INTERNATIONAL);
     $('input[id="id_mobile"]').val(formattedNumber);
 }