import json
import sys
from pathlib import Path

REQUIRED_METRICS = {
    "period",
    "revenue",
    "orders",
    "customers",
    "aov",
    "return_rate",
    "anomaly_days",
}

BLOCKED_KEYS = {
    "customer_name",
    "email",
    "phone",
    "address",
    "customer_email",
    "customer_phone",
}


def validate_metrics(metrics: dict) -> None:
    """Validate that only approved, aggregated analytics metrics are used."""

    missing = REQUIRED_METRICS - metrics.keys()
    if missing:
        raise ValueError(f"Missing required metrics: {sorted(missing)}")

    blocked = BLOCKED_KEYS.intersection(metrics.keys())
    if blocked:
        raise ValueError(f"Potential PII detected: {sorted(blocked)}")

    if metrics["revenue"] < 0:
        raise ValueError("Revenue cannot be negative.")

    if metrics["orders"] < 0 or metrics["customers"] < 0:
        raise ValueError("Orders/customers cannot be negative.")

    if not 0 <= metrics["return_rate"] <= 1:
        raise ValueError("return_rate must be between 0 and 1.")


def build_prompt(metrics: dict) -> str:
    validate_metrics(metrics)

    payload = json.dumps(metrics, indent=2)

    return f"""
You are an analytics summarization assistant.

Use ONLY the validated aggregate metrics supplied below.

Do not:
- invent values
- infer unsupported causes
- expose or request customer-level PII
- claim correlation implies causation
- execute SQL against production systems

Clearly separate observed facts from hypotheses.

VALIDATED METRICS
-----------------
{payload}

Return:

1. Executive Summary
   - maximum 3 bullets
   - emphasize material business changes

2. Key Observations
   - identify notable movements or unusual metrics

3. Possible Explanations
   - label each explanation as a hypothesis, not a fact

4. Recommended Follow-up Analysis
   - suggest 2 concrete analytical investigations

5. Data Quality / Interpretation Caveats
   - state limitations, uncertainty or missing context
""".strip()


def main():
    if len(sys.argv) != 2:
        print("Usage: python ai/insight_generator.py <validated_metrics.json>")
        sys.exit(1)

    path = Path(sys.argv[1])

    with path.open("r", encoding="utf-8") as file:
        metrics = json.load(file)

    print(build_prompt(metrics))


if __name__ == "__main__":
    main()
