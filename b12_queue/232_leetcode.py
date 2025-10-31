class MyQueue:

    def __init__(self):
        # Khởi tạo hai stack (dùng list làm stack)
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        # Đẩy vào input_stack
        self.input_stack.append(x)

    def pop(self) -> int:
        # Đảm bảo output_stack có phần tử để pop
        self._move_input_to_output_if_needed()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_input_to_output_if_needed()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return (not self.input_stack) and (not self.output_stack)

    def _move_input_to_output_if_needed(self) -> None:
        # Nếu output_stack rỗng, chuyển tất cả từ input_stack sang output_stack
        if not self.output_stack:
            while self.input_stack:
                val = self.input_stack.pop()
                self.output_stack.append(val)
