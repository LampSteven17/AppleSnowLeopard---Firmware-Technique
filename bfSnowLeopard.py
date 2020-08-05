##Brute Force Mockup of program used to crack Apple's firmware password (SIZE KNOWN)
##Steven Lamp

from itertools import permutations

def main():
    psswrd = 'dts'
    bruteish(psswrd,3)



def bruteish(crackMe, length):

#################################################
    #guesses = forceish(length)
    #for g in guesses:
        #if(g == crackMe):
            #print("PSWRD FOUND: "+g)
#################################################
################PROOF OF CONCEPT#################
    guesses = forceish(length)
    if crackMe in guesses:
        print("PSWRD FOUND")



def forceish(l):
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    uppers = lowers.upper()
    nums = '0123456789'

    return [''.join(p) for p in permutations(lowers+uppers+nums,l)]


if __name__ == "__main__":
    main()
