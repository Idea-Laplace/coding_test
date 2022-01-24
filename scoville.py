import heapq as h


def solution(scoville, K):
    h.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            f_min = h.heappop(scoville)
            s_min = h.heappop(scoville)
            h.heappush(scoville, f_min + 2 * s_min)
            answer += 1
        else:
            return -1

    return answer
