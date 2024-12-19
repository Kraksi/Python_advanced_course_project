import cv2

def connect_to_camera():

    rtsp_url = "rtsp://krasti:@anuBIS0431!@192.168.1.89:554/stream1"

    # Подключение к камере
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Ошибка: не удалось подключиться к камере.")
    else:
        print("Подключение к камере успешно!")

    # Чтение видеопотока
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Ошибка: не удалось получить кадр.")
            break


    return cap


connect_to_camera()
