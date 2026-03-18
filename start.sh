#!/bin/bash
set -e
echo "Starting AI-Driven Health Chatbot..."
uvicorn app:app --host 0.0.0.0 --port 9142 --workers 1
