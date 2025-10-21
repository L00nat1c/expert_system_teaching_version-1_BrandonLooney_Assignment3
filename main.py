from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    # Collect initial facts from user input.
    facts = []
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    if input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
    if input("Will you use the laptop for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Will you use your pc only for office work? (y/n): ").lower().startswith("y"):
        facts.append("office_work")
    if input("Will you use your pc for creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    if input("Do you prefer Mac OS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you prefer Linux OS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    return facts

def main():
    # Load rules and initialize engine
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)
    engine.run()
    results = engine.conclusions()

    # Display result in the expected format
    if results["recommendations"]:
        # Take the first recommendation (highest priority one fires first)
        recommendation = results["recommendations"][0]
        # Find the rule that produced it
        explanation = next(
            (trace["rule"] for trace in results["trace"] if trace["added"] == f"recommend:{recommendation}"),
            None
        )
        # Print the recommendation and explanation
        print(f"\n=> Recommendation: {recommendation}")
        if explanation:
            print(f"=> Explanation: derived from rule '{explanation}'")
    else:
        print("\n=> No recommendation could be determined.")

if __name__ == "__main__":
    main()
