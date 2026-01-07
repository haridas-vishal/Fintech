USERS
- user_id (PK)
- name
- email
- home_location

ACCOUNTS
- account_id (PK)
- user_id (FK)
- balance

TRANSACTIONS
- txn_id (PK)
- user_id (FK)
- amount
- location
- status
- created_at
