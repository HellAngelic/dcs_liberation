from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons

class WeaponsJ10A:

    J_10A_CENTER_TANK = {"clsid": "{J-10A CENTER TANK}", "name": "J-10A CENTER TANK", "weight": 802}
    J_10A_SIDE_TANK = {"clsid": "{J-10A SIDE TANK}", "name": "J-10A SIDE TANK", "weight": 641.6}
    DIS_AKD_10 = {"clsid": "DIS_AKD-10", "name": "AKD-10", "weight": 58}
    DIS_AKG_DLPOD = {"clsid": "DIS_AKG_DLPOD", "name": "DATA-LINK POD", "weight": 295}
    DIS_BOMB_250_2 = {"clsid": "DIS_BOMB_250_2", "name": "250-2 - 250kg GP Bombs HD", "weight": 250}
    DIS_BOMB_250_3 = {"clsid": "DIS_BOMB_250_3", "name": "250-3 - 250kg GP Bombs LD", "weight": 250}
    DIS_BRM1_90 = {"clsid": "DIS_BRM1_90", "name": "BRM-1_90MM", "weight": 462.5}
    DIS_CM_802AKG = {"clsid": "DIS_CM-802AKG", "name": "CM802AKG", "weight": 765}
    DIS_CM_802AKG_AI = {"clsid": "DIS_CM-802AKG_AI", "name": "CM-802AKG (AI Only)", "weight": 765}
    DIS_C_701IR = {"clsid": "DIS_C-701IR", "name": "C-701IR", "weight": 170}
    DIS_C_701T = {"clsid": "DIS_C-701T", "name": "C-701T", "weight": 170}
    DIS_C_802AK = {"clsid": "DIS_C-802AK", "name": "C802AK", "weight": 765}
    DIS_DF4A_KD20 = {"clsid": "DIS_DF4A_KD20", "name": "KD-20", "weight": 1750}
    DIS_DF4B_YJ12 = {"clsid": "DIS_DF4B_YJ12", "name": "YJ-12", "weight": 1800}
    DIS_GB6 = {"clsid": "DIS_GB6", "name": "GB-6", "weight": 672}
    DIS_GB6_HE = {"clsid": "DIS_GB6_HE", "name": "GB-6-HE", "weight": 672}
    DIS_GB6_TSP = {"clsid": "DIS_GB6_TSP", "name": "GB-6-SFW", "weight": 672}
    DIS_GBU_10 = {"clsid": "DIS_GBU_10", "name": "GBU-10", "weight": 1162}
    DIS_GBU_12 = {"clsid": "DIS_GBU_12", "name": "GBU-12", "weight": 275}
    DIS_GBU_12_DUAL_GDJ_II19_L = {"clsid": "DIS_GBU_12_DUAL_GDJ_II19_L", "name": "GDJ-II19 - 2 x GBU-12", "weight": 629}
    DIS_GBU_12_DUAL_GDJ_II19_R = {"clsid": "DIS_GBU_12_DUAL_GDJ_II19_R", "name": "GDJ-II19 - 2 x GBU-12", "weight": 629}
    DIS_GBU_16 = {"clsid": "DIS_GBU_16", "name": "GBU-16", "weight": 564}
    DIS_GDJ_KD63 = {"clsid": "DIS_GDJ_KD63", "name": "KD-63", "weight": 2050}
    DIS_GDJ_KD63B = {"clsid": "DIS_GDJ_KD63B", "name": "KD-63B", "weight": 2050}
    DIS_GDJ_YJ83K = {"clsid": "DIS_GDJ_YJ83K", "name": "YJ-83K", "weight": 765}
    DIS_H6_250_2_N12 = {"clsid": "DIS_H6_250_2_N12", "name": "12 x 250-2 - 250kg GP Bombs HD", "weight": 3000}
    DIS_H6_250_2_N24 = {"clsid": "DIS_H6_250_2_N24", "name": "24 x 250-2 - 250kg GP Bombs HD", "weight": 6000}
    DIS_KD20 = {"clsid": "DIS_KD20", "name": "KD-20", "weight": 1700}
    DIS_KD63 = {"clsid": "DIS_KD63", "name": "KD-63", "weight": 2000}
    DIS_KD63B = {"clsid": "DIS_KD63B", "name": "KD-63B", "weight": 2000}
    DIS_LAU68_MK5_DUAL_GDJ_II19_L = {"clsid": "DIS_LAU68_MK5_DUAL_GDJ_II19_L", "name": "GDJ-II19 - 2 x LAU68 MK5", "weight": 261.06}
    DIS_LAU68_MK5_DUAL_GDJ_II19_R = {"clsid": "DIS_LAU68_MK5_DUAL_GDJ_II19_R", "name": "GDJ-II19 - 2 x LAU68 MK5", "weight": 261.06}
    DIS_LD_10 = {"clsid": "DIS_LD-10", "name": "LD-10", "weight": 289}
    DIS_LD_10_DUAL_L = {"clsid": "DIS_LD-10_DUAL_L", "name": "LD-10 x 2", "weight": 558}
    DIS_LD_10_DUAL_R = {"clsid": "DIS_LD-10_DUAL_R", "name": "LD-10 x 2", "weight": 558}
    DIS_LS_6_100 = {"clsid": "DIS_LS_6_100", "name": "LS-6-100", "weight": 133}
    DIS_LS_6_100_DUAL_L = {"clsid": "DIS_LS_6_100_DUAL_L", "name": "LS-6-100 Dual", "weight": 221}
    DIS_LS_6_100_DUAL_R = {"clsid": "DIS_LS_6_100_DUAL_R", "name": "LS-6-100 Dual", "weight": 221}
    DIS_LS_6_250 = {"clsid": "DIS_LS_6_250", "name": "LS-6-250", "weight": 320}
    DIS_LS_6_250_DUAL_L = {"clsid": "DIS_LS_6_250_DUAL_L", "name": "LS-6-250 Dual", "weight": 595}
    DIS_LS_6_250_DUAL_R = {"clsid": "DIS_LS_6_250_DUAL_R", "name": "LS-6-250 Dual", "weight": 595}
    DIS_LS_6_500 = {"clsid": "DIS_LS_6_500", "name": "LS-6-500", "weight": 570}
    DIS_MER6_250_2_N6 = {"clsid": "DIS_MER6_250_2_N6", "name": "MER6 - 6 x 250-2 - 250kg GP Bombs HD", "weight": 1550}
    DIS_MER6_250_3_N6 = {"clsid": "DIS_MER6_250_3_N6", "name": "MER6 - 6 x 250-3 - 250kg GP Bombs LD", "weight": 1550}
    DIS_MK_20 = {"clsid": "DIS_MK_20", "name": "Mk-20", "weight": 222}
    DIS_MK_20_DUAL_GDJ_II19_L = {"clsid": "DIS_MK_20_DUAL_GDJ_II19_L", "name": "GDJ-II19 - 2 x Mk-20", "weight": 523}
    DIS_MK_20_DUAL_GDJ_II19_R = {"clsid": "DIS_MK_20_DUAL_GDJ_II19_R", "name": "GDJ-II19 - 2 x Mk-20", "weight": 523}
    DIS_MK_82S_DUAL_GDJ_II19_L = {"clsid": "DIS_MK_82S_DUAL_GDJ_II19_L", "name": "GDJ-II19 - 2 x Mk-82 SnakeEye", "weight": 543}
    DIS_MK_82S_DUAL_GDJ_II19_R = {"clsid": "DIS_MK_82S_DUAL_GDJ_II19_R", "name": "GDJ-II19 - 2 x Mk-82 SnakeEye", "weight": 543}
    DIS_MK_82_DUAL_GDJ_II19_L = {"clsid": "DIS_MK_82_DUAL_GDJ_II19_L", "name": "GDJ-II19 - 2 x Mk-82", "weight": 561}
    DIS_MK_82_DUAL_GDJ_II19_R = {"clsid": "DIS_MK_82_DUAL_GDJ_II19_R", "name": "GDJ-II19 - 2 x Mk-82", "weight": 561}
    DIS_mk46torp = {"clsid": "DIS_mk46torp", "name": "MK46 Torpedo", "weight": 231}
    DIS_PL_12 = {"clsid": "DIS_PL-12", "name": "PL-12", "weight": 199}
    DIS_PL_5EII = {"clsid": "DIS_PL-5EII", "name": "PL-5EII", "weight": 153}
    DIS_PL_8A = {"clsid": "DIS_PL-8A", "name": "PL-8A", "weight": 115}
    DIS_PL_8B = {"clsid": "DIS_PL-8B", "name": "PL-8B", "weight": 115}
    DIS_RKT_90_UG = {"clsid": "DIS_RKT_90_UG", "name": "UG_90MM", "weight": 462.5}
    DIS_SD_10 = {"clsid": "DIS_SD-10", "name": "SD-10", "weight": 289}
    DIS_SD_10_DUAL_L = {"clsid": "DIS_SD-10_DUAL_L", "name": "SD-10 x 2", "weight": 558}
    DIS_SD_10_DUAL_R = {"clsid": "DIS_SD-10_DUAL_R", "name": "SD-10 x 2", "weight": 558}
    DIS_SMOKE_GENERATOR_B = {"clsid": "DIS_SMOKE_GENERATOR_B", "name": "Smoke Generator - blue", "weight": 0}
    DIS_SMOKE_GENERATOR_G = {"clsid": "DIS_SMOKE_GENERATOR_G", "name": "Smoke Generator - green", "weight": 0}
    DIS_SMOKE_GENERATOR_O = {"clsid": "DIS_SMOKE_GENERATOR_O", "name": "Smoke Generator - orange", "weight": 0}
    DIS_SMOKE_GENERATOR_R = {"clsid": "DIS_SMOKE_GENERATOR_R", "name": "Smoke Generator - red", "weight": 0}
    DIS_SMOKE_GENERATOR_W = {"clsid": "DIS_SMOKE_GENERATOR_W", "name": "Smoke Generator - white", "weight": 0}
    DIS_SMOKE_GENERATOR_Y = {"clsid": "DIS_SMOKE_GENERATOR_Y", "name": "Smoke Generator - yellow", "weight": 0}
    DIS_SPJ_POD = {"clsid": "DIS_SPJ_POD", "name": "KG-600", "weight": 270}
    DIS_TANK1100 = {"clsid": "DIS_TANK1100", "name": "1100L Tank", "weight": 1064}
    DIS_TANK1100_EMPTY = {"clsid": "DIS_TANK1100_EMPTY", "name": "1100L Tank Empty", "weight": 75}
    DIS_TANK800 = {"clsid": "DIS_TANK800", "name": "800L Tank", "weight": 730}
    DIS_TANK800_EMPTY = {"clsid": "DIS_TANK800_EMPTY", "name": "800L Tank Empty", "weight": 45}
    DIS_TYPE200 = {"clsid": "DIS_TYPE200", "name": "TYPE-200A", "weight": 200}
    DIS_TYPE200_DUAL_L = {"clsid": "DIS_TYPE200_DUAL_L", "name": "TYPE-200A Dual", "weight": 400}
    DIS_TYPE200_DUAL_R = {"clsid": "DIS_TYPE200_DUAL_R", "name": "TYPE-200A Dual", "weight": 400}
    DIS_WMD7 = {"clsid": "DIS_WMD7", "name": "WMD7 POD", "weight": 295}
    DIS_YJ12 = {"clsid": "DIS_YJ12", "name": "YJ-12", "weight": 1750}
    DIS_YJ83K = {"clsid": "DIS_YJ83K", "name": "YJ-83K", "weight": 715}
    DIS_YU_6 = {"clsid": "DIS_YU_6", "name": "YU-6", "weight": 1558}



inject_weapons(WeaponsJ10A)

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

    class Liveries:
        class China(Enum):
            default = "J_10A"

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

    pylons = {1, 2, 3, 4, 5, 6, 7}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.FighterSweep
