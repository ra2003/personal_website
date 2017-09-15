# coding=utf-8
from jinja2 import Environment, FileSystemLoader

from personal_website.combine_static import get_css_file

template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('resume.html')


def stars(number=5):
    full_star = '<i class="fa fa-star" aria-hidden="true"></i>'
    half_star = '<i class="fa fa-star-half" aria-hidden="true"></i>'
    resultant_string = '(' + str(number) + ') ' + ''.join([full_star for _ in range(int(number))])
    resultant_string += half_star if (number - int(number)) > 0 else ''
    return resultant_string


def result(static_files, css_file):
    return template.render(
        css_file_path=css_file,
        page_title='Résumé',
        nav_button='resume',
        stars=stars,
    )


if __name__ == '__main__':
    print(result)
