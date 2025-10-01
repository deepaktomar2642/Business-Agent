import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from tools import book_meeting, update_crm, create_invoice
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=os.getenv("OPENAI_API_KEY"))

tools = [
    Tool(
        name="BookMeeting",
        func=lambda args: book_meeting(
            title=args.get("title"),
            start_time=args.get("start_time"),
            end_time=args.get("end_time"),
            attendees=args.get("attendees")
        ),
        description="Book a business meeting. Input: dict with title, start_time, end_time, attendees."
    ),
    Tool(
        name="UpdateCRM",
        func=lambda args: update_crm(
            customer_name=args.get("customer_name"),
            details=args.get("details")
        ),
        description="Update CRM for a customer. Input: dict with customer_name, details."
    ),
    Tool(
        name="CreateInvoice",
        func=lambda args: create_invoice(
            customer_name=args.get("customer_name"),
            amount=args.get("amount"),
            description=args.get("description")
        ),
        description="Create an invoice. Input: dict with customer_name, amount, description."
    )
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools,
    llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)
