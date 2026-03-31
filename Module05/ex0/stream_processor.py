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
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            for item in data:
                float(item)
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data type for NumericProcessor")
            values: int = 0
            sum: int = 0
            avg: float = 0
            for x in data:
                values += 1
                sum += x
            if values > 0:
                avg = sum / values
            else:
                avg = 0.0
            return (
                f"Processed {values} numeric values, sum={sum}, avg={avg}"
            )
        except ValueError as e:
            return f"Error: {e}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            data + ""
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data type for TextProcessor")

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
        except ValueError as e:
            return f"Error: {e}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            data + ""
            if data == "":
                return False
            if ":" not in data:
                return False
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            level: str = ""
            message: str = ""
            sep: bool = False
            in_message: bool = False

            for char in data:
                if not sep:
                    if char == ":":
                        sep = True
                    else:
                        level += char
                else:
                    if not in_message:
                        if char != " ":
                            message += char
                            in_message = True
                    else:
                        message += char

            if level == "ERROR":
                return "[ALERT] ERROR level detected: " + message

            if level == "WARNING":
                return "[WARNING] WARNING level detected: " + message

            return "[INFO] INFO level detected: " + message

        except Exception as error:
            return f"LogProcessor error: {error}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Processor...")

    print("Initializing Text Processor...")

    print("Initializing Log Processor...")


if __name__ == "__main__":
    main()
