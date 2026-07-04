"""Core unit economics calculations for mobile health appointments.

This module intentionally uses only the Python standard library so the first
version can run anywhere. It contains no patient data and no company-specific
pricing assumptions.
"""

from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class AppointmentEconomics:
    revenue: float
    clinician_cost: float = 0.0
    travel_time_cost: float = 0.0
    mileage_cost: float = 0.0
    supplies_cost: float = 0.0
    processing_cost: float = 0.0
    shipping_cost: float = 0.0
    parking_tolls: float = 0.0
    merchant_fees: float = 0.0
    expected_recollection_cost: float = 0.0
    other_direct_cost: float = 0.0
    drive_minutes: float = 0.0
    clinical_minutes: float = 0.0
    miles: float = 0.0

    @property
    def total_direct_cost(self) -> float:
        return sum([
            self.clinician_cost,
            self.travel_time_cost,
            self.mileage_cost,
            self.supplies_cost,
            self.processing_cost,
            self.shipping_cost,
            self.parking_tolls,
            self.merchant_fees,
            self.expected_recollection_cost,
            self.other_direct_cost,
        ])

    @property
    def contribution_margin(self) -> float:
        return self.revenue - self.total_direct_cost

    @property
    def contribution_margin_pct(self) -> float:
        return (self.contribution_margin / self.revenue * 100) if self.revenue else 0.0

    @property
    def total_service_hours(self) -> float:
        return (self.drive_minutes + self.clinical_minutes) / 60

    @property
    def revenue_per_service_hour(self) -> float:
        return (self.revenue / self.total_service_hours) if self.total_service_hours else 0.0

    @property
    def contribution_per_service_hour(self) -> float:
        return (self.contribution_margin / self.total_service_hours) if self.total_service_hours else 0.0

    @property
    def revenue_per_mile(self) -> float:
        return (self.revenue / self.miles) if self.miles else 0.0

    def summary(self) -> Dict[str, float]:
        return {
            "revenue": round(self.revenue, 2),
            "total_direct_cost": round(self.total_direct_cost, 2),
            "contribution_margin": round(self.contribution_margin, 2),
            "contribution_margin_pct": round(self.contribution_margin_pct, 2),
            "total_service_hours": round(self.total_service_hours, 2),
            "revenue_per_service_hour": round(self.revenue_per_service_hour, 2),
            "contribution_per_service_hour": round(self.contribution_per_service_hour, 2),
            "revenue_per_mile": round(self.revenue_per_mile, 2),
        }


if __name__ == "__main__":
    example = AppointmentEconomics(
        revenue=245.00,
        clinician_cost=75.00,
        mileage_cost=18.00,
        supplies_cost=8.00,
        merchant_fees=7.35,
        drive_minutes=60,
        clinical_minutes=30,
        miles=35,
    )
    print(example.summary())
