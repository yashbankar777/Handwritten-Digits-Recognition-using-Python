# 🎯 MNIST Digit Recognizer

A deep learning project that trains a Convolutional Neural Network to recognize handwritten digits (0-9) using the MNIST dataset, complete with an interactive GUI for real-time digit recognition.

## 🚀 Features

- **CNN Model Training**: Built with Keras/TensorFlow for high accuracy digit recognition
- **Interactive GUI**: Draw digits with your mouse and get instant predictions
- **Real-time Recognition**: Live prediction with confidence scores
- **Modern UI Design**: Clean, user-friendly interface with visual feedback
- **High Accuracy**: Achieves excellent performance on the MNIST test set

## 📋 Prerequisites

```bash
pip install keras tensorflow numpy pillow tkinter
```

## 🏗️ Project Structure

The project consists of two main components:

### 1. Model Training (`MODEL` section)
- Loads and preprocesses the MNIST dataset
- Builds a CNN with Conv2D, MaxPooling, and Dropout layers
- Trains the model with Adam optimizer
- Saves the trained model as `mnist.h5`

### 2. GUI Application (`GUI` section)
- Interactive drawing canvas for digit input
- Real-time prediction display
- Confidence score visualization
- Clear and recognize functionality

## 🎮 How to Use

### Training the Model

1. Run the model training section to create `mnist.h5`:
```python
# The training code will automatically:
# - Download MNIST dataset
# - Preprocess the data
# - Train the CNN model
# - Save as 'mnist.h5'
```

### Running the GUI

1. Ensure `mnist.h5` exists in your project directory
2. Run the GUI section:
```python
# This will launch the interactive application
```

3. **Draw a digit** (0-9) on the white canvas
4. Click **🧠 RECOGNIZE** to get the prediction
5. Use **🗑️ CLEAR** to start over

## 🧠 Model Architecture

```
Sequential Model:
├── Conv2D(32, 3x3, ReLU)
├── Conv2D(64, 3x3, ReLU)
├── MaxPooling2D(2x2)
├── Dropout(0.25)
├── Flatten()
├── Dense(256, ReLU)
├── Dropout(0.5)
└── Dense(10, Softmax)
```

**Training Parameters:**
- Batch Size: 128
- Epochs: 12
- Optimizer: Adam
- Loss: Categorical Crossentropy

## 🎨 GUI Features

- **🎯 Smart Drawing**: 15px brush size optimized for digit recognition
- **🔮 Live Predictions**: Instant feedback with confidence percentages
- **🌈 Color-coded Confidence**: 
  - Green (>80%): High confidence
  - Orange (60-80%): Medium confidence  
  - Red (<60%): Low confidence
- **📱 Fixed Canvas**: 280x280 pixels, automatically resized to 28x28 for model input

## 📊 Performance

The model typically achieves:
- **Training Accuracy**: ~99%
- **Test Accuracy**: ~98%+
- **Real-time Inference**: Near-instantaneous predictions

## 🛠️ Technical Details

### Data Preprocessing
- Reshapes images to (28, 28, 1) format
- Normalizes pixel values to [0, 1] range
- Converts labels to categorical format

### Image Processing (GUI)
- Converts canvas drawings to grayscale
- Resizes to 28x28 pixels using LANCZOS resampling
- Inverts colors (white digits on black background for MNIST compatibility)
- Normalizes pixel values for model input

## 🔧 Customization

You can modify various parameters:

```python
# Model parameters
batch_size = 128    # Adjust batch size
epochs = 12         # Training epochs
learning_rate = 0.001  # Adam optimizer learning rate

# GUI parameters
canvas_size = 280   # Drawing canvas size
brush_width = 15    # Drawing brush thickness
```

## 📝 File Output

- `mnist.h5`: Trained model file (required for GUI)
- Training logs and accuracy metrics printed to console

## 🎯 Use Cases

- **Educational**: Learn CNN architectures and digit recognition
- **Prototyping**: Quick handwriting recognition demos
- **Research**: Baseline model for digit classification experiments
- **Interactive Learning**: Visual demonstration of deep learning concepts

## 🚨 Troubleshooting

**Model not found error**: Ensure you've run the training section first to generate `mnist.h5`

**Poor recognition accuracy**: Try drawing larger, centered digits with clear strokes

**GUI not responding**: Check that all dependencies are properly installed

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

---

⭐ **Star this repository if you found it helpful!**
