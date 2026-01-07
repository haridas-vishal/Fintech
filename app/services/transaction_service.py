from app.services.rule_engine import evaluate_rules
from app.services.ml_model import ml_score
from app.services.alerts import send_alert

async def process_transaction(txn, rules):
    rule_risk = evaluate_rules(txn, rules)
    ml_risk = ml_score(txn)

    final_risk = max(rule_risk, ml_risk)

    status = "DECLINED" if final_risk > 0.7 else "APPROVED"

    if final_risk > 0.7:
        send_alert.delay(txn.id, final_risk)

    return status, final_risk
