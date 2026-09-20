import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from flask import Flask, request, jsonify, render_template

from src.retriever import load_resources, search
from src.answer_generator import generate_answer


app = Flask(
    __name__,
    template_folder="../templates"
)


print("Loading RAG resources...")

index, metadata, model = load_resources()

print("RAG resources loaded successfully.")


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:

        return jsonify({
            "error": "Please enter a question."
        }), 400

    # Retrieve relevant document chunks
    results = search(
        question,
        index,
        metadata,
        model
    )

    # No relevant information
    if not results:

        return jsonify({
            "answer": (
                "Information not found in the "
                "provided legal documents."
            ),
            "sources": []
        })

    # Generate grounded answer
    answer = generate_answer(
        question,
        results
    )

    # Prepare source information
    sources = []

    for result in results:

        sources.append({
            "file": result["source"],
            "page": result["page"],
            "distance": result["distance"]
        })

    return jsonify({
        "answer": answer,
        "sources": sources
    })


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )