# BizTone Converter - 업무 말투 자동 변환 솔루션

## 프로젝트 개요

'BizTone Converter'는 직장인들이 상황과 대상에 맞는 적절한 업무용 말투를 사용하는 데 겪는 어려움을 해결하기 위해 설계된 AI 기반 웹 솔루션입니다. 이 서비스는 사용자의 일상적인 표현을 전문적인 비즈니스 언어로 자동 변환하여, 명확하고 효과적인 커뮤니케이션을 지원합니다.

### 주요 기능

*   **대상별 말투 변환**: 사용자가 입력한 텍스트를 '상사', '동료', '고객' 세 가지 대상에 최적화된 비즈니스 톤으로 변환합니다.
*   **직관적인 UI/UX**: 데스크톱과 모바일 환경 모두에서 사용하기 편리한 반응형 웹 인터페이스를 제공합니다.
*   **간편한 결과 활용**: 변환된 텍스트를 한 번의 클릭으로 쉽게 복사하여 다양한 커뮤니케이션 채널에 활용할 수 있습니다.

### 문제 해결

많은 직장인, 특히 신입사원이나 비즈니스 커뮤니케이션에 익숙하지 않은 구성원들은 상황에 맞는 업무용 말투 사용에 어려움을 겪습니다. 이는 커뮤니케이션 비효율성, 오해 유발, 그리고 개인 및 조직의 전문성 저하로 이어질 수 있습니다. BizTone Converter는 이러한 문제를 해결하여 업무 생산성을 향상시키고, 커뮤니케이션 품질을 표준화하며, 직원의 교육 비용을 절감하는 데 기여합니다.

### 기술 스택

*   **Frontend**: HTML5, CSS3 (Flexbox/Grid), JavaScript (ES6+)
*   **Backend**: Python, Flask (RESTful API), python-dotenv, Flask-CORS
*   **AI**: Groq AI API
*   **Deployment**: Vercel
*   **Version Control**: Git, GitHub

## 시작하기

프로젝트를 로컬 환경에서 실행하려면 다음 단계를 따르세요.

### 1. 저장소 클론

```bash
git clone https://github.com/qudwnals/BizTalk-gemini-cli.git
cd BizTalk-gemini-cli
```

### 1.5. 프론트엔드 종속성 설치 및 빌드

프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 필요한 Node.js 패키지를 설치하고 Tailwind CSS를 빌드합니다.

```bash
npm install
npm run build:tailwind
```

### 2. 백엔드 설정

`backend` 디렉토리로 이동하여 필요한 Python 패키지를 설치하고 환경 변수를 설정합니다.

```bash
cd backend
pip install -r requirements.txt
```

`.env` 파일을 생성하고 Groq AI API 키를 추가합니다.

```
# backend/.env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Flask 애플리케이션을 실행합니다.

```bash
python app.py
```

### 3. 프론트엔드 실행

프론트엔드 파일(HTML, CSS, JS)은 정적 파일이므로, 웹 브라우저에서 `frontend/index.html` 파일을 직접 열거나, 간단한 웹 서버를 사용하여 서빙할 수 있습니다. 백엔드와 통신 시 CORS 문제가 발생할 수 있으므로, 로컬 웹 서버를 사용하는 것을 권장합니다.

```bash
# 옵션 1: 백엔드와 함께 실행 (권장)
# 백엔드가 프론트엔드 파일을 서빙하도록 설정되어 있습니다.
# 백엔드 실행 후, 웹 브라우저에서 http://localhost:5000 에 접속합니다.
# (별도의 프론트엔드 서버 실행 불필요)

# 옵션 2: Python의 SimpleHTTPServer로 서빙 (백엔드와 분리된 테스트 시)
# 새 터미널/창을 열고 프로젝트 루트 디렉토리에서 실행
python -m http.server 8000 --directory frontend
# 웹 브라우저에서 http://localhost:8000 에 접속합니다.
```

### 4. 사용 방법

1.  프론트엔드 페이지에서 텍스트 입력창에 변환하고자 하는 내용을 입력합니다.
2.  변환 대상(상사, 동료, 고객)을 선택합니다.
3.  '변환하기' 버튼을 클릭하면, 입력된 텍스트가 선택된 대상에 맞는 비즈니스 톤으로 변환되어 결과창에 표시됩니다.
4.  결과창 하단의 '복사하기' 버튼을 클릭하여 변환된 텍스트를 클립보드에 복사할 수 있습니다.

### 5. 통합 테스트 및 디버깅

프로젝트의 프론트엔드와 백엔드가 제대로 연동되는지 확인하기 위한 수동 테스트 절차입니다.

1.  **백엔드 실행 확인**:
    *   `backend` 디렉토리에서 `python app.py` 명령어를 실행합니다.
    *   웹 브라우저에서 `http://localhost:5000/health` 에 접속했을 때 `{"status": "healthy"}` 응답이 오는지 확인합니다.
2.  **프론트엔드 실행 및 API 호출 테스트**:
    *   새로운 터미널/명령 프롬프트를 열고 프로젝트 루트 디렉토리로 이동합니다.
    *   `npm install` 명령어를 실행하여 프론트엔드 종속성을 설치하고, `npm run build:tailwind`를 실행하여 Tailwind CSS를 빌드합니다. (아직 실행하지 않았다면)
    *   프론트엔드 파일을 서빙하기 위해 `python -m http.server 8000 --directory frontend` 명령어를 실행합니다.
    *   웹 브라우저에서 `http://localhost:8000` 에 접속합니다.
    *   텍스트 입력창에 내용을 입력하고, 변환 대상을 선택한 후 '변환하기' 버튼을 클릭합니다.
    *   백엔드 API (`http://localhost:5000/api/convert`)로 요청이 성공적으로 전송되고, 변환된 텍스트가 결과창에 표시되는지 확인합니다.
    *   브라우저의 개발자 도구(Console, Network 탭)를 열어 API 호출이 정상적으로 이루어지는지, 오류가 발생하는지 등을 확인할 수 있습니다. 특히 네트워크 탭에서 `/api/convert` 요청의 상태 코드(200 OK)와 응답 데이터를 확인하세요.

### 6. Vercel 배포

프로젝트를 Vercel에 배포하여 온라인에서 접근 가능하도록 설정하는 방법입니다.

1.  **Vercel 계정 및 프로젝트 생성**:
    *   Vercel 웹사이트에 접속하여 계정을 생성하거나 로그인합니다.
    *   새 프로젝트를 생성하고 GitHub 저장소(`qudwnals/BizTalk-gemini-cli`)를 연결합니다.
2.  **환경 변수 설정**:
    *   Vercel 프로젝트 설정에서 "Environment Variables" 섹션으로 이동합니다.
    *   `GROQ_API_KEY` 환경 변수를 추가하고, 발급받은 Groq API 키 값을 입력합니다. (Name: `GROQ_API_KEY`, Value: `YOUR_GROQ_API_KEY`)
    *   이 환경 변수는 백엔드 (`backend/app.py`)에서 Groq API를 호출할 때 사용됩니다.
3.  **배포 설정 (`vercel.json`)**:
    *   프로젝트 루트 디렉토리에 `vercel.json` 파일이 올바르게 생성되었는지 확인합니다. 이 파일은 Vercel이 프로젝트를 빌드하고 라우팅하는 방법을 정의합니다.
    *   `vercel.json`에 정의된 `builds` (Frontend 빌드 및 Backend 파이썬 런타임 설정) 및 `routes` (API 및 정적 파일 라우팅) 규칙에 따라 배포가 진행됩니다.
4.  **배포**:
    *   GitHub 저장소에 변경사항을 푸시하면 Vercel이 자동으로 새로운 배포를 시작합니다.
    *   Vercel 대시보드에서 배포 진행 상황을 확인하고, 배포가 완료되면 할당된 도메인을 통해 애플리케이션에 접속할 수 있습니다.
