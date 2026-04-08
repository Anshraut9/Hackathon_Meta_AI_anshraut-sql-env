import sys
import os
import uvicorn
from fastapi import FastAPI

# Add parent directory to path to find models.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Action, Observation, State
from .environment import SQLEnv 

app = FastAPI()
env = SQLEnv()

@app.post("/reset")
def reset():
    obs_text = env.reset()
    return {"observation": obs_text}

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step({"command": action.command, "args": action.args})
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def get_state():
    return {
        "step_count": env.step_count,
        "current_task_id": env.current_task,
        "query_history": []
    }

@app.get("/")
def health_check():
    return {"status": "alive", "framework": "OpenEnv"}

# CRITICAL: Added main() function for OpenEnv validator
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860, reload=False)

if __name__ == "__main__":
    main()
