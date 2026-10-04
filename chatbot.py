import ollama # type: ignore


def generate_answer(question, context):

    prompt = f"""
You are a helpful document assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:
"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    context = """
    Supervised learning is a machine learning technique
    where a model learns from labeled training data.
    """

    question = "What is supervised learning?"

    answer = generate_answer(question, context)

    print("\nAnswer:")
    print(answer)