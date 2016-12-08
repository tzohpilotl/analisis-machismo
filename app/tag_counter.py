class TagCounter():
    """ Wrapper for a tag counting method """
    
    def __init__(self, tagged_tweets):
        """ Store a list of tweets in case none is provided in count() """
        
        self.tags = {}
        self.tagged_tweets = tagged_tweets

    def count(self, tagged_tweets=None):
        """Handle the counting of tags inserting them in a dictionary to 
        ensure their uniqueness. Can manage a list of tags and a single
        string tag.
        """
        if tagged_tweets is not None:
            self.tagged_tweets = tagged_tweets
        for tweet in self.tagged_tweets:
            for word in tweet:
                try:
                    if isinstance(word[1], str):
                        if word[1] in self.tags:
                            self.tags[word[1]] += 1
                        else:
                            self.tags[word[1]] = 1
                    else:
                        for tag in word[1]:
                            if tag in self.tags:
                                self.tags[tag] += 1
                            else:
                                self.tags[tag] = 1
                except TypeError:
                    continue
                            
        return self.tags
