# Mobile Health Financial OS

An open financial intelligence framework for mobile healthcare, field-based clinical services, decentralized diagnostics, mobile phlebotomy, clinical trials, corporate wellness, specialty specimen collection, concierge health, and related healthcare access models.

## Mission

Turn mobile healthcare operating data into better financial decisions.

This repository treats a mobile health company as both a healthcare organization and a distributed logistics network. The system analyzes five economic levels:

1. Appointment economics
2. Route economics
3. Contract economics
4. Market economics
5. Platform economics

## Architecture

```text
mobile-health-financial-os/
├── SKILL.md
├── README.md
├── domains/mobile-health/
│   └── MOBILE-HEALTH-CONTEXT.md
├── schemas/
│   ├── appointment.schema.json
│   └── appointment-data-dictionary.md
├── scripts/
│   └── unit_economics.py
├── templates/
│   └── opportunity-analysis.md
└── companies/
    └── README.md
```

## Privacy Architecture

The public repository contains reusable methodology, schemas, calculation logic, and templates. Company-specific pricing, contracts, margins, customer data, and protected operating information should remain in a separate private repository or private data layer.

Never commit PHI, patient identifiers, credentials, API keys, bank data, tax records, or confidential customer contracts to this public repository.

## Core Financial Model

The appointment is the basic transaction. The route is the operational unit. The contract is the commercial unit. The market is the expansion unit. The platform is the enterprise-value unit.

## Initial Metrics

- Revenue per appointment
- Contribution per appointment
- Contribution margin percentage
- Revenue per clinical hour
- Contribution per clinical hour
- Revenue per route
- Contribution per route
- Revenue per mile
- Appointments per route
- Miles per appointment
- Days to payment
- Revenue concentration
- Market contribution

## Roadmap

### Phase 1 — Foundation
- Claude financial intelligence skill
- Mobile health domain context
- Appointment data schema
- Unit economics engine

### Phase 2 — Operating Intelligence
- Route economics engine
- Contract profitability model
- Pricing engine
- Market expansion model

### Phase 3 — Financial Command Center
- Data ingestion
- KPI dashboard
- Scenario modeling
- AI CFO decision layer

## Status

Version 0.1 — Foundation build.
