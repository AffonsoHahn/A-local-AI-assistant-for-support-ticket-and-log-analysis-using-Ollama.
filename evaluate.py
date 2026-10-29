"""Run the model against five sanitized examples and report category agreement.
This is a small smoke test, not a statistically meaningful benchmark.
"""
import json
import re
from pathlib import Path
from main import analyze

DATA = Path(__file__).with_name("sample_tickets.json")


def main() -> None:
    examples = json.loads(DATA.read_text(encoding="utf-8"))
    correct = 0
    results = []
    for item in examples:
        report = analyze(item["ticket"])
        match = re.search(r"^Category:\s*(.+)$", report, re.MULTILINE | re.IGNORECASE)
        predicted = match.group(1).strip() if match else "Unparsed"
        ok = item["category_expected"].lower() in predicted.lower()
        correct += int(ok)
        results.append({"id": item["id"], "expected": item["category_expected"], "predicted": predicted, "match": ok})
        print(f"{item['id']}: expected={item['category_expected']} | predicted={predicted} | match={ok}")
    print(f"\nCategory agreement: {correct}/{len(examples)} ({correct / len(examples):.0%})")
    print("Review each report manually; category agreement alone does not measure diagnostic quality.")


if __name__ == "__main__":
    main()
