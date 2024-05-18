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

    // Función para preprocesar la imagen capturada
    function preprocessImage(imageData) {
        // Aquí puedes realizar cualquier preprocesamiento necesario en la imagen antes de enviarla al modelo
        return imageData;
    }

    // Manejar la captura de la imagen
    captureButton.addEventListener('click', async () => {
        console.log("Inicia con click")
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);

        // Obtener la imagen capturada en formato de píxeles
        const imageData = context.getImageData(0, 0, canvas.width, canvas.height);

        // Preprocesar la imagen
        const processedImage = preprocessImage(imageData);

        // Cargar el modelo desde una URL
        const model = await tf.loadLayersModel('../model/modelo_de_reconocimiento_de_edad.keras');

        // Realizar la predicción de edad
        const predictedAge = predictAge(model, processedImage);

        // Actualizar el texto de la descripción con la edad predicha
        descriptionText.innerText = `Edad predicha: ${predictedAge}`;
    });

    // Función para realizar la predicción de edad
    function predictAge(model, imageData) {
        // Convertir la imagen a un tensor
        const tensor = tf.browser.fromPixels(imageData)
            .resizeNearestNeighbor([200, 200]) // Ajustar el tamaño de la imagen según el modelo
            .toFloat()
            .expandDims();

        // Normalizar la imagen
        const normalizedTensor = tensor.div(tf.scalar(255));

        // Realizar la predicción con el modelo
        const prediction = model.predict(normalizedTensor);

        // Obtener la edad predicha (por ejemplo, la clase con la mayor probabilidad)
        // Este código puede variar dependiendo de cómo sea tu modelo
        const predictedAge = prediction.dataSync()[0]; // Suponiendo que la predicción es un solo valor de edad

        return predictedAge;
    }

    // Iniciar el video cuando la página se carga
    startVideo();
});
