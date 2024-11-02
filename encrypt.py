import hashlib

class BruteForceCracker():
    def __init__(self, hash, salt='', crypto="sha256"):
        self.hash = hash
        self.salt = salt
        self.crypto = crypto
        self.dictionary = []


    def load_dictrionary(self, file_directory):
        with open(file_directory, 'r') as file_read:
            for line in file_read:
                self.dictionary.append(line.strip())


    def crack(self):
        hash_function = getattr(hashlib, self.crypto)
        for line in self.dictionary:
            if hash_function((self.salt + line).encode()).hexdigest() == self.hash:
                return f'Hash found: {line}, and the hash: {hash_function((self.salt + line).encode()).hexdigest()}'
        return "Hash not found"
    

    def change_algoritm(self, algoritm_name):
        self.crypto = algoritm_name

brute = BruteForceCracker("7142bf3247f01ce66500fd01d064769a401ac2cd247e2a215f2553fed24adf67")
brute.load_dictrionary("/Users/lovedr6s/programs/pass")
print(brute.crack())
# hashlib.sha256(line.strip().encode()).hexdigest()