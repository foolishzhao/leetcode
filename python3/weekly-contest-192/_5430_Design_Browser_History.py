class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.step = 1

    def visit(self, url: str) -> None:
        self.history = self.history[:self.step]
        self.history.append(url)
        self.step += 1

    def back(self, steps: int) -> str:
        self.step = max(self.step - steps, 1)
        return self.history[self.step - 1]

    def forward(self, steps: int) -> str:
        self.step = min(self.step + steps, len(self.history))
        return self.history[self.step - 1]
