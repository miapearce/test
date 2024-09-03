# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:10:37 2024

@author: pearcem
"""

from functools import partial
import pandas as pd
import numpy as np
from pathlib import Path
import yaml
import platform
import os

# Copy & Paste file names exactly. Need double slash after drive name "C:\\Users"
Vine_path = r"T:\cheny\VinelandConversion_08292024MiaTest.csv"
# Create a name for the converted file to be saved as. Need double slash after drive name "C:\\Users"
Vineconverted_path = r"T:\cheny\2Converted_VinelandConversion_08292024MiaTest.csv"
df = pd.read_csv(Vine_path)
keep_cols = ['FirstName', 'vi3_rec_raw', 'vi3_rec_ss', 'vi3_exp_raw', 'vi3_exp_ss',
    'vi3_wrn_raw', 'vi3_wrn_ss', 'vi3_com_ss', 'vi3_com_pr',
    'vi3_per_raw', 'vi3_per_ss', 'vi3_dom_raw', 'vi3_dom_ss',
    'vi3_cmm_raw', 'vi3_cmm_ss', 'vi3_dls_ss', 'vi3_dls_pr',
    'vi3_ipr_raw', 'vi3_ipr_ss', 'vi3_pla_raw', 'vi3_pla_ss',
    'vi3_cop_raw', 'vi3_cop_ss', 'vi3_soc_ss', 'vi3_soc_pr',
    'vi3_gmo_raw', 'vi3_gmo_ss', 'vi3_fmo_raw', 'vi3_fmo_ss',
    'vi3_mot_ss', 'vi3_mot_pr', 'vi3_abc_ss', 'vi3_abc_pr']
df = df[keep_cols]
lut = dict()
lut['vi3_rec_raw'] = 'vinelandcb_receptive_raw3comp'
lut['vi3_rec_ss'] = 'vinelandcb_receptive_vscale'
lut['vi3_exp_raw'] = 'vinelandcb_expressive_raw3comp'
lut['vi3_exp_ss'] = 'vinelandcb_expressive_vscale'
lut['vi3_wrn_raw'] = 'vinelandcb_written_raw3comp'
lut['vi3_wrn_ss'] = 'vinelandcb_written_vscale'
lut['vi3_com_ss'] = 'vinelandcb_communication_stdscr'
lut['vi3_com_pr'] = 'vinelandcb_communication_percent'
lut['vi3_per_raw'] = 'vinelandcb_personal_raw3comp'
lut['vi3_per_ss'] = 'vinelandcb_personal_vscale'
lut['vi3_dom_raw'] = 'vinelandcb_domestic_raw3comp'
lut['vi3_dom_ss'] = 'vinelandcb_domestic_vscale'
lut['vi3_cmm_raw'] = 'vinelandcb_community_raw3comp'
lut['vi3_cmm_ss'] = 'vinelandcb_community_vscale'
lut['vi3_dls_ss'] = 'vinelandcb_dailyliving_stdscr'
lut['vi3_dls_pr'] = 'vinelandcb_dailyliving_percentile'
lut['vi3_ipr_raw'] = 'vinelandcb_interpersonal_raw3comp'
lut['vi3_ipr_ss'] = 'vinelandcb_interpersonal_vscale'
lut['vi3_pla_raw'] = 'vinelandcb_playleis_raw3comp'
lut['vi3_pla_ss'] = 'vinelandcb_playleis_vscale'
lut['vi3_cop_raw'] = 'vinelandcb_coping_raw3comp'
lut['vi3_cop_ss'] = 'vinelandcb_coping_vscale'
lut['vi3_soc_ss'] = 'vinelandcb_socialization_stdscr'
lut['vi3_soc_pr'] = 'vinelandcb_socialization_percentile'
lut['vi3_gmo_raw'] = 'vinelandcb_grossmot_raw3comp'
lut['vi3_gmo_ss'] = 'vinelandcb_grossmot_vscale'
lut['vi3_fmo_raw'] = 'vinelandcb_finemot_raw3comp'
lut['vi3_fmo_ss'] = 'vinelandcb_finemot_vscale'
lut['vi3_mot_ss'] = 'vinelandcb_motorskills_stdscr'
lut['vi3_mot_pr'] = 'vinelandcb_motorskills_percentile'
lut['vi3_abc_ss'] = 'vinelandcb_abc_stdscr'
lut['vi3_abc_pr'] = 'vinelandcb_abc_percentile'
vine = df.rename(columns=lut)
vine[['study_id', 'redcap_event_name']] = vine['FirstName'].str.split('V', n=1, expand=True)
vine['redcap_event_name'] = vine['redcap_event_name'].map({'4': 'visit4_arm_1', '5': 'visit5_arm_1', '6': 'visit6_arm_1'})
vine['vineland_combined_2_3_complete'] = 2
vine = vine.reindex(columns=['study_id', 'redcap_event_name', 'vinelandcb_receptive_raw3comp', 'vinelandcb_receptive_vscale',
    'vinelandcb_expressive_raw3comp', 'vinelandcb_expressive_vscale',
    'vinelandcb_written_raw3comp', 'vinelandcb_written_vscale',
    'vinelandcb_communication_stdscr', 'vinelandcb_communication_percent',
    'vinelandcb_personal_raw3comp', 'vinelandcb_personal_vscale',
    'vinelandcb_domestic_raw3comp', 'vinelandcb_domestic_vscale',
    'vinelandcb_community_raw3comp', 'vinelandcb_community_vscale',
    'vinelandcb_dailyliving_stdscr', 'vinelandcb_dailyliving_percentile',
    'vinelandcb_interpersonal_raw3comp', 'vinelandcb_interpersonal_vscale',
    'vinelandcb_playleis_raw3comp', 'vinelandcb_playleis_vscale',
    'vinelandcb_coping_raw3comp', 'vinelandcb_coping_vscale',
    'vinelandcb_socialization_stdscr', 'vinelandcb_socialization_percentile',
    'vinelandcb_grossmot_raw3comp', 'vinelandcb_grossmot_vscale',
    'vinelandcb_finemot_raw3comp', 'vinelandcb_finemot_vscale',
    'vinelandcb_motorskills_stdscr', 'vinelandcb_motorskills_percentile',
    'vinelandcb_abc_stdscr', 'vinelandcb_abc_percentile'])
vine.to_csv(Vineconverted_path, index=False)