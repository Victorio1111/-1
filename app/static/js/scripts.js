document.addEventListener("DOMContentLoaded", function() {
    // Сопоставление ID <datalist> с их маршрутами
    const endpoints = {
        companies: "/get_companies",
        bean_origins: "/get_bean_origins",
        company_locations: "/get_company_locations",
        bean_types: "/get_bean_types",
        broad_bean_origins: "/get_broad_bean_origins"
    };

    // Проходим по каждому элементу
    for (const [datalistId, endpoint] of Object.entries(endpoints)) {
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                const datalist = document.getElementById(datalistId);

                if (datalist) {
                    data.forEach(item => {
                        const option = document.createElement("option");
                        option.value = item.name; // В базе всегда колонка 'name'
                        datalist.appendChild(option);
                    });
                } else {
                    console.warn(`Datalist с id='${datalistId}' не найден.`);
                }
            })
            .catch(error => {
                console.error(`Ошибка при загрузке данных для '${datalistId}':`, error);
            });
    }
});
