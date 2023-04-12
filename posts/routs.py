# from posts.__init__ import posts
from posts.controller import create,get
from . import posts

posts.add_url_rule('/','get',get,methods=['GET'])
posts.add_url_rule('/create','create',create,methods=['POST'])
