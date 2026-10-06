'''
- 루프엔지니어닝을 구성한 에이전틱 루프 처리 체크
'''
import asyncio
from app.loog_engine import run_agentic_loop

async def main():    
    result = await run_agentic_loop("")
    print( result )

asyncio.run(
   main()
)