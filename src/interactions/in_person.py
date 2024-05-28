from datetime import datetime, timedelta

class InPersonInteraction:
    def __init__(self, start_time: datetime, end_time: datetime, interaction_type: str, quality: int,
                 your_mood_before: str, your_mood_after: str, their_mood_before: str, their_mood_after: str,
                 topics_discussed: list, notes: str):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = end_time - start_time
        self.interaction_type = interaction_type
        self.quality = quality
        self.your_mood_before = your_mood_before
        self.your_mood_after = your_mood_after
        self.their_mood_before = their_mood_before
        self.their_mood_after = their_mood_after
        self.topics_discussed = topics_discussed
        self.notes = notes

    def to_dict(self):
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration_minutes": self.duration.total_seconds() / 60,
            "interaction_type": self.interaction_type,
            "quality": self.quality,
            "your_mood_before": self.your_mood_before,
            "your_mood_after": self.your_mood_after,
            "their_mood_before": self.their_mood_before,
            "their_mood_after": self.their_mood_after,
            "topics_discussed": self.topics_discussed,
            "notes": self.notes
        }