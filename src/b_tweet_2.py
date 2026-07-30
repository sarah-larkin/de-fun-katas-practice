def tweet_data(tweet): 
    data = { 
        'tags': [], 
        'mentions': [], 
        'tag_count': 0, 
        'mention_count': 0, 
        'length': 0 }
    
    split_tweet = tweet.split()

    #tags
    # tags = [word for word in split_tweet if word[0] == "#"]

    tags = []

    for word in split_tweet: 
        if word.startswith('#') and word not in tags: 
            tags.append(word)

    data['tags'] = tags
    data['tag_count'] = len(tags) 

    #mentions
    # mentions = [word for word in split_tweet if word not in mentions and word[0] == "@"]
    
    mentions = []
    for word in split_tweet: 
        if word.startswith('@') and word not in mentions: 
            mentions.append(word)

    data['mentions'] = mentions
    data['mention_count'] = len(mentions)
    
    # length 
    data['length'] = len(tweet)

    return data

