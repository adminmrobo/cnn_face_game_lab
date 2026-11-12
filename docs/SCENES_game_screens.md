# 게임 화면 장면 그림 — 지시문 묶음 (CNN 특집 1·2편)

두 편의 표지와 구간 머리에는 지금 **코드로 그린 게임 화면**이 들어 있습니다(액자 모니터 + 캐릭터 팩 표정 + 주사선 + 제목 띠). 아래 지시문으로 같은 콘셉트의 픽셀아트 그림을 만들면 `data-img` 키 자리에 바꿔 넣을 수 있습니다. 그림이 없어도 페이지는 완성 상태입니다.

## 공통 규칙

- 콘셉트: 16비트 RPG풍 픽셀아트, 어두운 연구실, 가운데에 **나무 액자 모니터**, 그 안에 주제 그림, 둘레에 캐릭터, 화면 전체에 옅은 가로 주사선.
- 비율 3:2 (1200×800), 표지는 16:9 (1920×1080). 아래쪽 20%는 제목 띠가 얹히므로 어둡고 단순하게.
- **로봇은 주판봇만.** 베이지 상자형 CRT 모니터 로봇, 짙은 초록 화면에 민트 픽셀 눈, 주판알 안테나, 무한궤도, 나무 주판. **흰 둥근 로봇·노란 눈·공 모양 안테나·공중 부유는 금지**입니다(회사 캐릭터와 섞이면 안 됨).
- 그림 안에 글자·숫자·로고 금지. 제목은 페이지가 얹습니다.
- 참고 그림: `fruitfly-lab-expressions`의 여섯 캐릭터 기본 표정(E13)과 주판봇 v2 단체 사진. 박사·조수·시아·모아는 좌우 반전 금지.
- 미공개 X1~X3는 그리지 않습니다.

**모든 프롬프트 앞에 붙이는 문장**
```
16-bit RPG style pixel art matching the attached reference images exactly, bold dark outline, 2–3 tone shading.
A dark research lab at night with cables, fans and small monitors; in the center a large monitor in a wooden frame; faint horizontal scanlines over the whole image; keep the bottom 20% dark and simple.
The only robot is a boxy beige retro CRT-monitor robot with a dark green screen face, mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, holding a wooden abacus. Do NOT draw any white round robot, yellow eyes, ball antenna or floating robot.
No text, no letters, no numbers, no logos.
```

## 장면 목록

| 키 | 쓰는 자리 | 액자 속 그림 | 둘레 캐릭터 |
|---|---|---|---|
| `cover_cnn_face` | 1편 표지 | 잡음에서 드러나는 도트 고양이 | 초파리(돋보기), 박사, 하루(주먹), 시아, 모아, 주판봇 |
| `sc_stage1` | 1편 1구간 | 잡음 반, 고양이 반 | 하루, 초파리, 주판봇, 모아 |
| `sc_stage3` | 1편 2구간 | 도트 얼굴 위를 지나는 노란 네모 창 | 박사(지시봉), 하루, 초파리, 주판봇 |
| `sc_stage9` | 1편 3구간 | 큰 모눈 네 칸이 한 칸으로 줄어듦 | 초파리(돋보기), 시아, 모아(응원), 주판봇 |
| `sc_stage13` | 1편 4구간 | 판 석 장이 한 줄로 펼쳐짐 | 시아(안내), 박사, 하루, 모아 |
| `sc_stage15` | 1편 5구간 | 분홍·회색·베이지 막대 셋 | 주판봇(주판), 하루, 초파리, 박사 |
| `sc_stage18` | 1편 6구간 | 세 도트 얼굴이 나란히 | 박사(보랏빛 불꽃), 하루, 시아, 모아 |
| `cover_cnn_find` | 2편 표지 | 넓은 모눈판의 세 얼굴에 네모 테두리 | 여섯 식구 |
| `sc_stage21` | 2편 찾기 | 모눈판 위를 지나는 창과 테두리 셋 | 박사, 하루, 초파리(돋보기), 주판봇 |
| `sc_stage25` | 2편 칠하기 | 세 얼굴이 서로 다른 색으로 칠해짐 | 시아, 하루, 모아, 초파리 |
| `sc_stage26` | 2편 빌려 쓰기 | 파란 새 얼굴 셋과 작은 돋보기 셋 | 주판봇, 박사, 하루, 모아 |

## 장면별 덧붙일 문장 (공통 문장 뒤에)

```
[cover_cnn_face] Wide 16:9. Inside the framed monitor a pixel cat face appears out of gray static noise, left half still noise, right half clear, with small sparkles. Around it: a girl researcher with long pink hair in two round buns with a navy streak, white lab coat over lavender hoodie, clenching a fist and holding a stopwatch; an anthropomorphic fruit fly researcher with red compound eyes and a blue helmet wiping the screen with a cloth; a chibi scientist with thin teal rectangular glasses and spiky black hair with one white streak; a calm maid intern with long straight black hair; a gentle maid intern with ash-beige wavy hair and a white frilled headband; and the beige CRT robot on the right wiping the screen from the other side.
[sc_stage1] Inside the monitor: half gray static, half a clear pixel cat. The pink-haired girl and the fruit fly on the left, the beige CRT robot and the ash-beige maid intern on the right.
[sc_stage3] Inside the monitor: a simple dot-matrix face made of pink squares with a small yellow square window sliding over it. The chibi scientist points with a baton; the pink-haired girl looks surprised; fruit fly and beige CRT robot on the right.
[sc_stage9] Inside the monitor: a 4-by-4 block of green tiles with one 2-by-2 group outlined in yellow, an arrow, and one larger green tile. Fruit fly with a magnifying glass and the black-haired maid on the left; the cheering ash-beige maid and the beige CRT robot on the right.
[sc_stage13] Inside the monitor: three small tile boards on top and one long single row of tiles below. The black-haired maid raises one finger; the scientist smiles; the pink-haired girl and the ash-beige maid on the right.
[sc_stage15] Inside the monitor: three vertical bars, pink tall, silver medium, beige short. The beige CRT robot flicks its abacus; the pink-haired girl raises a finger; fruit fly points; the scientist thinks with a hand on his chin.
[sc_stage18] Inside the monitor: three dot-matrix faces side by side in pink, silver and beige on a deep blue background. The scientist with purple sparks on both hands; the three girls stand beside the screen.
[cover_cnn_find] Wide 16:9. Inside the monitor: a wide grid board with three dot-matrix faces, each inside a glowing rectangle (pink, silver, beige), and a small yellow window passing over. All six characters around the screen; the fruit fly lifts away one extra overlapping rectangle.
[sc_stage21] Inside the monitor: a wide grid board with three dot faces, a yellow window sliding across, three colored rectangles. Scientist and pink-haired girl on the left; fruit fly with magnifying glass and beige CRT robot on the right.
[sc_stage25] Inside the monitor: three dot faces being painted in three different colors from left to right. Black-haired maid and laughing pink-haired girl on the left; sparkling-eyed ash-beige maid and fruit fly with clipboard on the right.
[sc_stage26] Inside the monitor: three new blue dot faces on top and three tiny 3-by-3 red-and-green tile patterns below. Surprised beige CRT robot and scientist on the left; pink-haired girl and cheering ash-beige maid on the right.
```

## 받은 뒤

1. 흰 둥근 로봇이 섞였는지 먼저 확인합니다. 섞였으면 쓰지 않고 다시 요청합니다: `Same scene. Replace the robot with the boxy beige CRT-monitor robot from the reference. Still no text.`
2. 장면은 1200×800 WebP(한 장 80 KB 안팎), 표지는 1600×900 WebP(220 KB 이하)로 바꿉니다.
3. 한 편의 그림 합계가 표지 포함 600 KB를 넘지 않게 합니다. 1편은 표정 그림이 이미 약 165 KB라서 장면 6장을 다 넣으려면 장면당 60 KB 안팎이어야 합니다.
