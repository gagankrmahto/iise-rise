#❗ Solve the Use Case Theory❗

import os
while True:
    p=input("Chat with me with your requirements : ")
    # BROWSERS

    if (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("chrome" in p) or "chrome browser" in p):
        os.system("chrome")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("youtube" in p):
        os.system("chrome www.youtube.com")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("fb" in p) or "facebook" in p):
        os.system("chrome www.facebook.com")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("insta" in p) or "instagram" in p):
        os.system("chrome www.instagram.com")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("mozilla" in p or "firefox" in p): 
        os.system("firefox")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("explorer" in p and "internet" in p): 
        os.system("iexplore")

    # TEXT EDITORS,IDE'S AND WORD PROCESSING
    elif (("run" in p) or ("execute" in p)) and (('notepad' in p) or ("editor" in p)):
        os.system("notepad")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("wordpad" in p): 
        os.system("wordpad")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("vscode" in p) or "visual studio code" in p):
        os.system("code")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("word" in p) or "ms word" in p or "microsoft word" in p):
        os.system("winword")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("powerpoint" in p) or "ms powerpoint" in p or "microsoft powerpoint" in p):
        os.system("powerpnt")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("excel" in p) or "ms excel" in p or "microsoft excel" in p):
        os.system("excel")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("outlook" in p) or "ms outlook" in p or "microsoft outlook" in p):
        os.system("outlook")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("publisher" in p) or "ms publisher" in p or "microsoft publisher" in p):
        os.system("mspub")
    
    # PHOTO AND RELATED SOFTWARE
    
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("illustrator" in p) or "adobe illustrator" in p):
        os.system("illustrator")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("photoshop" in p) or "adobe photoshop" in p):
        os.system("photoshop")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("vlc" in p or "vlc media player" in p): 
        os.system("vlc")
    elif (("run" in p) and ("player" in p ) and ("media" in p)) or ("play" in p and "song" in p):
        os.system("wmplayer")

    # TOOLS AND UTILITIES

    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("cmd" in p or "command prompt" in p): 
        os.system("cmd")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("calc" in p or "calculator" in p): 
        os.system("calc")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("windows powershell" in p or "powershell" in p): 
        os.system("powershell")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("control panel" in p) or ("settings" in p)): 
        os.system("control")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("explorer" in p or ("file" in p and  "explorer" in p)): 
        os.system("explorer")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("run" in p or ("windows" in p and "run" in p)): 
        os.system("run")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("anydesk" in p): 
        os.system("anydesk")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("anydesk" in p): 
        os.system("anydesk")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("github" in p and "desktop" in p) or "github" in p): 
        os.system("githubdesktop")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("utorrent" in p or "torrent" in p): 
        os.system("utweb")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and (("pdf" in p and "editor" in p) or ("pdf" in p and "xchange" in p and  "editor" in p)): 
        os.system("pdfxedit")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("bandicam" in p or ("video" in p and "recorder") or ("screen" in p and "recorder" in p)): 
        os.system("bdcam")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("virtualbox" in p or ("virtual" in p and "box")): 
        os.system("vituralbox")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("zoom" in p): 
        os.system("vituralbox")
    elif (("open" in p) or ("run" in p) or ("start" in p) or ("execute" in p)) and ("winrar" in p): 
        os.system("winrar")
    
    # GAMES

    else:
        print("don't support")
    if "stop" in p or "exit" in p:
        break
