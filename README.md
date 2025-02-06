# Number Classification API  

## Overview  
The **Number Classification API** takes a number as input and returns its mathematical properties along with a fun fact.  

## API Endpoint  
```http
GET <your-domain.com>/api/classify-number?number=371
```

## Response Format  

### ✅ **Success Response (200 OK)**  
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### ❌ **Error Response (400 Bad Request)**  
```json
{
    "number": "alphabet",
    "error": true
}
```

## Requirements  
- Accepts **GET** requests with a **number** parameter.  
- Returns JSON in the **specified format**.  
- Supports **all valid integers** as input.  
- Provides appropriate **HTTP status codes**.  

## Deployment  
- API must be **publicly accessible**.  
- Response time should be **less than 500ms**.  

## Submission Deadline  
📅 **6th February 2025, 11:59 PM WAT (GMT +1)**  

## Important Notes  
- Use the `math` type from the **Numbers API** to fetch the fun fact.  
- Ensure **accuracy, functionality, and compliance** with requirements before submission.
