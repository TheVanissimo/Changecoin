const output = document.getElementById('output'); // Элемент для отображения данных

fetch('http://127.0.0.1:8000/', {
    mode: 'no-cors',
})
// Ваш URL API
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json(); // Преобразование ответа в JSON
    })
    .then(data => {
        // Отобразим данные на странице
        output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => {
        // Отобразим ошибку на странице
        output.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
        console.error('There was a problem with the fetch operation:', error);
    });
