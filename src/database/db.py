import sqlite3

import sqlite3
import os

def create_tables():
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS in_person_interactions (
        id INTEGER PRIMARY KEY,
        start_time TEXT,
        end_time TEXT,
        duration_minutes REAL,
        interaction_type TEXT,
        quality INTEGER,
        your_mood_before TEXT,
        your_mood_after TEXT,
        their_mood_before TEXT,
        their_mood_after TEXT,
        topics_discussed TEXT,
        notes TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS text_interactions (
        id INTEGER PRIMARY KEY,
        start_time TEXT,
        end_time TEXT,
        num_messages_sent INTEGER,
        num_messages_received INTEGER,
        avg_length_sent INTEGER,
        avg_length_received INTEGER,
        avg_response_time INTEGER,
        quality INTEGER,
        sentiment TEXT,
        notes TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS call_interactions (
        id INTEGER PRIMARY KEY,
        start_time TEXT,
        end_time TEXT,
        duration_minutes REAL,
        quality INTEGER,
        your_mood_before TEXT,
        your_mood_after TEXT,
        their_mood_before TEXT,
        their_mood_after TEXT,
        notes TEXT
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()

def insert_in_person_interaction(interaction):
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO in_person_interactions (
        start_time, end_time, duration_minutes, interaction_type, quality, 
        your_mood_before, your_mood_after, their_mood_before, their_mood_after, 
        topics_discussed, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        interaction.start_time.isoformat(),
        interaction.end_time.isoformat(),
        interaction.duration.total_seconds() / 60,
        interaction.interaction_type,
        interaction.quality,
        interaction.your_mood_before,
        interaction.your_mood_after,
        interaction.their_mood_before,
        interaction.their_mood_after,
        ','.join(interaction.topics_discussed),
        interaction.notes
    ))

    conn.commit()
    conn.close()

def insert_text_interaction(interaction):
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO text_interactions (
        start_time, end_time, num_messages_sent, num_messages_received, avg_length_sent, 
        avg_length_received, avg_response_time, quality, sentiment, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        interaction.start_time.isoformat(),
        interaction.end_time.isoformat(),
        interaction.num_messages_sent,
        interaction.num_messages_received,
        interaction.avg_length_sent,
        interaction.avg_length_received,
        interaction.avg_response_time,
        interaction.quality,
        interaction.sentiment,
        interaction.notes
    ))

    conn.commit()
    conn.close()

def insert_call_interaction(interaction):
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO call_interactions (
        start_time, end_time, duration_minutes, quality, your_mood_before, 
        your_mood_after, their_mood_before, their_mood_after, notes
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        interaction.start_time.isoformat(),
        interaction.end_time.isoformat(),
        interaction.duration.total_seconds() / 60,
        interaction.quality,
        interaction.your_mood_before,
        interaction.your_mood_after,
        interaction.their_mood_before,
        interaction.their_mood_after,
        interaction.notes
    ))

    conn.commit()
    conn.close()

# Add these functions to db.py

import pandas as pd

def load_in_person_interactions():
    conn = sqlite3.connect('data/relationship_metrics.db')
    df = pd.read_sql_query('SELECT * FROM in_person_interactions', conn)
    conn.close()
    return df

def load_text_interactions():
    conn = sqlite3.connect('data/relationship_metrics.db')
    df = pd.read_sql_query('SELECT * FROM text_interactions', conn)
    conn.close()
    return df

def load_call_interactions():
    conn = sqlite3.connect('data/relationship_metrics.db')
    df = pd.read_sql_query('SELECT * FROM call_interactions', conn)
    conn.close()
    return df


def delete_in_person_interaction(interaction_id):
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()
    c.execute('DELETE FROM in_person_interactions WHERE id = ?', (interaction_id,))
    conn.commit()
    conn.close()

def delete_text_interaction(interaction_id):
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()
    c.execute('DELETE FROM text_interactions WHERE id = ?', (interaction_id,))
    conn.commit()
    conn.close()

def delete_call_interaction(interaction_id):
    conn = sqlite3.connect('data/relationship_metrics.db')
    c = conn.cursor()
    c.execute('DELETE FROM call_interactions WHERE id = ?', (interaction_id,))
    conn.commit()
    conn.close()