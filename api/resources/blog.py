# coding=utf-8
from flask_restful import Resource


data_json = [
            {
            'id': '2017-03-11-test-blog',
            'title': 'Test Blog',
            'author': 'Author',
            'post_date': '2017-03-11',
            'content': """ Far far away, behind the word mountains, far from the countries Vokalia and
                                    Consonantia, there live the blind texts. Separated they live in Bookmarksgrove
                                    right at the coast of the Semantics, a large language ocean. A small river named
                                    Duden flows by their place and supplies it with the necessary regelialia. It is a
                                    paradisematic country, in which roasted parts of sentences fly into your mouth. Even the
                                    all-powerful Pointing has no control about the blind texts it is an almost unorthographic
                                    life One day however a small line of blind text by the name of Lorem Ipsum decided
                                    to leave for the far World of Grammar. The Big Oxmox advised her not to do so,
                                    because there were thousands of bad Commas, wild Question Marks and devious Semikoli,
                                    but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial
                                    into the belt and made herself on the way. When she reached
                                    the first hills of the Italic Mountains, she had a last view back on the skyline of
                                    her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her
                                    own road, the Line Lane
                                    """
        },
            {
            'id': '2017-03-11-test-blog-2',
            'title': 'Test Blog 2',
            'author': 'Author',
            'post_date': '2017-03-11',
            'content': """The European languages are members of the same family. Their separate existence is a myth.
                          For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in
                          their grammar, their pronunciation and their most common words. Everyone realizes why a new
                          common language would be desirable: one could refuse to pay expensive translators.
                          To achieve this, it would be necessary to have uniform grammar, pronunciation and more
                          common words. If several languages coalesce, the grammar of the resulting language is more
                          simple and regular than that of the individual languages. The new common language will be more
                          simple and regular than the existing European languages. It will be as simple as Occidental;
                          in fact, it will be Occidental. To an English person, it will seem like simplified English,
                          as a skeptical Cambridge friend of mine told me what Occidental is. The European languages
                          are members of the same family. Their separate existence is a myth. For science, music,
                          sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar,
                          their pronunci
                          """
        },

        ]


class BlogList(Resource):

    def get(self):
        """
        Get list of latest blog
        :return:
        """
        posts = data_json

        return posts


class BlogDetail(Resource):

    def get(self, blog_title):
        """
        Get blog detailed by title
        :return:
        """
        posts = {}
        for post in data_json:
            if blog_title.replace(' ', '-').lower() == post['id']:
                posts = post
        return posts
