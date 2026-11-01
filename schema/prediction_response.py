from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    prediction_category: str = Field(
        ...,
        description="The predicted insurance premium",
        example="High"
    )

    confidence: float = Field(
        ...,
        description="Model confidence score for  the predicted class (range: 0 to 1)",
        example = "0.8457"

    )

    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all classes",
        example = {"Low": 0.01, "Medium": 0.15, "high": 0.84}

    )
