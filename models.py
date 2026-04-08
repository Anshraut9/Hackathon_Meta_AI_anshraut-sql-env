from pydantic import BaseModel
from typing import Any, Optional, Dict

class Action(BaseModel):
    command: str  # e.g., "run_query", "check_schema", "submit_solution"
    args: Dict[str, Any]

class Observation(BaseModel):
    output: str
    reward: float
    done: bool
    info: Optional[Dict[str, Any]] = None

class State(BaseModel):
    step_count: int
    current_task_id: str
    query_history: list[str]