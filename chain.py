from langchain_ollama import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

from prompt import prompt
from parser import parser

_model = ChatOllama(model="llama3.2:1b")

_chain = prompt | _model | parser

_store: dict[str, InMemoryChatMessageHistory] = {}


def _get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in _store:
        _store[session_id] = InMemoryChatMessageHistory()
    return _store[session_id]


chain = RunnableWithMessageHistory(
    _chain,
    _get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
