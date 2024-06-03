from enum import Enum


class AlternativeHypothesisType(Enum):
    TWO_SIDED = (True, True)
    GREATER_THAN = (False, True)
    LESS_THAN = (True, False)

    def __init__(
        self,
        has_left_rejection_region: bool,
        has_right_rejection_region: bool,
    ) -> None:
        self.has_left_rejection_region = has_left_rejection_region
        self.has_right_rejection_region = has_right_rejection_region


test_type = AlternativeHypothesisType.GREATER_THAN
print(test_type.has_left_rejection_region)
