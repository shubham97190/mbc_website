jQuery(document).ready(function($) {
    $('#myTab li a').on('click',function(event) {
        event.preventDefault();
        var href_id = $(this).attr('href');        
        var image_height = $('#myTabContent').find(href_id).find('img').parent();
        console.log(image_height.innerHeight(true));
    });
});

function fetchDetails($event){
  fetch('tournament_details', '/tournament-details/', $event.value)
}

function fetchTnc(){
  var value = $('#id_tournament').find(":selected").val()
  if(value != '' && value != undefined){
    fetch('tournament_term_condition_content', '/tournament-tnc/', value)
     $('#tournament_term_condition').on('hidden.bs.modal', function (e) {
          $('#tournament_term_condition_content').html('')
     })
  }else{
    console.log("$('#tournament_term_condition')", $('#tournament_term_condition'))
    $('#tournament_term_condition').modal('hide')
  }
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