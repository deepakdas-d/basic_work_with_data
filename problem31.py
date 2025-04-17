#Generalize the above implementation of csv parser to support any delimiter and comments.
def parse_csv(filename):
    parsed_data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()# Skip empty lines
            if not line or line.startswith('#'):#skip  comments
                continue
            values = line.split('!')
            parsed_data.append(values)
    return parsed_data
data = parse_csv('pro31.txt')
print(data)
