from google.cloud import vision
import os

def recognize_card(image_path):
    """Utilise Google Vision pour détecter le texte dans une image."""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "chemin/vers/ta_clé.json"
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description.strip()
    return None
