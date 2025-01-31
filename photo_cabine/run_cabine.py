import cv2
import pathlib
local_path = pathlib.Path().resolve()

cap = cv2.VideoCapture(0)
janela = 'CABINE DE FOTO'
img_counter = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow(janela, frame)

    k = cv2.waitKey(1)

    if k % 256 == 32:
        # SPACE pressed
        img_name = "{}/photo_cabine/opencv_frame_{}.png".format(local_path, img_counter)
        cropped_image = frame[100:400, 150:450]
        cv2.imwrite(img_name, cropped_image)
        print("{} written!".format(img_name))
        img_counter += 1

    if k == ord('k'):
        break

    if cv2.getWindowProperty(janela, cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()
cap.release()
print('Encerrou')
