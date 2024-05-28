from datetime import datetime, timedelta

class CallInteraction:
    def __init__(self, start_time: datetime, end_time: datetime, quality: int,
                 your_mood_before: str, your_mood_after: str, their_mood_before: str, their_mood_after: str,
                 notes: str):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = end_time - start_time
        self.quality = quality
        self.your_mood_before = your_mood_before
        self.your_mood_after = your_mood_after
        self.their_mood_before = their_mood_before
        self.their_mood_after = their_mood_after
        self.notes = notes

    def to_dict(self):
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration_minutes": self.duration.total_seconds() / 60,
            "quality": self.quality,
            "your_mood_before": self.your_mood_before,
            "your_mood_after": self.your_mood_after,
            "their_mood_before": self.their_mood_before,
            "their_mood_after": self.their_mood_after,
            "notes": self.notes
        }