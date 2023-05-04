$(function () {
  $('INPUT#btn_translate').click(function () {
    $.getJSON(
      'https://hellosalut.stefanbohacek.dev/?lang=' +
				$('INPUT#language_code').val(),
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });

  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.which === 13) {
        $.getJSON(
          'https://hellosalut.stefanbohacek.dev/?lang=' + $(this).val(),
          function (data) {
            $('DIV#hello').text(data.hello);
          }
        );
      }
      $(this).focusout();
    });
  });
});
