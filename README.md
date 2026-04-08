---
title: SQL Optimizer Env
emoji: 🚀
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# 📊 SQL Optimizer & Debugging Environment
A real-world OpenEnv simulation designed for training and evaluating AI agents in SQL optimization, syntax debugging, and data retrieval tasks.

## 🔗 Project Links
* **Live Environment (Hugging Face):** [https://huggingface.co/spaces/AnshRaut93/anshraut-sql-env](https://huggingface.co/spaces/AnshRaut93/anshraut-sql-env)
* **API Documentation:** [https://anshraut93-anshraut-sql-env.hf.space/docs](https://anshraut93-anshraut-sql-env.hf.space/docs)
* **GitHub Repository:** [https://github.com/Anshraut9/Hackathon_Meta_AI_anshraut-sql-env](https://github.com/Anshraut9/Hackathon_Meta_AI_anshraut-sql-env)

---

## 🚀 Overview
This environment follows the **OpenEnv** specification. It simulates a database administrator workflow where an agent must interact with a SQL engine to solve tasks ranging from simple queries to complex performance optimizations.

### Key Features
* **Stateful Interaction:** Uses `step()`, `reset()`, and `state()` API endpoints.
* **Deterministic Grading:** Built-in graders evaluate SQL correctness and efficiency.
* **Multi-Level Tasks:** Includes 3 distinct tasks (Easy, Medium, Hard).
* **Real-World Utility:** Models genuine developer tasks instead of toy games.

---

## 🛠 Tech Stack
* **Framework:** OpenEnv (Meta/Hugging Face)
* **Backend:** FastAPI & Uvicorn
* **Database Logic:** SQLite3 & Pandas
* **Deployment:** Docker on Hugging Face Spaces

---

## 📡 API Specification
The agent interacts with the environment via the following endpoints:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/reset` | POST | Resets the environment and returns the first task description. |
| `/step` | POST | Executes an action (SQL query) and returns an observation/reward. |
| `/state` | GET | Returns the current internal state of the environment. |

---

## 📝 Setup & Local Development
If you want to run this environment locally:

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/Anshraut9/Hackathon_Meta_AI_anshraut-sql-env.git](https://github.com/Anshraut9/Hackathon_Meta_AI_anshraut-sql-env.git)
   cd Hackathon_Meta_AI_anshraut-sql-env
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/AnshRaut93/anshraut-sql-env.git](https://github.com/AnshRaut93/anshraut-sql-env.git)
   cd anshraut-sql-env
