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

for i in range(start_dan, end_dan+1):
    print(f"{i}단")
    score = 0
    start_time = time.time()
    for j in range(1, 10):
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
        else:
            print(f"아쉽네요. 정답은 {correct_answer}입니다.")
            if i in wrong_answers:
                wrong_answers[i].append((j, correct_answer))
            else:
                wrong_answers[i] = [(j, correct_answer)]
                if time.time() - start_time > 10:
                    print("시간 초과! 다음 문제로 넘어갑니다.")
                    break
                scores[i] = score
                print()

print("오답노트:")
for num, mistakes in wrong_answers.items():
    print(f"{num}단 오답노트:")
    for mistake in mistakes:
        print(f"{mistake[0]} x {num} = {mistake[1]}")
    print()

print("구구단 점수 랭킹:")
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for rank, (num, score) in enumerate(sorted_scores, start=1):
    print(f"{rank}위: {num}단 - {score}점")
