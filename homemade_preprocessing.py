class Tokenizer:
    def __init__(self):
        self.cluster_smileys = ['xd','^^','@_@','xp', ':‑)', ':)', ':-]', ':]', ':-3', ':3', ':->', ':>', '8-)', '8)', ':-}', ':}', ':o)', ':c)', ':^)', '=]', '=)', ':d', ':b']
        self.cluster_extensions = ['rar', 'txt', 'xls', 'csv', 'py', 'pdf']
        self.cluster_websites = ['ca', 'com', 'co', 'fr', 'us', 'io', 'net', 'org']
        corrections = ['tag', 'hashtag', 'laughs', 'smileys', 'extensions', 'website', 'time', 'date', 'mail']
        self._result = {k:0 for k in corrections}
    
    def test_word(self, word):
        
        if word.count('ha')>=2 or word.count('he')>=2:
            self._result['laughs'] += 1
            return "LAUGH"

        if '@' in word and len(word)>4:
            if word[-3] == '.' or word[-4] == '.':
                self._result['mail'] += 1
                return 'MAIL'
            else :
                self._result['tag'] += 1
                return 'TAG'
        
        if '#' in word :
            if word == '#' :
                self._result['hashtag'] += 1
                return 'HASHTAG'
            if len(word) > 1 :
                self._result['hashtag'] += 1
                word = word.replace("#", "")
                return 'HASHTAG ' + word
            
        if word in self.cluster_smileys:
            self._result['smileys'] += 1
            return 'SMILEY'
        
        if 8 >= len(word) > 3:
            if (word[-2] == ':' or word[-3] == ':') and (word[1] == ':' or word[2] == ':'):
                self._result['time'] += 1
                return 'TIME'
        if 2 < len(word) <= 8:
            if word[-2:] in ['am', 'AM', 'pm', 'PM'] and word[-3] in '1234567890':
                self._result['time'] += 1
                return 'TIME'
        if 4 < len(word) <= 12:
            if word[-4:] in ['a.m.', 'A.M.', 'p.m.', 'P.M.'] and word[-5] in '1234567890':
                self._result['time'] += 1
                return 'TIME'

        if 5 < len(word)<=10:
            if (word[-3] == '/' or word[-5] == '/') and (word[1] == '/' or word[2] == '/'):
                self._result['date'] += 1
                return 'DATE'

        if len(word) >= 4:
            if (word[:4] == 'http') :
                self._result['website'] += 1
                return 'WEBSITE'
            if (word[-3] == '.' or word[-4] == '.'):
                if (word[-2:] in self.cluster_extensions or word[-3:] in self.cluster_extensions):
                    self._result['extensions'] += 1
                    return 'FILE_NAME'
                elif word[-2:] in self.cluster_websites or word[-3:] in self.cluster_websites:
                    self._result['website'] += 1
                    return 'WEBSITE'
                else:
                    #print(word[-4:])
                    pass
                    
        return word