# imports here
import importlib
import textToArray as tta

# ============



# ============

def mult(x,y):
    return x*y

def main():
    data = tta.textToArray("./templates/source.txt")
    print(data)
    return

if __name__ == "__main__":
    main()