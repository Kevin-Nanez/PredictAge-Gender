document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('video');
    const captureButton = document.getElementById('captureButton');
    const descriptionText = document.getElementById('descriptionText');

    // Solicitar acceso a la cámara del usuario
    async function startVideo() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
        } catch (error) {
            console.error('Error al acceder a la cámara: ', error);
            descriptionText.innerText = 'No se pudo acceder a la cámara.';
        }
    }

    // Manejar la captura de la imagen
    captureButton.addEventListener('click', () => {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Aquí puedes enviar la imagen a tu modelo de clasificación
        // y actualizar el texto de la descripción con el resultado
        // Por ejemplo:
        const exampleDescription = "Descripción de ejemplo";
        descriptionText.innerText = exampleDescription;
    });

    // Iniciar el video cuando la página se carga
    startVideo();
});
