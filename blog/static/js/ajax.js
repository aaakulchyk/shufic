$('#like_video').on('click', function() {
  console.log(this.val());
  var href = $(this).href();
  $.ajax({
    url: btn.attr('/ajax/like_video/'),
    data: {
      'action': href
    },
    dataType: 'json',
    success: function(data) {
      if(data.is_taken) {
        console.log('Like is already made.');
      }
    }
  });
});
