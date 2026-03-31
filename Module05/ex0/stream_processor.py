from abc import ABC, abstractmethod
from typing import Any, List


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
                if type(item) not in (int, float):
                    return False
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid data type for NumericProcessor")
            values: int = 0
            total: int = 0
            avg: float = 0
            for x in data:
                values += 1
                total += x
            if values > 0:
                avg = total / values
            else:
                avg = 0.0
            return (
                f"Processed {values} numeric values, sum={total}, avg={avg}"
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


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    np = NumericProcessor()
    data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    print("Validation: Numeric data verified")
    print(np.format_output(np.process(data)))
    print()

    print("Initializing Text Processor...")
    text = TextProcessor()
    print('Processing data: "Hello Nexus World"')
    result = text.process("Hello Nexus World")
    print("Validation: Text data verified")
    print(text.format_output(result))

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    print('Processing data: "ERROR: Connection timeout"')
    result = log.process("ERROR: Connection timeout")
    print("Validation: Log entry verified")
    print(log.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    print("\nProcessing multiple data types through same interface...")

    processors: List[DataProcessor] = [
            NumericProcessor(),
            TextProcessor(),
            LogProcessor()
        ]

    data_samples: List[Any] = [
            [1, 2, 3],
            "Hello World",
            "INFO: System ready"
        ]

    index: int = 0
    count: int = 1

    while index < 3:
        result = processors[index].process(data_samples[index])
        print(f"Result {count}: "
              f"{processors[index].format_output(result)}")
        index += 1
        count += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
