from werkzeug.exceptions import UnprocessableEntity, NotFound


class ModelException(Exception):
    pass


class ValidationException(UnprocessableEntity):
    def __init__(self, errors):
        response = dict(message="Validation Failed", errors=errors)
        super().__init__(response=response)


class ModelNotFoundException(NotFound):
    def __init__(self, table=None, id=None):
        error = "Couldn't find a given resource"
        if table:
            error = f"Coudnot find a {table} resource with  id: {id}"
        super().__init__(response=dict(error=error))
