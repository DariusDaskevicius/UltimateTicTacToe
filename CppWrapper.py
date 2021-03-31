elements = []

FileHandler = open("dummy", "r")
for line in FileHandler:
    stripped_line = line.strip()
    if 'namespace' in stripped_line:
        a = '->' + stripped_line.replace('namespace', '')  # why replace do not work here???
        elements.append(a)
        print(a)
    if 'class' in stripped_line:
        a = '-->' + stripped_line.replace('class', '')  # why replace do not work here???
        elements.append(a)
        print(a)
    if 'enum' in stripped_line:
        a = '--->' + stripped_line.replace('enum', '')  # why replace do not work here???
        elements.append(a)
        print(a)
    if 'UI16' in stripped_line or 'UI8' in stripped_line or 'UI8' in stripped_line or 'SI16' in stripped_line:
        a = stripped_line[:stripped_line.index(';')]
        a = '--->' + a[a.index(' '):]
        print(a)


FileHandler.close()


"""
cleaning
-> FlowMonitor
---> FlowMonitoringStates
---> floatSwitchTimeoutCounter_
---> balancingChamberStateMemory1_
---> balancingChamberStateMemory2_
-> HydraulicsMonitor
---> timeoutCounter_
"""
