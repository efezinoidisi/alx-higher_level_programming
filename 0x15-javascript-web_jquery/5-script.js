$(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').html(function (index, prev) {
      return prev + '<li>Item</li>';
    });
  });
});
