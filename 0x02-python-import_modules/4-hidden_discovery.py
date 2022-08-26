#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    for index in content:
        if index[:2] != "__":
            print(index)
