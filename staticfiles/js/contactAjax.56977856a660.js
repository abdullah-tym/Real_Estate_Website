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
        
       $('#ajaxMessage').append('<div class="alert alert-success" role="alert">' + response.message + '</div>')
      },
       error: function() {
         $('#ajaxMessage').append('<div class="alert alert-danger" role="alert">' + 'Error! Enter the fields properly'
 + '</div>')
       }
      
    });
  });
});