from backend import orchestrator
def generateResponse(user_input):
    return orchestrator.process(user_input)