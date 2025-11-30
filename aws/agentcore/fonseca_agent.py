from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()

@app.entrypoint
def invoke(payload):
    """Your AI agent function"""
    user_message = payload.get("prompt")
    result = Agent()(user_message)
    return {"result": result.message}

if __name__ == "__main__":
    app.run()