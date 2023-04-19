$(document).ready(function() {

  $("#contact form").submit(function(event){
    event.preventDefault();
    
    $.ajax({
      type:'POST',
      url: event.currentTarget.action,
      dataType: "json",
      data: $("#contact form").serialize(),
      
       success: function(data) {
        if  (data.result == 'success')
        {
            document.getElementById("contactForm").reset();
            $('#ajaxMessage').append('<div class="alert alert-success">' + data.message + '</div>')
        }
      }
    });
  });
});