def evaluate_rules(transaction, rules):
    risk = 0

    for rule in rules:
        if rule.rule_type == "AMOUNT" and transaction.amount > rule.threshold:
            risk += 0.4

        if rule.rule_type == "LOCATION" and transaction.location != "IN":
            risk += 0.3

    return min(risk, 1.0)
