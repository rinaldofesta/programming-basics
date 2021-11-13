class BillPrinter:
    """
    Helper class, prints to video bills details in a pretty ascii art format
    """

    def __init__(self, bills):
        """
        Takes a bills list in input and prints it in a pretty asci art format

        :param bills: a list containing instances of the Bill class
        """
        self.bills = bills
        self.print_bills(self.bills)

    @staticmethod
    def print_bills(bills):
        """
        Takes a bills list in input and prints it in a pretty asci art format like this:

        +----------+----------+------------------------------+----------+
        | TICKET N | GIOCATA  |        NUMERI GIOCATI        |  RUOTA   |
        +----------+----------+------------------------------+----------+
        | Ticket 1 | Quaterna |         6 17 79 66 3         |   Bari   |
        +----------+----------+------------------------------+----------+
        | Ticket 2 |  Terno   |        83 23 24 71 30        |  Napoli  |
        +----------+----------+------------------------------+----------+

        :param bills: a list containing instances of the Bill class
        """
        table_line = f"+{'-'*10}+{'-'*10}+{'-'*30}+{'-'*10}+"
        table_header = f"|{('TICKET N').center(10, ' ')}|{('GIOCATA').center(10, ' ')}|{('NUMERI GIOCATI').center(30, ' ')}|{('RUOTA').center(10, ' ')}|"

        print(table_line)
        print(table_header)
        print(table_line)
        for bill in bills:
            print(
                f"| Ticket {bill.bill_num + 1} |{(bill.type).center(10, ' ')}|{(' '.join(str(x) for x in bill.numbers)).center(30, ' ')}|{(bill.city).center(10, ' ')}|")
            print(table_line)
