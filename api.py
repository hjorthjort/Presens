from flask import jsonify
from twitter_trends import twitter
import weather
from alchemy import alchemy
from map_id_to_program import mapping
from handle_recommendations import recommendations


# Dummy data
programme_ids = ['2eda62d0-6d84-4552-802e-23dc569d9233', 'e69f9468-eef5-492f-8ea3-5fbe83ffcc97']

lists = [
    {
        'title': u'Classical Sunday',
        'items': [
            {
                'title':u'Gone With the Wind',
                'synopsis':u'Scarlett is a woman who can deal with a nation at war, Atlanta burning, the Union Army carrying off everything from her beloved Tara, the carpetbaggers who arrive after the war. Scarlett is beautiful. She has vitality. But Ashley, the man she has wanted for so long, is going to marry his placid cousin, Melanie. Mammy warns Scarlett to behave herself at the party at Twelve Oaks. There is a new man there that day, the day the Civil War begins. Rhett Butler. Scarlett does not know he is in the room when she pleads with Ashley to choose her instead of Melanie.',
                'imgurl':u'http://ia.media-imdb.com/images/M/MV5BNDUwMjAxNTU1MF5BMl5BanBnXkFtZTgwMzg4NzMxMDE@._V1_SX214_AL_.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=h2oX0zQA67U',
                'genre':u'classic,drama'
            },
            {
                'title':u'The Wizard of Oz',
                'synopsis':u'Dorothy lives on a farm in Kansas until a cyclone arrives, and picks her, her house, and her dog up and deposits them in the land of Oz. Things in Oz are strange and beautiful, but Dorothy just wants to get back home. She\'s helped by the Good Witch of the North, but she\'s also in trouble with the Wicked Witch of the West, who seeks revenge for the death of her sister; the Wicked Witch of the East, for which she blames Dorothy.',
                'imgurl':u'http://ia.media-imdb.com/images/M/MV5BMTU0MTA2OTIwNF5BMl5BanBnXkFtZTcwMzA0Njk3OA@@._V1_SY317_CR10,0,214,317_AL_.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=njdreZRjvpc',
                'genre':u'classic,musical'
            },
            #Pure dummy:
            {
                'title':u'World in White',
                'synopsis':u'Surrounded by dark forces who suppress and ridicule him, the Hero slowly blossoms into a mature figure who ultimately gets riches, a kingdom, and the perfect mate.',
                'imgurl':u'http://uploads.neatorama.com/images/posts/95/58/58095/1360112719-0.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=a2MnKebNlRo',
                'genre':u'classic,thriller'
            },
            {
                'title':u'World in White',
                'synopsis':u'Surrounded by dark forces who suppress and ridicule him, the Hero slowly blossoms into a mature figure who ultimately gets riches, a kingdom, and the perfect mate.',
                'imgurl':u'http://uploads.neatorama.com/images/posts/95/58/58095/1360112719-0.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=a2MnKebNlRo',
                'genre':u'classic,thriller'
            },
            {
                'title':u'World in White',
                'synopsis':u'Surrounded by dark forces who suppress and ridicule him, the Hero slowly blossoms into a mature figure who ultimately gets riches, a kingdom, and the perfect mate.',
                'imgurl':u'http://uploads.neatorama.com/images/posts/95/58/58095/1360112719-0.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=a2MnKebNlRo',
                'genre':u'classic,thriller'
            },
            {
                'title':u'World in White',
                'synopsis':u'Surrounded by dark forces who suppress and ridicule him, the Hero slowly blossoms into a mature figure who ultimately gets riches, a kingdom, and the perfect mate.',
                'imgurl':u'http://uploads.neatorama.com/images/posts/95/58/58095/1360112719-0.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=a2MnKebNlRo',
                'genre':u'classic,thriller'
            },
            {
                'title':u'World in White',
                'synopsis':u'Surrounded by dark forces who suppress and ridicule him, the Hero slowly blossoms into a mature figure who ultimately gets riches, a kingdom, and the perfect mate.',
                'imgurl':u'http://uploads.neatorama.com/images/posts/95/58/58095/1360112719-0.jpg',
                'trailerurl':u'https://www.youtube.com/watch?v=a2MnKebNlRo',
                'genre':u'classic,thriller'
            }
        ]
    },
]

meta = {
    'location': u'London, UK',
    'weather': weather.getWeather(2882, 'London'),
    'trends': twitter().get_trends()
}

def get_lists(recommendation):
    datapoint = np.array([1,1,1])
    list_of_rec = recommendation.get_recommendations(datapoint)
    return jsonify({'lists': mapping.programs_to_data(list_of_rec, recommendation.get_meta_data)})

def get_trending_concepts():
    twObject = twitter()
    alcObject = alchemy()
    concepts = []
    for trend in twObject.get_trends():
        tweets = twObject.get_tweets(trend)
        concept = alcObject.find_keywords(". ".join(tweets))
        concepts.append(concept)
    return jsonify({'trend-concepts': concepts})


def metadata():
    return jsonify({'metadata': meta})


def index():
    return "Hi!"
