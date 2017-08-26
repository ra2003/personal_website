from jinja2 import Environment, FileSystemLoader

with open('css.txt') as f:
    css_file_path = f.read()
css_file_path = '/' + '/'.join(css_file_path.split('/')[1:])
template = Environment(loader=FileSystemLoader('personal_website/pages/')).get_template('about.html')


def result(static_files):
    return template.render(
        css_file_path=css_file_path,
        page_title='About',
        nav_button='about',
    )


if __name__ == '__main__':
    print(result)
