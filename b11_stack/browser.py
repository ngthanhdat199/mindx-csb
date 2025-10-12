class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def visit_page(self, url):
        self.back_stack.append(url)
        self.forward_stack.clear()
        print(f"Visiting {url}")

    def back(self):
        if len(self.back_stack) > 1:
            url = self.back_stack.pop()
            self.forward_stack.append(url)
            print(f"Going back to {self.back_stack[-1]}")
        else:
            print("No more pages in back history")

    def forward(self):
        if self.forward_stack:
            url = self.forward_stack.pop()
            self.back_stack.append(url)
            print(f"Going forward to {url}")
        else:
            print("No more pages in forward history")