import cv2
import mediapipe as mp
import numpy as np
import pickle
import time
import requests
import pyttsx3
from collections import deque, Counter
from spellchecker import SpellChecker
import os

# ================== LOAD MODEL ==================
with open("model/sign_model.pkl", "rb") as f:
    model, scaler, label_encoder = pickle.load(f)

# ================== MEDIAPIPE ==================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7
)

# ================== SPELL CHECKER ==================
spell = SpellChecker()
custom_words = ["hello", "thanks", "thank", "help", "yes", "no", "good", "morning", "please"]
spell.word_frequency.load_words(custom_words)

def correct_word(word):
    if len(word) <= 1:
        return word
    corrected = spell.correction(word)
    return corrected if corrected else word

# ================== TEXT TO SPEECH ==================
engine = pyttsx3.init()

ELEVEN_API_KEY = "sk_c11e62579b7fbb5ccded89ecd21914066251ece33b242b08"
VOICE_ID = "EXAVITQu4vr4xnSDxMaL" 

def speak_text(text):
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {
            "xi-api-key": ELEVEN_API_KEY,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.7
            }
        }

        response = requests.post(url, json=data, headers=headers, timeout=5)
        response.raise_for_status()

        with open("temp_audio.mp3", "wb") as f:
            f.write(response.content)

        from playsound import playsound
        playsound("temp_audio.mp3", True)
        os.remove("temp_audio.mp3")

    except Exception as e:
        print("ElevenLabs failed, using pyttsx3:", e)
        engine.say(text)
        engine.runAndWait()

# ================== VARIABLES ==================
cap = cv2.VideoCapture(0)

prediction_buffer = deque(maxlen=15)

current_text = ""
last_letter_time = time.time()

LETTER_DELAY = 1.0   # seconds to confirm a letter
SPACE_DELAY = 2.0    # seconds for space

print("Press ENTER to speak | Press Q to quit")

# ================== MAIN LOOP ==================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    hand_count = len(result.multi_hand_landmarks) if result.multi_hand_landmarks else 0
    current_time = time.time()

    # ================== TWO HANDS → PAUSE ==================
    if hand_count > 1:
        prediction_buffer.clear()
        cv2.putText(
            frame,
            "PAUSED (Two hands detected)",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # ================== ONE HAND → RECOGNIZE ==================
    elif hand_count == 1:
        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        landmarks = []
        for lm in hand_landmarks.landmark:
            landmarks.extend([lm.x, lm.y, lm.z])

        X = np.array(landmarks).reshape(1, -1)
        X = scaler.transform(X)

        pred = model.predict(X)
        letter = label_encoder.inverse_transform(pred)[0]

        prediction_buffer.append(letter)
        stable_letter = Counter(prediction_buffer).most_common(1)[0][0]

        if current_time - last_letter_time > LETTER_DELAY:
            current_text += stable_letter
            last_letter_time = current_time

        cv2.putText(
            frame,
            f"Letter: {stable_letter}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # ================== NO HAND → SPACE + WORD CORRECTION ==================
    else:
        if current_time - last_letter_time > SPACE_DELAY and not current_text.endswith(" "):
            words = current_text.strip().split(" ")
            if words:
                words[-1] = correct_word(words[-1])
                current_text = " ".join(words) + " "
            last_letter_time = current_time

    # ================== DISPLAY TEXT ==================
    cv2.putText(
        frame,
        f"Text: {current_text}",
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    cv2.imshow("Sign Language → Text → Audio", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # ================== ENTER → SPEAK ==================
    elif key == 13 and current_text.strip():
        final_words = []
        for w in current_text.strip().split(" "):
            final_words.append(correct_word(w))

        final_text = " ".join(final_words)
        print("Speaking:", final_text)
        speak_text(final_text)

cap.release()
cv2.destroyAllWindows()
