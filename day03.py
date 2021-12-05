from input_prep import file_to_str_list
from results_out import solution


def part1(data):
    part = "1"
    gamma, epsilon = '',''
    line_size = len(data[0])

    for i in range(0,line_size):
        ones,zeroes = 0,0
        for line in data:
            if line[i] == '1':
                ones+=1
            else:
                zeroes+=1
        if ones > zeroes:
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
    power_consumption = int(gamma,2) * int(epsilon,2)
    solution(day, part, power_consumption)
    return


def part2(data):
    part = "2"
    


    solution(day, part, "TODO!")


if __name__ == "__main__":
    day = "3"
    
    data = file_to_str_list("input03.txt")
    
    part1(data)
    part2(data)