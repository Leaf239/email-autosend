import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time

# 이메일 전송 함수
def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, sender_password):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  
            server.login(sender_email, sender_password)
            server.send_message(message)
        print("이메일이 성공적으로 전송되었습니다.")
    except Exception as e:
        print(f"이메일 전송 실패: {e}")

# 매 정시마다 전송할 이메일 내용 설정
def send_hourly_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@example.com"
    subject = "Hourly Update"
    body = "This is an automated email sent every hour."
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_password = "your_email_password"
    
    send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, sender_password)

# 매 정각에 이메일을 보내는 루프
while True:
    current_time = datetime.now()
    # 현재 시간이 정각인지 확인 (분과 초가 모두 0일 때)
    if current_time.minute == 0 and current_time.second == 0:
        send_hourly_email()
        time.sleep(3600)  # 한 시간을 대기하여 중복 전송 방지
    else:
        time.sleep(1)  # 초 단위로 계속 체크
