
# MCP Hands-On Learning & Demo Guide

This project teaches the core concepts of the Model Context Protocol (MCP) through hands-on Python code.

## What is MCP?
MCP (Model Context Protocol) is an open protocol for standardizing how AI models, tools, and agents interact with their context (files, code, resources, etc.).

## Project Structure
- `models.py`: MCP data models
- `provider.py`: FastAPI MCP provider
- `agent.py`: MCP agent script
- `test_mcp.py`: Example tests
- `requirements.txt`: Python dependencies

## Quickstart for New Users

### 1. Clone or Download This Repository

### 2. Set Up Python Environment
Open a terminal in the `mcp_learn` directory and run:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Start the MCP Provider
In the same terminal, run:

```sh
uvicorn provider:app --reload
```
This starts the FastAPI MCP provider at [http://localhost:8000](http://localhost:8000).

### 4. Run the MCP Agent
Open a new terminal, activate the environment, and run:

```sh
source venv/bin/activate
python agent.py
```
You should see provider info, context items, and a read action result.

### 5. Run the Tests (Optional)

```sh
pytest test_mcp.py
```

## How It Works
- The provider exposes context and actions via a REST API.
- The agent interacts with the provider to perform actions.
- You can extend the provider and agent to add more actions or context types.

---
For questions or to extend this demo, edit the Python files as needed!
