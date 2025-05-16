# Python AI Service – Product Signal Classifier

This FastAPI microservice powers the **Product Signal Simulator** in the CX Demo Hub.  
It analyzes customer signals (e.g. complaints, compliments, feedback) and returns:

- **Sentiment**: positive / neutral / negative  
- **Customer Tier**: VIP / At Risk / Standard

---

## 🚀 How It Works

### Endpoint
`POST /score-signal`

### Request Body (JSON)
```json
{
  "message": "I can't complete checkout after adding a second item"
}
