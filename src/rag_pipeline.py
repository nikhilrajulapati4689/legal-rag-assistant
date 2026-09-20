from retriever import load_resources, search
from answer_generator import generate_answer


def main():

    print("===================================")
    print("      Legal Document RAG Assistant")
    print("===================================")

    print("\nLoading legal document resources...")

    index, metadata, model = load_resources()

    print("System ready.")

    question = input("\nEnter your legal question: ")

    # Step 1: Retrieve relevant chunks
    results = search(
        question,
        index,
        metadata,
        model
    )

    # Step 2: Check whether relevant information exists
    if not results:

        print("\nInformation not found in the provided legal documents.")
        return

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

    # Step 3: Generate answer using retrieved documents
    answer = generate_answer(
        question,
        results
    )

    print("\n===================================")
    print("Answer")
    print("===================================")

    print(answer)

    print("\nEducational Information Retrieval System — Not Legal Advice.")


if __name__ == "__main__":
    main()