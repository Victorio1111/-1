// Возвращение результата предсказания модели 
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

// Загрузка информации о выбранной модели, выпадающий список 
document.addEventListener("DOMContentLoaded", () => {
    fetch("/get_models")
      .then(res => res.json())
      .then(models => {
        const select = document.getElementById("model-select");
        const infoName = document.getElementById("model-name");
        const infoDesc = document.getElementById("model-description");
        const infoMetrics = document.getElementById("model-metrics");
  
        models.forEach(model => {
          const option = document.createElement("option");
          option.value = model.id;
          option.textContent = model.name;
          select.appendChild(option);
        });
  
        function updateInfo(modelId) {
          const model = models.find(m => m.id === modelId);
          if (!model) return;
          infoName.textContent = model.name;
          infoDesc.textContent = model.description;
  
          infoMetrics.innerHTML = "";
          for (const [metric, value] of Object.entries(model.metrics)) {
            const li = document.createElement("li");
            li.textContent = `${metric}: ${value}`;
            infoMetrics.appendChild(li);
          }
        }
  
        // обновление при выборе
        select.addEventListener("change", e => {
          updateInfo(e.target.value);
        });
  
        // инициализация по умолчанию
        if (models.length > 0) {
          select.value = models[0].id;
          updateInfo(models[0].id);
        }
      });
  });
  
