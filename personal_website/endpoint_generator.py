import os
from glob import glob

from constants import BLOG_PATH, IMAGE_PATH
from personal_website.blog_path import split_path, trim_left_path
from personal_website.flask_app import app


def freeze_endpoints(freezer):
    @freezer.register_generator
    def fonts():
        path = os.path.join(app.root_path, 'static/fonts') + '/'
        fonts_ = next(os.walk(path))[2]
        for font in fonts_:
            yield {'path': font}

    @freezer.register_generator
    def blog_post():
        files = next(os.walk(BLOG_PATH))[2]
        blog_posts = [file for file in files if file.endswith('.html')]
        for post in blog_posts:
            path = split_path('', '', post)[0]
            yield {
                'year': path[0],
                'month': path[1],
                'day': path[2],
                'name': path[3][:-5],
            }

    @freezer.register_generator
    def images():
        image_dir_ = glob(IMAGE_PATH + '*')
        for image_dir in image_dir_:
            files = next(os.walk(image_dir))[2]
            for image_file in files:
                yield {'path': trim_left_path(image_dir + '/' + image_file, IMAGE_PATH)}