The dataset3.csv file contains the dataset copied from the PHY 252 Parameter
Fitting Exercise google sheet

The visual.py file graphs the dataset to give an idea of the function type
    From the graph I determined it was an exponential function of the form
    \[a*e^(-bx)+c\]

    The dataset3.png file is the output of visual.py

The main.py file runs the actual regression using the odrpack package to
perform an orthogonal distance regression on the dataset
    I found the fitted parameters (a,b,c) to be
    (3.3443921514117605, 0.049998683094403716, 1.5905831034446964)

    The regression.png file is the output of main.py