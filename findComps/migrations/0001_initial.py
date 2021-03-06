# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-22 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Providerinfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('distance', models.TextField(blank=True, db_column='distance', null=True)),
                ('provnum', models.TextField(blank=True, null=True)),
                ('provname', models.TextField(blank=True, db_column='PROVNAME', null=True)),
                ('address', models.TextField(blank=True, db_column='ADDRESS', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('state', models.TextField(blank=True, db_column='STATE', null=True)),
                ('zip', models.TextField(blank=True, db_column='ZIP', null=True)),
                ('phone', models.TextField(blank=True, db_column='PHONE', null=True)),
                ('county_ssa', models.TextField(blank=True, db_column='COUNTY_SSA', null=True)),
                ('county_name', models.TextField(blank=True, db_column='COUNTY_NAME', null=True)),
                ('ownership', models.TextField(blank=True, db_column='OWNERSHIP', null=True)),
                ('bedcert', models.TextField(blank=True, db_column='BEDCERT', null=True)),
                ('restot', models.TextField(blank=True, db_column='RESTOT', null=True)),
                ('certification', models.TextField(blank=True, db_column='CERTIFICATION', null=True)),
                ('inhosp', models.TextField(blank=True, db_column='INHOSP', null=True)),
                ('lbn', models.TextField(blank=True, db_column='LBN', null=True)),
                ('participation_date', models.TextField(blank=True, db_column='PARTICIPATION_DATE', null=True)),
                ('ccrc_facil', models.TextField(blank=True, db_column='CCRC_FACIL', null=True)),
                ('sff', models.TextField(blank=True, db_column='SFF', null=True)),
                ('oldsurvey', models.TextField(blank=True, db_column='OLDSURVEY', null=True)),
                ('chow_last_12mos', models.TextField(blank=True, db_column='CHOW_LAST_12MOS', null=True)),
                ('resfamcouncil', models.TextField(blank=True, db_column='RESFAMCOUNCIL', null=True)),
                ('sprinkler_status', models.TextField(blank=True, db_column='SPRINKLER_STATUS', null=True)),
                ('overall_rating', models.TextField(blank=True, null=True)),
                ('overall_rating_fn', models.TextField(blank=True, null=True)),
                ('survey_rating', models.TextField(blank=True, null=True)),
                ('survey_rating_fn', models.TextField(blank=True, null=True)),
                ('quality_rating', models.TextField(blank=True, null=True)),
                ('quality_rating_fn', models.TextField(blank=True, null=True)),
                ('staffing_rating', models.TextField(blank=True, null=True)),
                ('staffing_rating_fn', models.TextField(blank=True, null=True)),
                ('rn_staffing_rating', models.TextField(blank=True, db_column='RN_staffing_rating', null=True)),
                ('rn_staffing_rating_fn', models.TextField(blank=True, null=True)),
                ('staffing_flag', models.TextField(blank=True, db_column='STAFFING_FLAG', null=True)),
                ('pt_staffing_flag', models.TextField(blank=True, db_column='PT_STAFFING_FLAG', null=True)),
                ('aidhrd', models.TextField(blank=True, db_column='AIDHRD', null=True)),
                ('vochrd', models.TextField(blank=True, db_column='VOCHRD', null=True)),
                ('rnhrd', models.TextField(blank=True, db_column='RNHRD', null=True)),
                ('totlichrd', models.TextField(blank=True, db_column='TOTLICHRD', null=True)),
                ('tothrd', models.TextField(blank=True, db_column='TOTHRD', null=True)),
                ('pthrd', models.TextField(blank=True, db_column='PTHRD', null=True)),
                ('exp_aide', models.TextField(blank=True, null=True)),
                ('exp_lpn', models.TextField(blank=True, null=True)),
                ('exp_rn', models.TextField(blank=True, null=True)),
                ('exp_total', models.TextField(blank=True, null=True)),
                ('adj_aide', models.TextField(blank=True, null=True)),
                ('adj_lpn', models.TextField(blank=True, null=True)),
                ('adj_rn', models.TextField(blank=True, null=True)),
                ('adj_total', models.TextField(blank=True, null=True)),
                ('cycle_1_defs', models.TextField(blank=True, null=True)),
                ('cycle_1_nfromdefs', models.TextField(blank=True, null=True)),
                ('cycle_1_nfromcomp', models.TextField(blank=True, null=True)),
                ('cycle_1_defs_score', models.TextField(blank=True, null=True)),
                ('cycle_1_survey_date', models.TextField(blank=True, db_column='CYCLE_1_SURVEY_DATE', null=True)),
                ('cycle_1_numrevis', models.TextField(blank=True, db_column='CYCLE_1_NUMREVIS', null=True)),
                ('cycle_1_revisit_score', models.TextField(blank=True, db_column='CYCLE_1_REVISIT_SCORE', null=True)),
                ('cycle_1_total_score', models.TextField(blank=True, db_column='CYCLE_1_TOTAL_SCORE', null=True)),
                ('cycle_2_defs', models.TextField(blank=True, null=True)),
                ('cycle_2_nfromdefs', models.TextField(blank=True, null=True)),
                ('cycle_2_nfromcomp', models.TextField(blank=True, null=True)),
                ('cycle_2_defs_score', models.TextField(blank=True, null=True)),
                ('cycle_2_survey_date', models.TextField(blank=True, db_column='CYCLE_2_SURVEY_DATE', null=True)),
                ('cycle_2_numrevis', models.TextField(blank=True, db_column='CYCLE_2_NUMREVIS', null=True)),
                ('cycle_2_revisit_score', models.TextField(blank=True, db_column='CYCLE_2_REVISIT_SCORE', null=True)),
                ('cycle_2_total_score', models.TextField(blank=True, db_column='CYCLE_2_TOTAL_SCORE', null=True)),
                ('cycle_3_defs', models.TextField(blank=True, null=True)),
                ('cycle_3_nfromdefs', models.TextField(blank=True, null=True)),
                ('cycle_3_nfromcomp', models.TextField(blank=True, null=True)),
                ('cycle_3_defs_score', models.TextField(blank=True, null=True)),
                ('cycle_3_survey_date', models.TextField(blank=True, db_column='CYCLE_3_SURVEY_DATE', null=True)),
                ('cycle_3_numrevis', models.TextField(blank=True, db_column='CYCLE_3_NUMREVIS', null=True)),
                ('cycle_3_revisit_score', models.TextField(blank=True, db_column='CYCLE_3_REVISIT_SCORE', null=True)),
                ('cycle_3_total_score', models.TextField(blank=True, db_column='CYCLE_3_TOTAL_SCORE', null=True)),
                ('weighted_all_cycles_score', models.TextField(blank=True, db_column='WEIGHTED_ALL_CYCLES_SCORE', null=True)),
                ('incident_cnt', models.TextField(blank=True, null=True)),
                ('cmplnt_cnt', models.TextField(blank=True, null=True)),
                ('fine_cnt', models.TextField(blank=True, db_column='FINE_CNT', null=True)),
                ('fine_tot', models.TextField(blank=True, db_column='FINE_TOT', null=True)),
                ('payden_cnt', models.TextField(blank=True, db_column='PAYDEN_CNT', null=True)),
                ('tot_penlty_cnt', models.TextField(blank=True, db_column='TOT_PENLTY_CNT', null=True)),
                ('filedate', models.TextField(blank=True, db_column='FILEDATE', null=True)),
                ('defstat', models.TextField(blank=True, db_column='DEFSTAT', null=True)),
                ('defpref', models.TextField(blank=True, db_column='DEFPREF', null=True)),
                ('statdate', models.TextField(blank=True, db_column='STATDATE', null=True)),
                ('surveytype', models.TextField(blank=True, db_column='SURVEYTYPE', null=True)),
                ('complaint', models.TextField(blank=True, db_column='COMPLAINT', null=True)),
                ('scope', models.TextField(blank=True, db_column='SCOPE', null=True)),
                ('cycle', models.TextField(blank=True, db_column='CYCLE', null=True)),
                ('tag', models.TextField(blank=True, db_column='TAG', null=True)),
                ('survey_date_output', models.TextField(blank=True, db_column='SURVEY_DATE_OUTPUT', null=True)),
                ('standard', models.TextField(blank=True, db_column='STANDARD', null=True)),
                ('tag_desc', models.TextField(blank=True, db_column='TAG_DESC', null=True)),
                ('role_desc', models.TextField(blank=True, db_column='ROLE_DESC', null=True)),
                ('owner_percentage', models.TextField(blank=True, db_column='OWNER_PERCENTAGE', null=True)),
                ('owner_type', models.TextField(blank=True, db_column='OWNER_TYPE', null=True)),
                ('association_date', models.TextField(blank=True, db_column='ASSOCIATION_DATE', null=True)),
                ('owner_name', models.TextField(blank=True, db_column='OWNER_NAME', null=True)),
                ('payden_days', models.TextField(blank=True, db_column='PAYDEN_DAYS', null=True)),
                ('payden_strt_dt', models.TextField(blank=True, db_column='PAYDEN_STRT_DT', null=True)),
                ('fine_amt', models.TextField(blank=True, db_column='FINE_AMT', null=True)),
                ('pnlty_date', models.TextField(blank=True, db_column='PNLTY_DATE', null=True)),
                ('pnlty_type', models.TextField(blank=True, db_column='PNLTY_TYPE', null=True)),
                ('qm415', models.TextField(blank=True, db_column='QM415', null=True)),
                ('qm407', models.TextField(blank=True, db_column='QM407', null=True)),
                ('qm434', models.TextField(blank=True, db_column='QM434', null=True)),
                ('c3_hlth_defs_cnt', models.TextField(blank=True, db_column='C3_HLTH_DEFS_CNT', null=True)),
                ('qm406', models.TextField(blank=True, db_column='QM406', null=True)),
                ('qm426', models.TextField(blank=True, db_column='QM426', null=True)),
                ('qm424', models.TextField(blank=True, db_column='QM424', null=True)),
                ('qm402', models.TextField(blank=True, db_column='QM402', null=True)),
                ('qm404', models.TextField(blank=True, db_column='QM404', null=True)),
                ('qm409', models.TextField(blank=True, db_column='QM409', null=True)),
                ('c2_fs_defs_cnt', models.TextField(blank=True, db_column='C2_FS_DEFS_CNT', null=True)),
                ('qm405', models.TextField(blank=True, db_column='QM405', null=True)),
                ('c1_fs_defs_cnt', models.TextField(blank=True, db_column='C1_FS_DEFS_CNT', null=True)),
                ('qm430', models.TextField(blank=True, db_column='QM430', null=True)),
                ('c1_hlth_defs_cnt', models.TextField(blank=True, db_column='C1_HLTH_DEFS_CNT', null=True)),
                ('qm410', models.TextField(blank=True, db_column='QM410', null=True)),
                ('qm425', models.TextField(blank=True, db_column='QM425', null=True)),
                ('qm419', models.TextField(blank=True, db_column='QM419', null=True)),
                ('qm408', models.TextField(blank=True, db_column='QM408', null=True)),
                ('qm403', models.TextField(blank=True, db_column='QM403', null=True)),
                ('c3_fs_defs_cnt', models.TextField(blank=True, db_column='C3_FS_DEFS_CNT', null=True)),
                ('c2_hlth_defs_cnt', models.TextField(blank=True, db_column='C2_HLTH_DEFS_CNT', null=True)),
                ('qm401', models.TextField(blank=True, db_column='QM401', null=True)),
                ('qm411', models.TextField(blank=True, db_column='QM411', null=True)),
                ('h_mistreat_n', models.TextField(blank=True, db_column='H_MISTREAT_N', null=True)),
                ('f_medical_gas_n', models.TextField(blank=True, db_column='F_MEDICAL_GAS_N', null=True)),
                ('f_miscellaneous_n', models.TextField(blank=True, db_column='F_MISCELLANEOUS_N', null=True)),
                ('h_survey_date', models.TextField(blank=True, db_column='H_SURVEY_DATE', null=True)),
                ('f_ij_n', models.TextField(blank=True, db_column='F_IJ_N', null=True)),
                ('h_ij_n', models.TextField(blank=True, db_column='H_IJ_N', null=True)),
                ('f_smoking_reg_n', models.TextField(blank=True, db_column='F_SMOKING_REG_N', null=True)),
                ('f_emergency_plan_n', models.TextField(blank=True, db_column='F_EMERGENCY_PLAN_N', null=True)),
                ('f_smoke_control_n', models.TextField(blank=True, db_column='F_SMOKE_CONTROL_N', null=True)),
                ('f_interior_n', models.TextField(blank=True, db_column='F_INTERIOR_N', null=True)),
                ('f_construction_n', models.TextField(blank=True, db_column='F_CONSTRUCTION_N', null=True)),
                ('f_severe_n', models.TextField(blank=True, db_column='F_SEVERE_N', null=True)),
                ('f_furnishings_n', models.TextField(blank=True, db_column='F_FURNISHINGS_N', null=True)),
                ('f_ss_max', models.TextField(blank=True, db_column='F_SS_MAX', null=True)),
                ('h_tot_dfcncy', models.TextField(blank=True, db_column='H_TOT_DFCNCY', null=True)),
                ('h_quality_care_n', models.TextField(blank=True, db_column='H_QUALITY_CARE_N', null=True)),
                ('h_res_asmnt_n', models.TextField(blank=True, db_column='H_RES_ASMNT_N', null=True)),
                ('h_substndrd_qoc_n', models.TextField(blank=True, db_column='H_SUBSTNDRD_QOC_N', null=True)),
                ('f_hazard_area_n', models.TextField(blank=True, db_column='F_HAZARD_AREA_N', null=True)),
                ('f_illumination_n', models.TextField(blank=True, db_column='F_ILLUMINATION_N', null=True)),
                ('f_survey_date', models.TextField(blank=True, db_column='F_SURVEY_DATE', null=True)),
                ('f_exit_access_n', models.TextField(blank=True, db_column='F_EXIT_ACCESS_N', null=True)),
                ('f_sprinkler_n', models.TextField(blank=True, db_column='F_SPRINKLER_N', null=True)),
                ('f_electrical_n', models.TextField(blank=True, db_column='F_ELECTRICAL_N', null=True)),
                ('f_tot_dfcncy', models.TextField(blank=True, db_column='F_TOT_DFCNCY', null=True)),
                ('f_fire_alarm_n', models.TextField(blank=True, db_column='F_FIRE_ALARM_N', null=True)),
                ('f_corridor_doors_n', models.TextField(blank=True, db_column='F_CORRIDOR_DOORS_N', null=True)),
                ('h_severe_n', models.TextField(blank=True, db_column='H_SEVERE_N', null=True)),
                ('f_exit_egress_n', models.TextField(blank=True, db_column='F_EXIT_EGRESS_N', null=True)),
                ('f_vert_openings_n', models.TextField(blank=True, db_column='F_VERT_OPENINGS_N', null=True)),
                ('f_service_equipment_n', models.TextField(blank=True, db_column='F_SERVICE_EQUIPMENT_N', null=True)),
                ('h_res_rights_n', models.TextField(blank=True, db_column='H_RES_RIGHTS_N', null=True)),
                ('h_ss_max', models.TextField(blank=True, db_column='H_SS_MAX', null=True)),
                ('f_laboratories_n', models.TextField(blank=True, db_column='F_LABORATORIES_N', null=True)),
                ('h_nutrition_n', models.TextField(blank=True, db_column='H_NUTRITION_N', null=True)),
                ('h_environmental_n', models.TextField(blank=True, db_column='H_ENVIRONMENTAL_N', null=True)),
                ('h_pharmacy_n', models.TextField(blank=True, db_column='H_PHARMACY_N', null=True)),
                ('h_administration_n', models.TextField(blank=True, db_column='H_ADMINISTRATION_N', null=True)),
                ('qual_msr_num_401', models.TextField(blank=True, db_column='QUAL_MSR_NUM_401', null=True)),
                ('qual_msr_num_402', models.TextField(blank=True, db_column='QUAL_MSR_NUM_402', null=True)),
                ('qual_msr_num_403', models.TextField(blank=True, db_column='QUAL_MSR_NUM_403', null=True)),
                ('qual_msr_num_404', models.TextField(blank=True, db_column='QUAL_MSR_NUM_404', null=True)),
                ('qual_msr_num_405', models.TextField(blank=True, db_column='QUAL_MSR_NUM_405', null=True)),
                ('qual_msr_num_406', models.TextField(blank=True, db_column='QUAL_MSR_NUM_406', null=True)),
                ('qual_msr_num_407', models.TextField(blank=True, db_column='QUAL_MSR_NUM_407', null=True)),
                ('qual_msr_num_408', models.TextField(blank=True, db_column='QUAL_MSR_NUM_408', null=True)),
                ('qual_msr_num_409', models.TextField(blank=True, db_column='QUAL_MSR_NUM_409', null=True)),
                ('qual_msr_num_410', models.TextField(blank=True, db_column='QUAL_MSR_NUM_410', null=True)),
                ('qual_msr_num_411', models.TextField(blank=True, db_column='QUAL_MSR_NUM_411', null=True)),
                ('qual_msr_num_415', models.TextField(blank=True, db_column='QUAL_MSR_NUM_415', null=True)),
                ('qual_msr_num_419', models.TextField(blank=True, db_column='QUAL_MSR_NUM_419', null=True)),
                ('qual_msr_num_424', models.TextField(blank=True, db_column='QUAL_MSR_NUM_424', null=True)),
                ('qual_msr_num_425', models.TextField(blank=True, db_column='QUAL_MSR_NUM_425', null=True)),
                ('qual_msr_num_426', models.TextField(blank=True, db_column='QUAL_MSR_NUM_426', null=True)),
                ('qual_msr_num_430', models.TextField(blank=True, db_column='QUAL_MSR_NUM_430', null=True)),
                ('qual_msr_num_434', models.TextField(blank=True, db_column='QUAL_MSR_NUM_434', null=True)),
            ],
            options={
                'db_table': 'ProviderInfo',
                'managed': False,
            },
        ),
    ]
