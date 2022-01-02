# Silently Crashing Application
user@ubuntu:~/purplebox$ strace ./purplebox.py

System calls : Calls that the programs running on our computer make to the running kernel

user@ubuntu:~/purplebox$ strace -o faliure.strace ./purplebox.py
user@ubuntu:~/purplebox$ less filure.strace

# Finding the Root Cause

iotop: One possible culprit could be too much disk input and output. To get more info on this, we could use iotop, which is a tool similar to top that lets us see which processes are using the most input and output. 

iostat or vmstat: Other related tools are iostat and vmstat, these tools show statistics on the input/output operations and the virtual memory operations. 

ionice: If the issue is that the process generates too much input or output, we could use a command like ionice to make our backup system reduce its priority to access the disk and let the web services use it too.

interfaces: We can check this using iftop, yet another tool similar to top that shows the current traffic on the network interfaces.

Trickle: If that option isn't available, we can use a program like Trickle to limit the bandwidth being used.

nice: Another option could be that the compression algorithms selected is too aggressive, and compressing the backups is using all of the server's processing power. We could solve this by reducing the compression level or using the nice command to reduce the priority of the process and accessing the CPU.