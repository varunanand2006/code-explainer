from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a code explanation assistant. "
        "The user will provide a code snippet in the first message. "
        "Explain it clearly, covering what it does, how it works, and any notable details. "
        "Answer any follow-up questions about that snippet.",
    ),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])
