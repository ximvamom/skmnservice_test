# 과제2_이름검색_시스템
## 🙋‍♀️ 지원자 정보
- 이름: 김윤지
- 전화번호: 010-9006-7146
- 제출일: 2025년 7월 3일

## 🚀 프로젝트 실행 방법

### 1. 프로젝트 구조

```
📁 90067146-task-2/
├── index.html
├── data/
    └── names.csv
└── feedback/
    └── README.md
```

### 2. 실행 방법 (Python 내장 서버 이용)

1. HTML 및 CSV 파일이 있는 디렉토리로 이동
2. 아래 명령어 실행
```bash
python -m http.server 8000
```

### 3. 브라우저에서 접속
> http://localhost:8000/index.html

## 📋 결과물 설명
### ✅ 기본 기능
- 이름 입력 시 자동완성 힌트 제공

- 입력한 텍스트를 포함하는 이름 리스트 출력

- 리스트 중 첫 번째 이름은 입력창에 hint로 표시

- 이름 클릭 시 해당 이름의 상세 정보 모달로 표시 (Dummy API 사용)

### ✅ 개선 기능
1. 데이터 분리

    - 기존 소스의 하드코딩된 이름 데이터를 `names.csv` 외부 파일로 분리

    - CSV → JavaScript에서 동적으로 fetch하여 로드

2. 유지보수성 향상

    - 불필요한 DOM 재생성 제거 (container를 반복 생성하는 방식 제거)

    - 상태 기반 렌더링 구조로 개선

    - 코드 간결화 및 함수 분리 (검색 로직, UI 업데이트 분리)

3. 대용량 데이터 대응

    - 검색 시 소문자/대문자 구분 없는 필터링

    - 리스트 출력 성능을 고려해 필요 시 가상 스크롤 또는 pagination 확장 가능

4. API 연동

    - 이름 클릭 시 가상의 상세 정보 API로부터 응답을 받아 modal로 정보 표시

    - 실제 API가 없으므로 dummy 데이터 기반 모의 응답 처리

## 🔧 원본 소스 문제점 및 개선 요약
| 항목 | 문제점 | 개선 내용 |
| --- | --- | --- |
| 데이터 관리 | 이름이 JS 내부에 하드코딩되어 있어 유지보수 불편 | `names.csv`로 외부 분리 |
| DOM 관리 | 검색마다 `.container` 전체를 새로 그리는 비효율적 방식 | 단일 DOM 재사용 + 이벤트 핸들러 최소화 |
| 코드 구조 | 함수 간 역할 불명확, 중복 함수 존재 | 검색 로직/렌더링 분리 및 재사용 구조로 개선 |
| 확장성 | 대량 데이터 대응 불가 | CSV 외부화 및 성능 고려 구조로 변경 |
| 검색 UX | 검색 결과 힌트가 명확하지 않음 | 오토컴플릿 힌트 명확히 표시 |
| 상세 정보 | 클릭 시 상세 정보 없음 | Dummy API 응답으로 정보 표시 기능 구현 |

## 📐 설계 및 구조 다이어그램
### 시스템 구성
```pgsql
[HTML 페이지]
   |
   └──> fetch(names.csv)
           ↓
   [이름 배열] ← search(input)
           ↓
   [검색 결과 DOM 업데이트]
           ↓
   [이름 클릭] → fetch(name detail API)
                           ↓
                  모달 창으로 이름 정보 출력
```