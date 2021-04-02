source_code1 = """
#include "platform/Types.h"
#include "cleaning/FlowMonitorCycleState.h"

namespace cleaning
{

class FlowMonitor
{
    enum FlowMonitoringStates
    {
        STATE_FLOW_MONITORING_ACTIVE = 0,
        STATE_FLOW_MONITORING_INACTIVE = 1,
        STATE_FLOW_MONITORING_ERROR_ACTIVE = 2,
        STATE_FLOW_MONITORING_ERROR_INACTIVE = 3,
        STATE_FLOW_MONITORING_ACTIVE_INIT = 4,
    };

    UI16 floatSwitchTimeoutCounter_; /*!< Counter for float switch timeout managing */
    UI8 balancingChamberStateMemory1_; /*!< is 1 when preceding Balancing Chamber state_ was balancing or filling state_ and 0 else */
    UI8 balancingChamberStateMemory2_; /*!< is 1 when preceding Balancing Chamber state_ was balancing or filling state_ and 0 else */
};

class HydraulicsMonitor
{
    SI16 timeoutCounter_; /*!< Counter for timeout */
};

}
"""

source_code2 = """
#include "platform/Types.h"
#include "cleaning/FlowMonitorCycleState.h"

namespace cleaning
{

class LevelMonitor
{
    UI8 is On; /*!< is 1 when preceding Balancing Chamber state_ was balancing or filling state_ and 0 else */
};
}
"""


# parse this source and come up with a way to iterate over it.

# for code_element in elements:
#   print(code_element.name)

from pprint import pprint


class Node:
    def __init__(self, name, ctype):
        self.name = name
        self.ctype = ctype
        self.parent: Node = None
        self.children: List[Node] = []

    def __str__(self):
        # self -> pointer to instance of class Node
        # self.__class__ -> pointer to class Node
        # self.__class__.__name__ -> pointer to class variable __name__ : Node.__name__

        # "Node(name, ctype, line_no)"
        return f"{self.__class__.__name__}(name={self.name}, ctype={self.ctype})"

    def __repr__(self):
        return self.__str__()


root_node = Node(name="root", ctype="namespace")
child_1 = Node(name="child_1", ctype="class")
child_2 = Node(name="child_2", ctype="enum")

root_node.children.append(child_1)
root_node.children.append(child_2)

child_1.parent = root_node
child_2.parent = root_node


for child in root_node:
    print(child)

    # child_1
    # child_2

print(root_node["child_1"])  # => Node(name="child_1", ctype="class")


# root_node = Node(name="root", ctype="namespace")
# root_node = Node(name="root", ctype="namespace")



# pprint(CppWrapper.elem())
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