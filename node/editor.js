$(document).ready(function() {
  socket = io();
  var file = window.location.search.substring(1) + ".py";

  $(".upload").on("click", function(event) {
      console.log(file.length)
      console.log(file)
      console.log($("textarea").val())
     socket.emit("uploadFile", file.length + file + $("textarea").val())
  });









  $(".findStrips").on("click", function() {
    socket.emit("findStrips", " ");
  });



  socket.on("stripInfo", function(data) {
    data = data.split(",");
    var found = false;
    $(".allStrips").children().each(function(index) {
      if ($(this).data("id") == data[0]) {
        found = true;
        $(this).text(data[1] + " " + data[2]);
      }
    });
    if (!found) {
      var div = $('<div class="strip">' + data[1] + ' ' + data[2] + '</div>');
      div.data("id", data[0]);
      $(".allStrips").prepend(div);
    }
  
    $(".strip").on("click", function() {
      var id = $(this).data("id");
      $(".currentStrip").data("id", id);
    });
  });


});