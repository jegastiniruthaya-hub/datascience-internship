import sys
import os

os.environ["USE_OPENROUTER"] = "false"

from chatbot_engine import MultilingualChatbot


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def run_demo_tests():
    bot = MultilingualChatbot()
    sid = "demo"

    cases = [
        ("Hello, I want to book a train ticket", "book_ticket", "en", "neutral"),
        ("मुझे दिल्ली जाना है", "book_ticket", "hi", "neutral"),
        ("tomorrow evening", "book_ticket", "en", "neutral"),
        ("¿Cuál es el clima en Madrid mañana?", "weather", "es", "neutral"),
        ("Bonjour, je veux annuler ma réservation", "cancel", "fr", "neutral"),
        ("Thanks, this service is really helpful!", "thanks", "en", "positive"),
        ("I am frustrated because my ticket is delayed and nobody helped me", "book_ticket", "en", "negative"),
        ("मुझे समस्या हो रही है, मेरा टिकट काम नहीं कर रहा", "book_ticket", "hi", "negative"),
    ]

    for message, expected_intent, expected_language, expected_sentiment in cases:
        result = bot.reply(message, session_id=sid)
        assert result["intent"] == expected_intent, result
        assert result["language"] == expected_language, result
        assert result["sentiment"]["label"] == expected_sentiment, result
        print(
            "PASS: "
            f"{message} -> {result['language']} / {result['intent']} / "
            f"{result['sentiment']['label']}"
        )
        print(f"      {result['reply']}")


if __name__ == "__main__":
    run_demo_tests()
