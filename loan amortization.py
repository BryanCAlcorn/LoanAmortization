#P = Loan Principal
#J = Monthly Interest Rate (Annual Rate / 1200)
#N = Number of Months (Years * 12)
#M = Monthly Payment
#V = Value of House
#eightyPercent = 80% of the value of the home
#H = Monthly Interest Payment
#C = Monthly Principal Payment
#Q = New Principal Balance
#PMIPmt = PMI Payment
#T = Monthly Tax
P = 351000;
J = 0.003125;
N = 360;
M = 1647;
V = 370000;
eightyPercent = V * .78;
Q = P;
i = 0;
PMIPmt = 350;
PMIHit = False;
TotalInt = 0;
TotalPMI = 0;
T = 352;

while(Q > 0):
    H = P*J;
    TotalInt += H;
    C = M-H;
    Q = P-C;
    P = Q;
    i += 1;
    print("Month: " + str(i));
    print("Interest Pmt: " + str(H));
    print("Principal Pmt: " + str(C));
    print("Balance: " + str(Q));
    if(Q < eightyPercent and not PMIHit):
            print("****************PMI Ends*****************");
            print("Years of PMI: " + str(i/12));
            TotalPMI = PMIPmt * i;
            print("Total PMI Payments: " + str(TotalPMI));
            print("****************PMI Ends*****************");
            PMIHit = True;
print("*********Loan Ends*********");
print("Years: " + str(i / 12));
print("Total Interest Paid: " + str(TotalInt));
print("Total PMI: " + str(TotalPMI));
TotalTax = T * i;
print("Total Tax: " + str(TotalTax));
TotalPaid = V + TotalInt + TotalPMI + TotalTax;
print("Total Paid: " + str(TotalPaid));
print("Interest to Value Ratio: " + str(TotalInt / V));
print("Value to Total Paid Ratio: " + str(V / TotalPaid));
