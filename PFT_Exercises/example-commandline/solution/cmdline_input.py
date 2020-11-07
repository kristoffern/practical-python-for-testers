import argparse


def flag_callback(option, opt_str, value, parser):
    print('flag_callback:')
    print('\topt_str:', opt_str)
    print('\tvalue:', value)


def with_callback(option, opt_str, value, parser):
    print('with_callback:')
    print('\topt_str:', opt_str)
    print('\tvalue:', value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", "--noarg", action="store_true", default=False)
    parser.add_argument("-w", "--withargs", action="store",
                        help="Sets the variable withargs to the value provided", dest="withargs")
    parser.add_argument("--withargs2", action="store",
                        help='Sets the variable withargs2 to the integer value provided, otherwise 3 by default', default=3, type=int)
    parser.add_argument("-c", "--choice", help='Select a valid value: "First, Second, Third"',
                        choices=['First', 'Second', 'Third'])
    parser.add_argument('--flag', callback=flag_callback)
    parser.add_argument('--with',
                        action="callback",
                        callback=with_callback,
                        type="string",
                        help="Include optional feature")

    options, args = parser.parse_args()

    print(options.noarg)
    print(options.withargs)
    print(options.choice)
