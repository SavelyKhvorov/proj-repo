<script>
  // Получаем все элементы с классом event-card__link
  var cardLinks = document.querySelectorAll('.event-card__link');

  // Добавляем обработчик событий для каждой карточки
  cardLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
      // Получаем значение атрибута href текущего элемента
      var href = event.currentTarget.getAttribute('href');
      // Переходим на страницу, указанную в атрибуте href
      window.location.href = href;
    })
  });
</script>