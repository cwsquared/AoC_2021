from input_prep import file_to_int_list
from results_out import solution


def part1(data):
    part = "1"
    count = 0
    prev_value = data[0]
    for measurement in data:
        next_value = measurement
        if next_value > prev_value:
            count += 1
        prev_value = next_value

    solution(day, part, count)
    return


def part2(data):
    part = "2"
    count = 0
    for i in range(0,len(data)-3):
        window1 = data[i] + data[i+1] + data[i+2]
        window2 = data[i+1] + data[i+2] + data[i+3]
        if window2 > window1:
            count += 1
    solution(day, part, count)
    return


if __name__ == "__main__":
    day = "1"
    
    data = file_to_int_list("input01.txt")
    
    part1(data)
    part2(data)