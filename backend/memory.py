conversation = []


class Memory:

    @staticmethod
    def store(user_input, assistant_reply):

        conversation.append({
            "role": "user",
            "content": str(user_input)
        })

        conversation.append({
            "role": "assistant",
            "content": str(assistant_reply)
        })

    @staticmethod
    def retrieve(limit=10):

        return conversation[-limit:]