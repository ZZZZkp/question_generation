import nltk
from pipelines import pipeline

nltk.download('punkt')
nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl", ans_model="valhalla/t5-base-qa-qg-hl", use_cuda=True)
str= "Forrest Gump is a 1994 American comedy-drama film directed by Robert Zemeckis and written by Eric Roth. \
It is based on the 1986 novel of the same name by Winston Groom and stars Tom Hanks, Robin Wright, Gary Sinise, \
Mykelti Williamson and Sally Field. The story depicts several decades in the life of Forrest Gump (Hanks), \
a slow-witted but kind-hearted man from Alabama who witnesses and unwittingly influences several defining \
historical events in the 20th century United States. The film differs substantially from the novel."
result = nlp(str)
print(result)