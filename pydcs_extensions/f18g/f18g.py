from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons

@planemod
class VSN_EA18G(PlaneType):
    id = "VSN_EA18G"
    flyable = True
    height = 4
    width = 13.05
    length = 18
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 30
    flare = 15
    charge_total = 60
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    livery_name = "VSN_EA18G"  # from type
    Liveries = Liveries()[livery_name]

    class Pylon1:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (1, Weapons.AIM_9X_Sidewinder_IR_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        L005_Sorbtsiya_ECM_pod__left_ = (1, Weapons.L005_Sorbtsiya_ECM_pod__left_)

    class Pylon2:
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (2, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (2, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}

    class Pylon3:
        LAU_115_2_LAU_127_AIM_9M = (3, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (3, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (3, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (3, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_2_LAU_127_AIM_120B = (3, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (3, Weapons.LAU_115_2_LAU_127_AIM_120C)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (3, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (3, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (3, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (3, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (3, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        Fuel_Tank_330_gallons = (3, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (3, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        ALQ_99_Function_as_tank = (3, Weapons.ALQ_99_Function_as_tank)

    class Pylon4:
        LAU_115_2_LAU_127_AIM_9M = (4, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (4, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (4, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (4, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_2_LAU_127_AIM_120B = (4, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (4, Weapons.LAU_115_2_LAU_127_AIM_120C)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (4, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (4, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (4, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (4, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (4, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (4, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        Fuel_Tank_330_gallons = (4, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (4, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        ALQ_99_Function_as_tank = (4, Weapons.ALQ_99_Function_as_tank)
#ERRR {6C0D552F-570B-42ff-9F6D-F10D9C1D4E1C}

    class Pylon5:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        L_081_Fantasmagoria_ELINT_pod = (5, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon6:
        Fuel_Tank_330_gallons = (6, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (6, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        ALQ_99_Function_as_tank = (6, Weapons.ALQ_99_Function_as_tank)
        Smokewinder___red = (6, Weapons.Smokewinder___red)
        Smokewinder___green = (6, Weapons.Smokewinder___green)
        Smokewinder___blue = (6, Weapons.Smokewinder___blue)
        Smokewinder___white = (6, Weapons.Smokewinder___white)
        Smokewinder___yellow = (6, Weapons.Smokewinder___yellow)
#ERRR {6C0D552F-570B-42ff-9F6D-F10D9C1D4E1C}

    class Pylon7:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        L_081_Fantasmagoria_ELINT_pod = (7, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon8:
        LAU_115_2_LAU_127_AIM_9M = (8, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (8, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (8, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (8, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_2_LAU_127_AIM_120B = (8, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (8, Weapons.LAU_115_2_LAU_127_AIM_120C)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (8, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (8, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (8, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (8, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (8, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        Fuel_Tank_330_gallons = (8, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (8, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        ALQ_99_Function_as_tank = (8, Weapons.ALQ_99_Function_as_tank)

    class Pylon9:
        LAU_115_2_LAU_127_AIM_9M = (9, Weapons.LAU_115_2_LAU_127_AIM_9M)
        LAU_115_2_LAU_127_CATM_9M = (9, Weapons.LAU_115_2_LAU_127_CATM_9M)
        LAU_115_2_LAU_127_AIM_9L = (9, Weapons.LAU_115_2_LAU_127_AIM_9L)
        LAU_115_2_LAU_127_AIM_9X = (9, Weapons.LAU_115_2_LAU_127_AIM_9X)
        LAU_115_2_LAU_127_AIM_120B = (9, Weapons.LAU_115_2_LAU_127_AIM_120B)
        LAU_115_2_LAU_127_AIM_120C = (9, Weapons.LAU_115_2_LAU_127_AIM_120C)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (9, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        AGM_84A_Harpoon_ASM = (9, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (9, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (9, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (9, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (9, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (9, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        Fuel_Tank_330_gallons = (9, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (9, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        ALQ_99_Function_as_tank = (9, Weapons.ALQ_99_Function_as_tank)

    class Pylon10:
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (10, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (10, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (10, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}

    class Pylon11:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (11, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (11, Weapons.AIM_9X_Sidewinder_IR_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        L005_Sorbtsiya_ECM_pod__right_ = (11, Weapons.L005_Sorbtsiya_ECM_pod__right_)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.FighterSweep
