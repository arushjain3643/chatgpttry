# AI Life Simulator

A tiny prototype inspired by your concept:

> Simulate life choices (drop out, start a business, move city, confess to your crush) and let AI show possible future scenarios.

## What this repo includes

- A **scenario simulation engine** (`simulator.py`) that models key life choices.
- A **CLI** so a user can run simulations from the terminal.
- A set of **unit tests** (`test_simulator.py`) to validate outcome generation.

## Why this is useful

The simulator demonstrates how a product can:

- Turn a single decision into multiple plausible future branches.
- Mix optimistic and risky outcomes.
- Generate concise narratives with confidence and risk scoring.

## Quick start

```bash
python3 simulator.py --choice start_business --samples 3
```

Available choices:

- `drop_out`
- `start_business`
- `move_city`
- `confess_crush`

## Output shape

Each generated scenario includes:

- `title`
- `timeline`
- `highlights`
- `risk_level`
- `confidence`

## Next product steps

- Add an LLM prompt layer for personalized narrative generation.
- Add memory/profile inputs (age, savings, personality, support system).
- Add timeline sliders (6 months, 2 years, 5 years).
- Convert the CLI to a mobile-friendly API + UI.
