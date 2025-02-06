# Number Classification API  

## Overview  
The **Number Classification API** takes a number as input and returns its mathematical properties along with a fun fact.  

## API Endpoint  
```http
GET https://hng-stage-one-427o.onrender.com/api/classify-number?number=371
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
