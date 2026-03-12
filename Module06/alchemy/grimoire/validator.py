def validate_ingredients(ingredients: str) -> str:
    valid_words = ["fire", "air", "water", "earth"]
    for word in valid_words:
        if word in ingredients:
            return (f"{ingredients} - VALID")

    return (f"{ingredients} - INVALID")
