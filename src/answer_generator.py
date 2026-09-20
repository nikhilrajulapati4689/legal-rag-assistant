import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, retrieved_chunks):

    context = ""

    for i, chunk in enumerate(retrieved_chunks):

        context += f"""
Source {i + 1}
File: {chunk['source']}
Page: {chunk['page']}

Content:
{chunk['text']}

-------------------------
"""

    prompt = f"""
You are a legal document question-answering assistant.

Answer the user's question ONLY using the information
provided in the retrieved legal documents.

If the answer cannot be found in the provided documents,
say:

"Information not found in the provided legal documents."

Do not use outside knowledge.
Do not make assumptions.
Do not invent legal information.

Always provide the source file and page number in this format:

Source: <file path>
Page: <page number>

Use the actual file path and page number from the retrieved documents.

Do not add an "Answer" heading.

User Question:
{question}

Retrieved Legal Documents:
{context}
"""

    try:

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        return interaction.output_text

    except Exception as error:

        error_message = str(error)

        if (
            "429" in error_message
            or "rate limit" in error_message.lower()
        ):

            return (
                "The AI answer-generation service has "
                "temporarily reached its usage limit. "
                "Please try again later."
            )

        return (
            "The AI answer-generation service is "
            "temporarily unavailable. Please try again later."
        )