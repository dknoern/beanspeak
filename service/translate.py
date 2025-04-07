import gradio as gr
import requests, uuid

key = "<KEY HERRE"
endpoint = "https://api.cognitive.microsofttranslator.com"


def translate(input, to_language):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': [to_language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': "westus2",
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': input
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text'], response[0]['detectedLanguage']['language']

demo = gr.Interface(
    translate,
    [
        "text",
        gr.Radio(["fr-CA", "fr", "en"], value="fr-CA", label="Target language")
    ],
    [gr.Textbox(label="Translated"),gr.Textbox(label="Detected Language")],
    examples=[
        ["Hello, how are you?", "fr"],
        ["Bonjour, comment ça va?", "en"],
        ["Bonjour, comment ça va?", "fr-CA"]
    ],
    title="Translator",
    description="Here's a sample translator.",
)

demo.launch(share=True)
