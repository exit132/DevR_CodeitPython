import yagmail

email = "bwvj132@gmail.com"
name = "기쁨"
subject = "기쁨님 제목"
body = "기쁨님 본문"

yag = yagmail.SMTP(
    user="bwvj132@gmail.com",
    password="Hskkoja1009!"
)

yag.send(
    to=email,
    subject=subject,
    contents=body
)