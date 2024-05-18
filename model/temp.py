
import tensorflowjs as tfjs

# Convertir el modelo a TensorFlow.js
output_dir = r'C:\Users\Kevin\OneDrive\Escritorio\Dataset\face_age'
model = r'C:\Users\Kevin\OneDrive\Escritorio\Seminario De sistemas\model\Edades.keras'

tfjs.converters.save_keras_model(model, output_dir)