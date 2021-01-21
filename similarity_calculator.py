
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
    """Calculate the similarity between two texts"""
    len2 = len(text2)
    scores = []
    streak = 0
    for index1, token_1 in enumerate(text1):
        score = 0
        max_dist = max(len2-index1-1, index1) #double check this

        for index2, token_2 in enumerate(text2):
            if token_1 == token_2:
                #we have a match
                streak += 1
                dist = abs(index2 - index1)
                score = 1 - (dist/max_dist)
                break

        scores.append(score)
        if score == 0:
            streak = 0
        if streak == 2:
            scores.append(1.0)
            streak = 0
    average_score = sum(scores)/len(scores)
    return average_score


if __name__ == '__main__':
    file1 = './inputs/sample1.txt'
    file2 = './inputs/sample2.txt'
    file3 = './inputs/sample3.txt'
    text1 = parse_file(file1)
    text2 = parse_file(file2)
    text3 = parse_file(file3)

    sim_1_2 = calc_similarity(text1, text2)
    sim_1_3 = calc_similarity(text1, text3)

    print('here')
