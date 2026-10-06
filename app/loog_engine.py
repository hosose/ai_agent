'''
- 에이전트릐 루프 구성(흐름)을 위한  구조 설계
- 플랜너, 검증 추가
- 루프 메인
'''
from pydantic import BaseModel, Field
from app.llm import get_chat_model
from app.agent.graph import build_graph


# 1. Planner 출력 구조 : 업무를 검증 가능한 범위내에 질문으로 분해(n개의 프럼프트(혹은 문장, 업무) 구성)
class Plan(BaseModel):
    subquestions:list[str] = Field(min_length=1, max_length=4) # 1, 혹은 4는 설정값
    pass

# 2. Verifier 출력 구조
class Verifier(BaseModel):
    pass

# 3. Agentic Loop 구성 : 계획 -> 실행 -> 검증 -> 부족하다는 피드백 나오면 재시도
#    시간/비용 고려, 최대 재시도 회수 설정(실제 주입, 배제 고민, 주입 -> 이후 Human 개입 고려)