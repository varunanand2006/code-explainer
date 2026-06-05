import sys
from chain import chain

SESSION_ID = "code-explain-session"
CONFIG = {"configurable": {"session_id": SESSION_ID}}


def read_code_snippet() -> str:
    print("Paste your code snippet below.")
    print("When done, press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows):\n")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return "\n".join(lines)


def main():
    print("=== Code Explainer ===\n")

    code = read_code_snippet()

    if not code.strip():
        print("No code provided. Exiting.")
        sys.exit(0)

    print("\nExplaining your code...\n")
    explanation = chain.invoke({"input": f"Explain this code:\n\n{code}"}, config=CONFIG)
    print(explanation)

    print("\n--- Follow-up questions (type 'exit' or 'quit' to end) ---\n")
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not question:
            continue

        response = chain.invoke({"input": question}, config=CONFIG)
        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    main()
