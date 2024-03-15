from exception.http_errors import NotFoundError, BadRequestError
from schemas import HttpErrorResponse
import utils.util as util

class HttpExceptionHanlder:
    def http_error_handle(self, func):
        def wrapper(*args, **kwargs):
            try:
                response = func(*args, **kwargs)
                return response
            except BadRequestError as e:
                response = {"ok": False, "message": e.args[0], "status_code": 400}
                return HttpErrorResponse(**response)
            except NotFoundError as e:
                response = {"ok": False, "message": e.args[0], "status_code": 404}
                return HttpErrorResponse(**response)
            finally:
                util.debug_message_for_decorator(f"response: {response}")

        return wrapper


handler = HttpExceptionHanlder()