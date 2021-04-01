class CppWrapper:
    def __init__(self, file):
        self.file = file

    def elem(self):
        elements = []
        FileHandler = open(f"{self.file}", "r")
        for line in FileHandler:
            stripped_line = line.strip()
            if 'namespace' in stripped_line:
                stripped_line = stripped_line.replace('namespace', '->')  # why replace do not work here???
                elements.append(stripped_line)
            if 'class' in stripped_line:
                stripped_line = stripped_line.replace('class', '-->')  # why replace do not work here???
                elements.append(stripped_line)
            if 'enum' in stripped_line:
                stripped_line = stripped_line.replace('enum', '--->')  # why replace do not work here???
                elements.append(stripped_line)
            if 'UI16' in stripped_line or 'UI8' in stripped_line or 'UI8' in stripped_line or 'SI16' in stripped_line:
                stripped_line = stripped_line[:stripped_line.index(';')]
                stripped_line = '--->' + stripped_line[stripped_line.index(' '):]
                elements.append(stripped_line)

        return elements


cw = CppWrapper('dummy')
elements = cw.elem()

for i in elements:
    print(i)

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
