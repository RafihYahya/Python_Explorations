"""
This module provides functionality for processing and managing data streams.
"""
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data stream processing."""
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of data from the stream.

        This method must be implemented by subclasses
        to define specific batch processing logic.

        Args:
            data_batch: A list of data items to
            be processed in the current batch.

        Returns:
            A string representing the result
            or status of the batch processing.
        """
    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str]
            ) -> str:
        """
        Filters the data batch based on a given criteria.
        """
        out_str = ""
        if criteria is None:
            return "Criteria Not Satisfied, Aborting from Life"
        keywords = criteria.split()
        for data in data_batch:
            for keyword in keywords:
                if keyword in data:
                    out_str += " " + data
        return out_str

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieves statistics about the data stream.
        """


class SensorStream(DataStream):
    """Concrete implementation of DataStream for sensor data."""
    streams_data = ""

    def __init__(self, stream_id):
        super().__init__()
        self.stream_id = stream_id
        print("\nInitializing Sensor Stream...")
        print(f"Sensor Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of data from the stream.
        """
        data_batch_length = len(data_batch)
        self.streams_data = self.filter_data(data_batch, "temp")
        dict_data = self.get_stats()
        return (f"Sensor analysis: {data_batch_length} readings processed, "
                f"avg {dict_data['tmp']}C")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieves statistics about the data stream.
        """
        returned_dict = {}
        returned_dict["stream_id"] = self.stream_id
        returned_dict["tmp"] = self.streams_data.split(":")[1]
        return returned_dict


class TransactionStream(DataStream):
    """Concrete implementation of DataStream for transaction data."""
    transaction_data = ""

    def __init__(self, stream_id):
        super().__init__()
        self.stream_id = stream_id
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of data from the stream.
        """
        data_batch_length = len(data_batch)
        self.transaction_data = self.filter_data(data_batch, "buy sell")
        stats = self.get_stats()
        return (
            f"Transaction analysis: {data_batch_length} operations, "
            f"net flow: {stats['net_flow']:+} units"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieves statistics about the data stream.
        """
        returned_dict = {}
        net_buy = 0
        net_sell = 0
        returned_dict["stream_id"] = self.stream_id
        for transaction in self.transaction_data.split():
            if transaction.startswith("buy"):
                net_buy += int(transaction.split(":")[1])
            elif transaction.startswith("sell"):
                net_sell += int(transaction.split(":")[1])
        returned_dict["net_flow"] = net_buy - net_sell
        return returned_dict


class EventStream(DataStream):
    """Concrete implementation of DataStream for event data."""
    filtered_data = ""

    def __init__(self, stream_id):
        super().__init__()
        self.stream_id = stream_id
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Processes a batch of data from the stream.
        """
        data_batch_length = len(data_batch)
        self.filtered_data = self.filter_data(data_batch, "error")
        stats = self.get_stats()
        return (f"Event analysis: {data_batch_length} events,"
                f" {stats['error_count']} error detected")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Retrieves statistics about the data stream.
        """
        returned_dict = {}
        returned_dict["stream_id"] = self.stream_id
        error_count = self.filtered_data.count("error")
        returned_dict["error_count"] = error_count
        return returned_dict


class StreamProcessor:
    """Manages and processes multiple data streams."""

    def __init__(self):
        self.streams: List[DataStream] = []
        self.streams_data: List[Any] = []

    def add_stream(self, stream: DataStream, data_batch: List[Any]):
        """
        Adds a DataStream object to the processor's list of streams.

        Args:
            stream: The DataStream object to be added.
            data_batch: The data associated with the stream.
        """
        try:
            self.streams.append(stream)
            self.streams_data.append(data_batch)
        except TypeError as e:
            print(f"Error: {e}")

    def batch_process(self) -> List[str]:
        """
        Processes data from all added streams and returns the results.
        """
        try:
            results = []
            for i, stream in enumerate(self.streams):
                results.append(stream.process_batch(self.streams_data[i]))
            return results
        except AttributeError as e:
            print(f"Error: {e}")

    def batch_filter(self, criteria: List[str]):
        """
        Filters data for all added streams based on a specified criteria.

        This method iterates through each stream in the processor,
        applies a filtering operation using the stream's `filter_data` method,
        and collects the results.

        Args:
            criteria: The filtering criteria to be applied to each
            stream's data.

        Returns:
            A list of strings, where each string represents the
            filtered data from a respective stream.
        """
        results = []
        for i, stream in enumerate(self.streams):
            results.append(stream.filter_data(self.streams_data[i], criteria))
        return results


sensor_data: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
trans_data = ["buy:100", "sell:150", "buy:75"]
event_data = ["login", "error", "logout"]


def main():
    """
    Demonstrates processing of various data streams.
    """
    print("=== CODE NEXUS- POLYMORPHIC STREAM SYSTEM ===")

    # Sensor Stream
    sensor_process = SensorStream("SENSOR_001")
    print(f"Processing sensor batch: {sensor_data}")
    sensor_result = sensor_process.process_batch(sensor_data)
    print(sensor_result)

    # Transaction Stream
    trans_process = TransactionStream("TRANS_001")
    print(f"\nProcessing transaction batch: {trans_data}")
    trans_result = trans_process.process_batch(trans_data)
    print(trans_result)

    # Event Stream
    event_process = EventStream("EVENT_001")
    print(f"\nProcessing event batch: {event_data}")
    event_result = event_process.process_batch(event_data)
    print(event_result)

    print("\n=== Polymorphic Stream Processing ===\n")
    stream_processor = StreamProcessor()
    stream_processor.add_stream(sensor_process, sensor_data)
    stream_processor.add_stream(trans_process, trans_data)
    stream_processor.add_stream(event_process, event_data)

    try:
        batch_results = stream_processor.batch_process()
        print("Batch Result: ")
        for result in batch_results:
            print(" " + "- " + result)
        try:
            print("\nStream filtering active: High-priority data only")
            filter_data_res = stream_processor.batch_filter("temp buy sell")
            sensor_count = len(filter_data_res[0].split(' ')) - 1
            trans_count = len(filter_data_res[1].split(' ')) - 1
            print(
                 "Filtered results: "
                 f"{sensor_count} critical sensor alerts, "
                 f"{trans_count} large transaction"
                 )
        except (AttributeError, ValueError, TypeError) as e:
            print(f"Error: {e}")
            print("Filtering Errors found")
        print(
            "\nAll streams processed successfully. Nexus throughput optimal."
            )
        return
    except AttributeError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    print("\nStream processing completed. With Some Errors")


if __name__ == "__main__":
    main()
