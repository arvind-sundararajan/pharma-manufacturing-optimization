```json
{
    "tests/test_quality_control.py": {
        "content": "
import logging
from typing import Tuple
from langfuse import StateGraph
from petals import RegimeSwitchModel
from dspy import NonStationaryDriftIndex

def calculate_non_stationary_drift_index(data: Tuple[float, float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
        data (Tuple[float, float]): A tuple containing the dataset.

    Returns:
        float: The non-stationary drift index.

    Raises:
        Exception: If an error occurs during calculation.
    """
    try:
        logging.info('Calculating non-stationary drift index')
        non_stationary_drift_index = NonStationaryDriftIndex(data)
        return non_stationary_drift_index.calculate()
    except Exception as e:
        logging.error(f'Error calculating non-stationary drift index: {e}')
        raise

def stochastic_regime_switch(model: RegimeSwitchModel) -> bool:
    """
    Perform a stochastic regime switch using the given model.

    Args:
        model (RegimeSwitchModel): The regime switch model.

    Returns:
        bool: Whether the regime switch was successful.

    Raises:
        Exception: If an error occurs during the regime switch.
    """
    try:
        logging.info('Performing stochastic regime switch')
        return model.switch_regime()
    except Exception as e:
        logging.error(f'Error performing stochastic regime switch: {e}')
        raise

def test_quality_control(data: Tuple[float, float], model: RegimeSwitchModel) -> Tuple[float, bool]:
    """
    Test the quality control of the given data and model.

    Args:
        data (Tuple[float, float]): A tuple containing the dataset.
        model (RegimeSwitchModel): The regime switch model.

    Returns:
        Tuple[float, bool]: A tuple containing the non-stationary drift index and whether the regime switch was successful.

    Raises:
        Exception: If an error occurs during the quality control test.
    """
    try:
        logging.info('Testing quality control')
        non_stationary_drift_index = calculate_non_stationary_drift_index(data)
        regime_switch_success = stochastic_regime_switch(model)
        return non_stationary_drift_index, regime_switch_success
    except Exception as e:
        logging.error(f'Error testing quality control: {e}')
        raise

def main():
    # Create a sample dataset
    data = (1.0, 2.0)
    
    # Create a sample regime switch model
    model = RegimeSwitchModel()
    
    # Create a StateGraph
    state_graph = StateGraph()
    
    # Test the quality control
    non_stationary_drift_index, regime_switch_success = test_quality_control(data, model)
    
    # Log the results
    logging.info(f'Non-stationary drift index: {non_stationary_drift_index}')
    logging.info(f'Regime switch success: {regime_switch_success}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
",
        "commit_message": "feat: implement specialized test_quality_control logic"
    }
}
```