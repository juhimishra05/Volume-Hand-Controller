# 🔊 Virtual Volume Controller — OpenCV + MediaPipe Project

Control your system volume using just your **fingers** — no keyboard, no mouse, just pure gesture magic! 🖐️🤏  
Built using **Python**, **OpenCV**, and **MediaPipe**, this project uses your webcam to detect finger distance and adjust the volume in real time.

## 🖼 Demo

![Demo](assets/Demo.gif)

## 🎯 How It Works

📷 Your webcam tracks your **index finger** and **thumb** using MediaPipe's hand tracking.  
The distance between them determines the volume level:

- 👉✌️ **Stretch fingers wide** → Volume increases
- 🤏 **Bring fingers close** → Volume decreases
- 👈👉 **Touch both fingers** → System is **muted**

This is a simple yet powerful demo of **gesture-based human-computer interaction**!

## 🚀 Features

✅ Real-time finger tracking with MediaPipe  
✅ Dynamically adjust system volume based on finger distance  
✅ Mute system when fingers are touching  
✅ Clean UI using OpenCV overlays  
✅ Works offline (on Windows)

## 🧠 What You’ll Learn

- Hand landmark detection using **MediaPipe**
- Measuring Euclidean distance between fingers
- Mapping distance to volume percentage
- Controlling system audio using **pycaw** (Windows)

## 🛠 Setup Instructions

1.  **Install the required dependencies, globlally or by creating a virtual environment:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**

    ```bash
    python volumeHandControl.py
    ```

## 🧰 Tech Stack & Dependencies

- Python
- OpenCV
- MediaPipe
- pycaw (for controlling system volume on Windows)


Contributions are welcome! 🙏 If you have any ideas for improvements, feel free to submit a pull request.\
Follow me for more exciting projects like this! 🤩
