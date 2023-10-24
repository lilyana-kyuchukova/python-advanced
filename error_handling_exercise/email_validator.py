
class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class MustContainDotError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


VALID_DOMAINS = ["org", "net", "bg", "com"]

while True:
    user_input = input()
    if user_input == "End":
        break

    if "@" not in user_input:
        raise MustContainAtSymbolError("Email must contain @")

    if user_input.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email must contain only one @ symbol")

    if "." not in user_input:
        raise MustContainDotError("Email address must contain a dot")

    index_at = user_input.index("@")
    index_dot = user_input.index(".")

    if len(user_input[:index_at]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if user_input[index_dot + 1:] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
