
# Sentiment Analysis Using NLP
# Pure Python - No External Libraries Required

import re

# Positive and negative word dictionaries
positive_words = [
    "good", "great", "excellent", "happy",
    "love", "wonderful", "best", "amazing",
    "nice", "awesome", "beautiful", "success"
]

negative_words = [
    "bad", "worst", "poor", "sad",
    "hate", "terrible", "awful", "angry",
    "disappointed", "fail", "boring", "ugly"
]

# Sentiment Analysis Function
def sentiment_analysis(sentence):

    # Convert sentence to lowercase
    sentence = sentence.lower()

    # Remove special characters
    words = re.findall(r'\b[a-z]+\b', sentence)

    positive_count = 0
    negative_count = 0

    # Count positive and negative words
    for word in words:

        if word in positive_words:
            positive_count += 1

        elif word in negative_words:
            negative_count += 1

    # Determine sentiment
    if positive_count > negative_count:
        result = "Positive Sentiment"

    elif negative_count > positive_count:
        result = "Negative Sentiment"

    else:
        result = "Neutral Sentiment"

    return result, positive_count, negative_count


# Main Program
print("================================")
print("     SENTIMENT ANALYSIS")
print("       USING NLP")
print("================================")

# Get user input
text = input("\nEnter a sentence: ")

# Perform sentiment analysis
result, positive, negative = sentiment_analysis(text)

# Display output
print("\n--------- RESULTS ---------")

print("Input Sentence:", text)

print("Positive Words:", positive)

print("Negative Words:", negative)

print("Sentiment:", result)

print("---------------------------")
print("Sentiment Analysis Completed!")
