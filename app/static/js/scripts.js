document.addEventListener("DOMContentLoaded", function() {
    fetch("/get_companies")
    .then(response => response.json())
    .then(data => {
        const datalist = document.getElementById("companies");

        data.forEach(company => {
            const option = document.createElement("option");
            option.value = company.name;
            datalist.appendChild(option);
        });
    })
    .catch(error => {
        console.error('Ошибка при загрузке компаний:', error);
    });
});
