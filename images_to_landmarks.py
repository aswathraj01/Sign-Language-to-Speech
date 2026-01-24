import cv2
import mediapipe as mp
import csv
import os

# ===== PATHS =====
DATASET_DIR = "dataset"              # Folder with A, B, C... subfolders
CSV_FILE = "data/sign_landmarks.csv"

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# ===== MEDIAPIPE SETUP =====
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.7
)

# ===== CREATE CSV HEADER =====
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        header = []
        for i in range(21):
            header.extend([f"x{i}", f"y{i}", f"z{i}"])
        header.append("label")
        writer.writerow(header)

print("Starting landmark extraction from images...")

# ===== PROCESS EACH LABEL FOLDER =====
for label in os.listdir(DATASET_DIR):
    label_path = os.path.join(DATASET_DIR, label)

    if not os.path.isdir(label_path):
        continue

    print(f"Processing label: {label}")

    for img_name in os.listdir(label_path):
        img_path = os.path.join(label_path, img_name)

        image = cv2.imread(img_path)
        if image is None:
            continue

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])

                with open(CSV_FILE, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(landmarks + [label])

print("Landmark extraction completed successfully.")
