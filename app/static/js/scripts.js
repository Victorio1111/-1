// Ждем полной загрузки HTML-страницы
document.addEventListener("DOMContentLoaded", function() {

    // Вызываем функцию для загрузки компаний в выпадающий список
    fetch("/get_companies")
        .then(response => response.json()) // Преобразуем ответ сервера в формат JSON
        .then(data => {
            // Находим элемент на странице по его id
            const companySelect = document.getElementById("company-select");

            // Проходимся по каждой компании в полученных данных
            data.forEach(company => {
                // Создаем новый элемент <option> для выпадающего списка
                const option = document.createElement("option");

                // Значение и текст внутри опции будет названием компании
                option.value = company.name;
                option.textContent = company.name;

                // Добавляем опцию в выпадающий список
                companySelect.appendChild(option);
            });
        })
        .catch(error => {
            // Если при загрузке данных произошла ошибка — выводим её в консоль
            console.error('Ошибка при загрузке компаний:', error);
        });
});
