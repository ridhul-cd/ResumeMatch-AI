ResumeMatch-AI

ResumeMatch-AI is a simple Generative AI powered REST API that compares
a resume and a job description and produces a structured match score,
matched skills, missing skills and personalized improvement suggestions.

The project demonstrates how a Large Language Model (LLM) can be used to
analyze unstructured text and generate contextual insights through a
lightweight backend service.

Architecture Overview

Client / UI / Postman
→ FastAPI Backend
→ Prompt Builder
→ OpenAI LLM API
→ Response Parser & Validator
→ JSON Response

Component Responsibilities

Client - Sends resume text and job description text to the API.

FastAPI Backend - Exposes REST endpoints. - Validates incoming requests.

Prompt Builder - Builds a structured prompt using the resume and job
description.

LLM API Layer - Sends the prompt to a Large Language Model. - Receives
generated content.

Response Parser & Validator - Parses the generated output. - Validates
the response structure using Pydantic.

Technology Stack

-   Python 3.10+
-   FastAPI
-   OpenAI API
-   Pydantic
-   python-dotenv

Folder Structure

ResumeMatch-AI/ - main.py : FastAPI application and API endpoints -
llm.py : Prompt creation and LLM API call - schemas.py : Request and
response data models - .env : Environment variables (not committed) -
.gitignore - venv/ : Python virtual environment

How Generative AI Is Used

This project uses a Large Language Model to: - understand and compare
unstructured resume text and job description text - infer skill
relationships and semantic matches - generate new structured outputs
such as match scores, skill gaps and personalized improvement
suggestions

The results are dynamically generated and are not produced using
rule-based or keyword matching logic.

Prerequisites

-   Python 3.10 or later
-   An OpenAI API key

Environment Configuration

Create a file named .env in the project root directory and add:

GEMINI_API_KEY,MODEL_NAME

The application loads environment variables using python-dotenv.

How to Run the Project

1.  Clone the repository

git clone cd ResumeMatch-AI

2.  Create and activate a virtual environment

python -m venv venv

Windows: venv

Linux / macOS: source venv/bin/activate

3.  Install dependencies

pip install fastapi uvicorn openai pydantic python-dotenv

4.  Start the application

 uvicorn app.main:app --reload
 
5.  Access API documentation

http://127.0.0.1:8000/docs

API Endpoint

POST /analyze

Request body:

{ 
  “resume_text”: “Resume content here”, 
  “job_description”: “Jobdescription content here”
}

Response:

{
   “match_score”: 75,
    “matched_skills”: [“Python”, “REST API”],
    “missing_skills”: [“Docker”], 
    “suggestions”: [ “Add experience related to Docker and containerization.” ]
}

Notes

-   The .env file is excluded from version control for security reasons.
-   This project intentionally avoids vector databases, embeddings and
    retrieval pipelines to keep the initial GenAI architecture simple
    and easy to understand.


