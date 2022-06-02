#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    li = []
    for i in dir(hidden_4):
        if i.startswith('_'):
            continue
        else:
            li.append(i)
    for i in li:
        print(i)
