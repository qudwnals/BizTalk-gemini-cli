import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

# .env 파일로부터 환경 변수를 로드합니다.
load_dotenv()

# API 키 로드 및 확인
groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    print("Error: GROQ_API_KEY not found in environment variables. Please set it in your .env file.")
    raise ValueError("GROQ_API_KEY not set.")

app = Flask(__name__)
CORS(app)  # 모든 경로에 대해 CORS 허용

# Groq 클라이언트 초기화
client = Groq(api_key=groq_api_key)

def generate_prompt(text, target):
    base_prompt = f"다음 텍스트를 {target} 대상에게 적합한 비즈니스 말투로 변환해 주세요. 원문의 의미를 유지하되, 각 대상의 톤앤매너에 맞게 변환해야 합니다. 최대한 자연스럽고 전문적인 표현을 사용해 주세요.\n\n원문: {text}\n\n"

    if target == "Upward":
        return base_prompt + """
---
**상사 (Upward) 대상 변환 지침:**
- 존중과 격식 사용, 명확하고 간결한 보고 형식.
"""
    elif target == "Lateral":
        return base_prompt + """
---
**타팀 동료 (Lateral) 대상 변환 지침:**
- 협력적이고 정중한 어투, 명확한 요청 사항 전달.
"""
    elif target == "External":
        return base_prompt + """
---
**고객 (External) 대상 변환 지침:**
- 극존칭과 친절함, 전문성과 신뢰성 강조.
"""
    return base_prompt

@app.route("/")
def serve_index():
    return send_from_directory('../frontend', 'index.html')

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory('../frontend', filename)

@app.route("/api/convert", methods=["POST"])
def convert_text():
    data = request.get_json()

    if not data or "text" not in data or "target" not in data:
        return jsonify({"error": "Invalid input. 'text' and 'target' are required."}), 400

    original_text = data.get("text")
    target = data.get("target")

    if not original_text.strip():
        return jsonify({"error": "변환할 텍스트를 입력해주세요."}), 400
    
    if len(original_text) > 500:
        return jsonify({"error": "텍스트는 최대 500자까지 입력 가능합니다."}), 400

    try:
        prompt = generate_prompt(original_text, target)
        
        # [수정] 모델명을 Groq에서 지원하는 llama3-8b-8192로 변경했습니다.
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant", 
            temperature=0.7,
            max_tokens=1024,
        )
        
        converted_text = chat_completion.choices[0].message.content
        
        return jsonify({
            "original_text": original_text,
            "converted_text": converted_text
        })

    except Exception as e:
        # 터미널에서 에러 내용을 자세히 볼 수 있도록 print 추가
        print(f"Groq API Error: {str(e)}")
        return jsonify({"error": f"AI 변환 중 오류가 발생했습니다: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)