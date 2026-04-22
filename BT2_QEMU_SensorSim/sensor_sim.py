import random


class SimLED:
    def __init__(self, pin, name="LED"):
        self.pin = pin
        self.name = name
        self.is_on = False

    def on(self):
        self.is_on = True
        print(f"[{self.name} pin {self.pin}] ON")

    def off(self):
        self.is_on = False
        print(f"[{self.name} pin {self.pin}] OFF")

    def blink(self, on_time=1, off_time=1):
        print(f"[{self.name}] BLINK on={on_time}s off={off_time}s")


class SimUltrasonic:
    def __init__(self, echo, trigger, base_distance=50.0):
        self.echo = echo
        self.trigger = trigger
        self.base_distance = base_distance

    @property
    def distance(self):
        raw = random.gauss(self.base_distance, 2.0)
        return max(2, min(400, raw))

    def set_base(self, new_val):
        self.base_distance = max(2, min(400, new_val))


class SimPotentiometer:
    def __init__(self, channel=0, initial_value=0.5):
        self._value = initial_value

    @property
    def value(self):
        return self._value

    def set_value(self, v):
        self._value = max(0.0, min(1.0, float(v)))


if __name__ == "__main__":
    led = SimLED(17, "TestLED")
    led.on()
    led.off()

    us = SimUltrasonic(echo=24, trigger=23)
    for i in range(5):
        print(f"  Distance: {us.distance:.1f} cm")

    pot = SimPotentiometer()
    print(f"  Pot value: {pot.value}")
    pot.set_value(0.8)
    print(f"  Pot after set: {pot.value}")
