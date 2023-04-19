$(document).ready(function() {

  $("#contact form").submit(function(event){
    event.preventDefault();
    
    $.ajax({
      type:'POST',
      url: event.currentTarget.action,
      dataType: "json",
      data: $("#contact form").serialize(),
      
       success: function(response) {
       document.getElementById("contactForm").reset();
        
       $('#ajaxMessage').append('<div class="alert alert-success">' + response.message + '</div>')
      },
       error: function(response) {
         $('#ajaxMessage').append('<div class="alert alert-error">' + response.message + '</div>')
       }
      
    });
  });
});