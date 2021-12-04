from input_prep import file_to_tuple_list
from results_out import solution


def part1(data):
    part = "1"
    h_pos,depth = 0,0
    for line in data:
        if line[0]=='forward':
            h_pos+=int(line[1])
        elif line[0]=='down':
            depth+=int(line[1])
        else:
            depth-=int(line[1])
    solution(day, part, h_pos * depth)


def part2(data):
    part = "2"
    h_pos,depth,aim = 0,0,0
    for line in data:
        if line[0]=='forward':
            h_pos += int(line[1])
            depth += aim * int(line[1])
        elif line[0]=='down':
            aim+=int(line[1])
        else:
            aim-=int(line[1])
    solution(day, part, h_pos * depth)


if __name__ == "__main__":
    day = "2"
    
    data = file_to_tuple_list("input02.txt")
    
    part1(data)
    part2(data)