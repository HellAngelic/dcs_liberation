from enum import Enum

from dcs import task
from dcs.planes import PlaneType
from dcs.weapons_data import Weapons

from game.modsupport import planemod
from pydcs_extensions.weapon_injector import inject_weapons

class WeaponsF18F:
    Fuel_Tank_330_gallons = {"clsid": "{VSN_EFT_PTB}", "name": "Fuel Tank 330 gallons", "weight": 1150}
    Fuel_Tank_330_gallons__ = {"clsid": "{VSN_F18F_PTB}", "name": "Fuel Tank 330 gallons", "weight": 1150}
    _NiteHawk_FLIR = {"clsid": "_NiteHawk_FLIR", "name": "AN/AAS-38 \"Nite hawk\" FLIR, Laser designator & Laser spot tracker pod", "weight": 200}
    FPU_8A_Fuel_Tank_330_gallons = {"clsid": "{FPU_8A_FUEL_TANK}", "name": "FPU-8A Fuel Tank 330 gallons", "weight": 1150}
    AGM_86C = {"clsid": "{AGM_86C}", "name": "AGM-86C", "weight": 2050}
    AGM_86D = {"clsid": "{769A15DF-6AFB-439F-9B24-5B7A45C59D16}", "name": "AGM-86D", "weight": 1950}
    _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = {"clsid": "{A76344EB-32D2-4532-8FA2-0C1BDC00747E}", "name": "3 x LAU-61 pods - 57 x 2.75\" Hydra, UnGd Rkts M151, HE", "weight": 876.45}



inject_weapons(WeaponsF18F)


@planemod
class VSN_FA18F(PlaneType):
    id = "VSN_FA18F"
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

    class Liveries:
        class USA(Enum):
            default = "VSN_FA18F"

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

    class Pylon2:
        AIM_9M_Sidewinder_IR_AAM = (2, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (2, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (2, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (2, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (2, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (2, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (2, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (2, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (2, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (2, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)

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
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (3, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (3, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (3, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (3, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        GBU_16___1000lb_Laser_Guided_Bomb = (3, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (3, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (3, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (3, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (3, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_84A_Harpoon_ASM = (3, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (3, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (3, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (3, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (3, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500LG___500kg_Laser_Guided_Bomb = (3, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (3, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (3, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (3, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (3, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        Fuel_Tank_330_gallons = (3, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (3, Weapons.FPU_8A_Fuel_Tank_330_gallons)

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
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (4, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (4, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (4, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (4, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (4, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (4, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        GBU_16___1000lb_Laser_Guided_Bomb = (4, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (4, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (4, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (4, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (4, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_84A_Harpoon_ASM = (4, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (4, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (4, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (4, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (4, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500LG___500kg_Laser_Guided_Bomb = (4, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (4, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (4, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (4, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = (4, Weapons._3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (4, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        Fuel_Tank_330_gallons = (4, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (4, Weapons.FPU_8A_Fuel_Tank_330_gallons)
#ERRR {6C0D552F-570B-42ff-9F6D-F10D9C1D4E1C}

    class Pylon5:
        AIM_120B_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (5, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (5, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        L_081_Fantasmagoria_ELINT_pod = (5, Weapons.L_081_Fantasmagoria_ELINT_pod)
        L005_Sorbtsiya_ECM_pod__left_ = (5, Weapons.L005_Sorbtsiya_ECM_pod__left_)

    class Pylon6:
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (6, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (6, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (6, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (6, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (6, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        Fuel_Tank_330_gallons = (6, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (6, Weapons.FPU_8A_Fuel_Tank_330_gallons)
        Smokewinder___red = (6, Weapons.Smokewinder___red)
        Smokewinder___green = (6, Weapons.Smokewinder___green)
        Smokewinder___blue = (6, Weapons.Smokewinder___blue)
        Smokewinder___white = (6, Weapons.Smokewinder___white)
        Smokewinder___yellow = (6, Weapons.Smokewinder___yellow)

    class Pylon7:
        AN_ASQ_173_Laser_Spot_Tracker_Strike_CAMera__LST_SCAM_ = (7, Weapons.AN_ASQ_173_Laser_Spot_Tracker_Strike_CAMera__LST_SCAM_)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (7, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (7, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        L_081_Fantasmagoria_ELINT_pod = (7, Weapons.L_081_Fantasmagoria_ELINT_pod)
        L005_Sorbtsiya_ECM_pod__left_ = (7, Weapons.L005_Sorbtsiya_ECM_pod__left_)

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
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (8, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (8, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (8, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (8, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (8, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        GBU_16___1000lb_Laser_Guided_Bomb = (8, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (8, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (8, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (8, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (8, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_84A_Harpoon_ASM = (8, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (8, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (8, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (8, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (8, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500LG___500kg_Laser_Guided_Bomb = (8, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (8, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (8, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (8, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        _3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE = (8, Weapons._3_x_LAU_61_pods___57_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (8, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        Fuel_Tank_330_gallons = (8, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (8, Weapons.FPU_8A_Fuel_Tank_330_gallons)

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
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (9, Weapons.Mk_83___1000lb_GP_Bomb_LD)
        Mk_84___2000lb_GP_Bomb_LD = (9, Weapons.Mk_84___2000lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (9, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD = (9, Weapons.MER2_with_2_x_Mk_82___500lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD = (9, Weapons.MER2_with_2_x_Mk_83___1000lb_GP_Bombs_LD)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (9, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        GBU_16___1000lb_Laser_Guided_Bomb = (9, Weapons.GBU_16___1000lb_Laser_Guided_Bomb)
        GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb = (9, Weapons.GBU_24_Paveway_III___2000lb_Laser_Guided_Bomb)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (9, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (9, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (9, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_84A_Harpoon_ASM = (9, Weapons.AGM_84A_Harpoon_ASM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (9, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        AGM_86D = (9, Weapons.AGM_86D)
        AGM_154C___JSOW_Unitary_BROACH = (9, Weapons.AGM_154C___JSOW_Unitary_BROACH)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (9, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500LG___500kg_Laser_Guided_Bomb = (9, Weapons.KAB_500LG___500kg_Laser_Guided_Bomb)
        KAB_1500L___1500kg_Laser_Guided_Bomb = (9, Weapons.KAB_1500L___1500kg_Laser_Guided_Bomb)
        KAB_500Kr___500kg_TV_Guided_Bomb = (9, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
#ERRR {F0ED00FC-24D6-4CD7-9EA5-DE4BEE69A5EA}
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (9, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (9, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (9, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)
        Fuel_Tank_330_gallons = (9, Weapons.Fuel_Tank_330_gallons)
        FPU_8A_Fuel_Tank_330_gallons = (9, Weapons.FPU_8A_Fuel_Tank_330_gallons)

    class Pylon10:
        AIM_9M_Sidewinder_IR_AAM = (10, Weapons.AIM_9M_Sidewinder_IR_AAM)
        AIM_9P_Sidewinder_IR_AAM = (10, Weapons.AIM_9P_Sidewinder_IR_AAM)
        AIM_9X_Sidewinder_IR_AAM = (10, Weapons.AIM_9X_Sidewinder_IR_AAM)
        AIM_120B_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120B_AMRAAM___Active_Rdr_AAM)
        AIM_120C_5_AMRAAM___Active_Rdr_AAM = (10, Weapons.AIM_120C_5_AMRAAM___Active_Rdr_AAM)
        AIM_7M_Sparrow_Semi_Active_Radar = (10, Weapons.AIM_7M_Sparrow_Semi_Active_Radar)
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (10, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_ = (10, Weapons.LAU_117_with_AGM_65K___Maverick_K__CCD_Imp_ASM_)
        LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_ = (10, Weapons.LAU_117_with_AGM_65D___Maverick_D__IIR_ASM_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (10, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_ = (10, Weapons.AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_)
        KAB_500Kr___500kg_TV_Guided_Bomb = (10, Weapons.KAB_500Kr___500kg_TV_Guided_Bomb)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (10, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE = (10, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M151__HE)
        LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos = (10, Weapons.LAU_61_pod___19_x_2_75_Hydra__UnGd_Rkts_M156__Wht_Phos)

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

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

    tasks = [task.CAP, task.Escort, task.FighterSweep, task.Intercept, task.Reconnaissance, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.FighterSweep
