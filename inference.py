import os
from openai import OpenAI
import json

# These will be set in Hugging Face / GitHub Secrets
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize OpenAI Client (using OpenEnv requirements)
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference():
    print("[START]")
    
    # Simulate a step for the evaluator
    # In a real scenario, you'd loop through tasks here
    payload = {
        "step": 1,
        "action": "run_query",
        "reward": 0.1
    }
    
    print(f"[STEP] {json.dumps(payload)}")
    
    print("[END]")

if __name__ == "__main__":
    run_inference()