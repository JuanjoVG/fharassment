# Inspiration
Every day, more and more children suffer from online harassment (wilful and malicious attacks that were intended to cause them fear, intimidation or in fact caused them) and they don't know how to defend themselves against it and its parents do not know they are being harassed. 

So here appears F**k Harassment, a web application that will allow parents or tutors detect online harassment from audio or text.

# How we built it
A frontend built in [Keen.io](https://keen.io/) to have a nice and fancy dashboard that lets you upload audio or WhatsApp chats in order to detect possible harassment. Both are send to a backend Flask application and analysed there to sentence if there's being harassment or not and show the evolution of a converation between two people in terms of sentimental analysis.

- Audios are uploaded and transcripted using [Cloud Speech API](https://cloud.google.com/speech/) from Google. Then, the resultant text is sentimentally analysed using IBM's Watson [Tone Analyzer](https://www.ibm.com/watson/developercloud/tone-analyzer.html) and sent to [TensorFlow (a machine learning Python library)](https://www.tensorflow.org/) previously trained, which decides if harassment is being committed.
- WhatsApp chats are parsed and analysed similarly to the audio transcriptions as long as it has two participants on it and send to TensorFlow library.

# Challenges we ran into
We had never used speech recognition software and having to record ourselves being harassed to have some audio to prove our software it's been hilarious. Thanks, to those that has harassed us throw Slack to train our machine learning algorithm.

# Accomplishments that we're proud of
After a 24 hours programming, we've got it done, so that's the best accomplish we are proud of
