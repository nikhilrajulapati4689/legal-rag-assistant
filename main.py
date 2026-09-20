from src.retriever import load_resources, search
from src.answer_generator import generate_answer


def main():

    print("===================================")
    print("      Legal Document RAG Assistant")
    print("===================================")

    print("\nLoading legal document resources...")

    index, metadata, model = load_resources()

    print("System ready.")

    while True:

        question = input(
            "\nEnter your legal question "
            "(type 'exit' to quit): "
        )

        if question.lower() == "exit":
            print("\nExiting Legal RAG Assistant...")
            break

        # Retrieve relevant chunks
        results = search(
            question,
            index,
            metadata,
            model
        )

        # Check whether information exists
        if not results:

            print(
                "\nInformation not found in the "
                "provided legal documents."
            )

            continue

        # Display retrieved sources
        print("\nRetrieved Sources:")

        for i, result in enumerate(results):

            print(
                f"  {i + 1}. "
                f"{result['source']} "
                f"(Page {result['page']}, "
                f"Distance: {result['distance']:.4f})"
            )

        print("\nGenerating grounded answer...")

        # Generate answer
        answer = generate_answer(
            question,
            results
        )

        print("\n===================================")
        print("Answer")
        print("===================================")

        print(answer)

        print(
            "\nEducational Information Retrieval "
            "System — Not Legal Advice."
        )


if __name__ == "__main__":
    main()