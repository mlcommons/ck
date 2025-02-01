#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import subprocess
import select
import sys
import grp


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if os.geteuid() == 0:
        env['CM_SUDO'] = ''  # root user does not need sudo
        env['CM_SUDO_USER'] = "yes"
    else:
        if can_execute_sudo_without_password() or prompt_sudo() == 0:
            env['CM_SUDO_USER'] = "yes"
            env['CM_SUDO'] = 'sudo'

        else:
            env['CM_SUDO_USER'] = "no"
            env['CM_SUDO'] = ''

    return {'return': 0}


def can_execute_sudo_without_password():
    try:
        # Run a harmless command using sudo
        result = subprocess.run(
            # -n prevents sudo from prompting for a password
            ['sudo', '-n', 'true'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Check the return code; if it's 0, sudo executed without needing a
        # password
        if result.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def reset_terminal():
    """Reset terminal to default settings."""
    subprocess.run(['stty', 'sane'])


def prompt_retry(timeout=10, default_retry=False):
    """Prompt the user with a yes/no question to retry the command, with a 10-second timeout."""

    # Check if we're in an interactive terminal
    if not sys.stdin.isatty():
        if default_retry:
            print(f"Non-interactive environment detected. Automatically retrying.")
        else:
            print(f"Non-interactive environment detected. Skipping retry.")
        return default_retry  # Automatically use the default in non-interactive terminals

    print(
        f"Timeout occurred. Do you want to try again? (y/n): ",
        end='',
        flush=True)

    # Use select to wait for user input with a timeout
    ready, _, _ = select.select([sys.stdin], [], [], timeout)

    if ready:
        answer = sys.stdin.readline().strip().lower()
        if answer in ['y', 'n']:
            return answer == 'y'  # Return True if 'y', False if 'n'
        print("\nInvalid input. Please enter 'y' or 'n'.")
        return prompt_retry(timeout)  # Re-prompt on invalid input
    else:
        print("\nNo input received in 10 seconds. Exiting.")
        return False  # No input within the timeout, so don't retry


def is_user_in_sudo_group():
    """Check if the current user is in the 'sudo' group."""
    try:
        sudo_group = grp.getgrnam('sudo').gr_mem
        return os.getlogin() in sudo_group
    except KeyError:
        # 'sudo' group doesn't exist (might be different on some systems)
        return False
    except Exception as e:
        print(f"Error checking sudo group: {str(e)}")
        return False


def prompt_sudo():
    if os.geteuid() != 0 and not is_user_in_sudo_group():  # No sudo required for root user

        # Prompt for the password
        import getpass

        if not os.isatty(sys.stdin.fileno()):
            print("Skipping password prompt - non-interactive terminal detected!")
            password = None
        else:
            password = getpass.getpass("Enter password (-1 to skip): ")

        # Check if the input is -1
        if password == "-1":
            print("Skipping sudo command.")
            return -1

        # Run the command with sudo, passing the password
        try:
            if password is None:
                r = subprocess.check_output(
                    ['sudo', '-S', 'echo'],
                    text=True,
                    stderr=subprocess.STDOUT,
                    timeout=15      # Capture the command output
                )
            else:
                r = subprocess.check_output(
                    ['sudo', '-S', 'echo'],
                    input=password + "\n",  # Pass the password to stdin
                    text=True,
                    stderr=subprocess.STDOUT,
                    timeout=15      # Capture the command output
                )
            return 0
        except subprocess.TimeoutExpired:
            print("Timedout")
            reset_terminal()  # Reset terminal to sane state
            if not prompt_retry():  # If the user chooses not to retry or times out
                return -1
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {e.output.decode('utf-8')}")
            reset_terminal()  # Reset terminal in case of failure
            return -1
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            reset_terminal()  # Always reset terminal after error
            return -1

    return 0


def postprocess(i):

    env = i['env']

    return {'return': 0}
