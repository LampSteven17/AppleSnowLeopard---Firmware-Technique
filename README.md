# AppleSnowLeopard---Firmware-Technique
Old version of brute forcing program used to exploit a vulnerability in OSX 10.6 Snow Leopard to gain admin access on any account. This is a now known and easily replicable technique documented here: https://www.lifewire.com/create-new-admin-account-for-login-issues-2259976. Originally devoloped in 2014-2015 and reported to Apple January 2015.

To gain an admin users account, simply remove a file known as applesetupdone that tells a computer if it is new or not. By doing this, the computer thinks it needs to create a new account on user login, and therfore lets you create an admin account without actually gaining root access. 

**DISCLAIMER** - FOR EDUCATIONAL PURPOSES ONLY

ITEMS NEEDED: 
Target MAC running OSX 10.6,
Secondary MAC UNLOCKED WITH FULL ADMIN PRIVELEGES on at least 1 account,
Brute forcing program in case of locked firmware password.

Steps for replication:
1. Shut down target computer and boot into single user mode (Command+R);
2. Crack firmware password using bootable Python or Bash Script. 
3. Shut down computer and open up bottom cover. Remove hard drive physically from the computer.
4. Connect target computer's hard drive to secondary computer, using root access on secondary computer: /sbin/mount -uw /
5. Remove the applesetupdone file on the target hard drive: rm -f /var/db/.applesetupdone
6. Replace the hard drive in computer, and relock firmware using cracked password. 
7. Boot up computer as normal. You should boot up into the inital setup program, and are able to create a user with admin access.
