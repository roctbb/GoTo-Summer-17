import requests

key = "ed949f112a524980ad1907524eb7d32d"

headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": key
}

url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

with open('faces.jpg', 'rb') as file:
    result = requests.post(url, file.read(), headers=headers)

faces = result.json()

for face in faces:
    print("Координаты:")
    print(face["faceRectangle"]['left'])
    print(face["faceRectangle"]['top'])

    print("Размер:")
    print(face["faceRectangle"]['width'])
    print(face["faceRectangle"]['height'])

    emotions_list = list(face["scores"].items())
    sorted_emotions = sorted(emotions_list, key=lambda x:x[1], reverse=True)

    print("Эмоция:")
    print(sorted_emotions[0][0])
    print('-' * 12)
