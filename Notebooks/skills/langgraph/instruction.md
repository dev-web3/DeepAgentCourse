# Instructions for LangGraph Skill
- Define a clear `State` TypedDict for every graph.
- Use `nodes` for logic and `edges` for transitions.
- Implement conditional edges for decision-making logic.
- Use `Checkpointer` for persisting state and enabling "time travel" debugging.
- Keep nodes modular and focused on a single responsibility.