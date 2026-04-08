from fastapi import FastAPI
from models import Action, Observation, State
from environment import SQLEnv

app = FastAPI()
env = SQLEnv()

@app.post("/reset")
def reset():
    obs_text = env.reset()
    return {"observation": obs_text}

@app.post("/step")
def step(action: Action):
    # Mapping the Pydantic Action model to the environment logic
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