import uuid

class user:
        def __init__(self, lang, tok = None):
             self.id = str(uuid.uuid4()).replace('-', '')
             self.sen = 0.0
             self.pow = 0
             self.lang = lang
             if tok is not None:
                tok = tok.split('_')
                if len(tok) == 3:
                       self.id = tok[0]
                       self.sen = float(tok[1])
                       self.pow = int(tok[2])

        def is_negatif(self):
             return False if self.sen > -0.1 else True

        def add_score(self, score):
             if score <= -0.6 and self.sen > 0.2:
               self.sen = -0.200
               self.pow = 1
             elif score >= 0.6 and self.sen < -0.2:
               self.sen = 0.0
               self.pow = 1
             else:
               self.sen = (self.sen * self.pow + score) / (self.pow + 1)
               self.pow += 1
             self.sen = round(self.sen, 3)

        def score(self):
             return self.sen

        def get_token(self):
             return self.id + '_' + str(self.sen) + '_' + str(self.pow)
