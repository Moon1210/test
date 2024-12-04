import time
import random

print("구구단 출력 프로그램")
wrong_answers = {}
scores = {}

difficulty = int(input("난이도를 선택하세요 (1-3): "))
if difficulty == 1:
    start_dan, end_dan = 2, 6
elif difficulty == 2:
    start_dan, end_dan = 2, 8
else:
    start_dan, end_dan = 2, 10

name = input("이름을 입력하세요:")
print(f"{name}님, 구구단 문제를 풀어주셔서 감사합니다!")

for i in range(start_dan, end_dan+1):
    print(f"{i}단")
    score = 0
    while True:
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        correct_answer = a * b
        try:
            answer = int(input(f"{a} x {b} ="))
        except ValueError:
            print("숫자만 입력해주세요.")
            continue
        if answer == correct_answer:
            print("정답입니다!")
            score += 1
            if score % 5 == 0 and start_dan < 10:
                start_dan += 1
                end_dan += 1
            print(f"점수가 {score}점이 되었습니다. 난이도가 상승합니다.")
        else:
            print(f"아쉽네요. 정답은 {correct_answer}입니다.")
            if a in wrong_answers:
                wrong_answers[a].append((b, correct_answer))
            else:
                wrong_answers[a] = [(b, correct_answer)]
                if score == 30:
                    print(f"{name}님, 구구단 마스타가 되셨습니다! 축하드립니다.")
                    break
                scores[i] = score
                print()

print("오답노트:")
for i in range(start_dan, end_dan+1):
    if i in wrong_answers:
        print(f"{i}단 오답노트:")
        for a, b, correct_answer in wrong_answers[i]:
            print(f"{a} x {b} = {correct_answer}")
    else:
        print(f"{i}단 오답노트: 없음")
    print()

print("구구단 점수 랭킹:")
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for rank, (num, score) in enumerate(sorted_scores, start=1):
    print(f"{rank}위: {num}단 - {score}점")

print("오답노트에 남은 문제를 다시 풀어보세요.")

while len(wrong_answers) > 0:
    dan = random.choice(list(wrong_answers.keys()))
    a, b, correct_answer = random.choice(wrong_answers[dan])
    try:
        user_answer = int(input(f"{a} x {b} = "))
    except ValueError:
        print("숫자만 입력해주세요.")
        continue
    if user_answer == correct_answer:
        print("정답입니다! 오답노트에서 삭제합니다.")
        wrong_answers[dan].remove((a, b, correct_answer))
        if not wrong_answers[dan]:
            del wrong_answers[dan]
    else:
        print(f"아쉽네요. 정답은 {correct_answer}입니다.")
