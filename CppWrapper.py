
class CppWrapper:
    c_types = ("UI16", "UI8", "SI16", "SI32")
    c_elements = ("namespace", "class", "enum")

    def __init__(self, file):
        self.file = file

    def elem(self):
        parents = {}
        elements = []
        FileHandler = open(f"{self.file}", "r")
        for line in FileHandler:
            stripped_line = line.strip()

            for i, elem in enumerate(self.c_elements):
                if elem not in stripped_line:
                    continue

                stripped_line = stripped_line.replace(elem, ('-'*i + '->'))
                elements.append(stripped_line)



            if any(t in stripped_line for t in self.c_types):
                stripped_line = stripped_line[:stripped_line.index(';')]
                stripped_line = '--->' + stripped_line[stripped_line.index(' '):]
                elements.append(stripped_line)

        return elements

    def get_el(self):
        dict = {}
        keys = {}
        index = 0
        keys[index] = 'root'
        dict[keys[index]] = []
        index += 1

        FileHandler = open(f"{self.file}", "r")
        for line in FileHandler:
            stripped_line = line.strip()
            print('0')
            if '{' in stripped_line:
                print('2')
                index += 1

            elif '}' in stripped_line:
                print('3')
                index -= 1

            else: #elem in stripped_line:
                for i, elem in enumerate(self.c_elements):
                    if elem in stripped_line:
                        keyword = stripped_line.replace(elem, '')
                        dict[(keys[index-1])].append(keyword)
                        keys[index] = keyword
                        dict[keyword] = []
                        # print(dict[(keys[index-1])])

        return dict

cw = CppWrapper('dummy')
elements = cw.get_el()

for key, value in elements.items():
    print(f'{key} : {value}')

# print(elements)

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
