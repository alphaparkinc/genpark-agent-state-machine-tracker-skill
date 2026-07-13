from client import AgentStateMachineTrackerClient
client = AgentStateMachineTrackerClient()
print(client.transit("idle", "start"))