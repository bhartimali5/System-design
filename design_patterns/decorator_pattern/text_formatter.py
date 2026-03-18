from abc import ABC, abstractmethod

class TextFormatter(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

## Base component/Concrete Component
class PlainText(TextFormatter):
    def __init__(self, text: str):
        self._text = text
    
    def render(self) -> str:
        return self._text
    
##Base Decorator/Abstract Decorator
class TextDecorator(TextFormatter):
    def __init__(self, wrapped: TextFormatter):
        self._wrapped = wrapped

    def render(self) -> str:
        return self._wrapped.render()

## Concrete Decorators
class UpperCaseFormatter(TextDecorator):
    def render(self) -> str:
        return self._wrapped.render().upper()
    
class ItalicFormatter(TextDecorator):
    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"
    
class BoldFormatter(TextDecorator):
    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"

class UnderlineFormatter(TextDecorator):
    def render(self) -> str:
        return f"<u>{self._wrapped.render()}</u>"
    
class HighlightFormatter(TextDecorator):
    def render(self) -> str:
        return f"<mark>{self._wrapped.render()}</mark>"

if __name__ == "__main__":
    text = PlainText("Hello World")
    print(text.render())

    text = UpperCaseFormatter(PlainText("Hello World"))
    print(text.render())

    text = ItalicFormatter(BoldFormatter(PlainText("Hello World")))
    print(text.render())

    text = UpperCaseFormatter(
            HighlightFormatter(
                BoldFormatter(
                    PlainText("hello world")
                )
            )
        )
    print(text.render())