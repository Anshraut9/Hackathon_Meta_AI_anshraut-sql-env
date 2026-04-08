import sqlite3
import pandas as pd

class SQLEnv:
    def __init__(self):
        self.tasks = {
            "easy": "Select all users older than 25.",
            "medium": "Find the average salary per department, joined with the locations table.",
            "hard": "Optimize this nested subquery into a JOIN with an index hint."
        }
        self.reset()

    def reset(self):
        self.step_count = 0
        self.current_task = "easy"
        # Create an in-memory database for the agent to play with
        self.conn = sqlite3.connect(':memory:', check_same_thread=False)
        self.conn.execute("CREATE TABLE users (id INT, name TEXT, age INT, salary INT)")
        self.conn.execute("INSERT INTO users VALUES (1, 'Ansh', 21, 50000), (2, 'AI', 30, 90000)")
        return "Environment Reset. Task: " + self.tasks[self.current_task]

    def step(self, action):
        self.step_count += 1
        cmd = action.get("command")
        args = action.get("args", {})
        
        reward = 0.0
        done = False
        obs = ""

        if cmd == "run_query":
            try:
                df = pd.read_sql_query(args.get("sql"), self.conn)
                obs = df.to_string()
                reward = 0.1 # Small reward for valid syntax
            except Exception as e:
                obs = f"Error: {str(e)}"
                reward = -0.1 # Penalty for crashing
        
        elif cmd == "submit_solution":
            # Logic to check if the SQL matches the requirement
            # For hackathon: compare output results vs expected results
            obs = "Task evaluated."
            reward = 1.0 # High reward for completion
            done = True
            
        return obs, reward, done, {"steps": self.step_count}