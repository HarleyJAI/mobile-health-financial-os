"""Contract profitability and working-capital engine for mobile healthcare."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class ContractEconomics:
    price_per_service: float
    monthly_volume: float
    direct_cost_per_service: float
    monthly_admin_cost: float = 0.0
    monthly_technology_cost: float = 0.0
    other_monthly_cost: float = 0.0
    startup_cost: float = 0.0
    payment_terms_days: int = 0
    cancellation_rate_pct: float = 0.0
    recollection_rate_pct: float = 0.0
    recollection_cost: float = 0.0

    @property
    def completed_volume(self) -> float:
        return self.monthly_volume * (1 - self.cancellation_rate_pct / 100)

    @property
    def monthly_revenue(self) -> float:
        return self.completed_volume * self.price_per_service

    @property
    def service_direct_cost(self) -> float:
        return self.completed_volume * self.direct_cost_per_service

    @property
    def expected_recollection_cost(self) -> float:
        return self.completed_volume * (self.recollection_rate_pct / 100) * self.recollection_cost

    @property
    def fixed_monthly_cost(self) -> float:
        return self.monthly_admin_cost + self.monthly_technology_cost + self.other_monthly_cost

    @property
    def monthly_contribution(self) -> float:
        return self.monthly_revenue - self.service_direct_cost - self.expected_recollection_cost - self.fixed_monthly_cost

    @property
    def contribution_margin_pct(self) -> float:
        return (self.monthly_contribution / self.monthly_revenue * 100) if self.monthly_revenue else 0.0

    @property
    def contribution_per_completed_service(self) -> float:
        return (self.monthly_contribution / self.completed_volume) if self.completed_volume else 0.0

    @property
    def break_even_completed_volume(self) -> float:
        variable_contribution = self.price_per_service - self.direct_cost_per_service - ((self.recollection_rate_pct / 100) * self.recollection_cost)
        return (self.fixed_monthly_cost / variable_contribution) if variable_contribution > 0 else float("inf")

    @property
    def estimated_working_capital_requirement(self) -> float:
        daily_operating_cost = (self.service_direct_cost + self.expected_recollection_cost + self.fixed_monthly_cost) / 30
        return daily_operating_cost * self.payment_terms_days

    @property
    def startup_payback_months(self) -> float:
        return (self.startup_cost / self.monthly_contribution) if self.monthly_contribution > 0 else float("inf")

    def summary(self) -> Dict[str, float]:
        return {
            "completed_volume": round(self.completed_volume, 2),
            "monthly_revenue": round(self.monthly_revenue, 2),
            "monthly_contribution": round(self.monthly_contribution, 2),
            "contribution_margin_pct": round(self.contribution_margin_pct, 2),
            "contribution_per_completed_service": round(self.contribution_per_completed_service, 2),
            "break_even_completed_volume": round(self.break_even_completed_volume, 2),
            "estimated_working_capital_requirement": round(self.estimated_working_capital_requirement, 2),
            "startup_payback_months": round(self.startup_payback_months, 2),
        }


if __name__ == "__main__":
    example = ContractEconomics(
        price_per_service=245,
        monthly_volume=60,
        direct_cost_per_service=105,
        monthly_admin_cost=1200,
        startup_cost=3000,
        payment_terms_days=30,
        cancellation_rate_pct=8,
        recollection_rate_pct=2,
        recollection_cost=125,
    )
    print(example.summary())
