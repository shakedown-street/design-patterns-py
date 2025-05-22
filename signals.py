"""
This is an example of the signals behavioral pattern implemented in Python.

Note:
This is not thread-safe, and there is no way to dispose of signals or
computations.
"""

_current_computation: "Computation" = None


class Signal:
    def __init__(self, value):
        self._value = value
        self._subscribers: set["Computation"] = set()

    def get(self):
        global _current_computation
        if _current_computation is not None:
            self._subscribers.add(_current_computation)
            _current_computation._dependencies.add(self)
        return self._value

    def set(self, value):
        if self._value != value:
            self._value = value
            for sub in list(self._subscribers):
                sub.run()


class Computation:
    def __init__(self, func):
        self._func = func
        self._dependencies: set[Signal] = set()
        self.run()

    def run(self):
        global _current_computation
        for dep in self._dependencies:
            dep._subscribers.discard(self)
        self._dependencies.clear()

        _current_computation = self
        try:
            self._func()
        finally:
            _current_computation = None


def create_signal(initial_value):
    sig = Signal(initial_value)
    return sig.get, sig.set


def create_effect(fn):
    return Computation(fn)


count_get, count_set = create_signal(0)

create_effect(lambda: print(f"Count is now {count_get()}"))

count_set(1)
count_set(2)
count_set(3)
