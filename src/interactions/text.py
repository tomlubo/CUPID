from datetime import datetime

class TextInteraction:
    def __init__(self, start_time: datetime, end_time: datetime, num_messages_sent: int,
                 num_messages_received: int, avg_length_sent: int, avg_length_received: int,
                 avg_response_time: int, quality: int, sentiment: str, notes: str):
        self.start_time = start_time
        self.end_time = end_time
        self.num_messages_sent = num_messages_sent
        self.num_messages_received = num_messages_received
        self.avg_length_sent = avg_length_sent
        self.avg_length_received = avg_length_received
        self.avg_response_time = avg_response_time
        self.quality = quality
        self.sentiment = sentiment
        self.notes = notes

    def to_dict(self):
        return {
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "num_messages_sent": self.num_messages_sent,
            "num_messages_received": self.num_messages_received,
            "avg_length_sent": self.avg_length_sent,
            "avg_length_received": self.avg_length_received,
            "avg_response_time": self.avg_response_time,
            "quality": self.quality,
            "sentiment": self.sentiment,
            "notes": self.notes
        }