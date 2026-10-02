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



```
python -m steps.step15_mcp
---
    await run(
        "2026-09-01 ~ 2026-09-05 기간내에 환불 현황을 확인하고, "
        "해당 비용을 원화와 달러 2개 통화로 알려주고, " 
        "사내 환불 정책을 확인해서 "
        "내가 선호하는 보고 방식으로 정리해줘."
    )
---    
MCP 서버 연결 완료
TOOL RESULT : 2026-09-01 ~ 2026-09-05 기간내에 환불 현황을 확인하고, 해당 비용을 원화와 달러 2개 통화로 알려주고, 사내 환불 정책을 확인해서 내가 선호하는 보고 방식으로 정리해줘.
TOOL CALLS  : ['recall_user_memory', 'refund_summary', 'get_exchange_rate', 'search_company_policy']
TOOL RESULT : [{'type': 'reasoning_content', 'reasoning_content': {'text': '', 'signature': 'EqsECnkIEhABGAIqQGYbMQcm8ruQ7XoQr0NOGhXfMwViOSXJLh+ooUnbZr4ddk/jXY1wzfNm82ftL97WifsP/0Wfvz+JWqtHWYz2viEyDmNsYXVkZS1zYWZmcm9uOABCCHRoaW5raW5nWgw4Mjc5MTM2MTc2MzWoAfyX/NUGEgyFwLT5gLGi1Uiby04aDP+57n0qllMWIdlUSCIwlAEDNKsXTQtEG3KEP9zIMtOfFu+vfpBBouyWC/05kam3kFk8CiiVEQcpMHfYduCeKt8CPBgN18JEfnbfOa+8BbLAqTkj5hV4Hcrv3iZ6PRojIPVVvuXZHdICCVFJzIw5Ao95Bw4bjq8Jzrc1oLBk7qgY4+OYsGrM1WiSqBj20FpB58kNx6jA+IDpweUMVOs7zouyp9k/6JKgivVU4ZqKxEOHvntZE7EIHU7rMixBS1NiQ/mCcPPJegDtR4o8oF46hvU8wFn+gQJXhKWEHTPDGWehuZeGWqFm+WXesd75qOTDDJhsQtjPAcwtpR0L51Dh8zM4lJFUZDJ+9QIKgtf5LguPs9EYL0z6e2C6tnJMJYAgknDEgW9nLXUozxnnI/owSmGf6lVXZMGoQGd8ATugtg3Awq6qAPGUh2DmCCUn8lX0MH18kjE2l8gwY7V8ozggQoTv8358WQNBQ8JJ+rOszAoJWuzkRofpf2BimknPEcB7Al139cap0/SYx7DB9gznYexHTxwYT4LqDWGUIMmWNpU0GAE='}}, {'type': 'text', 'text': '사용자의 선호 보고 방식을 먼저 확인하고, 환불 현황·환율·환불 정책을 함께 조회하겠습니다.'}, {'type': 'tool_use', 'name': 'recall_user_memory', 'input': {'query': '보고서 작성 방식 선호, 리포트 포맷 선호'}, 'id': 'tooluse_CLRAuSKDQpMbKHx12lpQLN'}, {'type': 'tool_use', 'name': 'refund_summary', 'input': {'start_date': '2026-09-01', 'end_date': '2026-09-05'}, 'id': 'tooluse_pnEnVfK1HVu5VH6sYvJN3I'}, {'type': 'tool_use', 'name': 'get_exchange_rate', 'input': {'base': 'USD', 'quote': 'KRW'}, 'id': 'tooluse_nhYnBEgFWJHc451WnpRyzi'}, {'type': 'tool_use', 'name': 'search_company_policy', 'input': {'query': '환불 정책 및 처리 기준', 'department': 'CS'}, 'id': 'tooluse_94Un29tqw3FYv3IDnWhFzc'}]
TOOL RESULT : [preference score=0.426 importance=0.8] 보고서 작성 시 매출 요약보다 CS 이슈 및 환불 현황을 먼저 제시하는 것을 선호함 (보고 순서: CS/환불 → 매출)
[preference score=0.288 importance=0.8] 답변은 짧은 bullet 형태로 제공하는 것을 선호함
[preference score=0.128 importance=0.9] 환불 요청 처리 정책: 5만원 이상 환불 요청은 팀장 승인을 받은 후 처리한다.
TOOL RESULT : refund_count=1, refund_amount=99000.00, range=2026-09-01~2026-09-05, reasons=product_defect
TOOL RESULT : {'base': 'USD', 'quote': 'KRW', 'rate': 1364.3, 'meta': 'dummy-exchange-rate'}
TOOL RESULT : [source=CS-REFUND-2026 | hybrid=0.464]
# 고객 반품 및 환불 정책

[source=CS-REFUND-2026 | hybrid=0.401]
환불은 반품 상품이 물류센터에 도착하여 검수된 이후 진행한다. 검수 과정에서는 상품의 사용 여부, 구성품 누락 여부, 훼손 여부와 반품 사유를 확인한다. 정상 반품으로 확인된 경우 원결제 수단을 기준으로 환불하며, 카드사나 결제대행사의 처리 일정에 따라 실제 환불 완료 시점에는 차이가 발생할 수 있다.

[source=CS-REFUND-2026 | hybrid=0.265]
고객센터 담당자는 반품 제한 또는 환불 거절이 필요한 경우 그 사유를 고객에게 명확하게 안내해야 한다. 판단이 어려운 품질 문제나 반복 분쟁 건은 임의로 처리하지 않고 CS 책임자에게 이관한다. 동일 유형의 문의가 반복될 경우 사례와 처리 결과를 기록하여 향후 정책 개선과 상담 기준 정비에 활용한다.

[source=CS-REFUND-2026 | hybrid=0.197]
상품 자체의 제조상 하자나 기능상 문제가 확인되면 상품 수령 후 30일 이내 교환 또는 환불을 신청할 수 있다. 이 경우 고객에게 귀책사유가 없는 것으로 판단되면 회수 배송비와 교환 상품의 재배송 비용은 회사가 부담한다. 필요한 경우 고객센터는 사진, 동영상 또는 제품 상태 확인 자료를 요청할 수 있다.

[source=CS-REFUND-2026 | hybrid=0.182]
주문한 상품과 다른 상품이 배송되었거나 수량이 잘못 배송된 경우 고객은 상품 수령 후 가능한 한 신속하게 고객센터에 접수한다. 오배송이 확인되면 회사가 회수 및 재배송 비용을 부담하며, 고객이 환불을 원하는 경우 회수 완료 후 결제 취소 절차를 진행한다.
TOOL RESULT : [{'type': 'reasoning_content', 'reasoning_content': {'text': '', 'signature': 'ErsDCnkIEhABGAIqQKPENn2RPGODfwkg7ZFig9MeC0xgch2gq0ia7HuRE724MeKJQTmUUo+KADs3+jnn/oQTs2xGzUnjCZVnvT1qJeQyDmNsYXVkZS1zYWZmcm9uOABCCHRoaW5raW5nWgw4Mjc5MTM2MTc2MzWoAYaY/NUGEgwE4ornHXqs39zpi+AaDPLPr2yXwP6/UU0DISIwopEpP3YEG+Vq6IXmO0L4XVwf+LyVg2F+FSm2D/C5psIWnVDNsjC6PhAkQZHnxBF8Ku8BwtTcWyaArXrY4N4DleuDePclWj/5kbnpy3Kbmw6rS1AKKePDyavYMUeE4EmZKsqLyE7MDDgd8iElya87IxcaQfOrvrSPE/563s0S0iY+SAc67zsyp+76C2gPdPLCr0K6a6tvAyhUfDeF6JU1bqtdXDkrJ0YKQUPsluajHNCg5RitrRoHZKb8AeDG2LxDSwlX8kCQBg2ZHTsKe0oBLCXlMp+NNpRj4DVYqffLaQht3f3kMSas5MeHlmIdnc3vrqyjCOyVGaDlmb26TjG0GDiCZcKcxVRgnI0EOXzFEH4lXIl8HC9l3l15fpSEv7XjKzwYAQ=='}}, {'type': 'text', 'text': '**📌 환불 현황 (2026-09-01 ~ 2026-09-05)**\n\n- 환불 건수: 1건\n- 환불 사유: 제품 불량(product_defect)\n- 환불 금액: ₩99,000 (KRW) / **$72.59 USD** (환율 1,364.3원/$ 기준, 참고용 환율)\n\n**💳 승인 필요 여부**\n- 금액이 ₩50,000 이상 → **팀장 승인 필요** (내부 기준)\n\n**📄 관련 사내 정책 (CS-REFUND-2026)**\n- 제조상 하자·기능 문제는 수령 후 **30일 이내** 교환/환불 가능, 고객 귀책 없을 시 회수·재배송비 **회사 부담**\n- 환불은 반품 상품의 **검수 완료 후** 진행, 원결제수단 기준 환불\n- 판단 애매한 품질 분쟁은 CS 책임자에게 이관\n\n필요하시면 매출 요약도 이어서 정리해드릴까요?'}]
++++++++++++++++++++++++++++++
[최종답변]

 [{'type': 'reasoning_content', 'reasoning_content': {'text': '', 'signature': 'ErsDCnkIEhABGAIqQKPENn2RPGODfwkg7ZFig9MeC0xgch2gq0ia7HuRE724MeKJQTmUUo+KADs3+jnn/oQTs2xGzUnjCZVnvT1qJeQyDmNsYXVkZS1zYWZmcm9uOABCCHRoaW5raW5nWgw4Mjc5MTM2MTc2MzWoAYaY/NUGEgwE4ornHXqs39zpi+AaDPLPr2yXwP6/UU0DISIwopEpP3YEG+Vq6IXmO0L4XVwf+LyVg2F+FSm2D/C5psIWnVDNsjC6PhAkQZHnxBF8Ku8BwtTcWyaArXrY4N4DleuDePclWj/5kbnpy3Kbmw6rS1AKKePDyavYMUeE4EmZKsqLyE7MDDgd8iElya87IxcaQfOrvrSPE/563s0S0iY+SAc67zsyp+76C2gPdPLCr0K6a6tvAyhUfDeF6JU1bqtdXDkrJ0YKQUPsluajHNCg5RitrRoHZKb8AeDG2LxDSwlX8kCQBg2ZHTsKe0oBLCXlMp+NNpRj4DVYqffLaQht3f3kMSas5MeHlmIdnc3vrqyjCOyVGaDlmb26TjG0GDiCZcKcxVRgnI0EOXzFEH4lXIl8HC9l3l15fpSEv7XjKzwYAQ=='}}, {'type': 'text', 'text': '**📌 환불 현황 (2026-09-01 ~ 2026-09-05)**\n\n- 환불 건수: 1건\n- 환불 사유: 제품 불량(product_defect)\n- 환불 금액: ₩99,000 (KRW) / **$72.59 USD** (환율 1,364.3원/$ 기준, 참고용 환율)\n\n**💳 승인 필요 여부**\n- 금액이 ₩50,000 이상 → **팀장 승인 필요** (내부 기준)\n\n**📄 관련 사내 정책 (CS-REFUND-2026)**\n- 제조상 하자·기능 문제는 수령 후 **30일 이내** 교환/환불 가능, 고객 귀책 없을 시 회수·재배송비 **회사 부담**\n- 환불은 반품 상품의 **검수 완료 후** 진행, 원결제수단 기준 환불\n- 판단 애매한 품질 분쟁은 CS 책임자에게 이관\n\n필요하시면 매출 요약도 이어서 정리해드릴까요?'}]
++++++++++++++++++++++++++++++
```