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
        
       $('#show_message').addClass("alert alert-success").html('Thank you! We have received your message, we will contact you as soon as possible.');
      },
       error: function() {
         $('#ajaxMessage').addClass("alert alert-danger").html('Thank you! We have received your message, we will contact you as soon as possible.');
       }
      
    });
  });
});