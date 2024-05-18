import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Definir parámetros
batch_size = 512
epochs = 10
image_height = 200
image_width = 200

# Directorio de los datos
train_dir = r'C:\Users\Kevin\OneDrive\Escritorio\Dataset\face_age'

# Preprocesamiento de datos y aumento de datos
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Generador de datos de entrenamiento
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(image_height, image_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# Generador de datos de validación
validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(image_height, image_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Construir el modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_height, image_width, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(512, activation='relu'),
    layers.Dense(68, activation='softmax') 
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
try:
    history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator,
    verbose=2  # Mostrar progreso de cada época
    )
except UnicodeEncodeError:
    pass  # Maneja el error de alguna otra manera

# Obtener el mapeo de índices a nombres de clases
class_indices = train_generator.class_indices

# Invertir el mapeo para obtener el mapeo de nombres de clases a etiquetas
label_mapping = {v: k for k, v in class_indices.items()}

# Imprimir el mapeo de nombres de clases a etiquetas
print(label_mapping)

# Guardar el modelo entrenado
model.save('modelo_de_reconocimiento_de_edad.keras')