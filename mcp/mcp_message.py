import uuid

def create_mcp_message(sender, receiver, type_, payload):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": type_,
        "trace_id": str(uuid.uuid4()),
        "payload": payload
    }
