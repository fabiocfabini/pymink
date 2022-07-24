import re

class Clean:
    """
    This class is used to clean the input text.
    Diferent cleaning processes could be implemented.

    Cleaning process:

        Process 1:
            - Remove all non-alphanumeric characters
            - Remove all digits
            - Turn all characters to upper case

            Exceptions:
                - the '-' character will only be removed if it starts or ends a word
                - the ''' (apostrophe) character will only be removed if it stars or ends a word

            Examples:
                1- "gato," -> "GATO"
                2- "comprar-lhe" -> "COMPRAR-LHE"
                3- "togetheer" -> "TOGETHEER"
                4- "older'" -> "OLDER"
                4- "it?" -> "IT"
    """

    def __init__(self) -> None:
        pass

    def clean(self, text: str) -> str:
        pass