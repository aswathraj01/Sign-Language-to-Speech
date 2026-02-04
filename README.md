<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aswathraj01/Sign-Language-to-Speech">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Sign Language to Speech</h3>

  <p align="center">
    A real-time sign language letter recognition system that converts hand gestures into audible speech.
    <br />
    <a href="https://github.com/aswathraj01/Sign-Language-to-Speech"><strong>Explore the repository »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/aswathraj01/Sign-Language-to-Speech/issues">Report Bug</a>
    ·
    <a href="https://github.com/aswathraj01/Sign-Language-to-Speech/issues">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

[![Product Screenshot][product-screenshot]](#)

Sign language is a primary mode of communication for deaf and speech-impaired individuals, yet most people do not understand it.  
This project aims to bridge that communication gap by converting **sign language letters (A–Z)** into **real-time audible speech** using a standard webcam.

The system uses **MediaPipe** for hand landmark detection and a **machine learning model** to classify hand gestures efficiently. Each recognized letter is spoken continuously in real time, even if the same sign is repeated.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### Built With

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [MediaPipe](https://developers.google.com/mediapipe)
* [NumPy](https://numpy.org/)
* [Scikit-learn](https://scikit-learn.org/)
* [pygame](https://www.pygame.org/)
* [pyttsx3](https://pyttsx3.readthedocs.io/)
* [ElevenLabs API](https://www.elevenlabs.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

Follow the steps below to set up the project locally.

### Prerequisites

* Python 3.9 or higher
* Webcam
* pip package manager

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/aswathraj01/Sign-Language-to-Speech.git
Navigate to the project directory

cd Sign-Language-to-Speech


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


Install required dependencies

pip install -r requirements.txt


(Optional) Add your ElevenLabs API key in the code

ELEVEN_API_KEY = "YOUR_API_KEY"

<p align="right">(<a href="#readme-top">back to top</a>)</p>
Usage

Run the real-time sign language recognition system:

python sign_language_to_speech.py

Controls

Q → Quit the application

Show a sign language letter → The system recognizes and speaks it continuously

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- ✅ Real-time hand detection
- ✅ Letter-level sign recognition
- ✅ Continuous audio output
- ⏳ Word-level recognition
- ⏳ Sentence-level recognition
- 📱 Mobile / Web deployment


See the open issues
 for a full list of proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
License

Distributed under the MIT License.
See LICENSE for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
Contact

Aswath Raj
GitHub: @aswathraj01

Project Link:
https://github.com/aswathraj01/Sign-Language-to-Speech

<p align="right">(<a href="#readme-top">back to top</a>)</p>
Acknowledgments

MediaPipe by Google

OpenCV Community

Scikit-learn

ElevenLabs Text-to-Speech API

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- MARKDOWN LINKS & IMAGES -->

---

### ✅ This README is:
- GitHub-professional  
- Portfolio-ready  
- Interview & viva safe  
- Clean and readable  
- Based on **Best-README-Template standard**

If you want next, I can:
- Add **badges for Python version**
- Generate **requirements.txt**
- Create **demo screenshots section**
- Make a **short academic README**

Just say 👍
