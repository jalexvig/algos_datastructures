import argparse


def setup_new_algo(name):

    with open('{}.py'.format(name), 'w') as f, open('template.txt') as g:
        f.write(g.read().format(name))

    with open('README.md', 'a') as f:
        f.write('* Add link for {}'.format(name))


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('name', help='Name of algorithm to intialize.')

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()
    setup_new_algo(args.name)