# KakaotalkChattingBot

** 테스트용 임시 코드  
  
카카오톡 채팅 실시간 이미지 저장 → 문자열 스캔 후 적절한 답변  
카카오톡 채팅방 창을 화면의 가장 왼쪽 위에 붙여놓고 코드 실행  
3초마다 채팅방을 스캔(screen.png로 저장)하여 (이미지에 대한) OCR 수행 후 if-else문에서 설정한 문자열을 추출(scan.txt)하여 그에 맞게 설정해놓은 답변 수행  
답변 부분은 if-else문에 작성 (임시 테스트용 코드라서..)  



필요한 파일  
Tesseract-OCR 설치 필요  
C:\Program Files\Tesseract-OCR\tessdata\에 첨부한 kor.traineddata를 넣어준 후 작동
