from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.graph.coach import coach_node

def create_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("coach", coach_node)
    
    # Set entry point
    workflow.set_entry_point("coach")
    
    # Set finish point
    workflow.add_edge("coach", END)
    
    return workflow.compile()

# Singleton instance to be imported by main app
app_graph = create_graph()
