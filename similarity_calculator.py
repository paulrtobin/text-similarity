
def parse_file(filepath):
    """Parses a text file into a list of tokens"""
    with open(filepath, 'r') as f:
        text = f.readline()
    token_list = []
    cur_token = ''
    for char in text.lower():
        if char == ' ':
            token_list.append(cur_token)
            cur_token = ''
        elif char in ['.', '?', ',', '!']:
            token_list.append(cur_token)
            cur_token = char
        else:
            cur_token = cur_token + char
    if cur_token not in ['\n', '']:
        token_list.append(cur_token.strip('\n'))
    return token_list


def calc_similarity(text1, text2):
    



if __name__ == '__main__':
    file1 = './inputs/sample1.txt'
    file2 = './inputs/sample2.txt'
    file3 = './inputs/sample3.txt'
    text1 = parse_file(file1)
    text2 = parse_file(file2)
    text3 = parse_file(file3)

    sim_1_2 = calc_similarity(text1, text2)

    print('here')
