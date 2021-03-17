class Solution:
    def interpret(self, command: str) -> str:
        mapping = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }

        position = 0
        result = []
        while position < len(command):
            token = self.get_next_token(command, position)
            if not token:
                break
            result.append(mapping.get(token))
            position += len(token)

        return "".join(result)

    def get_next_token(self, command: str, position: int):
        if position >= len(command):
            return None

        if command[position] == "G":
            return command[position]
        elif command[position + 1] == ")":
            return command[position:position + 2]
        else:
            return command[position:position + 4]


s = Solution()
print(s.interpret("G()(al)"))
print(s.interpret("G()()()()(al)"))