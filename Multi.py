from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import glob
files = []
data = []
files = ['data.json']


prediction_key = "da9a862e889848f995acfaf0745bba0b"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
Project_id = "98196bb6-2a1b-4699-ac46-44a71fa0ae12"
publish_iteration_name = "Adit123"

predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

for file in glob.glob("/home/lalit/Desktop/Demo1/test/*.jpeg"):
        base_image_url = file
        with open(base_image_url, "rb") as image_contents:
            results = predictor.classify_image(
                Project_id, publish_iteration_name, image_contents.read())

        # Display the results.
            for prediction in results.predictions:
                print("\t" + prediction.tag_name)
                t = prediction.tag_name
                data.append({
                    'name': t,
                    'price': "20rs"
                })
                break

        # end with
        with open('data.json', 'w+') as outfile:
          json.dump(data, outfile)

        # end with
        files = ['data.json']
