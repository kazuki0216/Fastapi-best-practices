from pydantic import BaseModel


class ValidationResult(BaseModel):
    result: bool = True
    details: str = ""


def string_input_validation(
    input, min_length: int = 3, max_length: int = 20
) -> ValidationResult:
    forbidden_chars = ["$", "#", "%"]
    if type(input) is not str:
        return ValidationResult(result=False, details="Input has to be a string")
    else:
        sanitized_string = input.strip()
        if not sanitized_string.isalpha():
            return ValidationResult(
                result=False, details="Input should only contain letters (a–z, A–Z)."
            )
        if "  " in sanitized_string:
            return ValidationResult(
                result=False, details="No excessive spaces allowed between words."
            )
        if sanitized_string == "":
            return ValidationResult(result=False, details="This is an empty string")
        if len(sanitized_string) < min_length:
            return ValidationResult(
                result=False, details=f"Input must be at least {min_length} characters."
            )
        if len(sanitized_string) > max_length:
            return ValidationResult(
                result=False,
                details=f"Input must be no longer than {max_length} characters.",
            )
        if any(char in sanitized_string for char in forbidden_chars):
            return ValidationResult(
                result=False, details="Input contains forbidden characters."
            )

    return ValidationResult(result=True, details="Valid String")
