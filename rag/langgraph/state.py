from typing import TypedDict, Annotated, Sequence
import operator
from typing import Annotated


from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    context: Annotated[Sequence[Document], operator.add]
    document: Annotated[Sequence[Document], operator.add]
    answer: Annotated[Sequence[Document], operator.add]
    question: Annotated[str, operator.add]
    tried: Annotated[int, operator.add]
    binary_score: Annotated[str, operator.add]

graph_builder = StateGraph(State)