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

for code_element in elements:
  print(code_element.name)


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