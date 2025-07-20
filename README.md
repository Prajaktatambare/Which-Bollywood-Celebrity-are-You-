**Which Bollywood celebrity are you ?**

**PROJECT DESCRIPTION** 

This project leverages pre-trained deep learning models and facial recognition techniques to extract features from an uploaded image and compare them against a database of Bollywood celebrities. The goal is to find the closest match and display the name and image of the predicted celebrity.

To run this project successfully, make sure you have the following Python packages installed.
⦁	!pip install mtcnn==0.1.0 

⦁	!pip install tensorflow==2.3.1

⦁	!pip install keras==2.4.3

⦁	!pip install keras-vggface==0.6

⦁	!pip install keras_applications==1.0.8

To run the project, open your terminal or command prompt, navigate to the project directory, and execute the following command:
**streamlit run app.py**

**FEATURES**

⦁	Upload your image and find out which Bollywood celebrity you look like
⦁	Uses VGGFace for feature extraction
⦁	Compares your facial features with a curated dataset of Bollywood celebrity images
⦁	Fun, interactive UI built using Streamlit

**TECHNOLOGY USED**

⦁	Python
⦁	TensorFlow / Keras
⦁	OpenCV
⦁	Keras VGGFace
⦁	Streamlit
⦁	NumPy, Pandas
⦁	Pickle (for saving precomputed embeddings)


**PROJECT STRUCTURE**

📁 bollywood-celebrity-predictor

⦁	Data/                   # Contains subfolders of celebrity images
⦁	embeddings/             # Stores precomputed facial embeddings
⦁	app.py                  # Streamlit application file
⦁	feature_extractor.py    # Script to extract features from images
⦁	test.py                 # Test script to validate predictions
⦁	filenames.pkl           # Pickled list of image file paths
⦁	embeddings.pkl          # Pickled array of face embeddings
⦁	requirements.txt        # Python dependencies


**How It Works**

⦁	Upload your image through the app.
⦁	The app detects your face and extracts features using the VGGFace model.
⦁	It then compares your facial features with those of Bollywood celebrities using cosine similarity.
⦁	The closest match is shown along with the celebrity’s name and image.
