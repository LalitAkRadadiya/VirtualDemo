from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import os
files = []


prediction_key = "da9a862e889848f995acfaf0745bba0b"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
Project_id = "98196bb6-2a1b-4699-ac46-44a71fa0ae12"
publish_iteration_name = "Adit123"
base_image_url = "/home/lalit/Desktop/Demo1/test/images.jpeg"

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open(base_image_url, "rb") as image_contents:
    results = predictor.classify_image(
        Project_id, publish_iteration_name, image_contents.read())

# Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name)
        break

data =[]
t = prediction.tag_name
data.append({
  'name': t,
  'price': "20rs"
  })
with open('data.json', 'w+') as outfile:
  json.dump(data, outfile)

# end with
files = ['data.json']
