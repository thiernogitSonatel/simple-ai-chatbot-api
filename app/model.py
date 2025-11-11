def generate_response(user_input: str) -> str:
    """
    Simple rule-based AI logic.
    Demonstrates chatbot behavior without using external models.
    """
    if not user_input.strip():
        return "Please say something."

    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"

    if "who are you" in user_input.lower():
        return "I'm a simple AI chatbot built with FastAPI."

    if "help" in user_input.lower():
        return "Sure! Ask me anything."

    return "Interesting! Tell me more."
