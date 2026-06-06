# Sentiment-Aware Customer Support Chatbot

This internship prototype detects customer sentiment during chat interactions and adjusts the bot response for positive, negative, or neutral messages. It also keeps the earlier multilingual support for English, Hindi, Spanish, and French.

## Features

- Sentiment detection for `positive`, `negative`, and `neutral` customer messages.
- Emotion-aware responses: appreciation for positive users, empathy for negative users, and direct help for neutral users.
- Automatic language detection for English, Hindi, Spanish, and French.
- Mixed-language support using language hints and Unicode script detection.
- Intent detection for greeting, ticket booking, weather, status checking, cancellation, and thanks.
- Context memory using a session ID, so follow-up messages can update previous intent and entities.
- Language switching inside the same conversation.
- Browser-based chat UI with live language, intent, sentiment score, engine, and turn count.
- Dependency-free Python backend using only the standard library.
- Optional OpenRouter API mode for stronger online reasoning.

## Run

```powershell
cd C:\your_folder\multilingual_chatbot
python app.py
```

Open:

```text
http://127.0.0.1:8000
```

## Test

```powershell
cd C:\Games\codex\multilingual_chatbot
python tests.py
```

## OpenRouter Online Mode

### Option 1: Enter the key in the app

1. Start the app.
2. Open `http://127.0.0.1:8000`.
3. Paste your OpenRouter key into the OpenRouter API section.
4. Keep the model as `openrouter/auto` or enter another OpenRouter model ID.
5. Click `Save API Key`.

The app saves the key to a local `.env` file and uses OpenRouter for the next message.

```text
OPENROUTER_API_KEY=sk-or-your-key-here
OPENROUTER_MODEL=openrouter/auto
```

4. Start the app again:

```powershell
python app.py
```

When the key is present, the app calls OpenRouter's OpenAI-compatible chat completions API:

```text
https://openrouter.ai/api/v1/chat/completions
```

If the internet is unavailable or the key/model is wrong, the app automatically falls back to the offline rule-based response.

## Sentiment Demo

```text
User: Thanks, this service is really helpful!
Detected sentiment: positive
Bot: I'm glad this is going well. You're welcome. I will keep the conversation context ready for your next message.

User: I am frustrated because my ticket is delayed and nobody helped me
Detected sentiment: negative
Bot: I'm sorry this has been frustrating. I'll keep this clear and help you fix it. ...

User: What is the status of booking ID 4821?
Detected sentiment: neutral
Bot: I understood you want to check status. Please share the booking or tracking ID.
```

## How It Works

The chatbot follows this pipeline:

```text
User message
  -> language detection
  -> sentiment detection
  -> intent detection
  -> entity extraction
  -> conversation state update
  -> emotion-aware response generation
```

The internal memory stores:

- preferred language
- last intent
- last sentiment analysis
- extracted entities such as destination, date, time, and travel mode
- full conversation history

## Evaluation Criteria

- Accuracy: run `python tests.py` to check expected sentiment labels for positive, negative, and neutral examples.
- Response appropriateness: verify that negative messages receive empathetic wording before the task answer.
- Customer satisfaction impact: compare normal answers with emotion-aware answers during demo conversations.

## Suggested Report Points

- The system improves customer support tone by recognizing emotion before generating the final response.
- The sentiment module is dependency-free and easy to explain because it uses weighted positive and negative keyword/phrase evidence.
- The system supports cross-lingual continuity because the same memory object is updated regardless of input language.
- Ambiguous follow-up messages reuse the previous intent when they contain useful entities.
- The prototype can later be upgraded with VADER, TextBlob, Hugging Face Transformers, Rasa, or a custom trained classifier.
