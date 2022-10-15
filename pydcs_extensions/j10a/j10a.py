from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons

@planemod
class J_10A(PlaneType):
    id = "J-10A"
    flyable = True
    height = 5.9
    width = 14.7
    length = 17.3
    fuel_max = 9400
    max_speed = 2500.92
    chaff = 2500
    flare = 2500
    charge_total = 5000
    chaff_charge_size = 1
    flare_charge_size = 1
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    livery_name = "J-10A"  # from type
    Liveries = Liveries()[livery_name]

    class Pylon1:
        DIS_PL_8A = (1, Weapons.DIS_PL_8A)
        DIS_PL_8B = (1, Weapons.DIS_PL_8B)
#ERRR {PLAAF_PL-10E}
#ERRR {1500 litre tank}

    class Pylon2:
        DIS_SD_10 = (2, Weapons.DIS_SD_10)
        DIS_PL_12 = (2, Weapons.DIS_PL_12)
        DIS_SD_10_DUAL_R = (2, Weapons.DIS_SD_10_DUAL_R)
#ERRR {96A7F676-F956-404A-AD04-F33FB2C74885}
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (2, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (2, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (2, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (2, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (2, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (2, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (2, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (2, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (2, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (2, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (2, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (2, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (2, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (2, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (2, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (2, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
#ERRR {youxiang}

    class Pylon3:
        DIS_SD_10 = (3, Weapons.DIS_SD_10)
        DIS_PL_12 = (3, Weapons.DIS_PL_12)
        J_10A_SIDE_TANK = (3, Weapons.J_10A_SIDE_TANK)
#ERRR {96A7F676-F956-404A-AD04-F33FB2C74885}
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (3, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (3, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (3, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (3, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (3, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (3, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (3, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (3, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (3, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (3, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (3, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (3, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (3, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (3, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)
#ERRR {fenhong}
#ERRR {juhuang}
#ERRR {zise}
#ERRR {huanglvse}
#ERRR {hongyan}
#ERRR {baiyan}
#ERRR {lanyan}
#ERRR {huangyan}

    class Pylon4:
        J_10A_CENTER_TANK = (4, Weapons.J_10A_CENTER_TANK)

    class Pylon5:
        DIS_SD_10 = (5, Weapons.DIS_SD_10)
        DIS_PL_12 = (5, Weapons.DIS_PL_12)
        J_10A_SIDE_TANK = (5, Weapons.J_10A_SIDE_TANK)
#ERRR {96A7F676-F956-404A-AD04-F33FB2C74885}
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (5, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (5, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (5, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (5, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (5, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (5, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (5, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (5, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (5, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (5, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (5, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (5, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (5, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (5, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (5, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (5, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)

    class Pylon6:
        DIS_SD_10 = (6, Weapons.DIS_SD_10)
        DIS_PL_12 = (6, Weapons.DIS_PL_12)
        DIS_SD_10_DUAL_L = (6, Weapons.DIS_SD_10_DUAL_L)
#ERRR {1500 litre tank}
#ERRR {96A7F676-F956-404A-AD04-F33FB2C74885}
        BetAB_500___500kg_Concrete_Piercing_Bomb_LD = (6, Weapons.BetAB_500___500kg_Concrete_Piercing_Bomb_LD)
        BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb = (6, Weapons.BetAB_500ShP___500kg_Concrete_Piercing_HD_w_booster_Bomb)
        FAB_250___250kg_GP_Bomb_LD = (6, Weapons.FAB_250___250kg_GP_Bomb_LD)
        FAB_500_M_62___500kg_GP_Bomb_LD = (6, Weapons.FAB_500_M_62___500kg_GP_Bomb_LD)
        RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP = (6, Weapons.RBK_250___42_x_PTAB_2_5M__250kg_CBU_Medium_HEAT_AP)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk = (6, Weapons.B_8M1_pod___20_x_S_8TsM__80mm_UnGd_Rkts__Smk)
        B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag = (6, Weapons.B_13L_pod___5_x_S_13_OF__122mm_UnGd_Rkts__Blast_Frag)
        B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP = (6, Weapons.B_8M1_pod___20_x_S_8KOM__80mm_UnGd_Rkts__HEAT_AP)
        MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_ = (6, Weapons.MBD2_67U_with_4_x_FAB_100___100kg_GP_Bombs_LD_)
        KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag = (6, Weapons.KMGU_2___96_x_AO_2_5RT_Dispenser__CBU__HE_Frag)
        KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP = (6, Weapons.KMGU_2___96_x_PTAB_2_5KO_Dispenser__CBU__HEAT_AP)
        S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator = (6, Weapons.S_25_OFM___340mm_UnGd_Rkt__480kg_Penetrator)
        S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__ = (6, Weapons.S_24B___240mm_UnGd_Rkt__235kg__HE_Frag___Low_Smk__)
        UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag = (6, Weapons.UB_32A_pod___32_x_S_5KO__57mm_UnGd_Rkts__HEAT_Frag)

    class Pylon7:
        DIS_PL_8A = (7, Weapons.DIS_PL_8A)
        DIS_PL_8B = (7, Weapons.DIS_PL_8B)
#ERRR {PLAAF_PL-10E}

    pylons: Set[int] = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.FighterSweep
