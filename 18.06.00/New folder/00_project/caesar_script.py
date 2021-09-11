import sys

from caesar_encryption import encrypt


def caesar():
    key = 1
    is_error = False

    for index, arg in enumerate(sys.argv):
        if arg in ['--key', '-k'] and len(sys.argv) > index + 1:
            key = int(sys.argv[index + 1])
            del sys.argv[index]
            del sys.argv[index]
            break

    for index, arg in enumerate(sys.argv):
        if arg in ['--encrypt', '-e']:
            del sys.argv[index]
            break
        if arg in ['--decrypt', '-d']:
            key = -key
            del sys.argv[index]
            break

    if len(sys.argv) == 1:
        is_error = True
    else:
        for arg in sys.argv:
            if arg.startswith('-'):
                is_error = True

    if is_error:
        print(f'Usage: python {sys.argv[0]} [ --key <key> ] [ --encrypt|decrypt ] <text>')
    else:
        print(encrypt(' '.join(sys.argv[1:]), key))

if __name__ == '__main__':
    caesar()




