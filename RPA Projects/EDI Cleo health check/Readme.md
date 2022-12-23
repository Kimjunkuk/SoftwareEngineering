1.Port Monitoring Project overview</br>
![diagram](https://user-images.githubusercontent.com/54308434/209359902-521ec9e5-fada-4a54-8fb2-da0b8a99f5fb.png)</br></br>
![image](https://user-images.githubusercontent.com/54308434/203085763-cd0e1769-9b86-4054-9249-af0f7bb20d2f.png)</br></br>
![image](https://user-images.githubusercontent.com/54308434/203654226-f0fdce3f-8a03-442c-a035-6972a945eb2b.png)</br></br>
![image](https://user-images.githubusercontent.com/54308434/204111862-cd9b3465-4d18-4505-a00b-2ddb4e6dff23.png)</br></br>
![image](https://user-images.githubusercontent.com/54308434/204115835-0ba5b0bb-901b-46fe-a629-dca4c2322346.png)</br></br>
![image](https://user-images.githubusercontent.com/54308434/204115855-53ee03b4-8b5c-489e-80c5-8ba08ae62c7f.png)</br></br>


1-2.Initial Configuration</br>
1-2-1.convert python script to .exe file type</br> 
1-2-2.Add the python script to VBScript</br>
1-2-3.Add the VBScript to shell:startup (shortcut: Window key+R, input: shell:startup)</br>
    '''Set objShell = CreateObject("Shell.Application")</br>
    objShell.ShellExecute "C:\Users\zinus admin\Downloads\test2\test2.exe", "", "", "runas", 0'''</br>
    </br>
1-2-4.Change setting to Never notify in "Change User Account Control settings"</br></br>

1-3.Requirments</br>
1-3-2.Port Health check</br>
1-3-2-1.Port: TCP5080, TCP/443</br>
1-3-2-2.Interval: 10 sec</br>
1-3-2-3.Threshold: 6 fail</br>
1-3-2-4.Alarm email trigger: Port no longer available, Port recovered.</br></br>

2.File Monitoring Project overview</br>
![image](https://user-images.githubusercontent.com/54308434/204115728-bb054c3c-1f73-4158-8249-98bfbcd6f05a.png)</br>
![image](https://user-images.githubusercontent.com/54308434/204115808-a857c4f1-c408-41c8-8ebe-829dcfe4f23e.png)</br>
![image](https://user-images.githubusercontent.com/54308434/204453837-026ecd2b-9e93-4974-85b1-4b733cab3420.png)</br></br>

2-1.Requirments</br>
2-1-1.Send Alarm email 
    > 2-1-1-1.(total:6) target Alram email address=["*"] </br>
2-1-2.File check process cycle period(sec) = 3600</br>
2-1-3.File path = "D:\FTP-DATA\CLEO_PRD\inbox"</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Amazon AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Amazon AU AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\ANZBank AU AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Apex AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Cleo VAN AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Commercehub AS2 Production</br>
    D:\FTP-DATA\CLEO_PRD\inbox\DSCO AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Hayneedle AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\MattressFirm AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Overstock.com AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\SPS Commerce AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Target.com AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Wal-Mart AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Wal-Mart.com AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\Wayfair AS2</br>
    D:\FTP-DATA\CLEO_PRD\inbox\WellsFargo AS2</br>
    > 2-1-3-1.exception: skip the "Commercehub AS2 Production"</br>
2-1-4.acceptable condition: minimum 1 file in the folder but if not send an email.
