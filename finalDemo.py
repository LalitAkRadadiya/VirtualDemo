from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import os
files = []

prediction_key = "80402eb76c0842bdb563237946b63f63"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
Project_id = "7845cd93-bbb0-4604-8a82-341d435f3fd5"
publish_iteration_name = "Demo"

base_image_url = "/home/lalit/Desktop/Data/test/images1.jpeg"


# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open(base_image_url, "rb") as image_contents:
    results = predictor.classify_image(
        Project_id, publish_iteration_name, image_contents.read())

# Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name)
        break
