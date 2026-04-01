from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.batches_processed: int = 0
        self.items_processed: int = 0
        self.failures: int = 0

        @abstractmethod
        def process_batch(self, data_batch: List[Any]) -> str:
            pass

        def filter_data(
                self,
                data_batch: List[Any],
                criteria: Optional[str] = None
                ) -> List[Any]:
            if criteria is None:
                return data_batch
            return [
                item for item in data_batch
                if isinstance(item, str) and criteria.lower() in item.lower()
            ]

        def get_stats(self) -> Dict[str, Union[str, int, float]]:
            return {
                "stream_id": self.stream_id,
                "type": self.stream_type,
                "batches_processed": self.batches_processed,
                "items_processed": self.items_processed,
                "failures": self.failures
            }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.batches_processed += 1
            self.items_processed += len(data_batch)

            temperatures: list[float] = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    value = float(item.split(":", 1)[1])
                temperatures.append(value)

            if len(temperatures) == 0:
                return f"Sensor analysis: {len(data_batch)} readings processed"

            avg_temp = sum(temperatures) / len(temperatures)
            return (
                f"Sensor analysis: {len(data_batch)} readings processed,"
                f"avg temp: {avg_temp:.1f}°C"
            )
        except Exception:
            self.failures += 1
            return "Sensor processing failed"

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            result: list[Any] = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    value = float(item.split(":", 1)[1])
                    if value >= 30:
                        result.append(item)
            return result
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.batches_processed += 1
            self.items_processed += len(data_batch)

            count = 0
            net_flow = 0
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    action, value = item.split(":", 1)
                    value_int = int(value)

                    if action == "buy":
                        net_flow += value_int
                        count += 1
                    elif action == "sell":
                        net_flow -= value_int
                        count += 1

            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {net_flow:+d} units"
            )
        except Exception:
            self.failures += 1
            return "Transaction processing failed"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")


if __name__ == "__main__":
    main()
