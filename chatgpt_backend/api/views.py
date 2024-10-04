from django.shortcuts import render 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수에서 API 키 가져오기
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')



# OpenAI API 키 설정
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')  # 환경 변수에서 API 키 가져오기
)



def get_completion(prompt):
    print(f"Prompt: {prompt}")

    try:
        # OpenAI Chat API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # 사용할 모델 이름
            messages=[
                {'role': 'user', 'content': prompt}  # 사용자 메시지 설정
            ],
            max_tokens=1024,  # 최대 토큰 수
            n=1,  # 생성할 응답 수
            temperature=0.5,  # 생성된 응답의 창의성 조정
        )

        # API 응답에서 내용 추출
        message = response.choices[0].message.content
        print(f"Response: {message}")

        return message

    except Exception as e:
        print(f"Error: {e}")
        return str(e)

@csrf_exempt  # CSRF 보호 비활성화
def query_view(request): 
    if request.method == 'POST': 
        # JSON 요청 본문을 읽음
        data = json.loads(request.body)  # JSON 파싱
        prompt = data.get('prompt', '')  # prompt 값 가져오기
        response = get_completion(prompt)  # OpenAI API 호출
        return JsonResponse({'response': response})  # JSON 응답 반환
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)