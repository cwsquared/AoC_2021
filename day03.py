import copy

from input_prep import file_to_str_list
from results_out import solution


def most_common_bit(data,pos):
    ones,zeroes = 0,0
    for line in data:
        if line[pos] == '1':
            ones+=1
        else:
            zeroes+=1
        if ones >= zeroes:
            most_common_bit = '1'
        else:
            most_common_bit = '0'
    return most_common_bit


def least_common_bit(data,pos):
    ones,zeroes = 0,0
    for line in data:
        if line[pos] == '1':
            ones+=1
        else:
            zeroes+=1
        if zeroes <= ones:
            least_common_bit = '0'
        else:
            least_common_bit = '1'
    return least_common_bit


def part1(data):
    part = "1"
    gamma, epsilon = '',''
    line_size = len(data[0])

    for i in range(0,line_size):
        bit = most_common_bit(data,i)
        if bit == '1':
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
    o2_gen = copy.deepcopy(data)
    co2_scrub = copy.deepcopy(data)
    line_size = len(data[0])

    for i in range(line_size):
        if len(o2_gen) > 1:
            remove_list = []
            mcb = most_common_bit(o2_gen,i)
            for j in range(0,len(o2_gen)):
                if o2_gen[j][i] != mcb:
                    remove_list.append(j)
            remove_list.reverse()
            for index in remove_list:
                    del o2_gen[index]
            
    for i in range(line_size):
        if len(co2_scrub) > 1:
            remove_list = []
            lcb = least_common_bit(co2_scrub,i)
            for j in range(0,len(co2_scrub)):
                if co2_scrub[j][i] != lcb:
                    remove_list.append(j)
            remove_list.reverse()
            for index in remove_list:
                    del co2_scrub[index]


    life_support_rating = int(o2_gen[0],2) * int(co2_scrub[0],2)
    solution(day, part, life_support_rating)


if __name__ == "__main__":
    day = "3"
    
    data = file_to_str_list("input03.txt")
    
    part1(data)
    part2(data)