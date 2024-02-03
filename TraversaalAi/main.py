API_KEY = 'ares_074164b222759dc553b2a6985a4490762409e5b600c3a44d023d9199404923b3'
data = '''
Title: "Harmony in Havenwood"

In the quaint town of Havenwood, nestled between rolling hills and surrounded by dense forests, a diverse group of characters lived harmoniously. Each had their own unique story, and their lives intertwined in unexpected ways.

Eleanor was a kind and wise librarian who had spent decades curating the town's vast collection of books. Her small library became a haven for book lovers and curious minds. One day, she discovered an ancient tome filled with forgotten secrets that would soon impact the whole town.

Oliver lived on the outskirts of Havenwood, tinkering with gadgets and gizmos in his quirky workshop. Despite his eccentricities, the townsfolk admired him for his brilliant inventions. Little did they know that one of Oliver's contraptions would play a pivotal role in an unforeseen event.

Sophie, a mysterious artist, painted vivid scenes of the forest and its mystical creatures. Her paintings seemed to come to life, captivating everyone who beheld them. Sophie harbored a secret connection to the magical beings that inhabited the woods, and her art held the key to maintaining the balance between two worlds.

Dr. Henry dedicated his life to healing the residents of Havenwood. His warm bedside manner and genuine concern for others made him a beloved figure in the town. When a mysterious illness struck Havenwood, Henry faced his greatest challenge, and the fate of the community rested on his shoulders.

Mabel ran the local bakery, where the tantalizing aroma of freshly baked goods wafted through the air. Her delicious treats brought joy to Havenwood, and her bakery served as the heart of the town. Unbeknownst to Mabel, her secret recipe held the power to bring unity to the community in times of crisis.

As the seasons changed, an ancient prophecy hinted at an impending challenge that would test the resilience of Havenwood. The wise librarian, eccentric inventor, enigmatic artist, compassionate doctor, and spirited baker found themselves drawn together by destiny.

Facing adversity, the characters discovered the strength that lay within their unique qualities. Eleanor's wisdom, Oliver's inventions, Sophie's mystical connection, Henry's compassion, and Mabel's secret recipe combined to create a force that would safeguard Havenwood from the impending threat.

Through their collective efforts, the town not only weathered the storm but emerged stronger and more united than ever. The characters' individual stories became interwoven, creating a tapestry of resilience, friendship, and the enduring spirit of Havenwood.
'''


import requests

url = "https://api-ares.traversaal.ai/d/predict"

payload = { "query": ["What could be improved in the story?"],
            "data": [data]
           }
headers = {
  "x-api-key": API_KEY,
  "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
