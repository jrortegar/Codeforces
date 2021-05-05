def main():
    a=input()
    c=set(a)
    c="".join(c)
    if(len(c)%2==0):
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
main()