```json
{
    "utils/visualization.py": {
        "content": "
import logging
from typing import Tuple, List
from langfuse import StateGraph
from petals import visualize_regime_switch

logger = logging.getLogger(__name__)

def visualize_non_stationary_drift_index(non_stationary_drift_index: List[float], 
                                        stochastic_regime_switch: bool) -> Tuple[StateGraph, str]:
    """
    Visualize the non-stationary drift index and stochastic regime switch.

    Args:
    - non_stationary_drift_index (List[float]): The non-stationary drift index values.
    - stochastic_regime_switch (bool): Whether to apply stochastic regime switch.

    Returns:
    - A tuple containing the StateGraph and a description of the visualization.
    """
    try:
        logger.info('Visualizing non-stationary drift index and stochastic regime switch')
        state_graph = StateGraph()
        state_graph.add_nodes_from(non_stationary_drift_index)
        if stochastic_regime_switch:
            state_graph.add_edges_from(visualize_regime_switch(non_stationary_drift_index))
        description = 'Non-stationary drift index with stochastic regime switch' if stochastic_regime_switch else 'Non-stationary drift index'
        return state_graph, description
    except Exception as e:
        logger.error(f'Error visualizing non-stationary drift index and stochastic regime switch: {e}')
        return None, None

def visualize_rocket_science_problem(rocket_science_data: List[float]) -> Tuple[StateGraph, str]:
    """
    Visualize the rocket science problem.

    Args:
    - rocket_science_data (List[float]): The rocket science data.

    Returns:
    - A tuple containing the StateGraph and a description of the visualization.
    """
    try:
        logger.info('Visualizing rocket science problem')
        state_graph = StateGraph()
        state_graph.add_nodes_from(rocket_science_data)
        description = 'Rocket science problem visualization'
        return state_graph, description
    except Exception as e:
        logger.error(f'Error visualizing rocket science problem: {e}')
        return None, None

if __name__ == '__main__':
    non_stationary_drift_index = [0.1, 0.2, 0.3, 0.4, 0.5]
    stochastic_regime_switch = True
    rocket_science_data = [10.0, 20.0, 30.0, 40.0, 50.0]
    
    state_graph, description = visualize_non_stationary_drift_index(non_stationary_drift_index, stochastic_regime_switch)
    print(f'Visualization description: {description}')
    
    state_graph, description = visualize_rocket_science_problem(rocket_science_data)
    print(f'Visualization description: {description}')
",
        "commit_message": "feat: implement specialized visualization logic"
    }
}
```