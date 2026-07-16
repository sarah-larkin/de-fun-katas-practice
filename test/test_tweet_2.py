from src.tweet_2 import tweet_data

def test_empty_str_returns_basic_dict(): 
    assert tweet_data("") == { 
        'tags': [], 
        'mentions': [], 
        'tag_count': 0, 
        'mention_count': 0, 
        'length': 0 
        }
    
def test_length_key_shows_lenght_of_tweet(): 
    assert tweet_data("hello") == {
        'tags': [], 
        'mentions': [], 
        'tag_count': 0, 
        'mention_count': 0, 
        'length': 5
    }

    assert tweet_data("hello my friend") == {
        'tags': [], 
        'mentions': [], 
        'tag_count': 0, 
        'mention_count': 0, 
        'length': 15
    }

def test_mention_count():   #updated to check mention_count only 
    #test_1
    output =  tweet_data("hello @northcoders") 
    mention_count = output['mention_count']
    assert  mention_count == 1
  
    # test_2
    output_1 = tweet_data("hello @northcoders and all @nc_tutors")
    mention_count_1 = output_1['mention_count']
    assert  mention_count_1 == 2

def test_mentions_added_to_list():    #updated to check mentions list only
    #test_1
    output = tweet_data("hello @northcoders")
    mentions_list = output['mentions']
    assert mentions_list == ["@northcoders"]
    
    #test_2
    output_1 = tweet_data("hello @northcoders and all @nc_tutors")
    mentions_list_1 = output_1['mentions']
    assert mentions_list_1 == ["@northcoders", "@nc_tutors"]
    
def test_tags_added_to_list(): 
    #test_1
    output = tweet_data("My awesome tweet about #coding")
    tags = output['tags']
    assert tags == ["#coding"]

    #test_2
    output_2 = tweet_data("My awesome tweet about #coding and #friends")
    tags_2 = output_2['tags']
    assert tags_2 == ["#coding", "#friends"]

def test_tag_count():
    #test_1
    output = tweet_data("My awesome tweet about #coding")
    tag_count = output['tag_count']
    assert tag_count == 1

    #test_2
    output_2 = tweet_data("My awesome tweet about #coding and #friends")
    tag_count_2 = output_2['tag_count']
    assert tag_count_2 == 2

def test_unique_mentions_list(): 
    output = tweet_data("I am #coding with @northcoders I love #coding and @northcoders") 
    mentions = output['mentions']
    mention_count = output['mention_count']
    assert mentions == ['@northcoders']  
    assert mention_count == 1

def test_unique_tags_list(): 
    output = tweet_data("I am #coding with @northcoders I love #coding and @northcoders") 
    tags = output['tags']
    tag_count = output['tag_count']
    assert tags == ['#coding'] 
    assert tag_count == 1