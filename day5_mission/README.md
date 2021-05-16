4주차가 끝났습니다! 무야호~ (그만큼 열심히 학습하신다는거지!)
이번 과제는 Core Mission(핵심 임무)와 Extra Mission(추가 임무)로 이루어져있습니다.

- Core Mission : 반드시 해결해야 하는 임무
- Extra Mission : 추가로 해결할 수 있는 임무
과제는 week4 내용을 담은 본인의 branch에 `/day5_mission` 폴더를 추가, 안에 파일을 추가한 후 PR을 날려주세요.

여러분이 해결할 수 있는 만큼 해결해주세요. 건승을 빕니다! 🙂

## Mission 1. My New Assistant

서울에 사는 호주니는 영화 <브론즈 맨>을 보고 감동을 받았다. 특히 브론즈 맨 슈트를 장착했을 때 나오는 어시스턴트 빅수비의 성능에 금치 못했다. 이를 통해 우리의 매일매일의 생활을 윤택하게 만들어 줄 나만의 빅수비를 만들어보면 좋겠다는 생각을 했다. 호주니를 도와 한국형 자비스, 빅수비를 만들어보자.

### Core Mission

- 제출할 파일 : `bicsubi_core_api.md` , API 구축에 사용되는 파일들

- 다음의 명세에 맞게 API를 작성합니다.

    - `GET /whoami`

        - 여러분의 github id를 반환합니다.
        - Example:
        ```json
        {
            "name" : "super-corini"
        }
        ```
    - `GET /echo?string="string"`

        - Query String : `string`
        - string 을 반환합니다.
        ```json
        {
           "value" : "string"
        }
        ```

- 다음의 요구사항에 맞게 API를 설계하고 작성합니다.

    -  빅수비는 자원 `weapon` 을 가집니다. 이 `weapon` 은 이름(`name : str`)과 수량(`stock : int`)을 가지며 각각에 대해 **Create, Read, Update, Delete**를 진행할 수 있습니다.
        - Create : 새로운 `weapon` 을 추가
        - Read : 현재 존재하는 `weapon` 을 확인
        - Update : 현재 존재하는 `weapon` 에서 특정 속성(이름, 수량)을 변경
        - Delete : 현재 존재하는 특정 `weapon` 을 삭제
- 작성한 API에 대한 명세(API Docs)를 `bicsubi_core_api.md` 에 작성하여 제출합니다.

- 모든 API는 작성자가 설계한대로 원활하게 동작되어야합니다.

### Extra Mission
- 제출할 파일 : bicsubi_extra_api.md , API 구축에 사용되는 파일들
- 다음의 명세서에 맞게 API를 설계하고 작성합니다.
    - 현재 위치의 위도와 경도 값을 이용해 현재 위치의 날씨(온도, 바람세기 등)을 알 수 있는 API
    - 현재 위치의 위도와 경도 값을 이용해 현재 위치에서 가장 가까운 버스 정류장의 도착정보를 알 수 있는 API
    - 이외에 빅수비에 추가하고 싶은 API가 있다면 추가하셔도 좋습니다.
- Swagger를 이용해 API docs를 만듭니다.
- 작성한 API에 대한 명세(API Docs)를 bicsubi_extra_api.md 에 작성하여 제출합니다.
- 모든 API는 작성자가 설계한대로 원활하게 동작되어야합니다.
- 이 과제는 필수 과제 이후에 진행되어야합니다.

💡 API의 목적을 파악하고, 이를 바탕으로 어떻게 REST하게 작성할 수 있을지 고민해봅시다.

💡 Swagger를 활용하면 더욱 편리하게 API를 관리할 수 있습니다.


```python

```

## Mission 2. Abengers, Assemble!
Bicsubi를 다 만들고 보니 사이렌이 울렸다. 국제보안기구 <U.B.U.N.T.U>에게서 긴급 이메일이 도착했다. 죄없는 컴퓨터들에게 무차별적인 Request를 통해 이상상태로 만드는 악당 <디도스>가 인터넷을 침략하려고 한다는 소식을 전했다. 이를 막기 위해 최정예부대인 우리는 Abengers (저작권을 조심합시다) 를 소집하기로 했다. 도와줘요 Abengers!

- 이 미션은 [다음 데이터셋](https://www.kaggle.com/dannielr/marvel-superheroes?select=charcters_stats.csv)을 이용해서 진행합니다.
- 제출할 파일 : abengers.ipynb

### Core Mission
- 다음 질문에 답하시오.

    - 캐릭터는 저마다 지능, 힘, ... 등 다양한 수치를 지니고 있다. 이러한 수치의 합이 가장 큰 캐릭터는 누구인가? 이를 보이기 위한 과정을 보여라.
    - 좋은 캐릭터와 나쁜 캐릭터의 능력치들의 수치 분포를 알고 싶다. 이를 표현하기 위한 적절한 그래프를 선택해서 이를 위한 전처리를 진행하고, 시각화하여라.

### Extra Mission
- 다음 질문에 답하시오.
    - 캐릭터는 저마다 지능, 힘, ... 등 다양한 수치를 지니고 있다. 또한 각 캐릭터는 DC, 마블 등 다양한 코믹스 회사를 바탕으로 하고 있다. 어떤 코믹스 회사의 캐릭터들이 능력치 합의 평균이 가장 큰가? 이를 보이기 위한 과정을 보여라.
    - 좋은 캐릭터와 나쁜 캐릭터가 격돌한다고 한다. 격돌하는 경우 캐릭터들의 능력치의 합의 평균이 큰 팀이 이긴다고 한다. 단, 불의를 못참는 중립 캐릭터들은 중립캐릭터가 없었을 당시에 열세인 팀에 가담한다. 이러한 상황일때 결과적으로 어떤 캐릭터 진영이 승리할 것인가? 이를 보이기 위한 과정을 보여라.
    - 이 데이터를 이용해 진행하고 싶은 EDA 및 시각화가 있다면 자유롭게 진행하여라.
    - 이 과제는 핵심 임무 이후에 진행되어야 한다.