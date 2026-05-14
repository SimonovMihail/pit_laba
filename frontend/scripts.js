const dialog = document.querySelector('.book-dialog');
const form = document.querySelector('.book-dialog__form');
const closeButton = document.querySelector('.book-dialog__form-close-button');

closeButton.addEventListener('onclick', (event) => {
    event.preventDefault();
    form.reset();
    dialog.close();
});

dialog.addEventListener('close', () => {
    form.reset();
});


async function sendData(endpoint, formData) {
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || `Ошибка сервера: ${response.status}`);
        }

        alert(data.message);
        form.reset();
        dialog.close();

    } catch (error) {
        alert('Ошибка: ' + error.message);
    }
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(form);

    const endpoint = 'http://localhost:8000/api/v1/public_order/';

    await sendData(endpoint, formData);
});