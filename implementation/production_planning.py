```json
{
    "implementation/production_planning.py": {
        "content": "
import logging
from typing import List, Dict
from langfuse import StateGraph
from petals import RegimeSwitchModel
from dspy import NonStationaryDriftIndex

def calculate_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    data (List[float]): The input dataset.

    Returns:
    float: The non-stationary drift index.

    Raises:
    ValueError: If the input data is empty.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        return NonStationaryDriftIndex(data).calculate()
    except Exception as e:
        logging.error(f'Error calculating non-stationary drift index: {e}')
        raise

def stochastic_regime_switch(model: RegimeSwitchModel, data: List[float]) -> Dict[str, float]:
    """
    Perform stochastic regime switching for a given model and dataset.

    Args:
    model (RegimeSwitchModel): The regime switch model.
    data (List[float]): The input dataset.

    Returns:
    Dict[str, float]: The regime switch results.

    Raises:
    ValueError: If the input data is empty.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        return model.stochastic_regime_switch(data)
    except Exception as e:
        logging.error(f'Error performing stochastic regime switch: {e}')
        raise

def create_state_graph(model: RegimeSwitchModel) -> StateGraph:
    """
    Create a state graph for a given regime switch model.

    Args:
    model (RegimeSwitchModel): The regime switch model.

    Returns:
    StateGraph: The state graph.

    Raises:
    ValueError: If the input model is None.
    """
    try:
        if not model:
            raise ValueError('Input model is None')
        return StateGraph(model)
    except Exception as e:
        logging.error(f'Error creating state graph: {e}')
        raise

def production_planning(data: List[float], model: RegimeSwitchModel) -> Dict[str, float]:
    """
    Perform production planning using stochastic regime switching and non-stationary drift index.

    Args:
    data (List[float]): The input dataset.
    model (RegimeSwitchModel): The regime switch model.

    Returns:
    Dict[str, float]: The production planning results.

    Raises:
    ValueError: If the input data is empty or the input model is None.
    """
    try:
        if not data:
            raise ValueError('Input data is empty')
        if not model:
            raise ValueError('Input model is None')
        non_stationary_drift_index = calculate_non_stationary_drift_index(data)
        regime_switch_results = stochastic_regime_switch(model, data)
        state_graph = create_state_graph(model)
        return {
            'non_stationary_drift_index': non_stationary_drift_index,
            'regime_switch_results': regime_switch_results,
            'state_graph': state_graph
        }
    except Exception as e:
        logging.error(f'Error performing production planning: {e}')
        raise

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    model = RegimeSwitchModel()
    results = production_planning(data, model)
    print(results)
",
        "commit_message": "feat: implement specialized production_planning logic"
    }
}
```