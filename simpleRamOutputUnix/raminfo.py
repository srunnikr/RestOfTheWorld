import subprocess

def getRamInfo():
    ram_status = subprocess.check_output(["free"], stderr=subprocess.PIPE);
    ram_status = ram_status.split()
    
    total = float(ram_status[7])
    used = float(ram_status[8])
    free = float(ram_status[9])

    print "=================================="

    print "Total : ",repr(total).rjust(10)," /",repr((total/1024.0)).rjust(10),"MB)"
    print "Used  : ",repr(used).rjust(10)," /",repr((used/1024.0)).rjust(10),"MB)"
    print "Free  : ",repr(free).rjust(10)," /",repr((free/1024.0)).rjust(10),"MB)"
    
    print "=================================="

if __name__ == "__main__":
    getRamInfo()
