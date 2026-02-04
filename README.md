\# AI Ops Assistant — GenAI Intern Assignment



\## Overview



This project is an AI-powered Ops Assistant that accepts natural language tasks, plans execution steps using an LLM, calls real APIs, verifies results, and returns a formatted final response.



It demonstrates multi-agent design and real-world API orchestration.



---



\## Architecture



The system uses three agents:



1\. Planner Agent  

\- Uses Groq LLM to convert user tasks into structured JSON plans



2\. Executor Agent  

\- Executes tool calls based on planner output  

\- Integrates GitHub API and OpenWeather API  



3\. Verifier Agent  

\- Validates execution results  

\- Formats final readable response  



Flow:



User Task → Planner → Executor → Verifier → Final Output



---



\## Integrated APIs



\- Groq LLM API  

\- GitHub REST API  

\- OpenWeather API  



---



\## Environment Variables

Create a `.env` file (do NOT commit it).  
Use `.env.example` as a reference.

Required variables:

GROQ_API_KEY=your_groq_api_key_here  
WEATHER_API_KEY=your_openweather_api_key_here




---



\## Setup Instructions



\### 1. Clone Repository



git clone <your-github-repo-url>

cd ai\_ops\_assistant





---



\### 2. Create Virtual Environment



python -m venv venv





Activate:



Windows:

venv\\Scripts\\activate





Mac/Linux:

source venv/bin/activate





---



\### 3. Install Dependencies



pip install -r requirements.txt





---



\### 4. Run the Project



Run server locally using one command:



uvicorn main:app --reload





---



\### 5. Open API Interface



Open browser:



http://127.0.0.1:8000/docs





Use POST `/run` endpoint.



---



\## Example Prompts To Test



Use these example inputs:



1\. Find trending GitHub repositories and weather in Mumbai  

2\. Get trending GitHub repos and weather in Delhi  

3\. Show popular GitHub projects and weather in Bangalore  

4\. Fetch GitHub trending repositories and weather in Chennai  

5\. Get GitHub repos and weather in Hyderabad  



---



\## Known Limitations / Tradeoffs



\- No caching implemented  

\- API rate limits depend on provider limits  

\- Sequential tool execution  

\- No database persistence  

\- No frontend UI (API-only backend service)  



---



\## Project Output



The system returns:



\- Structured execution plan  

\- Live GitHub repository data  

\- Live weather information  

\- Verified formatted final response  



---



\## Author



Srishti Nehra  

GenAI Intern Assignment Submission



