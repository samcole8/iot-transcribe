from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import markdown
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load your OpenAI API key

app = Flask(__name__)

transcripts = []

@app.route("/summary", methods=["GET"])
def summarise(transcripts=transcripts):
    message = "Can you give me a brief summary of the following meeting transcript? Focus on the key points and takeaways. It should be in a digestible format suitable for recapping to somebody who isnt in the meeting. The header must be Transcript Summary:"
    for item in transcripts:
        message += f"\n{item}"
    print(message)
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": message
        }
    ])
    print(completion.choices[0].message)
    return markdown.markdown(completion.choices[0].message.content)

@app.route("/")
def index():
    return render_template("index.html", transcripts=transcripts)

@app.route("/submit_transcript", methods=["POST"])
def submit_transcript():
    transcript = request.json.get("transcript")
    if transcript:
        transcripts.append(transcript)
        print(f"Received transcript: {transcript}")
        return "OK", 200
    return "No transcript provided", 400

@app.route("/get_transcripts", methods=["GET"])
def get_transcripts():
    return jsonify({"transcripts": transcripts})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
