
🤖 Understanding Key Concepts in OpenAI Agent SDK

This README outlines the core ideas behind OpenAI Agent SDK in a beginner-friendly way. We'll break down concepts like the Agent class, @dataclass, system prompts via instructions, the Runner class, and Python Generics with TContext.

📘 Q1: Why is the Agent class a dataclass?

Using @dataclass makes it easier to build classes that mainly hold data (like the agent's name, tools, etc.). It auto-generates methods like __init__, __repr__, and others to simplify your code.

🧪 Example:

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_number: int
    grade: str

# Creating a student object
student1 = Student(name="Ahmed", roll_number=101, grade="A")

# Printing student details
print(student1)

#output  Student(name='Ahmed', roll_number=101, grade='A')

📘 Q2(a): What are instructions in the Agent class and why can they be callable?

instructions work as the system prompt — telling the agent how to respond.

It can be:

A string like "Be helpful."

A function that generates a prompt based on context.

The Agent class can also implement __call__, allowing this usage:

agent("Hi")

This makes agents behave like functions — very intuitive!

📘 Q2(b): Why is the user prompt passed to Runner.run() and why is it a @classmethod?

You provide your query/input to Runner.

Runner delivers it to the agent.

Agent uses its instructions to form a reply.

Why use @classmethod?

You can call it like this:

Runner.run("Hello Agent")

No need to make an instance first.

Keeps usage neat and simple.

📘 Q3: What is the role of the Runner class?

The Runner acts as a coordinator that manages how agents operate when given an input.

💡 Responsibilities:

Accepts the user prompt

Combines it with the agent’s instructions

Executes the agent and returns a reply

✅ Benefits:

Keeps logic organized

Simplifies agent usage

Separates the agent’s logic from how it’s triggered

📘 Q4: What are Generics in Python and why use them with TContext?

What are Generics?

Allow classes/functions to work with any data type while keeping type checking.

Used via the typing module:

from typing import TypeVar, Generic

T = TypeVar('T')

from typing import TypeVar, Generic

T = TypeVar('T')  # T koi bhi type ho sakta hai

class StorageBox(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item

# Creating boxes for different types of items
pen_box = StorageBox("Blue Pen")
number_box = StorageBox(100)
tools_box = StorageBox(["Hammer", "Wrench", "Screwdriver"])

print("Pen:", pen_box.get_item())
print("Number:", number_box.get_item())
print("Tools:", tools_box.get_item())


Why use for TContext?

TContext allows agents to work with any context type (e.g., string, dict).

Ensures the agent knows what kind of context it's dealing with.

Helps catch type errors early — before execution.

🏁 Quick Recap

Concept

Role & Benefit

@dataclass

Easy class creation for storing data

instructions

System prompt guiding agent behavior

__call__

Use agents like functions

Runner.run()

Cleanly run the agent with user input

Generics (TContext)

Write flexible, type-safe code

This setup enables powerful, modular, and beginner-friendly agent workflows in OpenAI's Agent SDK. 🚀

