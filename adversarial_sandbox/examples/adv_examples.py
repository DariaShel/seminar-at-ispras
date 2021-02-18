import tensorflow as tf
from PIL import Image, ImageDraw 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

pretrained_model = tf.keras.applications.ResNet50()
pretrained_model.trainable = False

decode_predictions = tf.keras.applications.resnet50.decode_predictions

def preprocess(image):
    #redo using PIL
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = image[None, ...]
    return image

def get_imagenet_label(probs):
    return decode_predictions(probs, top=1)[0][0]

image = Image.open('cat.jpg')
image = preprocess(image)
image_probs = pretrained_model.predict(image)

loss_object = tf.keras.losses.CategoricalCrossentropy()

def create_adversarial_pattern(input_image, input_label):
    with tf.GradientTape() as tape:
        tape.watch(input_image)
        prediction = pretrained_model(input_image)
        loss = loss_object(input_label, prediction)
    gradient = tape.gradient(loss, input_image)
    signed_grad = tf.sign(gradient)
    return signed_grad

index = 208
label = tf.one_hot(index, image_probs.shape[-1])
label = tf.reshape(label, (1, image_probs.shape[-1]))

perturbations = create_adversarial_pattern(image, label)

adv_x = image + 0.1 * perturbations
adv_x = tf.clip_by_value(adv_x, -1, 1)

plt.imshow(adv_x)
plt.show()