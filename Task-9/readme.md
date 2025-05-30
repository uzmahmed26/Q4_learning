# 🤖 Tool Calling, Function Calling & MCP in AI

This project explains the core concepts of **Tool Calling**, **Function Calling**, and **MCP (Model Context Protocol)** used in modern LLMs like OpenAI's GPT-4.

---

## 📌 What is Function Calling?

Function Calling allows the model to **call external tools or functions** based on user instructions.

### Example:
User: "What's the weather in Islamabad?"

Model identifies:
```python
getWeather(city="Islamabad")
Then calls the tool and returns:

json
Copy
Edit
{
  "temperature": "30°C",
  "description": "Sunny in Lahore"
}
🔧 What is a Tool Function?
A tool function is any external capability (API or local function) that helps the AI do something instead of just replying.

Examples:
getWeather(city)

searchWeb(query)

sendEmail(to, message)

📦 What is MCP (Model Context Protocol)?
MCP stands for Model Context Protocol – a JSON structure that:

Describes available tools

Defines function parameters

Helps the model safely use tools

Example:
json
Copy
Edit
{
  "name": "getWeather",
  "description": "Get current weather of a city",
  "parameters": {
    "type": "object",
    "properties": {
      "city": { "type": "string" }
    },
    "required": ["city"]
  }
}
🚀 Why is Tool Calling Useful?
Feature	Benefit
🔗 Real-time API access	Weather, Stock, Flight Booking
🤖 Actionable responses	Bookings, Emails, Tasks
🧠 Smarter assistants	Personalized, Real-world help
💼 Enterprise apps	Workflow automation

🛠 Sample Project Idea
Use OpenAI's function_calling feature

Connect GPT with OpenWeatherMap API

Build a weather chatbot using Flask / FastAPI

📚 Related Topics
Agents and Tools in LangChain

OpenAI's Function Calling Docs

LLM Tool Integration
Made with 💡 by [Uzma Ahmed]
AI & Web Developer | (https://www.linkedin.com/in/uzma-ahmed-3557402ba/) 
