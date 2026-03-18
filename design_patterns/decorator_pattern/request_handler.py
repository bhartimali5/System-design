from abc import ABC, abstractmethod


# ─── Abstract Handler ─────────────────────────────────────────
class RequestHandler(ABC):
    @abstractmethod
    def handle(self, request: dict) -> dict:
        pass


# ─── Base Handler/Concrete Handler ──────────────────────────────────────
class BaseRequestHandler(RequestHandler):
    def handle(self, request: dict) -> dict:
        print(f"Handling request: {request['url']}")
        return {"status": 200, "body": "OK"}


# ─── base decorator/Abstract Decorator ───────────────────────────────────────
class RequestDecorator(RequestHandler):
    def __init__(self, handler: RequestHandler):
        self._handler = handler

    def handle(self, request: dict) -> dict:
        return self._handler.handle(request)


# ─── Concrete Decorators ──────────────────────────────────────
class AuthDecorator(RequestDecorator):
    def handle(self, request: dict) -> dict:
        if "token" not in request.get("headers", {}):
            print("Auth failed — no token")
            return {"status": 401, "body": "Unauthorized"}
        print("Auth passed ✅")
        return self._handler.handle(request)   # pass to next layer


class LoggingDecorator(RequestDecorator):
    def handle(self, request: dict) -> dict:
        print(f"LOG: Incoming request → {request['url']}")
        response = self._handler.handle(request)
        print(f"LOG: Response → {response['status']}")
        return response


class RateLimitDecorator(RequestDecorator):
    def __init__(self, handler: RequestHandler, limit: int):
        super().__init__(handler)
        self._limit = limit
        self._count = 0

    def handle(self, request: dict) -> dict:
        self._count += 1
        if self._count > self._limit:
            print(f"Rate limit exceeded!")
            return {"status": 429, "body": "Too Many Requests"}
        print(f"Rate limit check passed ({self._count}/{self._limit}) ✅")
        return self._handler.handle(request)


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":

    # Stack middleware like layers ✅
    handler = (
        LoggingDecorator(
            AuthDecorator(
                RateLimitDecorator(
                    BaseRequestHandler(),
                    limit=2
                )
            )
        )
    )

    # Request 1 — valid
    print("=== Request 1 ===")
    response = handler.handle({
        "url": "/api/users",
        "headers": {"token": "abc123"}
    })
    print(f"Final response: {response}\n")

    # Request 2 — valid
    print("=== Request 2 ===")
    response = handler.handle({
        "url": "/api/orders",
        "headers": {"token": "abc123"}
    })
    print(f"Final response: {response}\n")

    # Request 3 — rate limit exceeded
    print("=== Request 3 ===")
    response = handler.handle({
        "url": "/api/products",
        "headers": {"token": "abc123"}
    })
    print(f"Final response: {response}\n")

    # Request 4 — no auth token
    print("=== Request 4 ===")
    response = handler.handle({
        "url": "/api/users",
        "headers": {}
    })
    print(f"Final response: {response}")
