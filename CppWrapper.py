class CppWrapper:
    c_types = ("UI16", "UI8", "SI16", "SI32")
    c_elements = ("namespace", "class", "enum")

    def __init__(self, file):
        self.file = file

    def elem(self):
        elements = []
        FileHandler = open(f"{self.file}", "r")
        for line in FileHandler:
            stripped_line = line.strip()

            for i, elem in enumerate(self.c_elements):
                if elem not in stripped_line:
                    continue

                stripped_line = stripped_line.replace(elem, ('-'*i + '->'))  # why replace do not work here???
                elements.append(stripped_line)

            # if 'namespace' in stripped_line:
            #     stripped_line = stripped_line.replace('namespace', '->')  # why replace do not work here???
            #     elements.append(stripped_line)
            # if 'class' in stripped_line:
            #     stripped_line = stripped_line.replace('class', '-->')  # why replace do not work here???
            #     elements.append(stripped_line)
            # if 'enum' in stripped_line:
            #     stripped_line = stripped_line.replace('enum', '--->')  # why replace do not work here???
            #     elements.append(stripped_line)

            if any(t in stripped_line for t in self.c_types):
            # if 'UI16' in stripped_line or 'UI8' in stripped_line or 'UI8' in stripped_line or 'SI16' in stripped_line:
                stripped_line = stripped_line[:stripped_line.index(';')]
                stripped_line = '--->' + stripped_line[stripped_line.index(' '):]
                elements.append(stripped_line)

        return elements


cw = CppWrapper('dummy')
elements = cw.elem()

for i in elements:
    print(i)

for element in elements["FlowMonitor"]:
    print(element)

    """
    ---> FlowMonitoringStates, lineno = 5
    ---> floatSwitchTimeoutCounter_, lineno = 6
    ---> balancingChamberStateMemory1_, lineno = 7
    ---> balancingChamberStateMemory2_, lineno = 8
    """

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
