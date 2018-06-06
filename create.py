import os
import argparse


def setup_new_algo(name):

    os.mkdir(name)

    with open(os.path.join(name, 'README.md'), 'w') as f:
        f.write('# {}'.format(name))

    with open(os.path.join(name, '{}.py'.format(name)), 'w') as f:
        f.write('\n\ndef {}():\n    pass\n'.format(name))


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('name', help='Name of algorithm to intialize.')

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()
    setup_new_algo(args.name)
