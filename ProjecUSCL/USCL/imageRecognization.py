import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def recognize_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform edge detection (you can replace this with any other image processing technique)
    edges = cv2.Canny(gray, 100, 200)
    
    # Display the processed image
    cv2.imshow("Recognized Image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if file_path:
        image_label.config(text=file_path)
        recognize_image(file_path)

# Create the main window
root = tk.Tk()
root.title("Image Recognition")

# Create a label to display the image path
image_label = tk.Label(root, text="Select an image file")
image_label.pack()

# Create a button to browse for an image
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack()

# Start the Tkinter main loop
root.mainloop()