from re import findall


def match_indian_or_israel(string):
    """
    matches indian or isralie cellphone numbers
    """
    regex = '(\+91[0-9]{10}|\+972[0-9]{8,9})'
    return findall(regex, string)


def match_indian(string):
    """
    matches indian cellphone numbers
    """
    regex = '\+91[0-9]{10}'
    return findall(regex, string)


if __name__ == "__main__":
    print(match_indian_or_israel('garbage+9119797ann+919818611161asdas'))
    print(match_indian_or_israel('garbage+9119797ann+919818611161asdas+97212312313as'))
