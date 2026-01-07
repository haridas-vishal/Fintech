from celery import Celery

celery = Celery(
    "alerts",
    broker="redis://localhost:6379/0"
)

@celery.task
def send_alert(transaction_id, risk_score):
    print(f"🚨 Fraud Alert: Txn {transaction_id}, Risk {risk_score}")
