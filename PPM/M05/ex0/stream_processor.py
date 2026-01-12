"""A module for processing data streams."""

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """A class for processing data streams."""
    def __init__(self, data: Any) -> None:
        """Initialize the DataProcessor."""
        self.data = data

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the input data."""

    @abstractmethod
    def process_data(self, data: Any) -> str:
        """Process the input data."""

    def format_output(self, result: str) -> str:
        """Format the output result."""


class NumericProcessor(DataProcessor):
    """A processor for numerical data streams."""

    def __init__(self, data: Any) -> None:
        """Initialize the NumericProcessor."""
        super().__init__(data)
        self.data = data

    def process(self, data: Any) -> str:
        """Process numerical data."""
        print("\nInitializing Numeric Processor...")
        if not self.validate(data):
            return
        print("Validation: Numeric data verified")
        tsum: int = sum(i for i in data)
        avg: float = tsum / (len(data))
        result = (tsum, avg, len(data))
        self.format_output(result)

    def process_data(self, data: Any) -> str:
        """Process numerical data."""
        if not self.validate(data):
            return
        tsum: int = sum(i for i in data)
        avg: float = tsum / (len(data))
        result = (tsum, avg, len(data))
        self.format_output(result)

    def validate(self, data: Any) -> bool:
        """Validate numerical data."""
        if type(data) is not list:
            return False
        for i in data:
            if type(i) is not int and type(i) is not float:
                return False
        if len(data) == 0:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Format the output result for numerical data."""
        (tsum, avg, length) = result
        print(f"Output: Processed "
              f"{length} numeric values, sum={tsum}, avg={avg}")


class TextProcessor(DataProcessor):
    """A processor for text data streams."""

    def __init__(self, data: Any) -> None:
        """Initialize the TextProcessor."""
        super().__init__(data)
        self.data = data

    def process(self, data: Any) -> str:
        """Process text data."""
        print("\nInitializing Text Processor...")
        if not self.validate(data):
            return
        print("Validation: Text data verified")
        splitted = data.split()
        txt_length = len(data)
        split_length = len(splitted)
        result = (txt_length, split_length)
        self.format_output(result)

    def process_data(self, data: Any) -> str:
        """Process text data."""
        if not self.validate(data):
            return
        splitted = data.split()
        txt_length = len(data)
        split_length = len(splitted)
        result = (txt_length, split_length)
        self.format_output(result)

    def validate(self, data: Any) -> bool:
        """Validate text data."""
        if type(data) is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Format the output result for text data."""
        (txt_length, split_length) = result
        print(f"Output: Processed text: "
              f"{txt_length} characters, {split_length} words")


class LogProcessor(DataProcessor):
    """A processor for text data streams."""

    def __init__(self, data: Any) -> None:
        """Initialize the TextProcessor."""
        super().__init__(data)
        self.data = data

    def process(self, data: Any) -> str:
        """Process text data."""
        print("\nInitializing Log Processor...\n")
        print(f"Processing data: '{data}'")
        if not self.validate(data):
            return
        print("Validation: Log data verified")
        splitted = data.split()
        log_level = splitted[0]
        self.format_output(log_level)

    def process_data(self, data: Any) -> str:
        """Process text data."""
        if not self.validate(data):
            return
        splitted = data.split()
        log_level = splitted[3]
        self.format_output(log_level)

    def validate(self, data: Any) -> bool:
        """Validate text data."""
        if type(data) is not str:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Format the output result for text data."""
        print(f"Output: [ALERT] {result} level detected: "
              f"Connection timeout")


def polymorphic_process(data: Any) -> None:
    """Process data using a polymorphic DataProcessor."""
    match data:
        case list():
            num_process = NumericProcessor(data)
            polymorphic_process.count += 1
            print(f"Result {polymorphic_process.count}:", end=" ")
            num_process.process_data(data)
        case str():
            if "ERROR" in data:
                log_process = LogProcessor(data)
                polymorphic_process.count += 1
                print(f"Result {polymorphic_process.count}:", end=" ")
                log_process.process_data(data)
            else:
                text_process = TextProcessor(data)
                polymorphic_process.count += 1
                print(f"Result {polymorphic_process.count}:", end=" ")
                text_process.process_data(data)
        case _:
            print("Invalid data type")


def main() -> None:
    """Entry point for the stream processor application."""
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===")

    num_data = [1, 2, 3, 4, 5]
    num_process = NumericProcessor(num_data)
    num_process.process(num_data)

    text_data = "Hello Nexus World"
    text_process = TextProcessor(text_data)
    text_process.process(text_data)

    log_data = "ERROR : Connection timeout"
    log_process = LogProcessor(log_data)
    log_process.process(log_data)

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    polymorphic_process.count = 0
    polymorphic_process([data * 2 for data in num_data])
    polymorphic_process(text_data)
    polymorphic_process(log_data)


if __name__ == "__main__":
    main()
