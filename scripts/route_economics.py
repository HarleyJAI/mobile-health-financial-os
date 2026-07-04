"""Route economics engine for mobile healthcare operations."""

from dataclasses import dataclass, field
from typing import List, Dict
from unit_economics import AppointmentEconomics


@dataclass
class RouteEconomics:
    route_id: str
    appointments: List[AppointmentEconomics] = field(default_factory=list)
    route_overhead_cost: float = 0.0
    idle_minutes: float = 0.0

    @property
    def appointment_count(self) -> int:
        return len(self.appointments)

    @property
    def revenue(self) -> float:
        return sum(a.revenue for a in self.appointments)

    @property
    def appointment_direct_cost(self) -> float:
        return sum(a.total_direct_cost for a in self.appointments)

    @property
    def total_direct_cost(self) -> float:
        return self.appointment_direct_cost + self.route_overhead_cost

    @property
    def contribution(self) -> float:
        return self.revenue - self.total_direct_cost

    @property
    def contribution_margin_pct(self) -> float:
        return (self.contribution / self.revenue * 100) if self.revenue else 0.0

    @property
    def total_miles(self) -> float:
        return sum(a.miles for a in self.appointments)

    @property
    def total_minutes(self) -> float:
        appointment_minutes = sum(a.drive_minutes + a.clinical_minutes for a in self.appointments)
        return appointment_minutes + self.idle_minutes

    @property
    def total_hours(self) -> float:
        return self.total_minutes / 60

    def summary(self) -> Dict[str, float]:
        return {
            "appointment_count": self.appointment_count,
            "revenue": round(self.revenue, 2),
            "total_direct_cost": round(self.total_direct_cost, 2),
            "contribution": round(self.contribution, 2),
            "contribution_margin_pct": round(self.contribution_margin_pct, 2),
            "total_miles": round(self.total_miles, 2),
            "total_hours": round(self.total_hours, 2),
            "revenue_per_route_hour": round(self.revenue / self.total_hours, 2) if self.total_hours else 0.0,
            "contribution_per_route_hour": round(self.contribution / self.total_hours, 2) if self.total_hours else 0.0,
            "revenue_per_mile": round(self.revenue / self.total_miles, 2) if self.total_miles else 0.0,
            "contribution_per_mile": round(self.contribution / self.total_miles, 2) if self.total_miles else 0.0,
            "miles_per_appointment": round(self.total_miles / self.appointment_count, 2) if self.appointment_count else 0.0,
        }


if __name__ == "__main__":
    route = RouteEconomics(
        route_id="example-route",
        appointments=[
            AppointmentEconomics(revenue=245, clinician_cost=75, mileage_cost=12, drive_minutes=35, clinical_minutes=30, miles=18),
            AppointmentEconomics(revenue=245, clinician_cost=75, mileage_cost=8, drive_minutes=20, clinical_minutes=30, miles=12),
            AppointmentEconomics(revenue=245, clinician_cost=75, mileage_cost=10, drive_minutes=25, clinical_minutes=30, miles=15),
        ],
        route_overhead_cost=20,
        idle_minutes=20,
    )
    print(route.summary())
