class AgentStateMachineTrackerClient:
    def transit(self, current_state: str, action: str) -> dict:
        return {"next_state": "completed" if action == "finish" else "processing"}