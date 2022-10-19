from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons

@planemod
class VSN_F35A(PlaneType):
    id = "VSN_F35A"
    flyable = True
    height = 5.63
    width = 13.1
    length = 19.43
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 120
    flare = 120
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:
        class USA(enum):
            default = "VSN_F35A"

    class Pylon1:
        AIM_9M_Sidewinder_IR_AAM = (1, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (1, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (1, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    class Pylon2:
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        GBU_10___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (2, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (2, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (2, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (2, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        CBU_97___10_x_SFW_Cluster_Bomb = (2, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (2, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (2, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile)
        GBU_12___500lb_Laser_Guided_Bomb = (2, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (2, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (2, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (2, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        CBU_103___202_x_CEM__CBU_with_WCMD = (2, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (2, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        AGM_114K = (2, Weapons.AGM_114K)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (2, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        Fuel_tank_610_gal_ = (2, Weapons.Fuel_tank_610_gal_)

    class Pylon3:
        AIM_9M_Sidewinder_IR_AAM = (3, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (3, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (3, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        GBU_10___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (3, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (3, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        CBU_97___10_x_SFW_Cluster_Bomb = (3, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (3, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile)
        GBU_12___500lb_Laser_Guided_Bomb = (3, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (3, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (3, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        CBU_103___202_x_CEM__CBU_with_WCMD = (3, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (3, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        AGM_114K = (3, Weapons.AGM_114K)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (3, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)

    class Pylon4:
        AIM_9M_Sidewinder_IR_AAM = (4, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (4, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (4, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        GBU_12___500lb_Laser_Guided_Bomb = (4, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (4, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (4, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        CBU_103___202_x_CEM__CBU_with_WCMD = (4, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (4, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        AGM_114K = (4, Weapons.AGM_114K)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (4, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)

    class Pylon5:
        AIM_9M_Sidewinder_IR_AAM = (5, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (5, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)

    class Pylon6:
        Smokewinder___red = (6, Weapons.Smokewinder___red)
        Smokewinder___green = (6, Weapons.Smokewinder___green)
        Smokewinder___blue = (6, Weapons.Smokewinder___blue)
        Smokewinder___white = (6, Weapons.Smokewinder___white)
        Smokewinder___yellow = (6, Weapons.Smokewinder___yellow)
        L_081_Fantasmagoria_ELINT_pod = (6, Weapons.L_081_Fantasmagoria_ELINT_pod)

    class Pylon7:
        AIM_9M_Sidewinder_IR_AAM = (7, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (7, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)

    class Pylon8:
        AIM_9M_Sidewinder_IR_AAM = (8, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (8, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (8, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        GBU_12___500lb_Laser_Guided_Bomb = (8, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (8, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (8, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        CBU_103___202_x_CEM__CBU_with_WCMD = (8, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (8, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        AGM_114K = (8, Weapons.AGM_114K)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (8, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)

    class Pylon9:
        AIM_9M_Sidewinder_IR_AAM = (9, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (9, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (9, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        GBU_10___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (9, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (9, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_83___1000lb_GP_Bomb_LD = (9, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (9, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        CBU_97___10_x_SFW_Cluster_Bomb = (9, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (9, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (9, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_AGM_65G = (9, Weapons.LAU_117_AGM_65G)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile = (9, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile)
        GBU_12___500lb_Laser_Guided_Bomb = (9, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (9, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (9, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (9, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        CBU_103___202_x_CEM__CBU_with_WCMD = (9, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (9, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        AGM_114K = (9, Weapons.AGM_114K)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (9, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)

    class Pylon10:
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        GBU_10___2000lb_Laser_Guided_Bomb = (10, Weapons.GBU_10___2000lb_Laser_Guided_Bomb)
        GBU_16___1000lb_Laser_Guided_Bomb = (10, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (10, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (10, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_83___1000lb_GP_Bomb_LD = (10, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (10, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        Mk_84___2000lb_GP_Bomb_LD = (10, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        CBU_97___10_x_SFW_Cluster_Bomb = (10, Weapons.CBU_97___10_x_SFW_Cluster_Bomb)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (10, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (10, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (10, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_AGM_65G = (10, Weapons.LAU_117_AGM_65G)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile = (10, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile)
        GBU_12___500lb_Laser_Guided_Bomb = (10, Weapons.GBU_12___500lb_Laser_Guided_Bomb)
        GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb = (10, Weapons.GBU_31_V_1_B___JDAM__2000lb_GPS_Guided_Bomb)
        GBU_38___JDAM__500lb_GPS_Guided_Bomb = (10, Weapons.GBU_38___JDAM__500lb_GPS_Guided_Bomb)
        AGM_154C___JSOW_Unitary_BROACH = (10, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        CBU_103___202_x_CEM__CBU_with_WCMD = (10, Weapons.CBU_103___202_x_CEM__CBU_with_WCMD)
        CBU_105___10_x_SFW__CBU_with_WCMD = (10, Weapons.CBU_105___10_x_SFW__CBU_with_WCMD)
        AGM_114K = (10, Weapons.AGM_114K)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (10, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        Fuel_tank_610_gal_ = (10, Weapons.Fuel_tank_610_gal_)

    class Pylon11:
        AIM_9M_Sidewinder_IR_AAM = (11, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (11, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (11, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        Smokewinder___red = (11, Weapons.Smokewinder___red)
        Smokewinder___green = (11, Weapons.Smokewinder___green)
        Smokewinder___blue = (11, Weapons.Smokewinder___blue)
        Smokewinder___white = (11, Weapons.Smokewinder___white)
        Smokewinder___yellow = (11, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (11, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack]
    task_default = task.CAS
