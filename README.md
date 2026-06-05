# code-explain

A small CLI tool that explains code snippets using a local LLM. Paste in some code, get an explanation, then ask follow-up questions in a conversation loop.

## Requirements

- Python 3.11
- [Ollama](https://ollama.com) running locally with `llama3.2:1b` pulled

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Paste your code snippet when prompted, then press `Ctrl+Z` + Enter (Windows) or `Ctrl+D` (Mac/Linux) to submit. After the explanation, you can ask follow-up questions. Type `exit` or `quit` to end the session.

## Notes

- Chat history is kept in memory for the duration of the session, so follow-up questions have full context.
- No internet connection needed — everything runs through Ollama locally.
