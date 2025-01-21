def main():
    print('')

    # Import cmind to test break points
    import cmind.utils
    import os
    if os.environ.get('CM_TMP_DEBUG_UID', '') == 'f52670e5f3f345a2':
        cmind.utils.debug_here(
            __file__,
            port=5678,
            text='Debugging main.py!').breakpoint()

    print('HELLO WORLD from Python')

    x = 1
    print(x)


if __name__ == '__main__':
    main()
