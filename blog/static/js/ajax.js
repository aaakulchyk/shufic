$("document").ready (function () {
  $("#like_video").on("click", function () {
    var video_id = this.name;
    $.ajax ({
      type: "GET",
      url: "/ajax/like_video_ajax/",
      data: {"video_id": video_id, },
      dataType: "text",
      catch: false,
      success: function (data) {
        $("#rating").html (data);
      }
    });
  });
});
