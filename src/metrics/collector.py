"""Metrics collection and reporting for antimicrobial-resistance-tracker."""
import time
import logging
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class MetricPoint:
    name: str
    value: float
    timestamp: float = field(default_factory=time.time)
    tags: Dict[str, str] = field(default_factory=dict)


class DataQualityMetrics:
    """Collect, aggregate, and report data quality metrics."""

    def __init__(self, namespace: str = "antimicrobial-resistance-tracker"):
        self.namespace = namespace
        self._completeness: Dict[str, List[float]] = defaultdict(list)
        self._consistency: Dict[str, List[float]] = defaultdict(list)
        self._timeliness: Dict[str, List[float]] = defaultdict(list)
        self._accuracy: Dict[str, List[float]] = defaultdict(list)
        self._start_time = time.time()

    def record_completeness(self, data_source: str, value: float):
        self._completeness[data_source].append(value)

    def record_consistency(self, data_source: str, value: float):
        self._consistency[data_source].append(value)

    def record_timeliness(self, data_source: str, value: float):
        self._timeliness[data_source].append(value)

    def record_accuracy(self, data_source: str, value: float):
        self._accuracy[data_source].append(value)

    def get_quality_summary(self) -> Dict[str, Any]:
        summary = {
            "namespace": self.namespace,
            "uptime_seconds": time.time() - self._start_time,
            "data_sources": {},
        }

        for data_source in set(list(self._completeness.keys()) + list(self._consistency.keys()) + list(self._timeliness.keys()) + list(self._accuracy.keys())):
            completeness_values = self._completeness[data_source] if data_source in self._completeness else []
            consistency_values = self._consistency[data_source] if data_source in self._consistency else []
            timeliness_values = self._timeliness[data_source] if data_source in self._timeliness else []
            accuracy_values = self._accuracy[data_source] if data_source in self._accuracy else []

            completeness_score = self._calculate_dimension_score(completeness_values)
            consistency_score = self._calculate_dimension_score(consistency_values)
            timeliness_score = self._calculate_dimension_score(timeliness_values)
            accuracy_score = self._calculate_dimension_score(accuracy_values)

            overall_score = (completeness_score + consistency_score + timeliness_score + accuracy_score) / 4

            summary["data_sources"][data_source] = {
                "completeness": completeness_score,
                "consistency": consistency_score,
                "timeliness": timeliness_score,
                "accuracy": accuracy_score,
                "overall_score": overall_score,
            }

        return summary

    def _calculate_dimension_score(self, values: List[float]) -> float:
        """Calculates a score (0-100) for a given dimension."""
        if not values:
            return 0.0
        average = sum(values) / len(values)
        return max(0.0, min(100.0, average))  # Ensure score is between 0 and 100

    def reset(self):
        self._completeness.clear()
        self._consistency.clear()
        self._timeliness.clear()
        self._accuracy.clear()
        self._start_time = time.time()