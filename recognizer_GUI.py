from keras.models import load_model
from tkinter import *
import tkinter as tk
import numpy as np
from PIL import Image, ImageDraw

model = load_model('mnist.h5')

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("AI Digit Recognizer")
        self.geometry("500x400")
        self.configure(bg='#2C3E50')
        self.resizable(False, False)
        
        # Create internal image for proper processing
        self.image = Image.new("RGB", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        
        # Main frame
        main_frame = tk.Frame(self, bg='#2C3E50', padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        title = tk.Label(main_frame, text="🎯 Draw a Digit (0-9)", 
                        font=("Arial", 18, "bold"), fg='#ECF0F1', bg='#2C3E50')
        title.pack(pady=(0,20))
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg='#2C3E50')
        content_frame.pack()
        
        # Canvas frame
        canvas_frame = tk.Frame(content_frame, bg='#34495E', relief='raised', bd=3)
        canvas_frame.pack(side="left", padx=(0,20))
        
        # Canvas - FIXED SIZE
        self.canvas = tk.Canvas(canvas_frame, width=280, height=280, 
                               bg="white", cursor="cross")
        self.canvas.pack(padx=5, pady=5)
        
        # Right panel
        right_panel = tk.Frame(content_frame, bg='#2C3E50')
        right_panel.pack(side="left", fill="y")
        
        # Prediction frame
        pred_frame = tk.Frame(right_panel, bg='#34495E', relief='raised', bd=2)
        pred_frame.pack(pady=10, fill='x')
        
        pred_title = tk.Label(pred_frame, text="🔮 Prediction", 
                             font=("Arial", 12, "bold"), fg='#ECF0F1', bg='#34495E')
        pred_title.pack(pady=(10,5))
        
        self.label = tk.Label(pred_frame, text="Draw!", font=("Arial", 32, "bold"),
                             fg='#E74C3C', bg='#ECF0F1', padx=20, pady=15)
        self.label.pack(pady=10, padx=10)
        
        self.confidence_label = tk.Label(pred_frame, text="Confidence: ---%",
                                       font=("Arial", 10), fg='#BDC3C7', bg='#34495E')
        self.confidence_label.pack(pady=(0,10))
        
        # Buttons
        self.classify_btn = tk.Button(right_panel, text="🧠 RECOGNIZE", 
                                     command=self.classify_handwriting,
                                     font=("Arial", 10, "bold"), bg='#27AE60', fg='white',
                                     padx=15, pady=5, cursor='hand2')
        self.classify_btn.pack(pady=10, fill='x')
        
        self.button_clear = tk.Button(right_panel, text="🗑️ CLEAR", 
                                     command=self.clear_all,
                                     font=("Arial", 10, "bold"), bg='#E74C3C', fg='white',
                                     padx=15, pady=5, cursor='hand2')
        self.button_clear.pack(pady=5, fill='x')
        
        # Bind events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.paint)
        
        self.old_x = None
        self.old_y = None

    def paint(self, event):
        if self.old_x and self.old_y:
            # Draw on canvas
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                   width=15, fill='black', capstyle=ROUND, smooth=TRUE)
            # Draw on internal image
            self.draw.line([self.old_x, self.old_y, event.x, event.y], fill="black", width=15)
        
        self.old_x = event.x
        self.old_y = event.y
        
        # Reset on button release
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clear_all(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.label.configure(text="Draw!", fg='#E74C3C')
        self.confidence_label.configure(text="Confidence: ---%")

    def classify_handwriting(self):
        try:
            # Process the internal image (not screenshot)
            img = self.image.convert('L')  # Convert to grayscale
            img = img.resize((28, 28), Image.LANCZOS)  # Resize to 28x28
            
            # Invert colors (MNIST expects white digits on black background)
            img_array = np.array(img)
            img_array = 255 - img_array  # Invert
            
            # Normalize and reshape
            img_array = img_array.reshape(1, 28, 28, 1)
            img_array = img_array / 255.0
            
            # Predict
            prediction = model.predict(img_array, verbose=0)
            digit = np.argmax(prediction[0])
            confidence = np.max(prediction[0]) * 100
            
            # Update display
            if confidence > 80:
                color = '#27AE60'
            elif confidence > 60:
                color = '#F39C12'
            else:
                color = '#E74C3C'
                
            self.label.configure(text=f"🎯 {digit}", fg=color)
            self.confidence_label.configure(text=f"Confidence: {int(confidence)}%")
            
        except Exception as e:
            self.label.configure(text="❌ Error!", fg='#E74C3C')
            self.confidence_label.configure(text="Try again!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
