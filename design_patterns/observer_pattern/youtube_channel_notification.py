from abc import ABC, abstractmethod
from typing import List


# ─── Observer Interface ───────────────────────────────────────
class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data: dict) -> None:
        pass


# ─── Subject Interface ────────────────────────────────────────
class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, event: str, data: dict) -> None:
        pass


# ─── Concrete Subject ─────────────────────────────────────────
class YouTubeChannel(Subject):
    def __init__(self, name: str):
        self._name = name
        self._observers: List[Observer] = []   # list of subscribers
        self._videos = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"New subscriber added to {self._name}")

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Subscriber removed from {self._name}")

    def notify(self, event: str, data: dict) -> None:
        for observer in self._observers:
            observer.update(event, data)   # push to all subscribers ✅

    def upload_video(self, title: str, duration: str) -> None:
        video = {"title": title, "duration": duration, "channel": self._name}
        self._videos.append(video)
        print(f"\n{self._name} uploaded: '{title}'")
        self.notify("NEW_VIDEO", video)    # automatically notifies ✅

    def go_live(self, topic: str) -> None:
        print(f"\n{self._name} is going LIVE: '{topic}'")
        self.notify("LIVE_STREAM", {"topic": topic, "channel": self._name})


# ─── Concrete Observers ───────────────────────────────────────
class EmailSubscriber(Observer):
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email

    def update(self, event: str, data: dict) -> None:
        if event == "NEW_VIDEO":
            print(f"EMAIL to {self._email}: New video '{data['title']}' on {data['channel']}")
        elif event == "LIVE_STREAM":
            print(f"EMAIL to {self._email}: {data['channel']} is live — '{data['topic']}'")


## Pull model example (not used in this YouTube case, but for reference):
#def notify(self):
#    for observer in self._observers:
#        observer.update(self)          # passes self — observer pulls what it needs

#class EmailSubscriber(Observer):
#    def update(self, subject: Subject):
#        data = subject.get_latest()    # observer pulls data itself


class MobileSubscriber(Observer):
    def __init__(self, name: str, device_id: str):
        self._name = name
        self._device_id = device_id

    def update(self, event: str, data: dict) -> None:
        if event == "NEW_VIDEO":
            print(f"PUSH NOTIFICATION to {self._name}: New video — '{data['title']}'")
        elif event == "LIVE_STREAM":
            print(f"PUSH NOTIFICATION to {self._name}: LIVE NOW — '{data['topic']}'")


class SMSSubscriber(Observer):
    def __init__(self, name: str, phone: str):
        self._name = name
        self._phone = phone

    def update(self, event: str, data: dict) -> None:
        if event == "NEW_VIDEO":
            print(f"SMS to {self._phone}: '{data['title']}' just dropped on {data['channel']}!")


# ─── Usage ────────────────────────────────────────────────────
if __name__ == "__main__":

    # Create channel
    channel = YouTubeChannel("TechWithTim")

    # Create subscribers
    rahul = EmailSubscriber("Rahul", "rahul@gmail.com")
    priya = MobileSubscriber("Priya", "device_001")
    arjun = SMSSubscriber("Arjun", "+91-9876543210")

    # Subscribe
    channel.subscribe(rahul)
    channel.subscribe(priya)
    channel.subscribe(arjun)

    # Channel uploads video — all subscribers notified ✅
    channel.upload_video("Python Design Patterns", "45 mins")

    # Priya unsubscribes
    print()
    channel.unsubscribe(priya)

    # New video — only rahul and arjun notified ✅
    channel.upload_video("SOLID Principles Explained", "30 mins")

    # Go live — only email and mobile get this event
    channel.go_live("Live Coding Session")