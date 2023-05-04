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
});
