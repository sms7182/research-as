from transformers import T5ForConditionalGeneration, T5Tokenizer
import json


model_name = "google/flan-t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def handler(event):
    try:
        input_data = json.loads(event["input"])
        prompt = input_data.get("prompt", "")

        response = generate_response(prompt)

        return {
            "response": response
        }
    except Exception as e:
        return {
            "error": str(e)
        }