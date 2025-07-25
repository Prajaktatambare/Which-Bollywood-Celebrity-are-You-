# load image face detections and extract its feature
# find the cosine distance of current image with all the 8655 features
# recommend that image
from operator import index

from PIL.JpegPresets import presets
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import cv2
from mtcnn import MTCNN
from PIL import Image
from tensorflow.python.distribute.model_combinations import simple_subclass_model
from tensorflow.python.ops.ragged.ragged_array_ops import expand_dims

feature_list =np.array(pickle.load(open('embedding.pkl','rb')))
filenames = pickle.load(open('filenames.pkl','rb'))

model = VGGFace(model='resnet50',include_top=False,input_shape=(224,224,3),pooling='avg')

detector =MTCNN()

# load img ---> face detection
sample_img =cv2.imread('sample/images (2).jpg')
results = detector.detect_faces(sample_img)

x,y,width,height = results[0]['box']

face = sample_img[y:y+height , x:x+width]

# extract its feature

image = Image.fromarray(face)
image = image.resize((224,224))

face_array = np.asarray(image)

face_array = face_array.astype('float32')

expanded_img = np.expand_dims(face_array, axis=0)
preprocessed_img = preprocess_input(expanded_img)
result = model.predict(preprocessed_img).flatten()

# print(result)
# print(result.shape)

# Find the cosine distance of current image with all the 8655 feature

similarity = []
for i in range(len(feature_list)):
    similarity.append(cosine_similarity(result.reshape(1,-1), feature_list[i].reshape(1,-1))[0][0])

index_pos = sorted(list(enumerate(similarity)),reverse=True,key =lambda  x:x[1])[0][0]

temp_img = cv2.imread(filenames[index_pos])
cv2.imshow('output' , temp_img)
cv2. waitKey(0)
