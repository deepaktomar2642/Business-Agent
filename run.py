from agent_core import agent

if __name__ == "__main__":
    print("Business Agent started. Try example commands:")
    print("1. Book a meeting with Alice tomorrow at 10am for 30 minutes.")
    print("2. Update CRM for Bob with latest order details.")
    print("3. Create an invoice for Carol for $500 consultation.\n")

    while True:
        query = input("Your command: ")
        if query.lower() in ["exit", "quit"]:
            break
        result = agent.run(query)
        print("Agent result:", result)
