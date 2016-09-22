from django.db import models

class Providerinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    distance = models.TextField(db_column = 'distance', blank=True, null = True)
    provnum = models.TextField(blank=True, null=True)
    provname = models.TextField(db_column='PROVNAME', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase.
    county_ssa = models.TextField(db_column='COUNTY_SSA', blank=True, null=True)  # Field name made lowercase.
    county_name = models.TextField(db_column='COUNTY_NAME', blank=True, null=True)  # Field name made lowercase.
    ownership = models.TextField(db_column='OWNERSHIP', blank=True, null=True)  # Field name made lowercase.
    bedcert = models.TextField(db_column='BEDCERT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restot = models.TextField(db_column='RESTOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    certification = models.TextField(db_column='CERTIFICATION', blank=True, null=True)  # Field name made lowercase.
    inhosp = models.TextField(db_column='INHOSP', blank=True, null=True)  # Field name made lowercase.
    lbn = models.TextField(db_column='LBN', blank=True, null=True)  # Field name made lowercase.
    participation_date = models.TextField(db_column='PARTICIPATION_DATE', blank=True, null=True)  # Field name made lowercase.
    ccrc_facil = models.TextField(db_column='CCRC_FACIL', blank=True, null=True)  # Field name made lowercase.
    sff = models.TextField(db_column='SFF', blank=True, null=True)  # Field name made lowercase.
    oldsurvey = models.TextField(db_column='OLDSURVEY', blank=True, null=True)  # Field name made lowercase.
    chow_last_12mos = models.TextField(db_column='CHOW_LAST_12MOS', blank=True, null=True)  # Field name made lowercase.
    resfamcouncil = models.TextField(db_column='RESFAMCOUNCIL', blank=True, null=True)  # Field name made lowercase.
    sprinkler_status = models.TextField(db_column='SPRINKLER_STATUS', blank=True, null=True)  # Field name made lowercase.
    overall_rating = models.TextField(blank=True, null=True)
    overall_rating_fn = models.TextField(blank=True, null=True)
    survey_rating = models.TextField(blank=True, null=True)
    survey_rating_fn = models.TextField(blank=True, null=True)
    quality_rating = models.TextField(blank=True, null=True)
    quality_rating_fn = models.TextField(blank=True, null=True)
    staffing_rating = models.TextField(blank=True, null=True)
    staffing_rating_fn = models.TextField(blank=True, null=True)
    rn_staffing_rating = models.TextField(db_column='RN_staffing_rating', blank=True, null=True)  # Field name made lowercase.
    rn_staffing_rating_fn = models.TextField(blank=True, null=True)
    staffing_flag = models.TextField(db_column='STAFFING_FLAG', blank=True, null=True)  # Field name made lowercase.
    pt_staffing_flag = models.TextField(db_column='PT_STAFFING_FLAG', blank=True, null=True)  # Field name made lowercase.
    aidhrd = models.TextField(db_column='AIDHRD', blank=True, null=True)  # Field name made lowercase.
    vochrd = models.TextField(db_column='VOCHRD', blank=True, null=True)  # Field name made lowercase.
    rnhrd = models.TextField(db_column='RNHRD', blank=True, null=True)  # Field name made lowercase.
    totlichrd = models.TextField(db_column='TOTLICHRD', blank=True, null=True)  # Field name made lowercase.
    tothrd = models.TextField(db_column='TOTHRD', blank=True, null=True)  # Field name made lowercase.
    pthrd = models.TextField(db_column='PTHRD', blank=True, null=True)  # Field name made lowercase.
    exp_aide = models.TextField(blank=True, null=True)
    exp_lpn = models.TextField(blank=True, null=True)
    exp_rn = models.TextField(blank=True, null=True)
    exp_total = models.TextField(blank=True, null=True)
    adj_aide = models.TextField(blank=True, null=True)
    adj_lpn = models.TextField(blank=True, null=True)
    adj_rn = models.TextField(blank=True, null=True)
    adj_total = models.TextField(blank=True, null=True)
    cycle_1_defs = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_1_nfromdefs = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_1_nfromcomp = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_1_defs_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_1_survey_date = models.TextField(db_column='CYCLE_1_SURVEY_DATE', blank=True, null=True)  # Field name made lowercase.
    cycle_1_numrevis = models.TextField(db_column='CYCLE_1_NUMREVIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_1_revisit_score = models.TextField(db_column='CYCLE_1_REVISIT_SCORE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_1_total_score = models.TextField(db_column='CYCLE_1_TOTAL_SCORE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_2_defs = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_2_nfromdefs = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_2_nfromcomp = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_2_defs_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_2_survey_date = models.TextField(db_column='CYCLE_2_SURVEY_DATE', blank=True, null=True)  # Field name made lowercase.
    cycle_2_numrevis = models.TextField(db_column='CYCLE_2_NUMREVIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_2_revisit_score = models.TextField(db_column='CYCLE_2_REVISIT_SCORE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_2_total_score = models.TextField(db_column='CYCLE_2_TOTAL_SCORE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_3_defs = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_3_nfromdefs = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_3_nfromcomp = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_3_defs_score = models.TextField(blank=True, null=True)  # This field type is a guess.
    cycle_3_survey_date = models.TextField(db_column='CYCLE_3_SURVEY_DATE', blank=True, null=True)  # Field name made lowercase.
    cycle_3_numrevis = models.TextField(db_column='CYCLE_3_NUMREVIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_3_revisit_score = models.TextField(db_column='CYCLE_3_REVISIT_SCORE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cycle_3_total_score = models.TextField(db_column='CYCLE_3_TOTAL_SCORE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weighted_all_cycles_score = models.TextField(db_column='WEIGHTED_ALL_CYCLES_SCORE', blank=True, null=True)  # Field name made lowercase.
    incident_cnt = models.TextField(blank=True, null=True)  # This field type is a guess.
    cmplnt_cnt = models.TextField(blank=True, null=True)  # This field type is a guess.
    fine_cnt = models.TextField(db_column='FINE_CNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fine_tot = models.TextField(db_column='FINE_TOT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    payden_cnt = models.TextField(db_column='PAYDEN_CNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tot_penlty_cnt = models.TextField(db_column='TOT_PENLTY_CNT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    filedate = models.TextField(db_column='FILEDATE', blank=True, null=True)  # Field name made lowercase.
    defstat = models.TextField(db_column='DEFSTAT', blank=True, null=True)  # Field name made lowercase.
    defpref = models.TextField(db_column='DEFPREF', blank=True, null=True)  # Field name made lowercase.
    statdate = models.TextField(db_column='STATDATE', blank=True, null=True)  # Field name made lowercase.
    surveytype = models.TextField(db_column='SURVEYTYPE', blank=True, null=True)  # Field name made lowercase.
    complaint = models.TextField(db_column='COMPLAINT', blank=True, null=True)  # Field name made lowercase.
    scope = models.TextField(db_column='SCOPE', blank=True, null=True)  # Field name made lowercase.
    cycle = models.TextField(db_column='CYCLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tag = models.TextField(db_column='TAG', blank=True, null=True)  # Field name made lowercase.
    survey_date_output = models.TextField(db_column='SURVEY_DATE_OUTPUT', blank=True, null=True)  # Field name made lowercase.
    standard = models.TextField(db_column='STANDARD', blank=True, null=True)  # Field name made lowercase.
    tag_desc = models.TextField(db_column='TAG_DESC', blank=True, null=True)  # Field name made lowercase.
    role_desc = models.TextField(db_column='ROLE_DESC', blank=True, null=True)  # Field name made lowercase.
    owner_percentage = models.TextField(db_column='OWNER_PERCENTAGE', blank=True, null=True)  # Field name made lowercase.
    owner_type = models.TextField(db_column='OWNER_TYPE', blank=True, null=True)  # Field name made lowercase.
    association_date = models.TextField(db_column='ASSOCIATION_DATE', blank=True, null=True)  # Field name made lowercase.
    owner_name = models.TextField(db_column='OWNER_NAME', blank=True, null=True)  # Field name made lowercase.
    payden_days = models.TextField(db_column='PAYDEN_DAYS', blank=True, null=True)  # Field name made lowercase.
    payden_strt_dt = models.TextField(db_column='PAYDEN_STRT_DT', blank=True, null=True)  # Field name made lowercase.
    fine_amt = models.TextField(db_column='FINE_AMT', blank=True, null=True)  # Field name made lowercase.
    pnlty_date = models.TextField(db_column='PNLTY_DATE', blank=True, null=True)  # Field name made lowercase.
    pnlty_type = models.TextField(db_column='PNLTY_TYPE', blank=True, null=True)  # Field name made lowercase.
    qm415 = models.TextField(db_column='QM415', blank=True, null=True)  # Field name made lowercase.
    qm407 = models.TextField(db_column='QM407', blank=True, null=True)  # Field name made lowercase.
    qm434 = models.TextField(db_column='QM434', blank=True, null=True)  # Field name made lowercase.
    c3_hlth_defs_cnt = models.TextField(db_column='C3_HLTH_DEFS_CNT', blank=True, null=True)  # Field name made lowercase.
    qm406 = models.TextField(db_column='QM406', blank=True, null=True)  # Field name made lowercase.
    qm426 = models.TextField(db_column='QM426', blank=True, null=True)  # Field name made lowercase.
    qm424 = models.TextField(db_column='QM424', blank=True, null=True)  # Field name made lowercase.
    qm402 = models.TextField(db_column='QM402', blank=True, null=True)  # Field name made lowercase.
    qm404 = models.TextField(db_column='QM404', blank=True, null=True)  # Field name made lowercase.
    qm409 = models.TextField(db_column='QM409', blank=True, null=True)  # Field name made lowercase.
    c2_fs_defs_cnt = models.TextField(db_column='C2_FS_DEFS_CNT', blank=True, null=True)  # Field name made lowercase.
    qm405 = models.TextField(db_column='QM405', blank=True, null=True)  # Field name made lowercase.
    c1_fs_defs_cnt = models.TextField(db_column='C1_FS_DEFS_CNT', blank=True, null=True)  # Field name made lowercase.
    qm430 = models.TextField(db_column='QM430', blank=True, null=True)  # Field name made lowercase.
    c1_hlth_defs_cnt = models.TextField(db_column='C1_HLTH_DEFS_CNT', blank=True, null=True)  # Field name made lowercase.
    qm410 = models.TextField(db_column='QM410', blank=True, null=True)  # Field name made lowercase.
    qm425 = models.TextField(db_column='QM425', blank=True, null=True)  # Field name made lowercase.
    qm419 = models.TextField(db_column='QM419', blank=True, null=True)  # Field name made lowercase.
    qm408 = models.TextField(db_column='QM408', blank=True, null=True)  # Field name made lowercase.
    qm403 = models.TextField(db_column='QM403', blank=True, null=True)  # Field name made lowercase.
    c3_fs_defs_cnt = models.TextField(db_column='C3_FS_DEFS_CNT', blank=True, null=True)  # Field name made lowercase.
    c2_hlth_defs_cnt = models.TextField(db_column='C2_HLTH_DEFS_CNT', blank=True, null=True)  # Field name made lowercase.
    qm401 = models.TextField(db_column='QM401', blank=True, null=True)  # Field name made lowercase.
    qm411 = models.TextField(db_column='QM411', blank=True, null=True)  # Field name made lowercase.
    h_mistreat_n = models.TextField(db_column='H_MISTREAT_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_medical_gas_n = models.TextField(db_column='F_MEDICAL_GAS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_miscellaneous_n = models.TextField(db_column='F_MISCELLANEOUS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_survey_date = models.TextField(db_column='H_SURVEY_DATE', blank=True, null=True)  # Field name made lowercase.
    f_ij_n = models.TextField(db_column='F_IJ_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_ij_n = models.TextField(db_column='H_IJ_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_smoking_reg_n = models.TextField(db_column='F_SMOKING_REG_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_emergency_plan_n = models.TextField(db_column='F_EMERGENCY_PLAN_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_smoke_control_n = models.TextField(db_column='F_SMOKE_CONTROL_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_interior_n = models.TextField(db_column='F_INTERIOR_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_construction_n = models.TextField(db_column='F_CONSTRUCTION_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_severe_n = models.TextField(db_column='F_SEVERE_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_furnishings_n = models.TextField(db_column='F_FURNISHINGS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_ss_max = models.TextField(db_column='F_SS_MAX', blank=True, null=True)  # Field name made lowercase.
    h_tot_dfcncy = models.TextField(db_column='H_TOT_DFCNCY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_quality_care_n = models.TextField(db_column='H_QUALITY_CARE_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_res_asmnt_n = models.TextField(db_column='H_RES_ASMNT_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_substndrd_qoc_n = models.TextField(db_column='H_SUBSTNDRD_QOC_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_hazard_area_n = models.TextField(db_column='F_HAZARD_AREA_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_illumination_n = models.TextField(db_column='F_ILLUMINATION_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_survey_date = models.TextField(db_column='F_SURVEY_DATE', blank=True, null=True)  # Field name made lowercase.
    f_exit_access_n = models.TextField(db_column='F_EXIT_ACCESS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_sprinkler_n = models.TextField(db_column='F_SPRINKLER_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_electrical_n = models.TextField(db_column='F_ELECTRICAL_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_tot_dfcncy = models.TextField(db_column='F_TOT_DFCNCY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_fire_alarm_n = models.TextField(db_column='F_FIRE_ALARM_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_corridor_doors_n = models.TextField(db_column='F_CORRIDOR_DOORS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_severe_n = models.TextField(db_column='H_SEVERE_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_exit_egress_n = models.TextField(db_column='F_EXIT_EGRESS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_vert_openings_n = models.TextField(db_column='F_VERT_OPENINGS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    f_service_equipment_n = models.TextField(db_column='F_SERVICE_EQUIPMENT_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_res_rights_n = models.TextField(db_column='H_RES_RIGHTS_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_ss_max = models.TextField(db_column='H_SS_MAX', blank=True, null=True)  # Field name made lowercase.
    f_laboratories_n = models.TextField(db_column='F_LABORATORIES_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_nutrition_n = models.TextField(db_column='H_NUTRITION_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_environmental_n = models.TextField(db_column='H_ENVIRONMENTAL_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_pharmacy_n = models.TextField(db_column='H_PHARMACY_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    h_administration_n = models.TextField(db_column='H_ADMINISTRATION_N', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qual_msr_num_401 = models.TextField(db_column='QUAL_MSR_NUM_401', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_402 = models.TextField(db_column='QUAL_MSR_NUM_402', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_403 = models.TextField(db_column='QUAL_MSR_NUM_403', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_404 = models.TextField(db_column='QUAL_MSR_NUM_404', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_405 = models.TextField(db_column='QUAL_MSR_NUM_405', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_406 = models.TextField(db_column='QUAL_MSR_NUM_406', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_407 = models.TextField(db_column='QUAL_MSR_NUM_407', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_408 = models.TextField(db_column='QUAL_MSR_NUM_408', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_409 = models.TextField(db_column='QUAL_MSR_NUM_409', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_410 = models.TextField(db_column='QUAL_MSR_NUM_410', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_411 = models.TextField(db_column='QUAL_MSR_NUM_411', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_415 = models.TextField(db_column='QUAL_MSR_NUM_415', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_419 = models.TextField(db_column='QUAL_MSR_NUM_419', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_424 = models.TextField(db_column='QUAL_MSR_NUM_424', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_425 = models.TextField(db_column='QUAL_MSR_NUM_425', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_426 = models.TextField(db_column='QUAL_MSR_NUM_426', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_430 = models.TextField(db_column='QUAL_MSR_NUM_430', blank=True, null=True)  # Field name made lowercase.
    qual_msr_num_434 = models.TextField(db_column='QUAL_MSR_NUM_434', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProviderInfo'
