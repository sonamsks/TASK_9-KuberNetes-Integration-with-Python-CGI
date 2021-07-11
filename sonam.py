#!/usr/bin/python3
import cgi
import time
from subprocess import getoutput
print("content-type:text/html")
print("")

form = cgi.FieldStorage()
cmd = form.getvalue("cmd")

def kube(inp_cmd):
    print(getoutput(f"sudo kubectl {inp_cmd}"))

if ("show" in cmd or "display" in cmd) and  "pods" in cmd:
    kube("get pods")

elif ("launch" in cmd or "create" in cmd) and "pods" in cmd:
    if "name" in cmd and "image" in cmd:

        cmd_str = cmd.split()
        print(cmd_str)
        image_name = cmd_str[cmd_str.index("name")+1]
        name = cmd_str[cmd_str.index("name")+1]
        print(name)
        print(image_name)

        kube(f"run {name} --image {image_name}")

elif ("launch" in cmd or "create" in cmd) and "deployment" in cmd:
        if "name" in cmd  and "is" in cmd and "image" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")
            elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")

        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
             img_name = cmd1[cmd1.index("image")+1]
            kube(f"create deployment {name} --image {img_name}")


elif "expose" in cmd and  "deployment" in cmd:
        if "name" in cmd  and "is" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+2]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")
        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
              port = cmd1[cmd1.index("port")+1]
            kube(f"expose deployment {name} --port={port} --type=NodePort")
            kube(f"get service  {name}")


elif ("delete" in cmd or "terminate"  in cmd ) and ("everything" in cmd):
    kube(" delete all --all")

elif ("show" in cmd or "display" in cmd) and  "deployment" in cmd:
    kube("get deployments")

elif ("show" in cmd or "display" in cmd) and  "services" in cmd:
    kube("get services")


elif ("deployment" in cmd ) and ("increase" in cmd or "decrease" in cmd or "replicas" in cmd):
        cmd1 = cmd.split()
        number = cmd1[cmd1.index("to")+1]
        if "name" in cmd  and "is" in cmd and "image" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
             name = cmd1[cmd_index+2]
            img_name = cmd1[cmd1.index("image")+1]
            kube(f"scale deployment {name} --replicas={number}")
            time.sleep(1)
            kube("get pods")
        elif "name" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("name")
            name = cmd1[cmd_index+1]
            kube(f"scale deployment {name} --replicas={number}")
            time.sleep(1)
            kube("get pods")
        else:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("deployment")
            name = cmd1[cmd_index+1]
            kube(f"scale deployment {name} --replicas={number}")
            time.sleep(1)
            kube("get pods")


elif "delete" in cmd:
            cmd1 = cmd.split()
            cmd_index = cmd1.index("delete")
            name = cmd1[cmd_index+2]
            name1 = cmd1[cmd_index+1]
            kube(f"delete {name1} {name}")


# elif ("destroy" in cmd or "abrade" in cmd) and "everything" in cmd:
   # kube("delete all --all")


# print(cmd)

# print(getoutput("sudo "+cmd))



            
            
            
        
        
