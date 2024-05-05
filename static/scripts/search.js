document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы по умолчанию
  
    var query = document.getElementById('searchInput').value.trim().toLowerCase(); // Получаем поисковой запрос
    var eventCards = document.querySelectorAll('.recipe-card'); // Получаем все карточки событий
  
    eventCards.forEach(function(card) {
        var title = card.querySelector('.recipe-card__title').textContent.toLowerCase(); // Получаем текст названия события
        var description = card.querySelector('.recipe-card__description').textContent.toLowerCase(); // Получаем текст описания события
  
        // Проверяем, соответствует ли название или описание события поисковому запросу
        if (title.includes(query) || description.includes(query)) {
            card.style.display = 'block'; // Отображаем карточку, если соответствует запросу
        } else {
            card.style.display = 'none'; // Скрываем карточку, если не соответствует запросу
        }
    });
  });
