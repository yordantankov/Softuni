if __name__ == "__main__":
    N = int(input())
    longest_intersection = []
    longest_length = 0

    for i in range(N):
        range1, range2 = input().split('-')
        start1, end1 = map(int, range1.split(','))
        start2, end2 = map(int, range2.split(','))

        # Calculate the intersection
        start_intersection = max(start1, start2)
        end_intersection = min(end1, end2)

        # Check if this intersection is the longest so far
        if end_intersection >= start_intersection:
            intersection = list(range(start_intersection, end_intersection + 1))
            if len(intersection) > longest_length:
                longest_intersection = intersection
                longest_length = len(intersection)

    print(f"Longest intersection is {longest_intersection} with length {longest_length}")