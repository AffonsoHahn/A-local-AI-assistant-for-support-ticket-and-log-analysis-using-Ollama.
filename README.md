AI Log/Ticket Analysis Assistant



A Python CLI tool that uses a local language model to analyze support tickets and application logs, classify issues, suggest probable causes, and recommend troubleshooting steps.



Features



Structured analysis: summary, category, evidence, probable cause, confidence, next checks, missing context, and limitations.



Local AI inference using Ollama.



No paid API calls required when using the configured local model.



Input validation and a maximum input length of 15,000 characters.



Unit tests that run without API credits.



Requirements



Windows, macOS, or Linux



Python 3.10 or newer



Ollama



The local model llama3.2:3b



Setup on Windows (PowerShell)



Install Python and Ollama.



Open PowerShell in the project folder.



Create a virtual environment if needed:



py -m venv .venv



Install the Python dependencies:



.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt



Download the local model:



ollama pull llama3.2:3b



Confirm the model is available:



ollama list



Start the application:



.\\.venv\\Scripts\\python.exe main.py



Paste a fictional or sanitized support ticket or log. Type END on its own line to submit the input. Type EXIT on the first line to quit.



Ollama must be running locally while the application is in use. The default endpoint is http://localhost:11434/api/chat.



Run local tests



.\\.venv\\Scripts\\python.exe -m unittest discover -s tests -v



The unit tests should not require API credits.



Example input



Our reporting integration receives HTTP 401 from GET /api/v1/reports after a deployment. The request has an Authorization header, but we have not confirmed whether the token is expired or has the required scope.

END



Security and limitations



Use fictional or sanitized examples.



Never commit .env, API keys, passwords, access tokens, or confidential logs.



The application sends prompts to the local Ollama service instead of a paid OpenAI API. Avoid entering sensitive information, and validate the model's recommendations before acting on them.



The model's probable cause is a hypothesis, not a confirmed root cause. Validate recommendations against logs, system configuration, and product documentation.



The prototype does not connect to a ticketing system, inspect production environments, or automatically change systems.



Model quality and response speed depend on the local model and available hardware.



Suggested improvements



Add more labeled test cases and measure classification accuracy.



Add structured JSON output and automated validation.



Add a Streamlit interface.



Add CI tests with GitHub Actions.



Document false positives and missing-context cases.



Tech stack



Python, Ollama, local LLM inference, JSON, unittest, Git/GitHub.
