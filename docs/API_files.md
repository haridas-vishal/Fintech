# SentinelStream – API Contract

## Base URL
http://localhost:8000

---

## 1. Health Check API

### Endpoint
GET /

### Description
Checks whether the SentinelStream service is running.

### Request
No request body.

### Response
Status Code: 200 OK

```json
{
  "status": "running"
}



________________________________________________________________________________

# SentinelStream – API Contract

---

## 1. Create Transaction API

### Endpoint
POST /transaction

### Description
Receives a transaction request, evaluates fraud risk using rules and ML,
and returns transaction approval status.

### Request Body (JSON Example)
```json
{
  "user_id": 101,
  "amount": 2500,
  "location": "Hyderabad",
  "idempotency_key": "txn-abc-123"
}




Response Body (JSON Example)

{
  "transaction_id": "TXN789456",
  "status": "APPROVED",
  "risk_score": 0.18
}
____________________________________________________________________________
2. Get User Transaction History
Endpoint

GET /transactions/{user_id}

Description

Returns all past transactions of a user.

Response Body (JSON Example)

[
  {
    "transaction_id": "TXN123",
    "amount": 1200,
    "status": "APPROVED",
    "created_at": "2025-01-10T12:30:00"
  }
]


Error Responses (Common)
400 – Bad Request

{
  "error": "Invalid input"
}


500 – Internal Server Error
{
  "error": "Something went wrong"
}

_______________________________________________________________________________


❌ Do NOT store these in `app/` folder  
❌ Do NOT try to run them

They are **documentation only**.

---

## ✅ Why This Is the Correct Way (Interview Tip)

If asked:
> “Why did you write JSON in API_Contract.md?”

Answer:
> “JSON is the standard API data format, so I documented request and response structures as JSON examples to clearly define the API contract for backend and frontend integration.”

💯 Perfect answer.

---

## ✅ Final Confirmation

| Question | Answer |
|----|----|
Should it be in `API_Contract.md`? | ✅ YES |
Should it be JSON format? | ✅ As examples |
Should it be saved as `.json` file? | ❌ NO |
Is this Week-1 work? | ✅ YES |

---

## 🎯 You Are Doing This CORRECTLY

You are:
- Designing before coding
- Following industry standards
- Avoiding beginner mistakes

👏👏👏

---

## 🚀 Next Step (Choose One)

1️⃣ *“Check my API_Contract.md content”*  
2️⃣ *“Confirm Week-1 is fully complete”*  
3️⃣ *“Start Week-2 implementation (real coding)”*  

Tell me the number 👍
