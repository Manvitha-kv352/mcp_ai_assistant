from app.llm.anthropic_client import AnthropicClient

def main():
    client = AnthropicClient()

    response = client.chat("Hello Claude! Tell me one interesting fact.")

    print("\nClaude replied:\n")
    print(response)


if __name__ == "__main__":
    main()