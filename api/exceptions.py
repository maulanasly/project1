import json

class ApiException(Exception):
    extra = dict()

    def __init__(self, **kwargs):
        super(ApiException, self).__init__()
        for (key, value) in enumerate(kwargs):
            if key in self.extra:
                if not isinstance(self.extra[key], list):
                    self.extra[key] = [self.extra[key]]
                self.extra[key].append(value)
            else:
                self.extra[key] = value

    @classmethod
    def to_swagger(cls):
        reason = {
            "code": cls.code,
            "reason": cls.description,
            "extra_info": cls.extra
        }
        return {
            "code": cls.status_code,
            "message": json.dumps(reason)
        }


class PostNotFound(ApiException):
    description = "Post or artikel not found"
    code = 200
    status_code = 404


class InternalError(ApiException):
    description = "internal error"
    code = 402
    status_code = 500
