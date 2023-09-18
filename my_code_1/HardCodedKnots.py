from pyknotid.catalogue import get_knot
import pyknotid.representations as rep_

class HardCodedKnots:

    code_numbers = [31, 311, 3111, 312, 3113, 41, 411, 4112, 412, 51, 513, 5131, 52, 522, 61, 62, 63,
                    71, 72, 73, 74, 75, 76, 77] #31123


    def __init__(self, code_no = None, code_string = None):
        
        if code_no == 31 or code_string == "trefoil" or code_string == "3_1":
            k = get_knot('3_1').space_curve()
            self.code_gauss = k.gauss_code()
            return
        if code_no == 311 or code_string == "trefoil_twist" or code_string == "3_1_1":
            self.code_gauss = rep_.GaussCode('1+c,2-c,3+c,1-c,2+c,4+c,4-c,3-c')
            return

        if code_no == 3111 or code_string == "trefoil_twist_twist" or code_string == "3_1_1_1":
            self.code_gauss = rep_.GaussCode("1+c,2-c,3+c,4-a,5+a,5-a,4+a,1-c,2+c,3-c")
            return

        if code_no == 312 or code_string == "trefoil_poke" or code_string == "3_1_2":
            self.code_gauss = rep_.GaussCode("0-c,1+c,3-c,4-a,2-c,0+c,4+a,3+c,1-c,2+c")
            return

        if (code_no == 3113 or code_string == "trefoil_twist_slide" 
                or code_string == "3_1_1_3"):
            self.code_gauss = rep_.GaussCode("1+c,2-c,3+c,4+c,5+a,6-a,7-c,3-c,8-a,5-a,6+a,1-c,2+c,7+c,4-c,8+a")
            return

        # problem with reducing reidemeister moves 
        # if (code_no == 31123 or code_string == "trefoil_twist_poke_slide" 
        #         or code_string == "3_1_1_2_3"):
        #         self.code_gauss = rep_.GaussCode("1+c,2-c,3-c,6a,7-a,8-c,6+a,9+c,2+c,0+c,0-c,4-c,5-a,1-c,8+c,7+a,9-c,3+c,4+c,5+a")
        #         return

        if code_no == 41 or code_string == "figure_eight" or code_string == "4_1":
            k = get_knot('4_1').space_curve()
            self.code_gauss = k.gauss_code()
        
        if code_no == 411 or code_string == "figure_eight_twist" or code_string == "4_1_1":
            self.code_gauss = rep_.GaussCode("1+a,2-a,3+a,4-c,2+a,1-a,5+a,5-a,4+c,3-c")
            return
        
        if code_no == 4112 or code_string == "figure_eight_twist_poke" or code_string == "4_1_1_2":
            self.code_gauss = rep_.GaussCode("1+a,2-a,3+c,4-c,2+a,1-a,5+a,6+c,7+a,5-a,6-c,7-a,4+c,3-c")
            return
            
        if code_no == 412 or code_string == "figure_eight_poke" or code_string == "4_1_2":
            self.code_gauss = rep_.GaussCode("1-c,2-a,3+c,4-c,2+a,5-a,6+a,1+c,4+c,3-c,5+a,6-a")
            return

        if code_no == 51 or code_string == "star" or code_string == "5_1":
            k = get_knot("5_1").space_curve()
            self.code_gauss = k.gauss_code()
            return
        
        if code_no == 513 or code_string == "star_slide" or code_string == "5_1_3":
            self.code_gauss = rep_.GaussCode("1+c,2+c,3-c,4+c,5-c,6+c,7+a,1-c,8+c,3+c,2-c,8-c,9-a,7-a,4-c,5+c,6-c,9+a")
            return

        if code_no == 5131 or code_string == "star_slide_twist" or code_string == "5_1_3_1":
            self.code_gauss = rep_.GaussCode("1+c,2+c,3-c,4+c,5-c,6+c,7+a,1-c,8+c,3+c,2-c,8-c,0+c,0-c,9-a,7-a,4-c,5+c,6-c,9+a")
            return

        if code_no == 52 or code_string == "5_2":
            k = get_knot("5_2").space_curve()
            self.code_gauss = k.gauss_code()
            return
        
        if code_no == 522 or code_string == "5_2_2":
            self.code_gauss = rep_.GaussCode("1+c,2+a,3+c,4-c,5+c,6-c,7+c,1-c,4+c,3-c,2-a,7-c,6+c,5-c")
            # "1-c,2+c,3-c,4+c,5-c,6-a,7-c,1+c,6+a,5+c,4-c,3+c,2-c,7+c"
            return

        if code_no == 61 or code_string == "6_1":
            k = get_knot("6_1").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 62 or code_string == "6_2":
            k = get_knot("6_2").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 63 or code_string == "6_3":
            k = get_knot("6_3").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 71 or code_string == "7_1":
            k = get_knot("7_1").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 72 or code_string == "7_2":
            k = get_knot("7_2").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 73 or code_string == "7_3":
            k = get_knot("7_3").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 74 or code_string == "7_4":
            k = get_knot("7_4").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 75 or code_string == "7_5":
            self.code_gauss = rep_.GaussCode("1+a,2-a,3+a,4-a,5+a,6-a,7+a,5-a,4+a,1-a,2+a,3-a,6+a,7-a")
            return

        if code_no == 76 or code_string == "7_6":
            k = get_knot("7_6").space_curve()
            self.code_gauss = k.gauss_code()
            return

        if code_no == 77 or code_string == "7_7":
            k = get_knot("7_7").space_curve()
            self.code_gauss = k.gauss_code()
            return

    def get_code_gauss(self):
        return self.code_gauss