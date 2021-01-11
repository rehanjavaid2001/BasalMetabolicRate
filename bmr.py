# Rehan Javaid rj3dxu
"""
The purpose of this program is to create a function that provides the Mifflin St Jeor estimate of the
basal metabolic rate given mass, height, age and gender.

"""

def st_jeor (A, B, C, D):
    """
    This function uses four variables (A, B, C, and D) to estimate the basal metabolic rate

    Parameters:
        float(A) = the input for the mass of the person (in kg.)
        float(B) = The persons height (in cm.)
        int(C) = the age of the individual
        str (D) = the gender of the individual ("male" or "female")
    """
    mass = float(A)
    height = float(B)
    age = int(C)
    gender = str(D)
    if gender == "male":
        return(10*mass + 6.25*height - 5*age + 5)
    elif gender == "female":
        return (10*mass + 6.25*height - 5*age - 161)
    else:
        return "error"

