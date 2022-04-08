// fixes "remote modal shows same content every time"
$('.modal').on('hidden', function() {
  $(this).removeData('modal');
});

$(function() {
  // Apply flask-kunden form styles after the modal is loaded
  window.faForm.applyGlobalStyles(document);
});
