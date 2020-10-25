#Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
#Your task is to write a function maskify, which changes all but the last four characters into '#'.
#xamples
#maskify("4556364607935616") == "############5616"
#maskify(     "64607935616") ==      "#######5616"
#maskify(               "1") ==                "1"
#maskify(                "") ==                 ""
import random

# return masked string
def maskify(cc):    
    new_str=''.join("#" for i in range(len(cc[:-4]))) + cc[-4:]
    return new_str

def main():
    print(maskify("4556364607935616"))
    print(maskify("64607935616"))
    print(maskify("1"))
    print(maskify(""))
    
if __name__ == "__main__":
    main()