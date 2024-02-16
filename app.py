import cv2
import face_recognition

def detectAndDraw(image):
    #encontrar todas as localizacoes de rostos na imagem
    face_locations = face_recognition.face_locations(image)

    #desenhar retangulos ao redor dos rostos detectados
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

while True:
    print("---------Deteção de Rostos---------")
    print("1 - Vídeo(Câmara) (quando em uso utilize a tecla '3' para sair)")
    print("2 - Imagem")
    print("3 - Sair")

    choice = input("Selecione o método que pretende realizar: ")
    if choice == "1":
        camera = cv2.VideoCapture(0)
        while True:
            (sucesso, frame) = camera.read()
            if not sucesso:
                break

            detectAndDraw(frame)

            cv2.imshow("Camara", frame)

            if cv2.waitKey(1) & 0xFF == ord("3"):
                cv2.destroyAllWindows()
                break

        camera.release()

        innerChoice = input("Pressione '3' para sair ou qualquer tecla para continuar: ")
        if innerChoice == "3":
            print("Obrigado por utilizar o nosso programa. Bem-haja!")
            break

    elif choice == "2":
        imgPath = input("Digite o caminho da imagem: ")

        img = cv2.imread(imgPath)

        detectAndDraw(img)

        cv2.imshow("Imagem", img)
        cv2.waitKey(0)

        innerChoice = input("Pressione '3' para sair ou qualquer tecla para continuar: ")
        if innerChoice == "3":
            print("Obrigado por utilizar o nosso programa. Bem-haja!")
            break

    elif choice == "3":
        print("Obrigado por utilizar o nosso programa. Bem-haja!")
        break

    else:
        print("Opção inválida. Por favor, escolha novamente.")

cv2.destroyAllWindows()
