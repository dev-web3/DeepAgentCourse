# LangChain Examples
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
model = ChatOpenAI(model="gpt-4o")
chain = prompt | model

response = chain.invoke({"topic": "bears"})