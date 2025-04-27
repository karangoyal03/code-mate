from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import requests
import json
import re
router = APIRouter()

@router.post("/get-suggestions")
async def get_suggestions(request: Request):
    body = await request.json()
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
    def parse_streamed_chunks(raw_data: str):
    # Extract JSON blocks using regex
        json_blocks = re.findall(r'\{(?:[^{}]|(?R))*\}', raw_data, re.DOTALL)

        # Parse each block
        parsed_chunks = [json.loads(block) for block in json_blocks]

        # Extract and concatenate the "content" from each chunk
        final_content = ''.join(chunk["choices"][0]["delta"].get("content", "") for chunk in parsed_chunks)
        return final_content
        # Return as a JSON response
        # return JSONResponse(content={"response": final_content})

    def stream_openrouter():
        with requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",
                "Content-Type": "application/json",
            },
            stream=True,
            data=json.dumps({
                "model": "meta-llama/llama-4-maverick",
                "stream": True,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }),
        ) as r:
            for line in r.iter_lines(decode_unicode=True):
                if line.startswith("data:"):
                    clean = line[len("data:"):].strip()
                    if clean != "[DONE]":
                        try:
                            parsed = json.loads(clean)
                            yield json.dumps(parsed) + "\n"
                        except json.JSONDecodeError:
                            continue                    
    return parse_streamed_chunks(stream_openrouter())
    # json_blocks = re.findall(r'\{(?:[^{}]|(?R))*\}', stream_openrouter() , re.DOTALL)
    # parsed_chunks = [json.loads(block) for block in json_blocks]
    
    # return StreamingResponse(, media_type="application/json")