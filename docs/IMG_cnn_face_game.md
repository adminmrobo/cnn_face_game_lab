# CNN 특집 「얼굴 알아맞히기 게임 — 20칸으로 배우는 CNN」 이미지 제작 명세서

- 페이지: `index.html` (단일 파일) · 분야: 인공지능 · 형식: 게임형(대결 포함) · 주 앵커: 생활·현장(D)
- 대결 결과: **F (초파리 승)** — 아웃트로 표정은 박사 `doc_magic`, 초파리 `fly_arms`, 주판봇 `robo_sigh`, 조수 `asst_proud`
- 만든 날: 2026-11-12 · 캐릭터 팩 1.4 (`fruitfly-lab-expressions` @ 86d04ac)

## 1. 그림체와 고정 외형
캐릭터 팩 `CHAR_lab4.md` 18-3·18-4 그대로. 16비트 RPG풍 픽셀아트, 굵은 어두운 외곽선, 밤의 연구실 조명. 그림 안에 글자·숫자·로고를 넣지 않습니다.

## 2. 필요한 그림 전체

| 키 | 판 | 쓰는 자리 | 상태 | 비고 |
|---|---|---|---|---|
| `cover_cnn_face` | L 1920×1080 | 페이지 맨 위 표지 | **새로 그림** | 지금은 대체 표지(캐릭터 여섯 줄 세우기). 지시문 `COVER_cnn_face_game.md` |
| `og_cnn_face` | K 1200×630 | 공유 미리보기 | 표지에서 자름 | 표지 반영 때 `og:image` 메타 추가 |
| `thumb_cnn_face` | I 600×400 | 목차·현황판 썸네일 | 표지에서 자름 | |
| `sc_cnn_relay` | E 1200×800 | (선택) 「게임판 한눈에」 위 장면 | 새로 그림 · 선택 | 세 선수 이어달리기 |
| `sc_cnn_outro` | E 1200×800 | (선택) 아웃트로 장면 | 새로 그림 · 선택 | 가림막이 걷힌 뒤 |
| 표정 35장 | A~D | 말풍선·대화·식구 카드 | **캐릭터 팩 재사용** | 아래 4번 목록. 새로 그릴 것 없음 |

## 3. 새로 그릴 그림 상세

### 3-1. `cover_cnn_face` — 가림막 뒤의 세 사람
`COVER_cnn_face_game.md`의 프롬프트를 그대로 씁니다. 반영: 1600×900 WebP 220 KB 이하, `alt`는 지시문의 대체 글.

### 3-2. `sc_cnn_relay` — 이어달리기 (선택)
- 장면: 박사가 돋보기를 든 채 초록빛 작은 판을 초파리 연구원에게 건네고, 초파리 연구원은 그것을 더 작은 판으로 접어 주판봇에게 넘기려는 순간.
- 프롬프트:
```
Wide 3:2 scene, 16-bit RPG style pixel art matching the attached reference images, night research lab with purple light and teal monitor glow.
A relay of three: chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak, white lab coat, holding a magnifying glass and handing a glowing green square tile board to an anthropomorphic fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white lab coat, black gloves, transparent wings) who folds it into a smaller board; on the right a boxy beige retro CRT-monitor robot with a dark green screen face, mint pixel eyes, abacus-bead antenna and tank treads waits with a wooden abacus, facing left.
Keep faces in the upper 62% of the frame. No text, no letters, no numbers, no logos.
```

### 3-3. `sc_cnn_outro` — 가림막이 걷힌 뒤 (선택)
- 장면: 가림막이 옆으로 접혀 있고 하루·시아·모아가 나란히 서 있다. 하루는 모아의 머리띠를 장난으로 써 보고, 모아는 웃고, 시아는 조용히 지켜본다. 초파리 연구원은 팔짱, 주판봇은 한숨, 박사는 손에 보랏빛 불꽃.
- 프롬프트:
```
Wide 3:2 scene, 16-bit RPG style pixel art matching the attached reference images, night research lab, a folding screen pushed aside.
Three girls in a row: girl researcher with long pink hair with two round buns and a navy streak, white lab coat over lavender hoodie, playfully trying on a white frilled headband; gentle maid intern with long ash-beige wavy hair, camel cardigan and white frilled apron, laughing; calm maid intern with long straight jet-black hair, charcoal maid dress with gray bow, watching quietly.
On the left a fruit fly researcher with arms crossed looking confident; on the right a boxy beige CRT robot with a small sigh drop; in front a chibi scientist with teal glasses and purple sparks on both hands.
No text, no letters, no numbers, no logos.
```
- 주의: 대결 결과(F)와 표정이 맞아야 합니다. 틀리면 기존 그림 + 캐릭터 저장소의 표정 그림을 첨부해 "표정만 편집"으로 다시 요청합니다.

## 4. 캐릭터 팩에서 재사용한 표정 (새로 그릴 것 없음)

| 캐릭터 | 키 |
|---|---|
| 박사 | `doc_front` `doc_think` `doc_judge` `doc_magic` `doc_board` |
| 조수 하루 | `asst_smile` `asst_firm` `asst_report` `asst_spark` `asst_shock` `asst_proud` |
| 초파리 연구원 | `fly_clip` `fly_point` `fly_arms` `fly_coffee` `fly_magnify` |
| 주판봇 | `robo_smile` `robo_coin` `robo_happy` `robo_sigh` `robo_calc` `robo_wow` |
| 인턴 시아 | `sia_smile` `sia_explain` `sia_guide` `sia_shock` `sia_proud` |
| 인턴 모아 | `moa_smile` `moa_cheer` `moa_report` `moa_sparkle` `moa_shock` |
| 미공개 | `x1_hint` `x2_hint` `x3_hint` (버튼 뒤에서만 보임: 식구 명부, 13·14칸 "전달 요원 부르기") |

## 5. 일관성 지침
- 박사·조수·시아·모아는 좌우 반전 금지. 초파리는 왼쪽에서 오른쪽을, 주판봇은 오른쪽에서 왼쪽을 봅니다.
- 주판봇은 베이지 상자형 CRT(v2). 흰 둥근 로봇·금화는 쓰지 않습니다.
- 8×8 도트 얼굴은 페이지 코드가 그립니다. 그림으로 만들지 않습니다.
- 동작 팩(전신 프레임)은 이 페이지에서 쓰지 않았습니다.

## 6. 넘겨받은 뒤 처리
표지: 16:9 확인 → 1600×900 WebP(220 KB 이하) → `.cover.alt` 블록을 `<img class="cimg">` 표지로 바꿈 → `og_cnn_face`·`thumb_cnn_face` 자르기 → `og:image` 메타 추가 → 390·768·1280 폭 확인 → `cover_manifest.json`의 `status`를 `ok`로.

## 7. 체크리스트
- [x] 모든 그림 자리에 키가 있음 (`data-img="cover_cnn_face"`, `img[data-who][data-mood]`)
- [x] 그림 파일 없이도 페이지가 완성 상태 (대체 표지)
- [x] 결과 보기 전 표정에 승패가 드러나지 않음 (`fly_point`, `robo_coin`)
- [ ] 표지 그림 받기
- [ ] 표지 반영 후 페이지 그림 합계 600 KB 이하 확인 (지금 표정 그림 161 KB)

## 8. 매니페스트
```json
{"page":"cnn_face_game","images":[
 {"key":"cover_cnn_face","plate":"L","status":"todo","prompt":"docs/COVER_cnn_face_game.md"},
 {"key":"og_cnn_face","plate":"K","status":"todo","source_of":"cover_cnn_face"},
 {"key":"thumb_cnn_face","plate":"I","status":"todo","source_of":"cover_cnn_face"},
 {"key":"sc_cnn_relay","plate":"E","status":"optional"},
 {"key":"sc_cnn_outro","plate":"E","status":"optional"},
 {"key":"expressions","plate":"A-D","status":"done","count":35,"source":"character_pack 1.4 @ 86d04ac, 96px"}]}
```
