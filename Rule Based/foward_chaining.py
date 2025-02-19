class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact, outcome):
        self.facts[fact] = outcome

    def ask_user_for_fact(self, fact):
        if fact in self.facts:
            return self.facts[fact]

        response = input(f"Is it true that {fact}? y/n: ").strip().lower()
        if response == 'y':
            self.add_fact(fact, True)
            return True
        else:
            self.add_fact(fact, False)
            return False

    def infer(self):
        # best_matching_rule = None
        #
        # for rule in self.rules:
        #     if any(cond in self.facts and not self.facts[cond] for cond in rule.conditions):
        #         continue
        #
        #     match_count = 0
        #     for cond in rule.conditions:  # Check the conditions
        #         outcome = self.ask_user_for_fact(cond)
        #         if outcome:
        #             match_count += 1
        #         else:
        #             break
        #
        #     if match_count == len(rule.conditions):  # All conditions must be true
        #         best_matching_rule = rule
        #         break
        #
        # if best_matching_rule:
        #     print(f"{best_matching_rule.conclusion}")
        # else:
        #     print("No rules match the current facts.")
        for rule in self.rules:
            if any(rule for condition in rule.conditions):
                outcome = self.ask_user_for_fact(rule.conclusion)



if __name__ == "__main__":
    es = ExpertSystem()

    es.add_rule(Rule(["yellow fur", "long ears", "red cheeks"], "Pikachu"))
    es.add_rule(Rule(["yellow fur", "long ears", "black stripes"], "Electabuzz"))
    es.add_rule(Rule(["orange fur", "tail on fire"], "Charmander"))
    es.add_rule(Rule(["orange fur", "tail on fire", "a pointy head"], "Charmeleon"))
    es.add_rule(Rule(["orange fur", "tail on fire", "a pointy head", "wings"], "Charizard"))
    es.add_rule(Rule(["a plant on its back", "The ability to evolve"], "Bulbasaur"))
    es.add_rule(Rule(["a plant on its back", "a pink flower"], "Venusaur"))
    es.add_rule(Rule(["a plant on its back", "a pink flower", "The ability to evolve"], "Ivysaur"))
    es.add_rule(Rule(["A shell"], "Squirtle"))
    es.add_rule(Rule(["A shell", "visible ears"], "Wartortle"))
    es.add_rule(Rule(["A shell", "visible ears", "water cannons"], "Blastoise"))

    es.infer()
