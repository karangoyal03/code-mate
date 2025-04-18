import requests
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import json
router = APIRouter()

@router.post("/get-suggestions")
async def get_suggestions(request:Request):
    print("request", await request.json())
    body = await request.json()
    print("body", body)
    code = body["code"]
    prompt = f"""
    Act as a code mentor. Review the code below and suggest:
    - Refactoring opportunities
    - Complexity insights
    - Missing docstrings
    - Any best practice tips

    Code:
    {code}
        """
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "meta-llama/llama-4-maverick",
        "stream": True,
        "messages": [
        {
            "role": "user",
            "content": prompt
        }
        ],
        
    })
    )
    
    print('response',response)
    # if response.headers.get("Content-Type") == "application/json":
    #     return JSONResponse(content=response.json(), status_code=response.status_code)
    # else:
    #     return JSONResponse(
    #         content={"error": "Non-JSON response", "text": response.text},
    #         status_code=response.status_code
    #     )
    
