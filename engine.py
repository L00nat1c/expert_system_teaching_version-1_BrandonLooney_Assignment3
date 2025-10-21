from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:

    # Initialize the engine with a set of rules.
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        #Store initial facts into the working memory.
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
       # Return True if all antecedents are true and consequent not yet known.
        return all(cond in self.facts for cond in rule.antecedents) and rule.consequent not in self.facts

    def run(self) -> None:
        #Implement the forward chaining loop.
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        fired = True
        while fired:
            fired = False
            # Find all rules that can fire
            candidates = [r for r in self.rules if self.can_fire(r)]

            #If no rules can fire, we're done
            if not candidates:
                break

            # Choose the highest-priority rule (or first if tie)
            candidates.sort(key=lambda r: r.priority, reverse=True)
            rule = candidates[0]

            # Fire the rule
            self.facts.add(rule.consequent)
            self.trace.append({
                "rule": rule.name,
                "added": rule.consequent,
                "from": rule.antecedents
            })
            fired = True
    
    def conclusions(self) -> Dict[str, List[str]]:
        # Return separated results (recommendations, specs, other facts).
        recommendations = [f.split(":", 1)[1] for f in self.facts if f.startswith("recommend:")]
        specs = [f.split(":", 1)[1] for f in self.facts if f.startswith("spec:")]
        base_facts = [f for f in self.facts if not (f.startswith("recommend:") or f.startswith("spec:"))]

        return {
            "recommendations": recommendations,
            "specs": specs,
            "facts": base_facts,
            "trace": self.trace 
        }