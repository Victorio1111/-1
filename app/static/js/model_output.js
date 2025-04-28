document.getElementById('predict-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Нужно оставить, чтобы form не делал обычный reload

    const formData = new FormData(this);

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result-block').innerText = 'Предсказанный рейтинг: ' + data.predicted_rating;
    })
    .catch(error => {
        console.error('Ошибка:', error);
        document.getElementById('result-block').innerText = 'Ошибка при отправке запроса.';
    });
});
