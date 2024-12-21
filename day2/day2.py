reports = []
with open("day2/data.txt","r") as f:
    for line in f:
        reports.append( [int(level) for level in line.split()] )


def is_safe(report):
    deltas = []

    for i in range(len(report)-1):
        deltas.append(report[i+1]-report[i])
    if 0 in deltas:
        return False
    inc = None
    for d in deltas:
        if abs(d) > 3:
            #print("too large step")
            return False
        if inc is None:
            inc = d>0
        else:
            if not (inc == (d>0)):
                #print("dir mismatch")
                return False
    return True


def is_safe_with_damper(report):
    # Try out with one level removed to see if it's safe. if we find one, return early
    for i in range(len(report)):
        temp = report.copy()
        del temp[i]
        if is_safe(temp):
            return True
    
    return False

print(reports[956])
print(is_safe(reports[956]))

num_safe = 0
for report in reports:
    if is_safe(report):
        num_safe += 1

print("Part 1:")
print(num_safe)

num_safe = 0
for report in reports:
    if is_safe(report):
        num_safe += 1
    else:
        if is_safe_with_damper(report):
            num_safe +=1
print("Part 2:")
print(num_safe)   
        

