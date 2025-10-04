from textblob import TextBlob

def analyze_sentiment(text):
  """ Analyzes the sentiment of a given text and returns 'Positive', 'Negative', or 'Neutral'. """
  # Create a TextBlob object
  blob = TextBlob(text)
  
  # Get the polarity score (-1 to 1, where >0 is positive)
  polarity = blob.sentiment.polarity
  
  if polarity > 0:
    return "Positive"
  elif polarity < 0:
    return "Negative"
  else:
    return "Neutral"

#     Example Usage 
print("Sentiment Analyzer")
print("--------------------")

# Example sentences to test your analyzer
sentence1 = "I love this new phone, the camera is amazing!"
sentence2 = "The battery life on this device is terrible, it dies so quickly."
sentence3 = "The phone is made of aluminum."

print(f"'{sentence1}' -> Sentiment: {analyze_sentiment(sentence1)}")
print(f"'{sentence2}' -> Sentiment: {analyze_sentiment(sentence2)}")
print(f"'{sentence3}' -> Sentiment: {analyze_sentiment(sentence3)}")

# Allow the user to test their own sentences
while True:
    user_input = input("\nEnter a sentence to analyze (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    
    sentiment = analyze_sentiment(user_input)
    print(f"Sentiment: {sentiment}")
