$(document).ready (function () {
  var rating = $('#video-u-info-rating');
  $('#like-video').bind('click', function () {
    var video_id = this.name;
    $.ajax ({
      type: 'GET',
      url: '/ajax/like_video/',
      data: {'video_id': video_id, },
      dataType: 'text',
      catch: false,
      success: function (data) {
        rating.html (data);
      }
    });
  });
  $('#dislike-video').bind('click', function () {
    var video_id = this.name;
    $.ajax ({
      type: 'GET',
      url: '/ajax/dislike_video/',
      data: {'video_id': video_id, },
      dataType: 'text',
      catch: false,
      success: function (data) {
        rating.html (data);
      }
    });
  });
  $('#leave-comment').bind('submit', function () {
    var video_id = this.name;
    $.ajax ({
      type: 'POST',
      url: '/ajax/leave_comment/',
      data: {'video_id': video_id, 'text': text, },
      dataType: 'text',
      catch: false,
      success: function (data) {
        $(document).append(data);
      }
    });
  });
});
