from collections import Counter


def solution(participant, completion):
    participant_counts = dict(Counter(participant))
    completion_counts = dict(Counter(completion))

    for key in completion_counts:
        participant_counts[key] -= completion_counts[key]

    answer_list = [k for k, v in participant_counts.items() if v != 0]
    answer = answer_list[0]
    return answer