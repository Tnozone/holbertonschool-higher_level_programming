$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data) {
    $('DIV#hello').append(data.hello);
  });
});