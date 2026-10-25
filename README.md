# My First Agentic Backend - Log Detective Agent
My first Linux + MLOps + Agentic AI project. A backend that can use tools to answer questions about training logs.
Built from 0 in WSL Ubuntu - learned Linux, tmux, FastAPI, and agentic pattern.
## What it does
An AI agent that doesn't just chat - it uses real Linux tools:
- `list_files` - lists files in the project
- `read_file` - reads any txt/log file
- `grep_logs` - searches errors in training logs
- `get_time` - returns current time
Example: Ask "show errors" -> agent actually runs grep on `logs/train.log` and returns real errors.
## Architecture
