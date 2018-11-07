document.ready (function () {
  $('#like_video').bind('click', function () {
    var rating = $('#rating').text
    var video_id = $('#rating').name
    function funcBeforeSend () {
      $(rating).hide();
    }
    function funcSuccess (data) {
      $(rating).text (data);
    }
    $.ajax ({
      // URL, по которому мы отправляем данные
      url: '/ajax/like_video_ajax/',
      // Метод отправки данных
      type: 'POST',
      // Передаваемые данные
      data: {'video_id': video_id, 'rating': rating,},
      // Тип передаваемых данных
      dataType: 'text',
      // Что отправлять пользователю до подгрузки страницы
      beforeSend: funcBeforeSend,
      // Выполняется по выполнению запроса
      success: funcSuccess
    });
  });
});
