from app.data.pattern_repo import SQLitePatternRepository
from app.infrastructure.common.response_result import ResponseResult
from app.data.dto.pattern import Pattern

# repo
repository = SQLitePatternRepository()


def create_pattern(pattern_request: Pattern):
    pattern = pattern_request.pattern
    description = pattern_request.description

    repository.add_pattern(pattern, description)
    result = ResponseResult(result_code=200, result_msg="pattern added")
    return result


def delete_pattern(pattern_idx: int):
    repository.delete_pattern(pattern_idx)
    result = ResponseResult(result_code=200, result_msg="pattern deleted")
    return result
