from datetime import datetime
from interactions.in_person import InPersonInteraction
from interactions.text import TextInteraction
from interactions.call import CallInteraction
from database.db import (
    create_tables, insert_in_person_interaction, insert_text_interaction, insert_call_interaction,
    delete_in_person_interaction, delete_text_interaction, delete_call_interaction,
    load_in_person_interactions, load_text_interactions, load_call_interactions
)
import pandas as pd
import matplotlib.pyplot as plt

def add_in_person_interaction():
    start_time = datetime.strptime(input("Start time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(input("End time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
    interaction_type = input("Interaction type: ")
    quality = int(input("Quality (1-10): "))
    your_mood_before = input("Your mood before: ")
    your_mood_after = input("Your mood after: ")
    their_mood_before = input("Their mood before: ")
    their_mood_after = input("Their mood after: ")
    topics_discussed = input("Topics discussed (comma separated): ").split(',')
    notes = input("Notes: ")

    interaction = InPersonInteraction(start_time, end_time, interaction_type, quality,
                                      your_mood_before, your_mood_after, their_mood_before, their_mood_after,
                                      topics_discussed, notes)
    insert_in_person_interaction(interaction)
    print("In-person interaction added.")

def add_text_interaction():
    start_time = datetime.strptime(input("Start time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(input("End time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
    num_messages_sent = int(input("Number of messages sent: "))
    num_messages_received = int(input("Number of messages received: "))
    avg_length_sent = int(input("Average length of sent messages: "))
    avg_length_received = int(input("Average length of received messages: "))
    avg_response_time = int(input("Average response time (seconds): "))
    quality = int(input("Quality (1-10): "))
    sentiment = input("Sentiment: ")
    notes = input("Notes: ")

    interaction = TextInteraction(start_time, end_time, num_messages_sent, num_messages_received,
                                  avg_length_sent, avg_length_received, avg_response_time,
                                  quality, sentiment, notes)
    insert_text_interaction(interaction)
    print("Text interaction added.")

def add_call_interaction():
    start_time = datetime.strptime(input("Start time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(input("End time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
    quality = int(input("Quality (1-10): "))
    your_mood_before = input("Your mood before: ")
    your_mood_after = input("Your mood after: ")
    their_mood_before = input("Their mood before: ")
    their_mood_after = input("Their mood after: ")
    notes = input("Notes: ")

    interaction = CallInteraction(start_time, end_time, quality, your_mood_before,
                                  your_mood_after, their_mood_before, their_mood_after, notes)
    insert_call_interaction(interaction)
    print("Call interaction added.")

def delete_interaction():
    interaction_type = input("Enter interaction type to delete (in_person, text, call): ")
    interaction_id = int(input("Enter interaction ID to delete: "))

    if interaction_type == "in_person":
        delete_in_person_interaction(interaction_id)
    elif interaction_type == "text":
        delete_text_interaction(interaction_id)
    elif interaction_type == "call":
        delete_call_interaction(interaction_id)
    else:
        print("Invalid interaction type.")
        return

    print(f"{interaction_type} interaction with ID {interaction_id} deleted.")

def plot_interaction_quality(df, interaction_type):
    df['start_time'] = pd.to_datetime(df['start_time'])
    df = df.sort_values(by='start_time')

    plt.figure(figsize=(10, 5))
    plt.plot(df['start_time'], df['quality'], marker='o', linestyle='-', label=interaction_type)
    plt.xlabel('Date')
    plt.ylabel('Quality')
    plt.title(f'Quality of {interaction_type} Interactions Over Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    create_tables()
    
    while True:
        print("\nMenu:")
        print("1. Add In-Person Interaction")
        print("2. Add Text Interaction")
        print("3. Add Call Interaction")
        print("4. Delete Interaction")
        print("5. Plot In-Person Interaction Quality")
        print("6. Plot Text Interaction Quality")
        print("7. Plot Call Interaction Quality")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_in_person_interaction()
        elif choice == '2':
            add_text_interaction()
        elif choice == '3':
            add_call_interaction()
        elif choice == '4':
            delete_interaction()
        elif choice == '5':
            df = load_in_person_interactions()
            plot_interaction_quality(df, "In-Person")
        elif choice == '6':
            df = load_text_interactions()
            plot_interaction_quality(df, "Text")
        elif choice == '7':
            df = load_call_interactions()
            plot_interaction_quality(df, "Call")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")