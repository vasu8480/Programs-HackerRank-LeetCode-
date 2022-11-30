#dict.fromkeys()
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        t = string[i: i+k]
        u = list(dict.fromkeys(t))
        print("".join(u))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)