import sys

def process(N, tracks):
    max_sum = 0
    def track(index, current_sum):
        nonlocal max_sum
        if current_sum > N:
            return
        if index == len(tracks):
            if current_sum > max_sum:
                max_sum = current_sum
            return

        track(index + 1, current_sum)

        if current_sum + tracks[index] <= N:
            track(index + 1, current_sum + tracks[index])

    track(0, 0)
    print(f"sum:{max_sum}")

for line in sys.stdin:
    if line.strip() == "":
        continue
    parts = list(map(int, line.strip().split()))
    N = parts[0]
    track_count = parts[1]
    track_list = parts[2:]
    process(N, track_list)
