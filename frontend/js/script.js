document.addEventListener('DOMContentLoaded', () => {
    const originalTextarea = document.getElementById('originalText');
    const convertedTextarea = document.getElementById('convertedText');
    const convertButton = document.getElementById('convertButton');
    const copyButton = document.getElementById('copyButton');
    const charCountSpan = document.getElementById('currentCharCount');
    const errorMessageDiv = document.getElementById('errorMessage');
    const targetRadios = document.querySelectorAll('input[name="target"]');
    const feedbackButtons = document.querySelectorAll('.feedback-button');

    // FR-04: 실시간 글자 수 카운트
    originalTextarea.addEventListener('input', () => {
        const currentLength = originalTextarea.value.length;
        charCountSpan.textContent = currentLength;
    });

    // FR-01, FR-05: 변환 버튼 클릭 이벤트
    convertButton.addEventListener('click', async () => {
        const originalText = originalTextarea.value;
        const selectedTarget = document.querySelector('input[name="target"]:checked').value;

        errorMessageDiv.textContent = ''; // Clear previous errors
        convertedTextarea.value = ''; // Clear previous results

        if (originalText.trim() === '') {
            errorMessageDiv.textContent = '변환할 텍스트를 입력해주세요.';
            return;
        }

        convertButton.disabled = true;
        convertButton.textContent = '변환 중...'; // 로딩 상태 표시

        try {
            const response = await fetch('/api/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: originalText,
                    target: selectedTarget
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || '알 수 없는 오류가 발생했습니다.');
            }

            const data = await response.json();
            convertedTextarea.value = data.converted_text;
        } catch (error) {
            console.error('변환 오류:', error);
            errorMessageDiv.textContent = `오류: ${error.message}`;
        } finally {
            convertButton.disabled = false;
            convertButton.textContent = '변환하기'; // 로딩 상태 해제
        }
    });

    // FR-03: 복사 버튼 클릭 이벤트
    copyButton.addEventListener('click', () => {
        if (convertedTextarea.value.trim() !== '') {
            navigator.clipboard.writeText(convertedTextarea.value)
                .then(() => {
                    alert('변환된 텍스트가 클립보드에 복사되었습니다!');
                })
                .catch(err => {
                    console.error('클립보드 복사 실패:', err);
                    alert('클립보드 복사에 실패했습니다. 수동으로 복사해주세요.');
                });
        }
    });

    // FR-06: 피드백 버튼 클릭 이벤트 (간단한 구현)
    feedbackButtons.forEach(button => {
        button.addEventListener('click', () => {
            const feedback = button.dataset.feedback;
            alert(`피드백 감사합니다! (${feedback})`);
            // 실제 서비스에서는 이 피드백을 백엔드로 전송하여 저장 및 분석합니다.
        });
    });
});
