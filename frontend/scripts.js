const dialog = document.querySelector('.book-dialog');
const form = document.querySelector('.book-dialog__form');
const closeButton = document.querySelector('.book-dialog__form-close-button');
const sendButton = document.querySelector('.book-dialog__form-send-button');

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

        console.log(data.message || 'Данные отправлены!');
        return data;

    } catch (error) {
        console.error('Ошибка:', error);
        console.log(`Не удалось отправить: ${error.message}`);
    }
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    await sendData('', formData);
});
