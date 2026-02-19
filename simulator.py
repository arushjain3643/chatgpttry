from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass(frozen=True)
class Scenario:
    title: str
    timeline: str
    highlights: List[str]
    risk_level: str
    confidence: float


SCENARIO_LIBRARY: Dict[str, List[Scenario]] = {
    "drop_out": [
        Scenario(
            title="Freelance Rocket Start",
            timeline="0-18 months",
            highlights=[
                "You leave school and dive into freelancing.",
                "Income is unstable at first, then improves via referrals.",
                "You build practical skills faster than expected.",
            ],
            risk_level="high",
            confidence=0.52,
        ),
        Scenario(
            title="Reset and Return",
            timeline="0-24 months",
            highlights=[
                "You pause formal education to explore work.",
                "A tough year clarifies your long-term goals.",
                "You return to study with stronger focus and direction.",
            ],
            risk_level="medium",
            confidence=0.68,
        ),
    ],
    "start_business": [
        Scenario(
            title="Niche Product Breakthrough",
            timeline="0-3 years",
            highlights=[
                "You launch a tiny product for a specific audience.",
                "Customer feedback drives fast iterations.",
                "By year three, it becomes a sustainable small company.",
            ],
            risk_level="high",
            confidence=0.57,
        ),
        Scenario(
            title="Failed First Venture, Strong Second",
            timeline="0-4 years",
            highlights=[
                "Your first startup fails due to distribution issues.",
                "You document lessons and rebuild with a better model.",
                "Second attempt gains traction through partnerships.",
            ],
            risk_level="medium",
            confidence=0.63,
        ),
    ],
    "move_city": [
        Scenario(
            title="Network Expansion Arc",
            timeline="0-2 years",
            highlights=[
                "Moving feels lonely for the first few months.",
                "You build a new community through events and hobbies.",
                "Career opportunities expand because of local network effects.",
            ],
            risk_level="medium",
            confidence=0.71,
        ),
        Scenario(
            title="Cost-of-Living Reality Check",
            timeline="0-18 months",
            highlights=[
                "Higher rent creates pressure on your monthly budget.",
                "You adapt with side income and shared housing.",
                "The city still pays off by exposing you to better mentors.",
            ],
            risk_level="medium",
            confidence=0.66,
        ),
    ],
    "confess_crush": [
        Scenario(
            title="Mutual Spark",
            timeline="0-12 months",
            highlights=[
                "You confess honestly and respectfully.",
                "They feel similarly and you start dating.",
                "Even conflicts strengthen communication skills.",
            ],
            risk_level="low",
            confidence=0.74,
        ),
        Scenario(
            title="Graceful Rejection, Personal Growth",
            timeline="0-9 months",
            highlights=[
                "Your feelings are not reciprocated.",
                "You process it with maturity and boundaries.",
                "Confidence grows because you chose courage over regret.",
            ],
            risk_level="low",
            confidence=0.79,
        ),
    ],
}


def available_choices() -> List[str]:
    return sorted(SCENARIO_LIBRARY.keys())


def simulate(choice: str, samples: int = 1, seed: int | None = None) -> List[Scenario]:
    if choice not in SCENARIO_LIBRARY:
        raise ValueError(
            f"Unknown choice '{choice}'. Valid choices: {', '.join(available_choices())}"
        )
    if samples < 1:
        raise ValueError("samples must be >= 1")

    rng = random.Random(seed)
    options = SCENARIO_LIBRARY[choice]
    return [rng.choice(options) for _ in range(samples)]


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Life Simulator prototype")
    parser.add_argument("--choice", required=True, choices=available_choices())
    parser.add_argument("--samples", type=int, default=1)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    runs = simulate(args.choice, samples=args.samples, seed=args.seed)
    print(json.dumps([asdict(item) for item in runs], indent=2))


if __name__ == "__main__":
    main()
