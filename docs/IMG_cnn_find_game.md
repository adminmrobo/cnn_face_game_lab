# CNN 특집 2편 「얼굴 찾기 게임 — 맞히기 다음의 여섯 챕터」 이미지 제작 명세서

- 페이지: `part2.html` (단일 파일) · 분야: 인공지능 · 형식: 게임형(대결 포함) · 주 앵커: 생활·현장(D)
- 대결 결과: **R (주판봇 승)** — 아웃트로 표정은 박사 `doc_magic`, 주판봇 `robo_happy`, 초파리 `fly_cry`(차이 25%p), 조수 `asst_proud`. 시리즈 균형: 1편 F, 2편 R
- 만든 날: 2026-11-12 · 캐릭터 팩 1.4 (`fruitfly-lab-expressions` @ 86d04ac)

## 1. 그림체와 고정 외형
캐릭터 팩 `CHAR_lab4.md` 18-3·18-4 그대로. 그림 안에 글자·숫자·로고를 넣지 않습니다.

## 2. 필요한 그림 전체

| 키 | 판 | 쓰는 자리 | 상태 | 비고 |
|---|---|---|---|---|
| `cover_cnn_find` | L 1920×1080 | 페이지 맨 위 표지 | **새로 그림** | 지금은 대체 표지. 지시문 `COVER_cnn_find_game.md` |
| `og_cnn_find` | K 1200×630 | 공유 미리보기 | 표지에서 자름 | 반영 때 `og:image` 추가 |
| `thumb_cnn_find` | I 600×400 | 목차·현황판 썸네일 | 표지에서 자름 | |
| 표정 36장 | A~D | 말풍선·대화·식구 카드 | 캐릭터 팩 재사용 | 1편과 같은 묶음 + `fly_cry` |

## 3. 새로 그릴 그림 상세
`cover_cnn_find` 한 장. `COVER_cnn_find_game.md`의 프롬프트를 그대로 씁니다. 1편 표지를 먼저 받아 그림체를 확인한 뒤 참고 그림으로 함께 올립니다.

## 4. 일관성 지침
- 넓은 판, 상자, 색칠판은 모두 페이지 코드가 그립니다. 그림으로 만들지 않습니다.
- 미공개 X1~X3는 버튼 뒤에서만 보입니다(식구 명부, 26챕터 "새 식구 부르기"). 표지에 넣지 않습니다.
- 박사·조수·시아·모아 좌우 반전 금지. 주판봇은 베이지 상자형 CRT(v2).

## 5. 체크리스트
- [x] 그림 파일 없이도 페이지가 완성 상태 (대체 표지)
- [x] 결과 보기 전 표정에 승패가 드러나지 않음
- [x] 아웃트로 표정이 대결 결과(R)와 맞음
- [ ] 표지 그림 받기 → 1600×900 WebP 220 KB 이하로 반영

## 6. 매니페스트
```json
{"page":"cnn_find_game","images":[
 {"key":"cover_cnn_find","plate":"L","status":"todo","prompt":"docs/COVER_cnn_find_game.md"},
 {"key":"og_cnn_find","plate":"K","status":"todo","source_of":"cover_cnn_find"},
 {"key":"thumb_cnn_find","plate":"I","status":"todo","source_of":"cover_cnn_find"},
 {"key":"expressions","plate":"A-D","status":"done","count":36,"source":"character_pack 1.4 @ 86d04ac, 96px"}]}
```
