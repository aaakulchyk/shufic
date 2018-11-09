$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


$(document).ready (function () {
  var rating = $('#video-rating');
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
  $('#leave-comment').on('submit', function (event) {
    event.preventDefault();
    console.log('Form submitted!'); // sanity check
    var video_id = this.name;
    $.ajax ({
      type: 'POST',
      url: '/ajax/leave_comment/',
      data: {video_id: video_id, text: $('#commentform-text').val(), },
      dataType: 'html',
      catch: false,
      success: function (json) {
        $('#commentform-text').val('') // remove the value from the input
        console.log(json);
        var newComment = '<li class="video-u-comments-list-item"><div class="row video-u-comment"><div class="col-1 video-u-comment-rating"><a class="btn oi oi-chevron-top" aria-hidden="true"></a><p class="video-u-comment-rating-value text-center">' + json.rating + '</p><a class="btn oi oi-chevron-bottom" aria-hidden="true"></a></div><div class="col-8 video-u-comment-content"><div class="video-u-comment-date"><span class="video-u-comment-date">' + '</span></div><div class="video-u-comment-text"><p class="video-u-comment-text">' + json.text + '</p></div></div></div></li>';
        $('#video-comments').append(newComment);
      }
    });
  });
});
