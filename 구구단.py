import time
import random

print("구구단 출력 프로그램")
wrong_answers = {}
scores = {}

name = input("이름을 입력하세요:")
print(f"{name}님, 구구단 마스터가 되어볼까요?")

difficulty_level = input("난이도를 선택하세요 (쉬움/보통/어려움): ")

if difficulty_level == "쉬움":
    num_range = (2, 9)
    time_limit = 10
elif difficulty_level == "보통":
    num_range = (2, 9)
    time_limit = 7
elif difficulty_level == "어려움":
    num_range = (2, 12)
    time_limit = 5
else:
    print("올바른 난이도를 선택해주세요.")
    exit()

print(f"{name}님, {difficulty_level} 모드를 선택하셨습니다.")

for i in range(start_dan, end_dan+1):
    print(f"{i}단")
    score = 0
    check_interval = 10 #10문제마다 실력 점검

def ask_multiplication(a, b):
    try:
        user_answer = int(input(f"{a} x {b} = "))
    except ValueError:
        print("숫자만 입력해주세요.")
        return None
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print(f"시간 초과! 정답은 {a * b}입니다.")
        return None
    return user_answer

    while True:
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        correct_answer = a * b
        if answer == correct_answer:
            print("정답입니다!")
            score += 1
            if score % check_interval == 0:
                 print(f"{name}님, 지금까지 {score}문제를 맞추셨습니다. 멋집니다!")
                 if score >= 20:
                     print("구구단 실력이 점점 늘어나고 있어요. 계속 열심히 하세요!")
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

print("구구단 프로그램을 모두 완료하셨습니다.")
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

print("구구단 프로그램을 이용해주셔서 감사합니다.")
