import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os

# ================= CAMERA DETECTION =================
def get_available_cameras(max_tested=5):
    available = []
    for i in range(max_tested):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available.append(i)
            cap.release()
    return available

# ================= MAIN APP =================
class SignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language to Speech")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # Set custom icon (optional)
        try:
            self.root.iconbitmap("app_icon.ico")
        except:
            pass

        # ---------------- LEFT FRAME (CAMERA) ----------------
        self.camera_frame = tk.Frame(root, width=700, height=600, bg="black")
        self.camera_frame.pack(side="left", fill="both")

        self.video_label = tk.Label(self.camera_frame)
        self.video_label.pack()

        # ---------------- RIGHT FRAME (CONTROL PANEL) ----------------
        self.control_frame = tk.Frame(root, width=300, bg="#2c3e50")
        self.control_frame.pack(side="right", fill="y")

        tk.Label(
            self.control_frame,
            text="Control Panel",
            font=("Segoe UI", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=20)

        # Camera Selection
        tk.Label(
            self.control_frame,
            text="Select Camera",
            bg="#2c3e50",
            fg="white"
        ).pack(pady=10)

        self.camera_list = get_available_cameras()
        self.selected_camera = tk.IntVar()

        if self.camera_list:
            self.selected_camera.set(self.camera_list[0])

        self.camera_dropdown = ttk.Combobox(
            self.control_frame,
            values=self.camera_list,
            textvariable=self.selected_camera,
            state="readonly"
        )
        self.camera_dropdown.pack(pady=5)

        # Buttons
        ttk.Button(self.control_frame, text="Start", command=self.start).pack(pady=15)
        ttk.Button(self.control_frame, text="Stop", command=self.stop).pack(pady=15)
        ttk.Button(self.control_frame, text="Exit", command=self.exit_app).pack(pady=15)

        # Variables
        self.cap = None
        self.running = False

    # ---------------- START CAMERA ----------------
    def start(self):
        if not self.running:
            cam_index = self.selected_camera.get()
            self.cap = cv2.VideoCapture(cam_index)

            if not self.cap.isOpened():
                print("Error: Unable to open selected camera")
                return

            self.running = True
            self.update_frame()

    # ---------------- STOP CAMERA ----------------
    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()
            self.cap = None

    # ---------------- EXIT APP ----------------
    def exit_app(self):
        self.stop()
        self.root.destroy()

    # ---------------- UPDATE FRAME ----------------
    def update_frame(self):
        if self.running and self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                frame = cv2.resize(frame, (700, 600))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                img = ImageTk.PhotoImage(Image.fromarray(frame))
                self.video_label.imgtk = img
                self.video_label.configure(image=img)

            self.root.after(10, self.update_frame)

# ================= RUN APP =================
root = tk.Tk()
app = SignApp(root)
root.mainloop()
