def payments(bill,ppl):
    """
        This is the function for determining how much
        each person pays

        Args:   bill = the total bill
                ppl = the number of people

        Returns: The individual Payment per person
        
    """
    try:
        return round((bill/ppl),2)
    except:
        print "An Error Occured with the payments calculation"


def tip(bill,perc,ppl):
    """
        This is the function for determinging the tip.
        It also splits the tip over a group of ppl

        Args:   bill = the total bill
                perc = the percentage of the tip to give
                ppl = the number of people

        Returns: The individual Payment per person
    
    """
    try:
        return round(((bill * (perc/100.00))/ppl),2)
    except:
        print "An Error Occured with the tip calculation"
    


def main():
    """ This is the main function """
    print "How much is the bill ?"
    while True:
        try:
            total_bill = float(raw_input(">> $"))
            break
        except:
            print ""
            print "Must be a number value"
            print ""
    print ""

    print "How many people ?"
    while True:
        try:
            num_ppl = int(raw_input(">>"))
            break
        except:
            print ""
            print "Must be a number value"
            print ""
    print ""

    print "What Percentage of Tip ?"
    while True:
        try:
            perc = int(raw_input(">> %"))
            break
        except:
            print ""
            print "Must be a number value"
            print ""

    print ""
    print "Calculating Payment..."

    bill_payment = payments(total_bill,num_ppl)
    tip_payment = tip(total_bill,perc,num_ppl)
    total_payment = float(bill_payment)+float(tip_payment)
    
    print 'Each Person pays $%s for the bill' % \
          str(bill_payment)
    print 'Each Person pays $%s for the tip' % \
          str(tip_payment)
    print 'Which means each person will pay a total of $%s' % \
          str(total_payment)


if __name__ == '__main__':
    main()
