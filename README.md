🖌️ AI Digit Recognizer

An interactive handwritten digit recognition system built using Keras (TensorFlow backend) and Tkinter GUI.
The model is trained on the MNIST dataset using a Convolutional Neural Network (CNN) and deployed as a simple desktop application where you can draw digits (0–9) and get instant predictions with confidence scores.

🚀 Features

✅ CNN-based classifier trained on MNIST dataset

✅ Tkinter GUI with a canvas to draw digits

✅ Displays predicted digit 🎯 and confidence percentage

✅ Buttons to recognize or clear drawings

✅ Color-coded confidence levels (green = high, orange = medium, red = low)

📂 Project Structure
📦 AI-Digit-Recognizer
 ┣ 📜 mnist.h5           # Trained CNN model (saved after training)
 ┣ 📜 train_model.py     # Script for training & saving the model
 ┣ 📜 gui_app.py         # Tkinter GUI for digit recognition
 ┣ 📜 README.md          # Project documentation

🧠 Model Architecture

The CNN is built using Keras Sequential API:

Conv2D (32 filters, 3x3, ReLU)

Conv2D (64 filters, 3x3, ReLU)

MaxPooling2D (2x2)

Dropout (25%)

Flatten

Dense (256, ReLU)

Dropout (50%)

Dense (10, Softmax)

Optimizer: Adam
Loss: Categorical Crossentropy
Metrics: Accuracy

📊 Training

Dataset: MNIST (60,000 training, 10,000 test samples)

Epochs: 12

Batch size: 128

Final Accuracy: ~99% on training, ~98% on test set

🖥️ GUI Preview

🎯 Main Window:

Canvas to draw your digit

Prediction box with confidence score

Buttons to recognize or clear

(Insert screenshot here if available, e.g., ![GUI Screenshot](screenshot.png))

⚡ Installation & Usage

Clone the repository

git clone https://github.com/your-username/AI-Digit-Recognizer.git
cd AI-Digit-Recognizer


Install dependencies

pip install tensorflow keras pillow numpy


Train the model (optional, model already provided)

python train_model.py


Run the GUI

python gui_app.py

🎯 Example

Draw a digit on the canvas

Click 🧠 RECOGNIZE

Get prediction & confidence score instantly

Confidence colors:

🟢 > 80% → High confidence

🟠 60–80% → Medium confidence

🔴 < 60% → Low confidence

📌 Requirements

Python 3.7+

TensorFlow / Keras

NumPy

Pillow

Tkinter (pre-installed with Python)

🏆 Future Improvements

Add CNN training visualization (accuracy/loss plots)

Save drawing history & predictions

Export predictions as JSON/CSV

Extend to A–Z handwritten character recognition

🤝 Contributing

Contributions are welcome! Please fork this repo, make changes, and submit a PR.
