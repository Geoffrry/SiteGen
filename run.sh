#!/bin/bash

# Make sure Ollama is running and model is pulled
ollama serve &
ollama pull deepseek-coder

# Run the app
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
