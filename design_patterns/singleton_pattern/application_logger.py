## application logger using thread safe singleton pattern


import threading
from datetime import datetime


class ApplicationLogger:
    _instance = None
    _lock = threading.Lock()

    # Valid log levels
    VALID_LEVELS = {"INFO", "WARNING", "ERROR"}

    def __new__(cls):
        if cls._instance is None:                          # Check 1 — fast path
            with cls._lock:
                if cls._instance is None:                  # Check 2 — safe path
                    cls._instance = super().__new__(cls)
                    cls._instance._logs = []               # store as list of dicts
                    cls._instance._initialized = True
        return cls._instance

    def log(self, level: str, message: str):
        # Validate level
        if level not in self.VALID_LEVELS:
            raise ValueError(f"Invalid log level: {level}. Must be one of {self.VALID_LEVELS}")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Store as structured dict — easier to filter ✅
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }

        # Thread safe append ✅
        with self._lock:
            self._logs.append(log_entry)

        # Formatted output
        formatted = f"{timestamp} [{level}] {message}"
        print(formatted)

    def get_logs(self, level: str = None):
        with self._lock:                          # thread safe read ✅
            if level is None:
                logs = self._logs
            else:
                # Case insensitive filtering ✅
                logs = [log for log in self._logs if log["level"] == level.upper()]

        # Return formatted strings
        return [
            f"{log['timestamp']} [{log['level']}] {log['message']}"
            for log in logs
        ]


# ─── Usage ───────────────────────────────────────────────────
if __name__ == "__main__":
    logger1 = ApplicationLogger()
    logger2 = ApplicationLogger()

    # Singleton check
    print(f"Same instance: {logger1 is logger2}")   # True ✅

    # Logging
    logger1.log("INFO", "Application started")
    logger1.log("WARNING", "High memory usage")
    logger2.log("ERROR", "Database connection failed")
    logger2.log("INFO", "User logged in")

    # Filter by level
    print("\nINFO logs:")
    for log in logger1.get_logs("INFO"):
        print(log)

    print("\nERROR logs:")
    for log in logger1.get_logs("ERROR"):
        print(log)

    print("\nAll logs:")
    for log in logger1.get_logs():
        print(log)

    # Invalid level
    try:
        logger1.log("CRITICAL", "This should fail")
    except ValueError as e:
        print(f"\nCaught error: {e}")