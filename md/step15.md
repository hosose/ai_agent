# 목표
- MCP 이해, 직접 구성, 연동, tool로 사용
    - Model Context `Protocol`
    - `LLM/Agent`와 `외부` 도구/데이터/서비스를 연결하기 위한 `표준 통신 규격`
    - github 공식 MCP
        - https://github.com/github/github-mcp-server
    - 그외 오피셜 MCP 
        - 국내
            - https://playmcp.kakao.com/
            - ..
        - 해외
            - ..
        - 서비스 주체별 MCP 제공
    - 사용
        - 이미 구성된 MCP 사용 -> 서비스 업체(노션, 슬렉등에서 개방된 규격 사용하면 본인 앱에서 연동가능)
        - playmcp등 해당 사이트는 사용의 제한(클로드,openai등 특정 회사를 거쳐서 사용 가능함)

    - 장점
        - Agent <->  MCP 표준화   <-> 서비스등
            - 누가 만들어도 MCP 규격을 준수하면 어떤 LLM/Agent도 호환 가능하게 됨
        - 각 서비스 주체들은 오피셜 MCP 개발하여 개방해줌
            - 서비스명 + MCP => 확인 or MCP 커뮤니티/공인(포털) 사이트 검색 사용 => 바로 적용됨
        - 사내용 MCP 없음 => 비공개용, 사내용임 

- 참고
    - MCP 구성 요소
    
        | 구성 | 역할 | 현재 예제 |
        |---|---|---|
        | **MCP Host** | MCP를 사용하는 전체 애플리케이션 | LangChain Agent |
        | **MCP Client** | MCP Server와 통신 | `FastMCP Client` |
        | **MCP Server** | Tool을 외부에 제공 | `exchange_server.py` |

    - MCP Server를 개발하여 24시간 운영되는 어딘가의 호스팅/클라우드등에서 운영
        - 운영/관리 비용 발생
        - playmcp, 기타 밴더들에서 운영하는곳에 등록 해당 비용 상쇄할수 있음
    - MCP Server와 통신하여서 해당 서비스를 이용하기 위해서는 MCP Client를 개발해야함
        - FastMCP 패키지를 이용하여 개발
    - 개발자가 만드는 AI 서비스에서 MCP를 사용한다면, MCP Client가 개발/설치되어서 사용되어야함
        - LLM/Agent가 도구로서 MCP Client을 사용 -> MCP Server로 요청이 가고 -> 외부 서비스와 엑세스 요청/응답 -> 응답 -> LLM/Agent까지 도달함
        - 개발자가 만드는 AI 서비스 => MCP host 라고 부름


# 구조
```
/
L mcp_servers
    L exchange_server.py    : 편의상 MCP Server 역활, MCP host에 위치시킴
L app
    L tools
        L mcp_tools.py      : MCP Client 역활, 랭그래프상 도구로 등록 -> Agent에서 사용
    L agent
        L graph.py          : 도구 등록
L steps
    L step15_mcp.py         : MCP 테스트용,  MCP host 포지션
```

# 실행
```
python -m steps.step15_mcp
---
MCP 서버 연결 완료
TOOL RESULT : 위완화 대비 원화 환율을 확인해.
TOOL CALLS  : ['get_exchange_rate']
TOOL RESULT : [{'type': 'reasoning_content', 'reasoning_content': {'text': '', 'signature': 'Eu8BCnkIEhABGAIqQAv4Xs3Xm0Hl5FUqfzTPRaCASF3NHAItm8kgYliovPTaRvXXsUnUtwIHCkpySfjOksA5JhVJnp/dndGVeGS2B8oyDmNsYXVkZS1zYWZmcm9uOABCCHRoaW5raW5nWgw4Mjc5MTM2MTc2MzWoAY+B/NUGEgxF8Qp76nck8wYyY8waDCiLnRlFjaDCXjOMmyIwP79SXUnxubelWTiu2xFyVE7eVUOF50fhdCTatVcOvCOIFasrSvWDIXlLLgidFAn2KiS5fmjhmDSFqgLtyGemnrptXVEO5Vb+/QUP3Uh/8EfcnR/2N8MYAQ=='}}, {'type': 'tool_use', 'name': 'get_exchange_rate', 'input': {'base': 'JPY', 'quote': 'KRW'}, 'id': 'tooluse_upy1gbYjk282P9qREDW5AH'}]
TOOL RESULT : {'base': 'JPY', 'quote': 'KRW', 'rate': 863.24, 'meta': 'dummy-exchange-rate'}
TOOL RESULT : **엔화(JPY) 대비 원화(KRW) 환율 조회 결과**

- 기준: JPY → KRW
- 환율: **1 JPY = 863.24 KRW**

⚠️ 참고: 해당 환율 정보는 실시간 환율이 아니며, 더미(dummy) 데이터 기반 수치입니다. 실제 환전/정산 업무에는 실시간 환율 확인이 필요합니다.
++++++++++++++++++++++++++++++
[최종답변]

 **엔화(JPY) 대비 원화(KRW) 환율 조회 결과**

- 기준: JPY → KRW
- 환율: **1 JPY = 863.24 KRW**

⚠️ 참고: 해당 환율 정보는 실시간 환율이 아니며, 더미(dummy) 데이터 기반 수치입니다. 실제 환전/정산 업무에는 실시간 환율 확인이 필요합니다.
++++++++++++++++++++++++++++++
(agent) PS C:\Users\NT551_11TH\Desktop\workspace\ai_agent> python -m steps.step15_mcp
TOOL RESULT : 위안화 대비 원화 환율을 확인해.
TOOL RESULT : [{'type': 'reasoning_content', 'reasoning_content': {'text': '', 'signature': 'Eq0CCnkIEhABGAIqQJ2+IB/0hnIdyZ1POtsJ0mKxirjiNHY/M7qlWD//HP1xHqzlmRYCMGYRngetc/SUDJ2rKsN/TGw3pegLrAT/lzMyDmNsYXVkZS1zYWZmcm9uOABCCHRoaW5raW5nWgw4Mjc5MTM2MTc2MzWoAc2B/NUGEgw0RKGNZ2PisedJLFgaDB8fljUNf3S8EihfGiIwX1ZH7k/ujHEhxCtIkdlms8BBYgG4exqPPdO0U92CdE3YCaKdF0xA1OlXk0znmf0gKmIEpkVOfr3y6oqrDaKqoEGU+uB9kQcb821mV/kKnKuf3bl7Z/tNcW3AsxxbAf36kDLw6s+XpBKre9Rg8k0YkKhIUdkLHRATrtahykRGvvS6IBb7KTC2jb4I3F7PfcfXMdk4pRgB'}}, {'type': 'text', 'text': '위안화(CNY) 관련해서는 안내드릴 수 있는 사항이 제한적입니다.\n\n현재 환율 조회 도구는 **USD, EUR, JPY 대비 KRW**만 지원하며, **CNY(위안화)는 지원되지 않습니다.**\n\n필요하시다면 아래 중 하나로 안내드릴 수 있습니다:\n- USD/KRW, EUR/KRW, JPY/KRW 환율 조회\n- 외부 환율 정보 소스를 별도로 확인하시는 방법 안내\n\n원하시는 환율이 있으신가요?'}]
++++++++++++++++++++++++++++++
[최종답변]

 [{'type': 'reasoning_content', 'reasoning_content': {'text': '', 'signature': 'Eq0CCnkIEhABGAIqQJ2+IB/0hnIdyZ1POtsJ0mKxirjiNHY/M7qlWD//HP1xHqzlmRYCMGYRngetc/SUDJ2rKsN/TGw3pegLrAT/lzMyDmNsYXVkZS1zYWZmcm9uOABCCHRoaW5raW5nWgw4Mjc5MTM2MTc2MzWoAc2B/NUGEgw0RKGNZ2PisedJLFgaDB8fljUNf3S8EihfGiIwX1ZH7k/ujHEhxCtIkdlms8BBYgG4exqPPdO0U92CdE3YCaKdF0xA1OlXk0znmf0gKmIEpkVOfr3y6oqrDaKqoEGU+uB9kQcb821mV/kKnKuf3bl7Z/tNcW3AsxxbAf36kDLw6s+XpBKre9Rg8k0YkKhIUdkLHRATrtahykRGvvS6IBb7KTC2jb4I3F7PfcfXMdk4pRgB'}}, {'type': 'text', 'text': '위안화(CNY) 관련해서는 안내드릴 수 있는 사항이 제한적입니다.\n\n현재 환율 조회 도구는 **USD, EUR, JPY 대비 KRW**만 지원하며, **CNY(위안화)는 지원되지 않습니다.**\n\n필요하시다면 아래 중 하나로 안내드릴 수 있습니다:\n- USD/KRW, EUR/KRW, JPY/KRW 환율 조회\n- 외부 환율 정보 소스를 별도로 확인하시는 방법 안내\n\n원하시는 환율이 있으신가요?'}]
```