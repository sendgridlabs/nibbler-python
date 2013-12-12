import string


class State(object):
    def __init__(self):
        self.in_quotes = False
        self.in_comment = False
        self.previous_dot = False
        self.previous_slash = False
        self.in_domain = False

ATEXT = "!#$%&'*+-/=?^_`.{|}~@\"" + string.ascii_letters + string.digits
SPECIAL = ['(', ')', ',', ':', ';', '<', '>', '[', '\\', ']', ' ']
HOSTNAME = "-." + string.ascii_letters + string.digits


def parse_email(email_str):

    state = State()
    valid = True
    address = ''

    for offset, character in enumerate(email_str):
        # Local part
        if not state.in_domain:
            if character == '\\':
                if state.in_quotes:
                    # Check if slash was backslashed within quotes
                    if state.previous_slash:
                        state.previous_slash = False
                    else:
                        state.previous_slash = True
                # \ can only occur within slashes
                else:
                    valid = False
                    break
            elif character == '"':

                if state.in_quotes:
                    # Ignore if it was preceded by a backslash
                    if not state.previous_slash:
                        state.in_quotes = False
                    else:
                        state.previous_slash = False
                else:
                    # Quotes must happen as the first character or after a dot
                    if offset != 0 and not state.previous_dot:
                        valid = False
                        break
                    state.in_quotes = True

            elif character == '.':
                # We can't have two consecutive dots
                if not state.in_quotes:
                    state.previous_dot = True

            elif character == '@' and not state.in_quotes:
                state.in_domain = True

            # These characters must only occur in quotes
            if character in SPECIAL:
                if not state.in_quotes:
                    valid = False
                    break
                else:
                    address += character
            else:
                if character not in ATEXT:
                    valid = False
                    break
                else:
                    address += character

            # Check states and clear them if necessary
            if state.previous_slash and character != '\\':
                state.previous_slash = False
            if state.previous_dot and character != '.':
                state.previous_dot = False

        # Domain part, we don't allow ip addresses [x.x.x.x] only host names
        else:
            if character not in HOSTNAME:
                valid = False
                break
            address += character

    if not state.in_domain:
        valid = False

    return valid, address
