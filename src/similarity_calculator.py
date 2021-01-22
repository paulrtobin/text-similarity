
def tokenize_text(text):
    """Parses a text file into a list of tokens"""
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
    tokens1 = tokenize_text(text1)
    tokens2 = tokenize_text(text2)

    len2 = len(tokens2)
    scores = []
    streak = 0
    for index1, token_1 in enumerate(tokens1):
        score = 0
        max_dist = max(len2-index1-1, index1) #double check this

        for index2, token_2 in enumerate(tokens2):
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


