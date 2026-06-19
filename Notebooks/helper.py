from typing import Any

from IPython.display import display, Markdown


def print_last_content(result: Any) -> None:
    last_msg = result["messages"][-1]
    print(last_msg.usage_metadata)
    print("=" * 100)
    display(Markdown(last_msg.content))
