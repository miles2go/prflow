import sys
import requests

def main():
    print(sys.argv[1])
    r = requests.get("https://gist.githubusercontent.com/baijum/c916342fa97f558fef9fb2de71322abe/raw/truth.txt")
    if r.text.strip() != "true":
        print("not true")
        sys.exit(1)

    print("true")

if __name__ == '__main__':
    main()
