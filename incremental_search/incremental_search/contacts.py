JOHN = "first_name_john"

JOHNSON = "last_name_johnson"
THOMPSON = "last_name_thompson"

JOHN_JOHNSON = "contact_john_johnson"
JOHN_THOMPSON = "contact_john_thompson"

CONTACTS = {
    JOHN_JOHNSON: {
        "first_name": JOHN,
        "last_name": JOHNSON,
    },
    JOHN_THOMPSON: {
        "first_name": JOHN,
        "last_name": THOMPSON,
    },
}


PHONE_NUMBERS = {
    JOHN_JOHNSON: "0702446698",
    JOHN_THOMPSON: "0705444211",
}


FIRST_NAMES_ENGLISH = {"John": JOHN}
FIRST_NAMES_FRENCH =  {"Jean": JOHN}
FIRST_NAMES_DUTCH =   {"Jan": JOHN}

FIRST_NAMES = {
    "eng": FIRST_NAMES_ENGLISH,
    "fre": FIRST_NAMES_FRENCH,
    "dut": FIRST_NAMES_DUTCH,
}


LAST_NAMES_ENGLISH = {
    "Johnson": JOHNSON,
    "Thompson": THOMPSON,
}

LAST_NAMES_FRENCH = {
    "Juneau": JOHNSON,
    "Thomas": THOMPSON,
}

LAST_NAMES_DUTCH = {
    "Janssen": JOHNSON,
    "Thomassen": THOMPSON,
}

LAST_NAMES = {
    "eng": LAST_NAMES_ENGLISH,
    "fre": LAST_NAMES_FRENCH,
    "dut": LAST_NAMES_DUTCH,
}