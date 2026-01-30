import cv2


cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("ERROR: Cannot access the camera")
    exit()

print("Camera opened successfully. Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Failed to grab frame")
        break

    cv2.imshow("Camera Input - Step 1", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
