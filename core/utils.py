from fastapi.params import Param


def user_dep(name: str = Param, password: str = Param) -> dict[str, str | bool]:
    return {"name": name, "valid": True}
