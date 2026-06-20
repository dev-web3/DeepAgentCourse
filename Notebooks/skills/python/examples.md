# Python Examples
```python
def calculate_metrics(data: list[float]) -> dict[str, float]:
    """Calculates mean and variance of a dataset."""
    if not data:
        return {"mean": 0.0, "variance": 0.0}
    
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return {"mean": mean, "variance": variance}