# LangGraph Examples
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated

class AgentState(TypedDict):
    messages: list[str]

def call_model(state: AgentState):
    # Logic to call LLM
    return {"messages": ["Model response"]}

workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)
app = workflow.compile()