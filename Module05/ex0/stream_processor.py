from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return "Output: " + result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            for item in data:
                float(item)
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            counter: int = 0
            total: int = 0
            avg: float = 0
            for x in data:
                counter += 1
                total += x
            if counter > 0:
                avg = total / counter
            else:
                avg = 0.0
            return (
                f"Processed {counter} numeric values, sum={total}, avg={avg}"
            )
        else:
            raise ValueError("Invalid data type for NumericProcessor")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            data + ""
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if self.validate(data):

            counter: int = 0
            words: int = 0
            in_word: bool = False

            for char in data:
                counter += 1

                if char != " " and not in_word:
                    words += 1
                    in_word = True
                elif char == " ":
                    in_word = False

            return (
                f"Processed text: {counter} characters, {words} words"
            )
        else:
            raise ValueError("Invalid data type for TextProcessor")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Processor...")


if __name__ == "__main__":
    main()
