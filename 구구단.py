print("구구단 출력 프로그램")
wrong_answers = {}
scores = {}

for i in range(2, 10):
    print(f"{i}단")
    score = 0
    for j in range(1, 10):
        answer = int(input(f"{i} x {j} = "))
        correct_answer = i * j
        if answer == correct_answer:
            print("정답입니다!")
            score += 1
        else:
            print(f"아쉽네요. 정답은 {correct_answer}입니다.")
            if i in wrong_answers:
                wrong_answers[i].append((j, correct_answer))
            else:
                wrong_answers[i] = [(j, correct_answer)]
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
