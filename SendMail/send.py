import pandas as pd

contacts_df = pd.read_csv('./contacts.csv')
print(contacts_df.head())

for index, contact in contacts_df.iterrows():
    name = contact['Given Name']
    email = contact['E-mail 1 - Value']
    subject = f'사랑하는 {name}에게'
    body = (
        f'안녕, {name}~\n'
        f'\n'
        f'요즘 나로 인해 걱정도 많이 되고 힘들지?\n'
        f'여보에게 항상 미안한 마음이야.\n'
        f'\n'
        f'같이 결혼하고 살게 되었을 때 꼭 지켜내자라고\n'
        f'마음먹고 했는데 평소에 내가하는 행동은 항상 불안하기 짝이 없네..\n'
        f'이 번에 꼭 성격도 마음도 행실도 잘 다스리고 개선해서\n'
        f'다음엔 이런 일이 없도록 할게.\n'
        f'\n'
        f'지금 조금 힘들지만 우리 힘내고 여느 때처럼 잘 걸어가 보자.\n'
        f'우리에게 있는 소중한 해인이를 위해서라도 내가 최선을 다할게\n'
        f'빠른 시간 안에 우린 괜찮아질 거야.우린 초록 불임을 난 믿고 있어.\n'
        f'항상 미안하고 사랑한다.파이팅!\n'
        f'\n'
        f'2024년 6월 12일 사랑하는 남편이\n'
    )

    print(f'받는 사람: {email}\n제목: {subject}\n본문: {body}\n\n')
