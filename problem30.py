#Write a python function parse_csv to parse csv (comma separated values) files.
def parse_csv(filename):
    ls=[]
    with open(filename,'r')as f:
        for i in f:
            v=i.strip().split(',')
            ls.append(v)
    print(ls)
a=parse_csv('csvv.csv')
print(a)
        #output
        #[['name', 'age', 'city'], ['Alice', '30', 'New York'], ['Bob', '25', 'Los Angeles'], ['Charlie', '35', 'Chicago']]