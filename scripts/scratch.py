from pprint import pprint
import maya.cmds
import maya.cmds as mc
import follicle
import chains
import skinCluster
import softModCon

import glTools.tools

reload(follicle)
reload(chains)
reload(skinCluster)
reload(softModCon)

"""
import scratch
reload(scratch)

# run first
cs = scratch.build()

'''
cs = [{'circles': [u'makeNurbCircle6', u'makeNurbCircle7', u'makeNurbCircle8', u'makeNurbCircle9', u'makeNurbCircle10', u'makeNurbCircle11', u'makeNurbCircle12', u'makeNurbCircle13'], 'curve': u'braidHair_07_CRV', 'tube': [u'braidHair_07_CRV_TUBE', u'loft1'], 'nulls': [u'braidHair_07_CRV_0_JNT_CIRCLE_JNT', u'braidHair_07_CRV_1_JNT_CIRCLE_JNT', u'braidHair_07_CRV_2_JNT_CIRCLE_JNT', u'braidHair_07_CRV_3_JNT_CIRCLE_JNT', u'braidHair_07_CRV_4_JNT_CIRCLE_JNT', u'braidHair_07_CRV_5_JNT_CIRCLE_JNT', u'braidHair_07_CRV_6_JNT_CIRCLE_JNT', u'braidHair_07_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape1', u'curveShape2', u'curveShape3', u'curveShape4', u'curveShape5', u'curveShape6', u'curveShape7', u'curveShape8'], 'shapes': [u'nurbsCircleShape108', u'nurbsCircleShape109', u'nurbsCircleShape110', u'nurbsCircleShape111', u'nurbsCircleShape112', u'nurbsCircleShape113', u'nurbsCircleShape114', u'nurbsCircleShape115'], 'proxy': [u'braidHair_07_CRV_PXY', u'nurbsTessellate1'], 'influences': [u'bind_braidHair_07_CRV_7_JNT', u'bind_braidHair_07_CRV_6_JNT', u'bind_braidHair_07_CRV_5_JNT', u'bind_braidHair_07_CRV_4_JNT', u'bind_braidHair_07_CRV_3_JNT', u'bind_braidHair_07_CRV_2_JNT', u'bind_braidHair_07_CRV_1_JNT', u'bind_braidHair_07_CRV_0_JNT'], 'skin': u'skinCluster352', 'ribbon': [u'braidHair_07_CRV_RIBBON', u'loft2']}, {'circles': [u'makeNurbCircle14', u'makeNurbCircle15', u'makeNurbCircle16', u'makeNurbCircle17', u'makeNurbCircle18', u'makeNurbCircle19', u'makeNurbCircle20', u'makeNurbCircle21'], 'curve': u'braidHair_14_CRV', 'tube': [u'braidHair_14_CRV_TUBE', u'loft3'], 'nulls': [u'braidHair_14_CRV_0_JNT_CIRCLE_JNT', u'braidHair_14_CRV_1_JNT_CIRCLE_JNT', u'braidHair_14_CRV_2_JNT_CIRCLE_JNT', u'braidHair_14_CRV_3_JNT_CIRCLE_JNT', u'braidHair_14_CRV_4_JNT_CIRCLE_JNT', u'braidHair_14_CRV_5_JNT_CIRCLE_JNT', u'braidHair_14_CRV_6_JNT_CIRCLE_JNT', u'braidHair_14_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape9', u'curveShape10', u'curveShape11', u'curveShape12', u'curveShape13', u'curveShape14', u'curveShape15', u'curveShape16'], 'shapes': [u'nurbsCircleShape116', u'nurbsCircleShape117', u'nurbsCircleShape118', u'nurbsCircleShape119', u'nurbsCircleShape120', u'nurbsCircleShape121', u'nurbsCircleShape122', u'nurbsCircleShape123'], 'proxy': [u'braidHair_14_CRV_PXY', u'nurbsTessellate2'], 'influences': [u'bind_braidHair_14_CRV_7_JNT', u'bind_braidHair_14_CRV_6_JNT', u'bind_braidHair_14_CRV_5_JNT', u'bind_braidHair_14_CRV_4_JNT', u'bind_braidHair_14_CRV_3_JNT', u'bind_braidHair_14_CRV_2_JNT', u'bind_braidHair_14_CRV_1_JNT', u'bind_braidHair_14_CRV_0_JNT'], 'skin': u'skinCluster353', 'ribbon': [u'braidHair_14_CRV_RIBBON', u'loft4']}, {'circles': [u'makeNurbCircle22', u'makeNurbCircle23', u'makeNurbCircle24', u'makeNurbCircle25', u'makeNurbCircle26', u'makeNurbCircle27', u'makeNurbCircle28', u'makeNurbCircle29'], 'curve': u'braidHair_21_CRV', 'tube': [u'braidHair_21_CRV_TUBE', u'loft5'], 'nulls': [u'braidHair_21_CRV_0_JNT_CIRCLE_JNT', u'braidHair_21_CRV_1_JNT_CIRCLE_JNT', u'braidHair_21_CRV_2_JNT_CIRCLE_JNT', u'braidHair_21_CRV_3_JNT_CIRCLE_JNT', u'braidHair_21_CRV_4_JNT_CIRCLE_JNT', u'braidHair_21_CRV_5_JNT_CIRCLE_JNT', u'braidHair_21_CRV_6_JNT_CIRCLE_JNT', u'braidHair_21_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape17', u'curveShape18', u'curveShape19', u'curveShape20', u'curveShape21', u'curveShape22', u'curveShape23', u'curveShape24'], 'shapes': [u'nurbsCircleShape124', u'nurbsCircleShape125', u'nurbsCircleShape126', u'nurbsCircleShape127', u'nurbsCircleShape128', u'nurbsCircleShape129', u'nurbsCircleShape130', u'nurbsCircleShape131'], 'proxy': [u'braidHair_21_CRV_PXY', u'nurbsTessellate3'], 'influences': [u'bind_braidHair_21_CRV_7_JNT', u'bind_braidHair_21_CRV_6_JNT', u'bind_braidHair_21_CRV_5_JNT', u'bind_braidHair_21_CRV_4_JNT', u'bind_braidHair_21_CRV_3_JNT', u'bind_braidHair_21_CRV_2_JNT', u'bind_braidHair_21_CRV_1_JNT', u'bind_braidHair_21_CRV_0_JNT'], 'skin': u'skinCluster354', 'ribbon': [u'braidHair_21_CRV_RIBBON', u'loft6']}, {'circles': [u'makeNurbCircle30', u'makeNurbCircle31', u'makeNurbCircle32', u'makeNurbCircle33', u'makeNurbCircle34', u'makeNurbCircle35', u'makeNurbCircle36', u'makeNurbCircle37'], 'curve': u'braidHair_23_CRV', 'tube': [u'braidHair_23_CRV_TUBE', u'loft7'], 'nulls': [u'braidHair_23_CRV_0_JNT_CIRCLE_JNT', u'braidHair_23_CRV_1_JNT_CIRCLE_JNT', u'braidHair_23_CRV_2_JNT_CIRCLE_JNT', u'braidHair_23_CRV_3_JNT_CIRCLE_JNT', u'braidHair_23_CRV_4_JNT_CIRCLE_JNT', u'braidHair_23_CRV_5_JNT_CIRCLE_JNT', u'braidHair_23_CRV_6_JNT_CIRCLE_JNT', u'braidHair_23_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape25', u'curveShape26', u'curveShape27', u'curveShape28', u'curveShape29', u'curveShape30', u'curveShape31', u'curveShape32'], 'shapes': [u'nurbsCircleShape132', u'nurbsCircleShape133', u'nurbsCircleShape134', u'nurbsCircleShape135', u'nurbsCircleShape136', u'nurbsCircleShape137', u'nurbsCircleShape138', u'nurbsCircleShape139'], 'proxy': [u'braidHair_23_CRV_PXY', u'nurbsTessellate4'], 'influences': [u'bind_braidHair_23_CRV_7_JNT', u'bind_braidHair_23_CRV_6_JNT', u'bind_braidHair_23_CRV_5_JNT', u'bind_braidHair_23_CRV_4_JNT', u'bind_braidHair_23_CRV_3_JNT', u'bind_braidHair_23_CRV_2_JNT', u'bind_braidHair_23_CRV_1_JNT', u'bind_braidHair_23_CRV_0_JNT'], 'skin': u'skinCluster355', 'ribbon': [u'braidHair_23_CRV_RIBBON', u'loft8']}, {'circles': [u'makeNurbCircle38', u'makeNurbCircle39', u'makeNurbCircle40', u'makeNurbCircle41', u'makeNurbCircle42', u'makeNurbCircle43', u'makeNurbCircle44', u'makeNurbCircle45'], 'curve': u'braidHair_30_CRV', 'tube': [u'braidHair_30_CRV_TUBE', u'loft9'], 'nulls': [u'braidHair_30_CRV_0_JNT_CIRCLE_JNT', u'braidHair_30_CRV_1_JNT_CIRCLE_JNT', u'braidHair_30_CRV_2_JNT_CIRCLE_JNT', u'braidHair_30_CRV_3_JNT_CIRCLE_JNT', u'braidHair_30_CRV_4_JNT_CIRCLE_JNT', u'braidHair_30_CRV_5_JNT_CIRCLE_JNT', u'braidHair_30_CRV_6_JNT_CIRCLE_JNT', u'braidHair_30_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape33', u'curveShape34', u'curveShape35', u'curveShape36', u'curveShape37', u'curveShape38', u'curveShape39', u'curveShape40'], 'shapes': [u'nurbsCircleShape140', u'nurbsCircleShape141', u'nurbsCircleShape142', u'nurbsCircleShape143', u'nurbsCircleShape144', u'nurbsCircleShape145', u'nurbsCircleShape146', u'nurbsCircleShape147'], 'proxy': [u'braidHair_30_CRV_PXY', u'nurbsTessellate5'], 'influences': [u'bind_braidHair_30_CRV_7_JNT', u'bind_braidHair_30_CRV_6_JNT', u'bind_braidHair_30_CRV_5_JNT', u'bind_braidHair_30_CRV_4_JNT', u'bind_braidHair_30_CRV_3_JNT', u'bind_braidHair_30_CRV_2_JNT', u'bind_braidHair_30_CRV_1_JNT', u'bind_braidHair_30_CRV_0_JNT'], 'skin': u'skinCluster356', 'ribbon': [u'braidHair_30_CRV_RIBBON', u'loft10']}, {'circles': [u'makeNurbCircle46', u'makeNurbCircle47', u'makeNurbCircle48', u'makeNurbCircle49', u'makeNurbCircle50', u'makeNurbCircle51', u'makeNurbCircle52', u'makeNurbCircle53'], 'curve': u'braidHair_42_CRV', 'tube': [u'braidHair_42_CRV_TUBE', u'loft11'], 'nulls': [u'braidHair_42_CRV_0_JNT_CIRCLE_JNT', u'braidHair_42_CRV_1_JNT_CIRCLE_JNT', u'braidHair_42_CRV_2_JNT_CIRCLE_JNT', u'braidHair_42_CRV_3_JNT_CIRCLE_JNT', u'braidHair_42_CRV_4_JNT_CIRCLE_JNT', u'braidHair_42_CRV_5_JNT_CIRCLE_JNT', u'braidHair_42_CRV_6_JNT_CIRCLE_JNT', u'braidHair_42_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape41', u'curveShape42', u'curveShape43', u'curveShape44', u'curveShape45', u'curveShape46', u'curveShape47', u'curveShape48'], 'shapes': [u'nurbsCircleShape148', u'nurbsCircleShape149', u'nurbsCircleShape150', u'nurbsCircleShape151', u'nurbsCircleShape152', u'nurbsCircleShape153', u'nurbsCircleShape154', u'nurbsCircleShape155'], 'proxy': [u'braidHair_42_CRV_PXY', u'nurbsTessellate6'], 'influences': [u'bind_braidHair_42_CRV_7_JNT', u'bind_braidHair_42_CRV_6_JNT', u'bind_braidHair_42_CRV_5_JNT', u'bind_braidHair_42_CRV_4_JNT', u'bind_braidHair_42_CRV_3_JNT', u'bind_braidHair_42_CRV_2_JNT', u'bind_braidHair_42_CRV_1_JNT', u'bind_braidHair_42_CRV_0_JNT'], 'skin': u'skinCluster357', 'ribbon': [u'braidHair_42_CRV_RIBBON', u'loft12']}, {'circles': [u'makeNurbCircle54', u'makeNurbCircle55', u'makeNurbCircle56', u'makeNurbCircle57', u'makeNurbCircle58', u'makeNurbCircle59', u'makeNurbCircle60', u'makeNurbCircle61'], 'curve': u'braidHair_48_CRV', 'tube': [u'braidHair_48_CRV_TUBE', u'loft13'], 'nulls': [u'braidHair_48_CRV_0_JNT_CIRCLE_JNT', u'braidHair_48_CRV_1_JNT_CIRCLE_JNT', u'braidHair_48_CRV_2_JNT_CIRCLE_JNT', u'braidHair_48_CRV_3_JNT_CIRCLE_JNT', u'braidHair_48_CRV_4_JNT_CIRCLE_JNT', u'braidHair_48_CRV_5_JNT_CIRCLE_JNT', u'braidHair_48_CRV_6_JNT_CIRCLE_JNT', u'braidHair_48_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape49', u'curveShape50', u'curveShape51', u'curveShape52', u'curveShape53', u'curveShape54', u'curveShape55', u'curveShape56'], 'shapes': [u'nurbsCircleShape156', u'nurbsCircleShape157', u'nurbsCircleShape158', u'nurbsCircleShape159', u'nurbsCircleShape160', u'nurbsCircleShape161', u'nurbsCircleShape162', u'nurbsCircleShape163'], 'proxy': [u'braidHair_48_CRV_PXY', u'nurbsTessellate7'], 'influences': [u'bind_braidHair_48_CRV_7_JNT', u'bind_braidHair_48_CRV_6_JNT', u'bind_braidHair_48_CRV_5_JNT', u'bind_braidHair_48_CRV_4_JNT', u'bind_braidHair_48_CRV_3_JNT', u'bind_braidHair_48_CRV_2_JNT', u'bind_braidHair_48_CRV_1_JNT', u'bind_braidHair_48_CRV_0_JNT'], 'skin': u'skinCluster358', 'ribbon': [u'braidHair_48_CRV_RIBBON', u'loft14']}, {'circles': [u'makeNurbCircle62', u'makeNurbCircle63', u'makeNurbCircle64', u'makeNurbCircle65', u'makeNurbCircle66', u'makeNurbCircle67', u'makeNurbCircle68', u'makeNurbCircle69'], 'curve': u'braidHair_51_CRV', 'tube': [u'braidHair_51_CRV_TUBE', u'loft15'], 'nulls': [u'braidHair_51_CRV_0_JNT_CIRCLE_JNT', u'braidHair_51_CRV_1_JNT_CIRCLE_JNT', u'braidHair_51_CRV_2_JNT_CIRCLE_JNT', u'braidHair_51_CRV_3_JNT_CIRCLE_JNT', u'braidHair_51_CRV_4_JNT_CIRCLE_JNT', u'braidHair_51_CRV_5_JNT_CIRCLE_JNT', u'braidHair_51_CRV_6_JNT_CIRCLE_JNT', u'braidHair_51_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape57', u'curveShape58', u'curveShape59', u'curveShape60', u'curveShape61', u'curveShape62', u'curveShape63', u'curveShape64'], 'shapes': [u'nurbsCircleShape164', u'nurbsCircleShape165', u'nurbsCircleShape166', u'nurbsCircleShape167', u'nurbsCircleShape168', u'nurbsCircleShape169', u'nurbsCircleShape170', u'nurbsCircleShape171'], 'proxy': [u'braidHair_51_CRV_PXY', u'nurbsTessellate8'], 'influences': [u'bind_braidHair_51_CRV_7_JNT', u'bind_braidHair_51_CRV_6_JNT', u'bind_braidHair_51_CRV_5_JNT', u'bind_braidHair_51_CRV_4_JNT', u'bind_braidHair_51_CRV_3_JNT', u'bind_braidHair_51_CRV_2_JNT', u'bind_braidHair_51_CRV_1_JNT', u'bind_braidHair_51_CRV_0_JNT'], 'skin': u'skinCluster359', 'ribbon': [u'braidHair_51_CRV_RIBBON', u'loft16']}, {'circles': [u'makeNurbCircle70', u'makeNurbCircle71', u'makeNurbCircle72', u'makeNurbCircle73', u'makeNurbCircle74', u'makeNurbCircle75', u'makeNurbCircle76', u'makeNurbCircle77'], 'curve': u'hair_01_CRV', 'tube': [u'hair_01_CRV_TUBE', u'loft17'], 'nulls': [u'hair_01_CRV_0_JNT_CIRCLE_JNT', u'hair_01_CRV_1_JNT_CIRCLE_JNT', u'hair_01_CRV_2_JNT_CIRCLE_JNT', u'hair_01_CRV_3_JNT_CIRCLE_JNT', u'hair_01_CRV_4_JNT_CIRCLE_JNT', u'hair_01_CRV_5_JNT_CIRCLE_JNT', u'hair_01_CRV_6_JNT_CIRCLE_JNT', u'hair_01_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape65', u'curveShape66', u'curveShape67', u'curveShape68', u'curveShape69', u'curveShape70', u'curveShape71', u'curveShape72'], 'shapes': [u'nurbsCircleShape172', u'nurbsCircleShape173', u'nurbsCircleShape174', u'nurbsCircleShape175', u'nurbsCircleShape176', u'nurbsCircleShape177', u'nurbsCircleShape178', u'nurbsCircleShape179'], 'proxy': [u'hair_01_CRV_PXY', u'nurbsTessellate9'], 'influences': [u'bind_hair_01_CRV_7_JNT', u'bind_hair_01_CRV_6_JNT', u'bind_hair_01_CRV_5_JNT', u'bind_hair_01_CRV_4_JNT', u'bind_hair_01_CRV_3_JNT', u'bind_hair_01_CRV_2_JNT', u'bind_hair_01_CRV_1_JNT', u'bind_hair_01_CRV_0_JNT'], 'skin': u'skinCluster360', 'ribbon': [u'hair_01_CRV_RIBBON', u'loft18']}, {'circles': [u'makeNurbCircle78', u'makeNurbCircle79', u'makeNurbCircle80', u'makeNurbCircle81', u'makeNurbCircle82', u'makeNurbCircle83', u'makeNurbCircle84', u'makeNurbCircle85'], 'curve': u'hair_02_CRV', 'tube': [u'hair_02_CRV_TUBE', u'loft19'], 'nulls': [u'hair_02_CRV_0_JNT_CIRCLE_JNT', u'hair_02_CRV_1_JNT_CIRCLE_JNT', u'hair_02_CRV_2_JNT_CIRCLE_JNT', u'hair_02_CRV_3_JNT_CIRCLE_JNT', u'hair_02_CRV_4_JNT_CIRCLE_JNT', u'hair_02_CRV_5_JNT_CIRCLE_JNT', u'hair_02_CRV_6_JNT_CIRCLE_JNT', u'hair_02_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape73', u'curveShape74', u'curveShape75', u'curveShape76', u'curveShape77', u'curveShape78', u'curveShape79', u'curveShape80'], 'shapes': [u'nurbsCircleShape180', u'nurbsCircleShape181', u'nurbsCircleShape182', u'nurbsCircleShape183', u'nurbsCircleShape184', u'nurbsCircleShape185', u'nurbsCircleShape186', u'nurbsCircleShape187'], 'proxy': [u'hair_02_CRV_PXY', u'nurbsTessellate10'], 'influences': [u'bind_hair_02_CRV_7_JNT', u'bind_hair_02_CRV_6_JNT', u'bind_hair_02_CRV_5_JNT', u'bind_hair_02_CRV_4_JNT', u'bind_hair_02_CRV_3_JNT', u'bind_hair_02_CRV_2_JNT', u'bind_hair_02_CRV_1_JNT', u'bind_hair_02_CRV_0_JNT'], 'skin': u'skinCluster361', 'ribbon': [u'hair_02_CRV_RIBBON', u'loft20']}, {'circles': [u'makeNurbCircle86', u'makeNurbCircle87', u'makeNurbCircle88', u'makeNurbCircle89', u'makeNurbCircle90', u'makeNurbCircle91', u'makeNurbCircle92', u'makeNurbCircle93'], 'curve': u'hair_03_CRV', 'tube': [u'hair_03_CRV_TUBE', u'loft21'], 'nulls': [u'hair_03_CRV_0_JNT_CIRCLE_JNT', u'hair_03_CRV_1_JNT_CIRCLE_JNT', u'hair_03_CRV_2_JNT_CIRCLE_JNT', u'hair_03_CRV_3_JNT_CIRCLE_JNT', u'hair_03_CRV_4_JNT_CIRCLE_JNT', u'hair_03_CRV_5_JNT_CIRCLE_JNT', u'hair_03_CRV_6_JNT_CIRCLE_JNT', u'hair_03_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape81', u'curveShape82', u'curveShape83', u'curveShape84', u'curveShape85', u'curveShape86', u'curveShape87', u'curveShape88'], 'shapes': [u'nurbsCircleShape188', u'nurbsCircleShape189', u'nurbsCircleShape190', u'nurbsCircleShape191', u'nurbsCircleShape192', u'nurbsCircleShape193', u'nurbsCircleShape194', u'nurbsCircleShape195'], 'proxy': [u'hair_03_CRV_PXY', u'nurbsTessellate11'], 'influences': [u'bind_hair_03_CRV_7_JNT', u'bind_hair_03_CRV_6_JNT', u'bind_hair_03_CRV_5_JNT', u'bind_hair_03_CRV_4_JNT', u'bind_hair_03_CRV_3_JNT', u'bind_hair_03_CRV_2_JNT', u'bind_hair_03_CRV_1_JNT', u'bind_hair_03_CRV_0_JNT'], 'skin': u'skinCluster362', 'ribbon': [u'hair_03_CRV_RIBBON', u'loft22']}, {'circles': [u'makeNurbCircle94', u'makeNurbCircle95', u'makeNurbCircle96', u'makeNurbCircle97', u'makeNurbCircle98', u'makeNurbCircle99', u'makeNurbCircle100', u'makeNurbCircle101'], 'curve': u'hair_04_CRV', 'tube': [u'hair_04_CRV_TUBE', u'loft23'], 'nulls': [u'hair_04_CRV_0_JNT_CIRCLE_JNT', u'hair_04_CRV_1_JNT_CIRCLE_JNT', u'hair_04_CRV_2_JNT_CIRCLE_JNT', u'hair_04_CRV_3_JNT_CIRCLE_JNT', u'hair_04_CRV_4_JNT_CIRCLE_JNT', u'hair_04_CRV_5_JNT_CIRCLE_JNT', u'hair_04_CRV_6_JNT_CIRCLE_JNT', u'hair_04_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape89', u'curveShape90', u'curveShape91', u'curveShape92', u'curveShape93', u'curveShape94', u'curveShape95', u'curveShape96'], 'shapes': [u'nurbsCircleShape196', u'nurbsCircleShape197', u'nurbsCircleShape198', u'nurbsCircleShape199', u'nurbsCircleShape200', u'nurbsCircleShape201', u'nurbsCircleShape202', u'nurbsCircleShape203'], 'proxy': [u'hair_04_CRV_PXY', u'nurbsTessellate12'], 'influences': [u'bind_hair_04_CRV_7_JNT', u'bind_hair_04_CRV_6_JNT', u'bind_hair_04_CRV_5_JNT', u'bind_hair_04_CRV_4_JNT', u'bind_hair_04_CRV_3_JNT', u'bind_hair_04_CRV_2_JNT', u'bind_hair_04_CRV_1_JNT', u'bind_hair_04_CRV_0_JNT'], 'skin': u'skinCluster363', 'ribbon': [u'hair_04_CRV_RIBBON', u'loft24']}, {'circles': [u'makeNurbCircle102', u'makeNurbCircle103', u'makeNurbCircle104', u'makeNurbCircle105', u'makeNurbCircle106', u'makeNurbCircle107', u'makeNurbCircle108', u'makeNurbCircle109'], 'curve': u'hair_05_CRV', 'tube': [u'hair_05_CRV_TUBE', u'loft25'], 'nulls': [u'hair_05_CRV_0_JNT_CIRCLE_JNT', u'hair_05_CRV_1_JNT_CIRCLE_JNT', u'hair_05_CRV_2_JNT_CIRCLE_JNT', u'hair_05_CRV_3_JNT_CIRCLE_JNT', u'hair_05_CRV_4_JNT_CIRCLE_JNT', u'hair_05_CRV_5_JNT_CIRCLE_JNT', u'hair_05_CRV_6_JNT_CIRCLE_JNT', u'hair_05_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape97', u'curveShape98', u'curveShape99', u'curveShape100', u'curveShape101', u'curveShape102', u'curveShape103', u'curveShape104'], 'shapes': [u'nurbsCircleShape204', u'nurbsCircleShape205', u'nurbsCircleShape206', u'nurbsCircleShape207', u'nurbsCircleShape208', u'nurbsCircleShape209', u'nurbsCircleShape210', u'nurbsCircleShape211'], 'proxy': [u'hair_05_CRV_PXY', u'nurbsTessellate13'], 'influences': [u'bind_hair_05_CRV_7_JNT', u'bind_hair_05_CRV_6_JNT', u'bind_hair_05_CRV_5_JNT', u'bind_hair_05_CRV_4_JNT', u'bind_hair_05_CRV_3_JNT', u'bind_hair_05_CRV_2_JNT', u'bind_hair_05_CRV_1_JNT', u'bind_hair_05_CRV_0_JNT'], 'skin': u'skinCluster364', 'ribbon': [u'hair_05_CRV_RIBBON', u'loft26']}, {'circles': [u'makeNurbCircle110', u'makeNurbCircle111', u'makeNurbCircle112', u'makeNurbCircle113', u'makeNurbCircle114', u'makeNurbCircle115', u'makeNurbCircle116', u'makeNurbCircle117'], 'curve': u'hair_06_CRV', 'tube': [u'hair_06_CRV_TUBE', u'loft27'], 'nulls': [u'hair_06_CRV_0_JNT_CIRCLE_JNT', u'hair_06_CRV_1_JNT_CIRCLE_JNT', u'hair_06_CRV_2_JNT_CIRCLE_JNT', u'hair_06_CRV_3_JNT_CIRCLE_JNT', u'hair_06_CRV_4_JNT_CIRCLE_JNT', u'hair_06_CRV_5_JNT_CIRCLE_JNT', u'hair_06_CRV_6_JNT_CIRCLE_JNT', u'hair_06_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape105', u'curveShape106', u'curveShape107', u'curveShape108', u'curveShape109', u'curveShape110', u'curveShape111', u'curveShape112'], 'shapes': [u'nurbsCircleShape212', u'nurbsCircleShape213', u'nurbsCircleShape214', u'nurbsCircleShape215', u'nurbsCircleShape216', u'nurbsCircleShape217', u'nurbsCircleShape218', u'nurbsCircleShape219'], 'proxy': [u'hair_06_CRV_PXY', u'nurbsTessellate14'], 'influences': [u'bind_hair_06_CRV_7_JNT', u'bind_hair_06_CRV_6_JNT', u'bind_hair_06_CRV_5_JNT', u'bind_hair_06_CRV_4_JNT', u'bind_hair_06_CRV_3_JNT', u'bind_hair_06_CRV_2_JNT', u'bind_hair_06_CRV_1_JNT', u'bind_hair_06_CRV_0_JNT'], 'skin': u'skinCluster365', 'ribbon': [u'hair_06_CRV_RIBBON', u'loft28']}, {'circles': [u'makeNurbCircle118', u'makeNurbCircle119', u'makeNurbCircle120', u'makeNurbCircle121', u'makeNurbCircle122', u'makeNurbCircle123', u'makeNurbCircle124', u'makeNurbCircle125'], 'curve': u'hair_07_CRV', 'tube': [u'hair_07_CRV_TUBE', u'loft29'], 'nulls': [u'hair_07_CRV_0_JNT_CIRCLE_JNT', u'hair_07_CRV_1_JNT_CIRCLE_JNT', u'hair_07_CRV_2_JNT_CIRCLE_JNT', u'hair_07_CRV_3_JNT_CIRCLE_JNT', u'hair_07_CRV_4_JNT_CIRCLE_JNT', u'hair_07_CRV_5_JNT_CIRCLE_JNT', u'hair_07_CRV_6_JNT_CIRCLE_JNT', u'hair_07_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape113', u'curveShape114', u'curveShape115', u'curveShape116', u'curveShape117', u'curveShape118', u'curveShape119', u'curveShape120'], 'shapes': [u'nurbsCircleShape220', u'nurbsCircleShape221', u'nurbsCircleShape222', u'nurbsCircleShape223', u'nurbsCircleShape224', u'nurbsCircleShape225', u'nurbsCircleShape226', u'nurbsCircleShape227'], 'proxy': [u'hair_07_CRV_PXY', u'nurbsTessellate15'], 'influences': [u'bind_hair_07_CRV_7_JNT', u'bind_hair_07_CRV_6_JNT', u'bind_hair_07_CRV_5_JNT', u'bind_hair_07_CRV_4_JNT', u'bind_hair_07_CRV_3_JNT', u'bind_hair_07_CRV_2_JNT', u'bind_hair_07_CRV_1_JNT', u'bind_hair_07_CRV_0_JNT'], 'skin': u'skinCluster366', 'ribbon': [u'hair_07_CRV_RIBBON', u'loft30']}, {'circles': [u'makeNurbCircle126', u'makeNurbCircle127', u'makeNurbCircle128', u'makeNurbCircle129', u'makeNurbCircle130', u'makeNurbCircle131', u'makeNurbCircle132', u'makeNurbCircle133'], 'curve': u'hair_08_CRV', 'tube': [u'hair_08_CRV_TUBE', u'loft31'], 'nulls': [u'hair_08_CRV_0_JNT_CIRCLE_JNT', u'hair_08_CRV_1_JNT_CIRCLE_JNT', u'hair_08_CRV_2_JNT_CIRCLE_JNT', u'hair_08_CRV_3_JNT_CIRCLE_JNT', u'hair_08_CRV_4_JNT_CIRCLE_JNT', u'hair_08_CRV_5_JNT_CIRCLE_JNT', u'hair_08_CRV_6_JNT_CIRCLE_JNT', u'hair_08_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape121', u'curveShape122', u'curveShape123', u'curveShape124', u'curveShape125', u'curveShape126', u'curveShape127', u'curveShape128'], 'shapes': [u'nurbsCircleShape228', u'nurbsCircleShape229', u'nurbsCircleShape230', u'nurbsCircleShape231', u'nurbsCircleShape232', u'nurbsCircleShape233', u'nurbsCircleShape234', u'nurbsCircleShape235'], 'proxy': [u'hair_08_CRV_PXY', u'nurbsTessellate16'], 'influences': [u'bind_hair_08_CRV_7_JNT', u'bind_hair_08_CRV_6_JNT', u'bind_hair_08_CRV_5_JNT', u'bind_hair_08_CRV_4_JNT', u'bind_hair_08_CRV_3_JNT', u'bind_hair_08_CRV_2_JNT', u'bind_hair_08_CRV_1_JNT', u'bind_hair_08_CRV_0_JNT'], 'skin': u'skinCluster367', 'ribbon': [u'hair_08_CRV_RIBBON', u'loft32']}, {'circles': [u'makeNurbCircle134', u'makeNurbCircle135', u'makeNurbCircle136', u'makeNurbCircle137', u'makeNurbCircle138', u'makeNurbCircle139', u'makeNurbCircle140', u'makeNurbCircle141'], 'curve': u'hair_09_CRV', 'tube': [u'hair_09_CRV_TUBE', u'loft33'], 'nulls': [u'hair_09_CRV_0_JNT_CIRCLE_JNT', u'hair_09_CRV_1_JNT_CIRCLE_JNT', u'hair_09_CRV_2_JNT_CIRCLE_JNT', u'hair_09_CRV_3_JNT_CIRCLE_JNT', u'hair_09_CRV_4_JNT_CIRCLE_JNT', u'hair_09_CRV_5_JNT_CIRCLE_JNT', u'hair_09_CRV_6_JNT_CIRCLE_JNT', u'hair_09_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape129', u'curveShape130', u'curveShape131', u'curveShape132', u'curveShape133', u'curveShape134', u'curveShape135', u'curveShape136'], 'shapes': [u'nurbsCircleShape236', u'nurbsCircleShape237', u'nurbsCircleShape238', u'nurbsCircleShape239', u'nurbsCircleShape240', u'nurbsCircleShape241', u'nurbsCircleShape242', u'nurbsCircleShape243'], 'proxy': [u'hair_09_CRV_PXY', u'nurbsTessellate17'], 'influences': [u'bind_hair_09_CRV_7_JNT', u'bind_hair_09_CRV_6_JNT', u'bind_hair_09_CRV_5_JNT', u'bind_hair_09_CRV_4_JNT', u'bind_hair_09_CRV_3_JNT', u'bind_hair_09_CRV_2_JNT', u'bind_hair_09_CRV_1_JNT', u'bind_hair_09_CRV_0_JNT'], 'skin': u'skinCluster368', 'ribbon': [u'hair_09_CRV_RIBBON', u'loft34']}, {'circles': [u'makeNurbCircle142', u'makeNurbCircle143', u'makeNurbCircle144', u'makeNurbCircle145', u'makeNurbCircle146', u'makeNurbCircle147', u'makeNurbCircle148', u'makeNurbCircle149'], 'curve': u'hair_10_CRV', 'tube': [u'hair_10_CRV_TUBE', u'loft35'], 'nulls': [u'hair_10_CRV_0_JNT_CIRCLE_JNT', u'hair_10_CRV_1_JNT_CIRCLE_JNT', u'hair_10_CRV_2_JNT_CIRCLE_JNT', u'hair_10_CRV_3_JNT_CIRCLE_JNT', u'hair_10_CRV_4_JNT_CIRCLE_JNT', u'hair_10_CRV_5_JNT_CIRCLE_JNT', u'hair_10_CRV_6_JNT_CIRCLE_JNT', u'hair_10_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape137', u'curveShape138', u'curveShape139', u'curveShape140', u'curveShape141', u'curveShape142', u'curveShape143', u'curveShape144'], 'shapes': [u'nurbsCircleShape244', u'nurbsCircleShape245', u'nurbsCircleShape246', u'nurbsCircleShape247', u'nurbsCircleShape248', u'nurbsCircleShape249', u'nurbsCircleShape250', u'nurbsCircleShape251'], 'proxy': [u'hair_10_CRV_PXY', u'nurbsTessellate18'], 'influences': [u'bind_hair_10_CRV_7_JNT', u'bind_hair_10_CRV_6_JNT', u'bind_hair_10_CRV_5_JNT', u'bind_hair_10_CRV_4_JNT', u'bind_hair_10_CRV_3_JNT', u'bind_hair_10_CRV_2_JNT', u'bind_hair_10_CRV_1_JNT', u'bind_hair_10_CRV_0_JNT'], 'skin': u'skinCluster369', 'ribbon': [u'hair_10_CRV_RIBBON', u'loft36']}, {'circles': [u'makeNurbCircle150', u'makeNurbCircle151', u'makeNurbCircle152', u'makeNurbCircle153', u'makeNurbCircle154', u'makeNurbCircle155', u'makeNurbCircle156', u'makeNurbCircle157'], 'curve': u'hair_11_CRV', 'tube': [u'hair_11_CRV_TUBE', u'loft37'], 'nulls': [u'hair_11_CRV_0_JNT_CIRCLE_JNT', u'hair_11_CRV_1_JNT_CIRCLE_JNT', u'hair_11_CRV_2_JNT_CIRCLE_JNT', u'hair_11_CRV_3_JNT_CIRCLE_JNT', u'hair_11_CRV_4_JNT_CIRCLE_JNT', u'hair_11_CRV_5_JNT_CIRCLE_JNT', u'hair_11_CRV_6_JNT_CIRCLE_JNT', u'hair_11_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape145', u'curveShape146', u'curveShape147', u'curveShape148', u'curveShape149', u'curveShape150', u'curveShape151', u'curveShape152'], 'shapes': [u'nurbsCircleShape252', u'nurbsCircleShape253', u'nurbsCircleShape254', u'nurbsCircleShape255', u'nurbsCircleShape256', u'nurbsCircleShape257', u'nurbsCircleShape258', u'nurbsCircleShape259'], 'proxy': [u'hair_11_CRV_PXY', u'nurbsTessellate19'], 'influences': [u'bind_hair_11_CRV_7_JNT', u'bind_hair_11_CRV_6_JNT', u'bind_hair_11_CRV_5_JNT', u'bind_hair_11_CRV_4_JNT', u'bind_hair_11_CRV_3_JNT', u'bind_hair_11_CRV_2_JNT', u'bind_hair_11_CRV_1_JNT', u'bind_hair_11_CRV_0_JNT'], 'skin': u'skinCluster370', 'ribbon': [u'hair_11_CRV_RIBBON', u'loft38']}, {'circles': [u'makeNurbCircle158', u'makeNurbCircle159', u'makeNurbCircle160', u'makeNurbCircle161', u'makeNurbCircle162', u'makeNurbCircle163', u'makeNurbCircle164', u'makeNurbCircle165'], 'curve': u'hair_12_CRV', 'tube': [u'hair_12_CRV_TUBE', u'loft39'], 'nulls': [u'hair_12_CRV_0_JNT_CIRCLE_JNT', u'hair_12_CRV_1_JNT_CIRCLE_JNT', u'hair_12_CRV_2_JNT_CIRCLE_JNT', u'hair_12_CRV_3_JNT_CIRCLE_JNT', u'hair_12_CRV_4_JNT_CIRCLE_JNT', u'hair_12_CRV_5_JNT_CIRCLE_JNT', u'hair_12_CRV_6_JNT_CIRCLE_JNT', u'hair_12_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape153', u'curveShape154', u'curveShape155', u'curveShape156', u'curveShape157', u'curveShape158', u'curveShape159', u'curveShape160'], 'shapes': [u'nurbsCircleShape260', u'nurbsCircleShape261', u'nurbsCircleShape262', u'nurbsCircleShape263', u'nurbsCircleShape264', u'nurbsCircleShape265', u'nurbsCircleShape266', u'nurbsCircleShape267'], 'proxy': [u'hair_12_CRV_PXY', u'nurbsTessellate20'], 'influences': [u'bind_hair_12_CRV_7_JNT', u'bind_hair_12_CRV_6_JNT', u'bind_hair_12_CRV_5_JNT', u'bind_hair_12_CRV_4_JNT', u'bind_hair_12_CRV_3_JNT', u'bind_hair_12_CRV_2_JNT', u'bind_hair_12_CRV_1_JNT', u'bind_hair_12_CRV_0_JNT'], 'skin': u'skinCluster371', 'ribbon': [u'hair_12_CRV_RIBBON', u'loft40']}, {'circles': [u'makeNurbCircle166', u'makeNurbCircle167', u'makeNurbCircle168', u'makeNurbCircle169', u'makeNurbCircle170', u'makeNurbCircle171', u'makeNurbCircle172', u'makeNurbCircle173'], 'curve': u'hair_13_CRV', 'tube': [u'hair_13_CRV_TUBE', u'loft41'], 'nulls': [u'hair_13_CRV_0_JNT_CIRCLE_JNT', u'hair_13_CRV_1_JNT_CIRCLE_JNT', u'hair_13_CRV_2_JNT_CIRCLE_JNT', u'hair_13_CRV_3_JNT_CIRCLE_JNT', u'hair_13_CRV_4_JNT_CIRCLE_JNT', u'hair_13_CRV_5_JNT_CIRCLE_JNT', u'hair_13_CRV_6_JNT_CIRCLE_JNT', u'hair_13_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape161', u'curveShape162', u'curveShape163', u'curveShape164', u'curveShape165', u'curveShape166', u'curveShape167', u'curveShape168'], 'shapes': [u'nurbsCircleShape268', u'nurbsCircleShape269', u'nurbsCircleShape270', u'nurbsCircleShape271', u'nurbsCircleShape272', u'nurbsCircleShape273', u'nurbsCircleShape274', u'nurbsCircleShape275'], 'proxy': [u'hair_13_CRV_PXY', u'nurbsTessellate21'], 'influences': [u'bind_hair_13_CRV_7_JNT', u'bind_hair_13_CRV_6_JNT', u'bind_hair_13_CRV_5_JNT', u'bind_hair_13_CRV_4_JNT', u'bind_hair_13_CRV_3_JNT', u'bind_hair_13_CRV_2_JNT', u'bind_hair_13_CRV_1_JNT', u'bind_hair_13_CRV_0_JNT'], 'skin': u'skinCluster372', 'ribbon': [u'hair_13_CRV_RIBBON', u'loft42']}, {'circles': [u'makeNurbCircle174', u'makeNurbCircle175', u'makeNurbCircle176', u'makeNurbCircle177', u'makeNurbCircle178', u'makeNurbCircle179', u'makeNurbCircle180', u'makeNurbCircle181'], 'curve': u'hair_14_CRV', 'tube': [u'hair_14_CRV_TUBE', u'loft43'], 'nulls': [u'hair_14_CRV_0_JNT_CIRCLE_JNT', u'hair_14_CRV_1_JNT_CIRCLE_JNT', u'hair_14_CRV_2_JNT_CIRCLE_JNT', u'hair_14_CRV_3_JNT_CIRCLE_JNT', u'hair_14_CRV_4_JNT_CIRCLE_JNT', u'hair_14_CRV_5_JNT_CIRCLE_JNT', u'hair_14_CRV_6_JNT_CIRCLE_JNT', u'hair_14_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape169', u'curveShape170', u'curveShape171', u'curveShape172', u'curveShape173', u'curveShape174', u'curveShape175', u'curveShape176'], 'shapes': [u'nurbsCircleShape276', u'nurbsCircleShape277', u'nurbsCircleShape278', u'nurbsCircleShape279', u'nurbsCircleShape280', u'nurbsCircleShape281', u'nurbsCircleShape282', u'nurbsCircleShape283'], 'proxy': [u'hair_14_CRV_PXY', u'nurbsTessellate22'], 'influences': [u'bind_hair_14_CRV_7_JNT', u'bind_hair_14_CRV_6_JNT', u'bind_hair_14_CRV_5_JNT', u'bind_hair_14_CRV_4_JNT', u'bind_hair_14_CRV_3_JNT', u'bind_hair_14_CRV_2_JNT', u'bind_hair_14_CRV_1_JNT', u'bind_hair_14_CRV_0_JNT'], 'skin': u'skinCluster373', 'ribbon': [u'hair_14_CRV_RIBBON', u'loft44']}, {'circles': [u'makeNurbCircle182', u'makeNurbCircle183', u'makeNurbCircle184', u'makeNurbCircle185', u'makeNurbCircle186', u'makeNurbCircle187', u'makeNurbCircle188', u'makeNurbCircle189'], 'curve': u'hair_15_CRV', 'tube': [u'hair_15_CRV_TUBE', u'loft45'], 'nulls': [u'hair_15_CRV_0_JNT_CIRCLE_JNT', u'hair_15_CRV_1_JNT_CIRCLE_JNT', u'hair_15_CRV_2_JNT_CIRCLE_JNT', u'hair_15_CRV_3_JNT_CIRCLE_JNT', u'hair_15_CRV_4_JNT_CIRCLE_JNT', u'hair_15_CRV_5_JNT_CIRCLE_JNT', u'hair_15_CRV_6_JNT_CIRCLE_JNT', u'hair_15_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape177', u'curveShape178', u'curveShape179', u'curveShape180', u'curveShape181', u'curveShape182', u'curveShape183', u'curveShape184'], 'shapes': [u'nurbsCircleShape284', u'nurbsCircleShape285', u'nurbsCircleShape286', u'nurbsCircleShape287', u'nurbsCircleShape288', u'nurbsCircleShape289', u'nurbsCircleShape290', u'nurbsCircleShape291'], 'proxy': [u'hair_15_CRV_PXY', u'nurbsTessellate23'], 'influences': [u'bind_hair_15_CRV_7_JNT', u'bind_hair_15_CRV_6_JNT', u'bind_hair_15_CRV_5_JNT', u'bind_hair_15_CRV_4_JNT', u'bind_hair_15_CRV_3_JNT', u'bind_hair_15_CRV_2_JNT', u'bind_hair_15_CRV_1_JNT', u'bind_hair_15_CRV_0_JNT'], 'skin': u'skinCluster374', 'ribbon': [u'hair_15_CRV_RIBBON', u'loft46']}, {'circles': [u'makeNurbCircle190', u'makeNurbCircle191', u'makeNurbCircle192', u'makeNurbCircle193', u'makeNurbCircle194', u'makeNurbCircle195', u'makeNurbCircle196', u'makeNurbCircle197'], 'curve': u'hair_16_CRV', 'tube': [u'hair_16_CRV_TUBE', u'loft47'], 'nulls': [u'hair_16_CRV_0_JNT_CIRCLE_JNT', u'hair_16_CRV_1_JNT_CIRCLE_JNT', u'hair_16_CRV_2_JNT_CIRCLE_JNT', u'hair_16_CRV_3_JNT_CIRCLE_JNT', u'hair_16_CRV_4_JNT_CIRCLE_JNT', u'hair_16_CRV_5_JNT_CIRCLE_JNT', u'hair_16_CRV_6_JNT_CIRCLE_JNT', u'hair_16_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape185', u'curveShape186', u'curveShape187', u'curveShape188', u'curveShape189', u'curveShape190', u'curveShape191', u'curveShape192'], 'shapes': [u'nurbsCircleShape292', u'nurbsCircleShape293', u'nurbsCircleShape294', u'nurbsCircleShape295', u'nurbsCircleShape296', u'nurbsCircleShape297', u'nurbsCircleShape298', u'nurbsCircleShape299'], 'proxy': [u'hair_16_CRV_PXY', u'nurbsTessellate24'], 'influences': [u'bind_hair_16_CRV_7_JNT', u'bind_hair_16_CRV_6_JNT', u'bind_hair_16_CRV_5_JNT', u'bind_hair_16_CRV_4_JNT', u'bind_hair_16_CRV_3_JNT', u'bind_hair_16_CRV_2_JNT', u'bind_hair_16_CRV_1_JNT', u'bind_hair_16_CRV_0_JNT'], 'skin': u'skinCluster375', 'ribbon': [u'hair_16_CRV_RIBBON', u'loft48']}, {'circles': [u'makeNurbCircle198', u'makeNurbCircle199', u'makeNurbCircle200', u'makeNurbCircle201', u'makeNurbCircle202', u'makeNurbCircle203', u'makeNurbCircle204', u'makeNurbCircle205'], 'curve': u'hair_17_CRV', 'tube': [u'hair_17_CRV_TUBE', u'loft49'], 'nulls': [u'hair_17_CRV_0_JNT_CIRCLE_JNT', u'hair_17_CRV_1_JNT_CIRCLE_JNT', u'hair_17_CRV_2_JNT_CIRCLE_JNT', u'hair_17_CRV_3_JNT_CIRCLE_JNT', u'hair_17_CRV_4_JNT_CIRCLE_JNT', u'hair_17_CRV_5_JNT_CIRCLE_JNT', u'hair_17_CRV_6_JNT_CIRCLE_JNT', u'hair_17_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape193', u'curveShape194', u'curveShape195', u'curveShape196', u'curveShape197', u'curveShape198', u'curveShape199', u'curveShape200'], 'shapes': [u'nurbsCircleShape300', u'nurbsCircleShape301', u'nurbsCircleShape302', u'nurbsCircleShape303', u'nurbsCircleShape304', u'nurbsCircleShape305', u'nurbsCircleShape306', u'nurbsCircleShape307'], 'proxy': [u'hair_17_CRV_PXY', u'nurbsTessellate25'], 'influences': [u'bind_hair_17_CRV_7_JNT', u'bind_hair_17_CRV_6_JNT', u'bind_hair_17_CRV_5_JNT', u'bind_hair_17_CRV_4_JNT', u'bind_hair_17_CRV_3_JNT', u'bind_hair_17_CRV_2_JNT', u'bind_hair_17_CRV_1_JNT', u'bind_hair_17_CRV_0_JNT'], 'skin': u'skinCluster376', 'ribbon': [u'hair_17_CRV_RIBBON', u'loft50']}, {'circles': [u'makeNurbCircle206', u'makeNurbCircle207', u'makeNurbCircle208', u'makeNurbCircle209', u'makeNurbCircle210', u'makeNurbCircle211', u'makeNurbCircle212', u'makeNurbCircle213'], 'curve': u'hair_18_CRV', 'tube': [u'hair_18_CRV_TUBE', u'loft51'], 'nulls': [u'hair_18_CRV_0_JNT_CIRCLE_JNT', u'hair_18_CRV_1_JNT_CIRCLE_JNT', u'hair_18_CRV_2_JNT_CIRCLE_JNT', u'hair_18_CRV_3_JNT_CIRCLE_JNT', u'hair_18_CRV_4_JNT_CIRCLE_JNT', u'hair_18_CRV_5_JNT_CIRCLE_JNT', u'hair_18_CRV_6_JNT_CIRCLE_JNT', u'hair_18_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape201', u'curveShape202', u'curveShape203', u'curveShape204', u'curveShape205', u'curveShape206', u'curveShape207', u'curveShape208'], 'shapes': [u'nurbsCircleShape308', u'nurbsCircleShape309', u'nurbsCircleShape310', u'nurbsCircleShape311', u'nurbsCircleShape312', u'nurbsCircleShape313', u'nurbsCircleShape314', u'nurbsCircleShape315'], 'proxy': [u'hair_18_CRV_PXY', u'nurbsTessellate26'], 'influences': [u'bind_hair_18_CRV_7_JNT', u'bind_hair_18_CRV_6_JNT', u'bind_hair_18_CRV_5_JNT', u'bind_hair_18_CRV_4_JNT', u'bind_hair_18_CRV_3_JNT', u'bind_hair_18_CRV_2_JNT', u'bind_hair_18_CRV_1_JNT', u'bind_hair_18_CRV_0_JNT'], 'skin': u'skinCluster377', 'ribbon': [u'hair_18_CRV_RIBBON', u'loft52']}, {'circles': [u'makeNurbCircle214', u'makeNurbCircle215', u'makeNurbCircle216', u'makeNurbCircle217', u'makeNurbCircle218', u'makeNurbCircle219', u'makeNurbCircle220', u'makeNurbCircle221'], 'curve': u'hair_19_CRV', 'tube': [u'hair_19_CRV_TUBE', u'loft53'], 'nulls': [u'hair_19_CRV_0_JNT_CIRCLE_JNT', u'hair_19_CRV_1_JNT_CIRCLE_JNT', u'hair_19_CRV_2_JNT_CIRCLE_JNT', u'hair_19_CRV_3_JNT_CIRCLE_JNT', u'hair_19_CRV_4_JNT_CIRCLE_JNT', u'hair_19_CRV_5_JNT_CIRCLE_JNT', u'hair_19_CRV_6_JNT_CIRCLE_JNT', u'hair_19_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape209', u'curveShape210', u'curveShape211', u'curveShape212', u'curveShape213', u'curveShape214', u'curveShape215', u'curveShape216'], 'shapes': [u'nurbsCircleShape316', u'nurbsCircleShape317', u'nurbsCircleShape318', u'nurbsCircleShape319', u'nurbsCircleShape320', u'nurbsCircleShape321', u'nurbsCircleShape322', u'nurbsCircleShape323'], 'proxy': [u'hair_19_CRV_PXY', u'nurbsTessellate27'], 'influences': [u'bind_hair_19_CRV_7_JNT', u'bind_hair_19_CRV_6_JNT', u'bind_hair_19_CRV_5_JNT', u'bind_hair_19_CRV_4_JNT', u'bind_hair_19_CRV_3_JNT', u'bind_hair_19_CRV_2_JNT', u'bind_hair_19_CRV_1_JNT', u'bind_hair_19_CRV_0_JNT'], 'skin': u'skinCluster378', 'ribbon': [u'hair_19_CRV_RIBBON', u'loft54']}, {'circles': [u'makeNurbCircle222', u'makeNurbCircle223', u'makeNurbCircle224', u'makeNurbCircle225', u'makeNurbCircle226', u'makeNurbCircle227', u'makeNurbCircle228', u'makeNurbCircle229'], 'curve': u'hair_20_CRV', 'tube': [u'hair_20_CRV_TUBE', u'loft55'], 'nulls': [u'hair_20_CRV_0_JNT_CIRCLE_JNT', u'hair_20_CRV_1_JNT_CIRCLE_JNT', u'hair_20_CRV_2_JNT_CIRCLE_JNT', u'hair_20_CRV_3_JNT_CIRCLE_JNT', u'hair_20_CRV_4_JNT_CIRCLE_JNT', u'hair_20_CRV_5_JNT_CIRCLE_JNT', u'hair_20_CRV_6_JNT_CIRCLE_JNT', u'hair_20_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape217', u'curveShape218', u'curveShape219', u'curveShape220', u'curveShape221', u'curveShape222', u'curveShape223', u'curveShape224'], 'shapes': [u'nurbsCircleShape324', u'nurbsCircleShape325', u'nurbsCircleShape326', u'nurbsCircleShape327', u'nurbsCircleShape328', u'nurbsCircleShape329', u'nurbsCircleShape330', u'nurbsCircleShape331'], 'proxy': [u'hair_20_CRV_PXY', u'nurbsTessellate28'], 'influences': [u'bind_hair_20_CRV_7_JNT', u'bind_hair_20_CRV_6_JNT', u'bind_hair_20_CRV_5_JNT', u'bind_hair_20_CRV_4_JNT', u'bind_hair_20_CRV_3_JNT', u'bind_hair_20_CRV_2_JNT', u'bind_hair_20_CRV_1_JNT', u'bind_hair_20_CRV_0_JNT'], 'skin': u'skinCluster379', 'ribbon': [u'hair_20_CRV_RIBBON', u'loft56']}, {'circles': [u'makeNurbCircle230', u'makeNurbCircle231', u'makeNurbCircle232', u'makeNurbCircle233', u'makeNurbCircle234', u'makeNurbCircle235', u'makeNurbCircle236', u'makeNurbCircle237'], 'curve': u'hair_21_CRV', 'tube': [u'hair_21_CRV_TUBE', u'loft57'], 'nulls': [u'hair_21_CRV_0_JNT_CIRCLE_JNT', u'hair_21_CRV_1_JNT_CIRCLE_JNT', u'hair_21_CRV_2_JNT_CIRCLE_JNT', u'hair_21_CRV_3_JNT_CIRCLE_JNT', u'hair_21_CRV_4_JNT_CIRCLE_JNT', u'hair_21_CRV_5_JNT_CIRCLE_JNT', u'hair_21_CRV_6_JNT_CIRCLE_JNT', u'hair_21_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape225', u'curveShape226', u'curveShape227', u'curveShape228', u'curveShape229', u'curveShape230', u'curveShape231', u'curveShape232'], 'shapes': [u'nurbsCircleShape332', u'nurbsCircleShape333', u'nurbsCircleShape334', u'nurbsCircleShape335', u'nurbsCircleShape336', u'nurbsCircleShape337', u'nurbsCircleShape338', u'nurbsCircleShape339'], 'proxy': [u'hair_21_CRV_PXY', u'nurbsTessellate29'], 'influences': [u'bind_hair_21_CRV_7_JNT', u'bind_hair_21_CRV_6_JNT', u'bind_hair_21_CRV_5_JNT', u'bind_hair_21_CRV_4_JNT', u'bind_hair_21_CRV_3_JNT', u'bind_hair_21_CRV_2_JNT', u'bind_hair_21_CRV_1_JNT', u'bind_hair_21_CRV_0_JNT'], 'skin': u'skinCluster380', 'ribbon': [u'hair_21_CRV_RIBBON', u'loft58']}, {'circles': [u'makeNurbCircle238', u'makeNurbCircle239', u'makeNurbCircle240', u'makeNurbCircle241', u'makeNurbCircle242', u'makeNurbCircle243', u'makeNurbCircle244', u'makeNurbCircle245'], 'curve': u'hair_22_CRV', 'tube': [u'hair_22_CRV_TUBE', u'loft59'], 'nulls': [u'hair_22_CRV_0_JNT_CIRCLE_JNT', u'hair_22_CRV_1_JNT_CIRCLE_JNT', u'hair_22_CRV_2_JNT_CIRCLE_JNT', u'hair_22_CRV_3_JNT_CIRCLE_JNT', u'hair_22_CRV_4_JNT_CIRCLE_JNT', u'hair_22_CRV_5_JNT_CIRCLE_JNT', u'hair_22_CRV_6_JNT_CIRCLE_JNT', u'hair_22_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape233', u'curveShape234', u'curveShape235', u'curveShape236', u'curveShape237', u'curveShape238', u'curveShape239', u'curveShape240'], 'shapes': [u'nurbsCircleShape340', u'nurbsCircleShape341', u'nurbsCircleShape342', u'nurbsCircleShape343', u'nurbsCircleShape344', u'nurbsCircleShape345', u'nurbsCircleShape346', u'nurbsCircleShape347'], 'proxy': [u'hair_22_CRV_PXY', u'nurbsTessellate30'], 'influences': [u'bind_hair_22_CRV_7_JNT', u'bind_hair_22_CRV_6_JNT', u'bind_hair_22_CRV_5_JNT', u'bind_hair_22_CRV_4_JNT', u'bind_hair_22_CRV_3_JNT', u'bind_hair_22_CRV_2_JNT', u'bind_hair_22_CRV_1_JNT', u'bind_hair_22_CRV_0_JNT'], 'skin': u'skinCluster381', 'ribbon': [u'hair_22_CRV_RIBBON', u'loft60']}, {'circles': [u'makeNurbCircle246', u'makeNurbCircle247', u'makeNurbCircle248', u'makeNurbCircle249', u'makeNurbCircle250', u'makeNurbCircle251', u'makeNurbCircle252', u'makeNurbCircle253'], 'curve': u'hair_23_CRV', 'tube': [u'hair_23_CRV_TUBE', u'loft61'], 'nulls': [u'hair_23_CRV_0_JNT_CIRCLE_JNT', u'hair_23_CRV_1_JNT_CIRCLE_JNT', u'hair_23_CRV_2_JNT_CIRCLE_JNT', u'hair_23_CRV_3_JNT_CIRCLE_JNT', u'hair_23_CRV_4_JNT_CIRCLE_JNT', u'hair_23_CRV_5_JNT_CIRCLE_JNT', u'hair_23_CRV_6_JNT_CIRCLE_JNT', u'hair_23_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape241', u'curveShape242', u'curveShape243', u'curveShape244', u'curveShape245', u'curveShape246', u'curveShape247', u'curveShape248'], 'shapes': [u'nurbsCircleShape348', u'nurbsCircleShape349', u'nurbsCircleShape350', u'nurbsCircleShape351', u'nurbsCircleShape352', u'nurbsCircleShape353', u'nurbsCircleShape354', u'nurbsCircleShape355'], 'proxy': [u'hair_23_CRV_PXY', u'nurbsTessellate31'], 'influences': [u'bind_hair_23_CRV_7_JNT', u'bind_hair_23_CRV_6_JNT', u'bind_hair_23_CRV_5_JNT', u'bind_hair_23_CRV_4_JNT', u'bind_hair_23_CRV_3_JNT', u'bind_hair_23_CRV_2_JNT', u'bind_hair_23_CRV_1_JNT', u'bind_hair_23_CRV_0_JNT'], 'skin': u'skinCluster382', 'ribbon': [u'hair_23_CRV_RIBBON', u'loft62']}, {'circles': [u'makeNurbCircle254', u'makeNurbCircle255', u'makeNurbCircle256', u'makeNurbCircle257', u'makeNurbCircle258', u'makeNurbCircle259', u'makeNurbCircle260', u'makeNurbCircle261'], 'curve': u'hair_24_CRV', 'tube': [u'hair_24_CRV_TUBE', u'loft63'], 'nulls': [u'hair_24_CRV_0_JNT_CIRCLE_JNT', u'hair_24_CRV_1_JNT_CIRCLE_JNT', u'hair_24_CRV_2_JNT_CIRCLE_JNT', u'hair_24_CRV_3_JNT_CIRCLE_JNT', u'hair_24_CRV_4_JNT_CIRCLE_JNT', u'hair_24_CRV_5_JNT_CIRCLE_JNT', u'hair_24_CRV_6_JNT_CIRCLE_JNT', u'hair_24_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape249', u'curveShape250', u'curveShape251', u'curveShape252', u'curveShape253', u'curveShape254', u'curveShape255', u'curveShape256'], 'shapes': [u'nurbsCircleShape356', u'nurbsCircleShape357', u'nurbsCircleShape358', u'nurbsCircleShape359', u'nurbsCircleShape360', u'nurbsCircleShape361', u'nurbsCircleShape362', u'nurbsCircleShape363'], 'proxy': [u'hair_24_CRV_PXY', u'nurbsTessellate32'], 'influences': [u'bind_hair_24_CRV_7_JNT', u'bind_hair_24_CRV_6_JNT', u'bind_hair_24_CRV_5_JNT', u'bind_hair_24_CRV_4_JNT', u'bind_hair_24_CRV_3_JNT', u'bind_hair_24_CRV_2_JNT', u'bind_hair_24_CRV_1_JNT', u'bind_hair_24_CRV_0_JNT'], 'skin': u'skinCluster383', 'ribbon': [u'hair_24_CRV_RIBBON', u'loft64']}, {'circles': [u'makeNurbCircle262', u'makeNurbCircle263', u'makeNurbCircle264', u'makeNurbCircle265', u'makeNurbCircle266', u'makeNurbCircle267', u'makeNurbCircle268', u'makeNurbCircle269'], 'curve': u'hair_25_CRV', 'tube': [u'hair_25_CRV_TUBE', u'loft65'], 'nulls': [u'hair_25_CRV_0_JNT_CIRCLE_JNT', u'hair_25_CRV_1_JNT_CIRCLE_JNT', u'hair_25_CRV_2_JNT_CIRCLE_JNT', u'hair_25_CRV_3_JNT_CIRCLE_JNT', u'hair_25_CRV_4_JNT_CIRCLE_JNT', u'hair_25_CRV_5_JNT_CIRCLE_JNT', u'hair_25_CRV_6_JNT_CIRCLE_JNT', u'hair_25_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape257', u'curveShape258', u'curveShape259', u'curveShape260', u'curveShape261', u'curveShape262', u'curveShape263', u'curveShape264'], 'shapes': [u'nurbsCircleShape364', u'nurbsCircleShape365', u'nurbsCircleShape366', u'nurbsCircleShape367', u'nurbsCircleShape368', u'nurbsCircleShape369', u'nurbsCircleShape370', u'nurbsCircleShape371'], 'proxy': [u'hair_25_CRV_PXY', u'nurbsTessellate33'], 'influences': [u'bind_hair_25_CRV_7_JNT', u'bind_hair_25_CRV_6_JNT', u'bind_hair_25_CRV_5_JNT', u'bind_hair_25_CRV_4_JNT', u'bind_hair_25_CRV_3_JNT', u'bind_hair_25_CRV_2_JNT', u'bind_hair_25_CRV_1_JNT', u'bind_hair_25_CRV_0_JNT'], 'skin': u'skinCluster384', 'ribbon': [u'hair_25_CRV_RIBBON', u'loft66']}, {'circles': [u'makeNurbCircle270', u'makeNurbCircle271', u'makeNurbCircle272', u'makeNurbCircle273', u'makeNurbCircle274', u'makeNurbCircle275', u'makeNurbCircle276', u'makeNurbCircle277'], 'curve': u'hair_26_CRV', 'tube': [u'hair_26_CRV_TUBE', u'loft67'], 'nulls': [u'hair_26_CRV_0_JNT_CIRCLE_JNT', u'hair_26_CRV_1_JNT_CIRCLE_JNT', u'hair_26_CRV_2_JNT_CIRCLE_JNT', u'hair_26_CRV_3_JNT_CIRCLE_JNT', u'hair_26_CRV_4_JNT_CIRCLE_JNT', u'hair_26_CRV_5_JNT_CIRCLE_JNT', u'hair_26_CRV_6_JNT_CIRCLE_JNT', u'hair_26_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape265', u'curveShape266', u'curveShape267', u'curveShape268', u'curveShape269', u'curveShape270', u'curveShape271', u'curveShape272'], 'shapes': [u'nurbsCircleShape372', u'nurbsCircleShape373', u'nurbsCircleShape374', u'nurbsCircleShape375', u'nurbsCircleShape376', u'nurbsCircleShape377', u'nurbsCircleShape378', u'nurbsCircleShape379'], 'proxy': [u'hair_26_CRV_PXY', u'nurbsTessellate34'], 'influences': [u'bind_hair_26_CRV_7_JNT', u'bind_hair_26_CRV_6_JNT', u'bind_hair_26_CRV_5_JNT', u'bind_hair_26_CRV_4_JNT', u'bind_hair_26_CRV_3_JNT', u'bind_hair_26_CRV_2_JNT', u'bind_hair_26_CRV_1_JNT', u'bind_hair_26_CRV_0_JNT'], 'skin': u'skinCluster385', 'ribbon': [u'hair_26_CRV_RIBBON', u'loft68']}, {'circles': [u'makeNurbCircle278', u'makeNurbCircle279', u'makeNurbCircle280', u'makeNurbCircle281', u'makeNurbCircle282', u'makeNurbCircle283', u'makeNurbCircle284', u'makeNurbCircle285'], 'curve': u'hair_27_CRV', 'tube': [u'hair_27_CRV_TUBE', u'loft69'], 'nulls': [u'hair_27_CRV_0_JNT_CIRCLE_JNT', u'hair_27_CRV_1_JNT_CIRCLE_JNT', u'hair_27_CRV_2_JNT_CIRCLE_JNT', u'hair_27_CRV_3_JNT_CIRCLE_JNT', u'hair_27_CRV_4_JNT_CIRCLE_JNT', u'hair_27_CRV_5_JNT_CIRCLE_JNT', u'hair_27_CRV_6_JNT_CIRCLE_JNT', u'hair_27_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape273', u'curveShape274', u'curveShape275', u'curveShape276', u'curveShape277', u'curveShape278', u'curveShape279', u'curveShape280'], 'shapes': [u'nurbsCircleShape380', u'nurbsCircleShape381', u'nurbsCircleShape382', u'nurbsCircleShape383', u'nurbsCircleShape384', u'nurbsCircleShape385', u'nurbsCircleShape386', u'nurbsCircleShape387'], 'proxy': [u'hair_27_CRV_PXY', u'nurbsTessellate35'], 'influences': [u'bind_hair_27_CRV_7_JNT', u'bind_hair_27_CRV_6_JNT', u'bind_hair_27_CRV_5_JNT', u'bind_hair_27_CRV_4_JNT', u'bind_hair_27_CRV_3_JNT', u'bind_hair_27_CRV_2_JNT', u'bind_hair_27_CRV_1_JNT', u'bind_hair_27_CRV_0_JNT'], 'skin': u'skinCluster386', 'ribbon': [u'hair_27_CRV_RIBBON', u'loft70']}, {'circles': [u'makeNurbCircle286', u'makeNurbCircle287', u'makeNurbCircle288', u'makeNurbCircle289', u'makeNurbCircle290', u'makeNurbCircle291', u'makeNurbCircle292', u'makeNurbCircle293'], 'curve': u'hair_28_CRV', 'tube': [u'hair_28_CRV_TUBE', u'loft71'], 'nulls': [u'hair_28_CRV_0_JNT_CIRCLE_JNT', u'hair_28_CRV_1_JNT_CIRCLE_JNT', u'hair_28_CRV_2_JNT_CIRCLE_JNT', u'hair_28_CRV_3_JNT_CIRCLE_JNT', u'hair_28_CRV_4_JNT_CIRCLE_JNT', u'hair_28_CRV_5_JNT_CIRCLE_JNT', u'hair_28_CRV_6_JNT_CIRCLE_JNT', u'hair_28_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape281', u'curveShape282', u'curveShape283', u'curveShape284', u'curveShape285', u'curveShape286', u'curveShape287', u'curveShape288'], 'shapes': [u'nurbsCircleShape388', u'nurbsCircleShape389', u'nurbsCircleShape390', u'nurbsCircleShape391', u'nurbsCircleShape392', u'nurbsCircleShape393', u'nurbsCircleShape394', u'nurbsCircleShape395'], 'proxy': [u'hair_28_CRV_PXY', u'nurbsTessellate36'], 'influences': [u'bind_hair_28_CRV_7_JNT', u'bind_hair_28_CRV_6_JNT', u'bind_hair_28_CRV_5_JNT', u'bind_hair_28_CRV_4_JNT', u'bind_hair_28_CRV_3_JNT', u'bind_hair_28_CRV_2_JNT', u'bind_hair_28_CRV_1_JNT', u'bind_hair_28_CRV_0_JNT'], 'skin': u'skinCluster387', 'ribbon': [u'hair_28_CRV_RIBBON', u'loft72']}, {'circles': [u'makeNurbCircle294', u'makeNurbCircle295', u'makeNurbCircle296', u'makeNurbCircle297', u'makeNurbCircle298', u'makeNurbCircle299', u'makeNurbCircle300', u'makeNurbCircle301'], 'curve': u'hair_29_CRV', 'tube': [u'hair_29_CRV_TUBE', u'loft73'], 'nulls': [u'hair_29_CRV_0_JNT_CIRCLE_JNT', u'hair_29_CRV_1_JNT_CIRCLE_JNT', u'hair_29_CRV_2_JNT_CIRCLE_JNT', u'hair_29_CRV_3_JNT_CIRCLE_JNT', u'hair_29_CRV_4_JNT_CIRCLE_JNT', u'hair_29_CRV_5_JNT_CIRCLE_JNT', u'hair_29_CRV_6_JNT_CIRCLE_JNT', u'hair_29_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape289', u'curveShape290', u'curveShape291', u'curveShape292', u'curveShape293', u'curveShape294', u'curveShape295', u'curveShape296'], 'shapes': [u'nurbsCircleShape396', u'nurbsCircleShape397', u'nurbsCircleShape398', u'nurbsCircleShape399', u'nurbsCircleShape400', u'nurbsCircleShape401', u'nurbsCircleShape402', u'nurbsCircleShape403'], 'proxy': [u'hair_29_CRV_PXY', u'nurbsTessellate37'], 'influences': [u'bind_hair_29_CRV_7_JNT', u'bind_hair_29_CRV_6_JNT', u'bind_hair_29_CRV_5_JNT', u'bind_hair_29_CRV_4_JNT', u'bind_hair_29_CRV_3_JNT', u'bind_hair_29_CRV_2_JNT', u'bind_hair_29_CRV_1_JNT', u'bind_hair_29_CRV_0_JNT'], 'skin': u'skinCluster388', 'ribbon': [u'hair_29_CRV_RIBBON', u'loft74']}, {'circles': [u'makeNurbCircle302', u'makeNurbCircle303', u'makeNurbCircle304', u'makeNurbCircle305', u'makeNurbCircle306', u'makeNurbCircle307', u'makeNurbCircle308', u'makeNurbCircle309'], 'curve': u'hair_30_CRV', 'tube': [u'hair_30_CRV_TUBE', u'loft75'], 'nulls': [u'hair_30_CRV_0_JNT_CIRCLE_JNT', u'hair_30_CRV_1_JNT_CIRCLE_JNT', u'hair_30_CRV_2_JNT_CIRCLE_JNT', u'hair_30_CRV_3_JNT_CIRCLE_JNT', u'hair_30_CRV_4_JNT_CIRCLE_JNT', u'hair_30_CRV_5_JNT_CIRCLE_JNT', u'hair_30_CRV_6_JNT_CIRCLE_JNT', u'hair_30_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape297', u'curveShape298', u'curveShape299', u'curveShape300', u'curveShape301', u'curveShape302', u'curveShape303', u'curveShape304'], 'shapes': [u'nurbsCircleShape404', u'nurbsCircleShape405', u'nurbsCircleShape406', u'nurbsCircleShape407', u'nurbsCircleShape408', u'nurbsCircleShape409', u'nurbsCircleShape410', u'nurbsCircleShape411'], 'proxy': [u'hair_30_CRV_PXY', u'nurbsTessellate38'], 'influences': [u'bind_hair_30_CRV_7_JNT', u'bind_hair_30_CRV_6_JNT', u'bind_hair_30_CRV_5_JNT', u'bind_hair_30_CRV_4_JNT', u'bind_hair_30_CRV_3_JNT', u'bind_hair_30_CRV_2_JNT', u'bind_hair_30_CRV_1_JNT', u'bind_hair_30_CRV_0_JNT'], 'skin': u'skinCluster389', 'ribbon': [u'hair_30_CRV_RIBBON', u'loft76']}, {'circles': [u'makeNurbCircle310', u'makeNurbCircle311', u'makeNurbCircle312', u'makeNurbCircle313', u'makeNurbCircle314', u'makeNurbCircle315', u'makeNurbCircle316', u'makeNurbCircle317'], 'curve': u'hair_31_CRV', 'tube': [u'hair_31_CRV_TUBE', u'loft77'], 'nulls': [u'hair_31_CRV_0_JNT_CIRCLE_JNT', u'hair_31_CRV_1_JNT_CIRCLE_JNT', u'hair_31_CRV_2_JNT_CIRCLE_JNT', u'hair_31_CRV_3_JNT_CIRCLE_JNT', u'hair_31_CRV_4_JNT_CIRCLE_JNT', u'hair_31_CRV_5_JNT_CIRCLE_JNT', u'hair_31_CRV_6_JNT_CIRCLE_JNT', u'hair_31_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape305', u'curveShape306', u'curveShape307', u'curveShape308', u'curveShape309', u'curveShape310', u'curveShape311', u'curveShape312'], 'shapes': [u'nurbsCircleShape412', u'nurbsCircleShape413', u'nurbsCircleShape414', u'nurbsCircleShape415', u'nurbsCircleShape416', u'nurbsCircleShape417', u'nurbsCircleShape418', u'nurbsCircleShape419'], 'proxy': [u'hair_31_CRV_PXY', u'nurbsTessellate39'], 'influences': [u'bind_hair_31_CRV_7_JNT', u'bind_hair_31_CRV_6_JNT', u'bind_hair_31_CRV_5_JNT', u'bind_hair_31_CRV_4_JNT', u'bind_hair_31_CRV_3_JNT', u'bind_hair_31_CRV_2_JNT', u'bind_hair_31_CRV_1_JNT', u'bind_hair_31_CRV_0_JNT'], 'skin': u'skinCluster390', 'ribbon': [u'hair_31_CRV_RIBBON', u'loft78']}, {'circles': [u'makeNurbCircle318', u'makeNurbCircle319', u'makeNurbCircle320', u'makeNurbCircle321', u'makeNurbCircle322', u'makeNurbCircle323', u'makeNurbCircle324', u'makeNurbCircle325'], 'curve': u'hair_32_CRV', 'tube': [u'hair_32_CRV_TUBE', u'loft79'], 'nulls': [u'hair_32_CRV_0_JNT_CIRCLE_JNT', u'hair_32_CRV_1_JNT_CIRCLE_JNT', u'hair_32_CRV_2_JNT_CIRCLE_JNT', u'hair_32_CRV_3_JNT_CIRCLE_JNT', u'hair_32_CRV_4_JNT_CIRCLE_JNT', u'hair_32_CRV_5_JNT_CIRCLE_JNT', u'hair_32_CRV_6_JNT_CIRCLE_JNT', u'hair_32_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape313', u'curveShape314', u'curveShape315', u'curveShape316', u'curveShape317', u'curveShape318', u'curveShape319', u'curveShape320'], 'shapes': [u'nurbsCircleShape420', u'nurbsCircleShape421', u'nurbsCircleShape422', u'nurbsCircleShape423', u'nurbsCircleShape424', u'nurbsCircleShape425', u'nurbsCircleShape426', u'nurbsCircleShape427'], 'proxy': [u'hair_32_CRV_PXY', u'nurbsTessellate40'], 'influences': [u'bind_hair_32_CRV_7_JNT', u'bind_hair_32_CRV_6_JNT', u'bind_hair_32_CRV_5_JNT', u'bind_hair_32_CRV_4_JNT', u'bind_hair_32_CRV_3_JNT', u'bind_hair_32_CRV_2_JNT', u'bind_hair_32_CRV_1_JNT', u'bind_hair_32_CRV_0_JNT'], 'skin': u'skinCluster391', 'ribbon': [u'hair_32_CRV_RIBBON', u'loft80']}, {'circles': [u'makeNurbCircle326', u'makeNurbCircle327', u'makeNurbCircle328', u'makeNurbCircle329', u'makeNurbCircle330', u'makeNurbCircle331', u'makeNurbCircle332', u'makeNurbCircle333'], 'curve': u'hair_34_CRV', 'tube': [u'hair_34_CRV_TUBE', u'loft81'], 'nulls': [u'hair_34_CRV_0_JNT_CIRCLE_JNT', u'hair_34_CRV_1_JNT_CIRCLE_JNT', u'hair_34_CRV_2_JNT_CIRCLE_JNT', u'hair_34_CRV_3_JNT_CIRCLE_JNT', u'hair_34_CRV_4_JNT_CIRCLE_JNT', u'hair_34_CRV_5_JNT_CIRCLE_JNT', u'hair_34_CRV_6_JNT_CIRCLE_JNT', u'hair_34_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape321', u'curveShape322', u'curveShape323', u'curveShape324', u'curveShape325', u'curveShape326', u'curveShape327', u'curveShape328'], 'shapes': [u'nurbsCircleShape428', u'nurbsCircleShape429', u'nurbsCircleShape430', u'nurbsCircleShape431', u'nurbsCircleShape432', u'nurbsCircleShape433', u'nurbsCircleShape434', u'nurbsCircleShape435'], 'proxy': [u'hair_34_CRV_PXY', u'nurbsTessellate41'], 'influences': [u'bind_hair_34_CRV_7_JNT', u'bind_hair_34_CRV_6_JNT', u'bind_hair_34_CRV_5_JNT', u'bind_hair_34_CRV_4_JNT', u'bind_hair_34_CRV_3_JNT', u'bind_hair_34_CRV_2_JNT', u'bind_hair_34_CRV_1_JNT', u'bind_hair_34_CRV_0_JNT'], 'skin': u'skinCluster392', 'ribbon': [u'hair_34_CRV_RIBBON', u'loft82']}, {'circles': [u'makeNurbCircle334', u'makeNurbCircle335', u'makeNurbCircle336', u'makeNurbCircle337', u'makeNurbCircle338', u'makeNurbCircle339', u'makeNurbCircle340', u'makeNurbCircle341'], 'curve': u'hair_35_CRV', 'tube': [u'hair_35_CRV_TUBE', u'loft83'], 'nulls': [u'hair_35_CRV_0_JNT_CIRCLE_JNT', u'hair_35_CRV_1_JNT_CIRCLE_JNT', u'hair_35_CRV_2_JNT_CIRCLE_JNT', u'hair_35_CRV_3_JNT_CIRCLE_JNT', u'hair_35_CRV_4_JNT_CIRCLE_JNT', u'hair_35_CRV_5_JNT_CIRCLE_JNT', u'hair_35_CRV_6_JNT_CIRCLE_JNT', u'hair_35_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape329', u'curveShape330', u'curveShape331', u'curveShape332', u'curveShape333', u'curveShape334', u'curveShape335', u'curveShape336'], 'shapes': [u'nurbsCircleShape436', u'nurbsCircleShape437', u'nurbsCircleShape438', u'nurbsCircleShape439', u'nurbsCircleShape440', u'nurbsCircleShape441', u'nurbsCircleShape442', u'nurbsCircleShape443'], 'proxy': [u'hair_35_CRV_PXY', u'nurbsTessellate42'], 'influences': [u'bind_hair_35_CRV_7_JNT', u'bind_hair_35_CRV_6_JNT', u'bind_hair_35_CRV_5_JNT', u'bind_hair_35_CRV_4_JNT', u'bind_hair_35_CRV_3_JNT', u'bind_hair_35_CRV_2_JNT', u'bind_hair_35_CRV_1_JNT', u'bind_hair_35_CRV_0_JNT'], 'skin': u'skinCluster393', 'ribbon': [u'hair_35_CRV_RIBBON', u'loft84']}, {'circles': [u'makeNurbCircle342', u'makeNurbCircle343', u'makeNurbCircle344', u'makeNurbCircle345', u'makeNurbCircle346', u'makeNurbCircle347', u'makeNurbCircle348', u'makeNurbCircle349'], 'curve': u'hair_36_CRV', 'tube': [u'hair_36_CRV_TUBE', u'loft85'], 'nulls': [u'hair_36_CRV_0_JNT_CIRCLE_JNT', u'hair_36_CRV_1_JNT_CIRCLE_JNT', u'hair_36_CRV_2_JNT_CIRCLE_JNT', u'hair_36_CRV_3_JNT_CIRCLE_JNT', u'hair_36_CRV_4_JNT_CIRCLE_JNT', u'hair_36_CRV_5_JNT_CIRCLE_JNT', u'hair_36_CRV_6_JNT_CIRCLE_JNT', u'hair_36_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape337', u'curveShape338', u'curveShape339', u'curveShape340', u'curveShape341', u'curveShape342', u'curveShape343', u'curveShape344'], 'shapes': [u'nurbsCircleShape444', u'nurbsCircleShape445', u'nurbsCircleShape446', u'nurbsCircleShape447', u'nurbsCircleShape448', u'nurbsCircleShape449', u'nurbsCircleShape450', u'nurbsCircleShape451'], 'proxy': [u'hair_36_CRV_PXY', u'nurbsTessellate43'], 'influences': [u'bind_hair_36_CRV_7_JNT', u'bind_hair_36_CRV_6_JNT', u'bind_hair_36_CRV_5_JNT', u'bind_hair_36_CRV_4_JNT', u'bind_hair_36_CRV_3_JNT', u'bind_hair_36_CRV_2_JNT', u'bind_hair_36_CRV_1_JNT', u'bind_hair_36_CRV_0_JNT'], 'skin': u'skinCluster394', 'ribbon': [u'hair_36_CRV_RIBBON', u'loft86']}, {'circles': [u'makeNurbCircle350', u'makeNurbCircle351', u'makeNurbCircle352', u'makeNurbCircle353', u'makeNurbCircle354', u'makeNurbCircle355', u'makeNurbCircle356', u'makeNurbCircle357'], 'curve': u'hair_37_CRV', 'tube': [u'hair_37_CRV_TUBE', u'loft87'], 'nulls': [u'hair_37_CRV_0_JNT_CIRCLE_JNT', u'hair_37_CRV_1_JNT_CIRCLE_JNT', u'hair_37_CRV_2_JNT_CIRCLE_JNT', u'hair_37_CRV_3_JNT_CIRCLE_JNT', u'hair_37_CRV_4_JNT_CIRCLE_JNT', u'hair_37_CRV_5_JNT_CIRCLE_JNT', u'hair_37_CRV_6_JNT_CIRCLE_JNT', u'hair_37_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape345', u'curveShape346', u'curveShape347', u'curveShape348', u'curveShape349', u'curveShape350', u'curveShape351', u'curveShape352'], 'shapes': [u'nurbsCircleShape452', u'nurbsCircleShape453', u'nurbsCircleShape454', u'nurbsCircleShape455', u'nurbsCircleShape456', u'nurbsCircleShape457', u'nurbsCircleShape458', u'nurbsCircleShape459'], 'proxy': [u'hair_37_CRV_PXY', u'nurbsTessellate44'], 'influences': [u'bind_hair_37_CRV_7_JNT', u'bind_hair_37_CRV_6_JNT', u'bind_hair_37_CRV_5_JNT', u'bind_hair_37_CRV_4_JNT', u'bind_hair_37_CRV_3_JNT', u'bind_hair_37_CRV_2_JNT', u'bind_hair_37_CRV_1_JNT', u'bind_hair_37_CRV_0_JNT'], 'skin': u'skinCluster395', 'ribbon': [u'hair_37_CRV_RIBBON', u'loft88']}, {'circles': [u'makeNurbCircle358', u'makeNurbCircle359', u'makeNurbCircle360', u'makeNurbCircle361', u'makeNurbCircle362', u'makeNurbCircle363', u'makeNurbCircle364', u'makeNurbCircle365'], 'curve': u'hair_38_CRV', 'tube': [u'hair_38_CRV_TUBE', u'loft89'], 'nulls': [u'hair_38_CRV_0_JNT_CIRCLE_JNT', u'hair_38_CRV_1_JNT_CIRCLE_JNT', u'hair_38_CRV_2_JNT_CIRCLE_JNT', u'hair_38_CRV_3_JNT_CIRCLE_JNT', u'hair_38_CRV_4_JNT_CIRCLE_JNT', u'hair_38_CRV_5_JNT_CIRCLE_JNT', u'hair_38_CRV_6_JNT_CIRCLE_JNT', u'hair_38_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape353', u'curveShape354', u'curveShape355', u'curveShape356', u'curveShape357', u'curveShape358', u'curveShape359', u'curveShape360'], 'shapes': [u'nurbsCircleShape460', u'nurbsCircleShape461', u'nurbsCircleShape462', u'nurbsCircleShape463', u'nurbsCircleShape464', u'nurbsCircleShape465', u'nurbsCircleShape466', u'nurbsCircleShape467'], 'proxy': [u'hair_38_CRV_PXY', u'nurbsTessellate45'], 'influences': [u'bind_hair_38_CRV_7_JNT', u'bind_hair_38_CRV_6_JNT', u'bind_hair_38_CRV_5_JNT', u'bind_hair_38_CRV_4_JNT', u'bind_hair_38_CRV_3_JNT', u'bind_hair_38_CRV_2_JNT', u'bind_hair_38_CRV_1_JNT', u'bind_hair_38_CRV_0_JNT'], 'skin': u'skinCluster396', 'ribbon': [u'hair_38_CRV_RIBBON', u'loft90']}, {'circles': [u'makeNurbCircle366', u'makeNurbCircle367', u'makeNurbCircle368', u'makeNurbCircle369', u'makeNurbCircle370', u'makeNurbCircle371', u'makeNurbCircle372', u'makeNurbCircle373'], 'curve': u'hair_39_CRV', 'tube': [u'hair_39_CRV_TUBE', u'loft91'], 'nulls': [u'hair_39_CRV_0_JNT_CIRCLE_JNT', u'hair_39_CRV_1_JNT_CIRCLE_JNT', u'hair_39_CRV_2_JNT_CIRCLE_JNT', u'hair_39_CRV_3_JNT_CIRCLE_JNT', u'hair_39_CRV_4_JNT_CIRCLE_JNT', u'hair_39_CRV_5_JNT_CIRCLE_JNT', u'hair_39_CRV_6_JNT_CIRCLE_JNT', u'hair_39_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape361', u'curveShape362', u'curveShape363', u'curveShape364', u'curveShape365', u'curveShape366', u'curveShape367', u'curveShape368'], 'shapes': [u'nurbsCircleShape468', u'nurbsCircleShape469', u'nurbsCircleShape470', u'nurbsCircleShape471', u'nurbsCircleShape472', u'nurbsCircleShape473', u'nurbsCircleShape474', u'nurbsCircleShape475'], 'proxy': [u'hair_39_CRV_PXY', u'nurbsTessellate46'], 'influences': [u'bind_hair_39_CRV_7_JNT', u'bind_hair_39_CRV_6_JNT', u'bind_hair_39_CRV_5_JNT', u'bind_hair_39_CRV_4_JNT', u'bind_hair_39_CRV_3_JNT', u'bind_hair_39_CRV_2_JNT', u'bind_hair_39_CRV_1_JNT', u'bind_hair_39_CRV_0_JNT'], 'skin': u'skinCluster397', 'ribbon': [u'hair_39_CRV_RIBBON', u'loft92']}, {'circles': [u'makeNurbCircle374', u'makeNurbCircle375', u'makeNurbCircle376', u'makeNurbCircle377', u'makeNurbCircle378', u'makeNurbCircle379', u'makeNurbCircle380', u'makeNurbCircle381'], 'curve': u'hair_40_CRV', 'tube': [u'hair_40_CRV_TUBE', u'loft93'], 'nulls': [u'hair_40_CRV_0_JNT_CIRCLE_JNT', u'hair_40_CRV_1_JNT_CIRCLE_JNT', u'hair_40_CRV_2_JNT_CIRCLE_JNT', u'hair_40_CRV_3_JNT_CIRCLE_JNT', u'hair_40_CRV_4_JNT_CIRCLE_JNT', u'hair_40_CRV_5_JNT_CIRCLE_JNT', u'hair_40_CRV_6_JNT_CIRCLE_JNT', u'hair_40_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape369', u'curveShape370', u'curveShape371', u'curveShape372', u'curveShape373', u'curveShape374', u'curveShape375', u'curveShape376'], 'shapes': [u'nurbsCircleShape476', u'nurbsCircleShape477', u'nurbsCircleShape478', u'nurbsCircleShape479', u'nurbsCircleShape480', u'nurbsCircleShape481', u'nurbsCircleShape482', u'nurbsCircleShape483'], 'proxy': [u'hair_40_CRV_PXY', u'nurbsTessellate47'], 'influences': [u'bind_hair_40_CRV_7_JNT', u'bind_hair_40_CRV_6_JNT', u'bind_hair_40_CRV_5_JNT', u'bind_hair_40_CRV_4_JNT', u'bind_hair_40_CRV_3_JNT', u'bind_hair_40_CRV_2_JNT', u'bind_hair_40_CRV_1_JNT', u'bind_hair_40_CRV_0_JNT'], 'skin': u'skinCluster398', 'ribbon': [u'hair_40_CRV_RIBBON', u'loft94']}, {'circles': [u'makeNurbCircle382', u'makeNurbCircle383', u'makeNurbCircle384', u'makeNurbCircle385', u'makeNurbCircle386', u'makeNurbCircle387', u'makeNurbCircle388', u'makeNurbCircle389'], 'curve': u'hair_41_CRV', 'tube': [u'hair_41_CRV_TUBE', u'loft95'], 'nulls': [u'hair_41_CRV_0_JNT_CIRCLE_JNT', u'hair_41_CRV_1_JNT_CIRCLE_JNT', u'hair_41_CRV_2_JNT_CIRCLE_JNT', u'hair_41_CRV_3_JNT_CIRCLE_JNT', u'hair_41_CRV_4_JNT_CIRCLE_JNT', u'hair_41_CRV_5_JNT_CIRCLE_JNT', u'hair_41_CRV_6_JNT_CIRCLE_JNT', u'hair_41_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape377', u'curveShape378', u'curveShape379', u'curveShape380', u'curveShape381', u'curveShape382', u'curveShape383', u'curveShape384'], 'shapes': [u'nurbsCircleShape484', u'nurbsCircleShape485', u'nurbsCircleShape486', u'nurbsCircleShape487', u'nurbsCircleShape488', u'nurbsCircleShape489', u'nurbsCircleShape490', u'nurbsCircleShape491'], 'proxy': [u'hair_41_CRV_PXY', u'nurbsTessellate48'], 'influences': [u'bind_hair_41_CRV_7_JNT', u'bind_hair_41_CRV_6_JNT', u'bind_hair_41_CRV_5_JNT', u'bind_hair_41_CRV_4_JNT', u'bind_hair_41_CRV_3_JNT', u'bind_hair_41_CRV_2_JNT', u'bind_hair_41_CRV_1_JNT', u'bind_hair_41_CRV_0_JNT'], 'skin': u'skinCluster399', 'ribbon': [u'hair_41_CRV_RIBBON', u'loft96']}, {'circles': [u'makeNurbCircle390', u'makeNurbCircle391', u'makeNurbCircle392', u'makeNurbCircle393', u'makeNurbCircle394', u'makeNurbCircle395', u'makeNurbCircle396', u'makeNurbCircle397'], 'curve': u'hair_42_CRV', 'tube': [u'hair_42_CRV_TUBE', u'loft97'], 'nulls': [u'hair_42_CRV_0_JNT_CIRCLE_JNT', u'hair_42_CRV_1_JNT_CIRCLE_JNT', u'hair_42_CRV_2_JNT_CIRCLE_JNT', u'hair_42_CRV_3_JNT_CIRCLE_JNT', u'hair_42_CRV_4_JNT_CIRCLE_JNT', u'hair_42_CRV_5_JNT_CIRCLE_JNT', u'hair_42_CRV_6_JNT_CIRCLE_JNT', u'hair_42_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape385', u'curveShape386', u'curveShape387', u'curveShape388', u'curveShape389', u'curveShape390', u'curveShape391', u'curveShape392'], 'shapes': [u'nurbsCircleShape492', u'nurbsCircleShape493', u'nurbsCircleShape494', u'nurbsCircleShape495', u'nurbsCircleShape496', u'nurbsCircleShape497', u'nurbsCircleShape498', u'nurbsCircleShape499'], 'proxy': [u'hair_42_CRV_PXY', u'nurbsTessellate49'], 'influences': [u'bind_hair_42_CRV_7_JNT', u'bind_hair_42_CRV_6_JNT', u'bind_hair_42_CRV_5_JNT', u'bind_hair_42_CRV_4_JNT', u'bind_hair_42_CRV_3_JNT', u'bind_hair_42_CRV_2_JNT', u'bind_hair_42_CRV_1_JNT', u'bind_hair_42_CRV_0_JNT'], 'skin': u'skinCluster400', 'ribbon': [u'hair_42_CRV_RIBBON', u'loft98']}, {'circles': [u'makeNurbCircle398', u'makeNurbCircle399', u'makeNurbCircle400', u'makeNurbCircle401', u'makeNurbCircle402', u'makeNurbCircle403', u'makeNurbCircle404', u'makeNurbCircle405'], 'curve': u'hair_43_CRV', 'tube': [u'hair_43_CRV_TUBE', u'loft99'], 'nulls': [u'hair_43_CRV_0_JNT_CIRCLE_JNT', u'hair_43_CRV_1_JNT_CIRCLE_JNT', u'hair_43_CRV_2_JNT_CIRCLE_JNT', u'hair_43_CRV_3_JNT_CIRCLE_JNT', u'hair_43_CRV_4_JNT_CIRCLE_JNT', u'hair_43_CRV_5_JNT_CIRCLE_JNT', u'hair_43_CRV_6_JNT_CIRCLE_JNT', u'hair_43_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape393', u'curveShape394', u'curveShape395', u'curveShape396', u'curveShape397', u'curveShape398', u'curveShape399', u'curveShape400'], 'shapes': [u'nurbsCircleShape500', u'nurbsCircleShape501', u'nurbsCircleShape502', u'nurbsCircleShape503', u'nurbsCircleShape504', u'nurbsCircleShape505', u'nurbsCircleShape506', u'nurbsCircleShape507'], 'proxy': [u'hair_43_CRV_PXY', u'nurbsTessellate50'], 'influences': [u'bind_hair_43_CRV_7_JNT', u'bind_hair_43_CRV_6_JNT', u'bind_hair_43_CRV_5_JNT', u'bind_hair_43_CRV_4_JNT', u'bind_hair_43_CRV_3_JNT', u'bind_hair_43_CRV_2_JNT', u'bind_hair_43_CRV_1_JNT', u'bind_hair_43_CRV_0_JNT'], 'skin': u'skinCluster401', 'ribbon': [u'hair_43_CRV_RIBBON', u'loft100']}, {'circles': [u'makeNurbCircle406', u'makeNurbCircle407', u'makeNurbCircle408', u'makeNurbCircle409', u'makeNurbCircle410', u'makeNurbCircle411', u'makeNurbCircle412', u'makeNurbCircle413'], 'curve': u'hair_44_CRV', 'tube': [u'hair_44_CRV_TUBE', u'loft101'], 'nulls': [u'hair_44_CRV_0_JNT_CIRCLE_JNT', u'hair_44_CRV_1_JNT_CIRCLE_JNT', u'hair_44_CRV_2_JNT_CIRCLE_JNT', u'hair_44_CRV_3_JNT_CIRCLE_JNT', u'hair_44_CRV_4_JNT_CIRCLE_JNT', u'hair_44_CRV_5_JNT_CIRCLE_JNT', u'hair_44_CRV_6_JNT_CIRCLE_JNT', u'hair_44_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape401', u'curveShape402', u'curveShape403', u'curveShape404', u'curveShape405', u'curveShape406', u'curveShape407', u'curveShape408'], 'shapes': [u'nurbsCircleShape508', u'nurbsCircleShape509', u'nurbsCircleShape510', u'nurbsCircleShape511', u'nurbsCircleShape512', u'nurbsCircleShape513', u'nurbsCircleShape514', u'nurbsCircleShape515'], 'proxy': [u'hair_44_CRV_PXY', u'nurbsTessellate51'], 'influences': [u'bind_hair_44_CRV_7_JNT', u'bind_hair_44_CRV_6_JNT', u'bind_hair_44_CRV_5_JNT', u'bind_hair_44_CRV_4_JNT', u'bind_hair_44_CRV_3_JNT', u'bind_hair_44_CRV_2_JNT', u'bind_hair_44_CRV_1_JNT', u'bind_hair_44_CRV_0_JNT'], 'skin': u'skinCluster402', 'ribbon': [u'hair_44_CRV_RIBBON', u'loft102']}, {'circles': [u'makeNurbCircle414', u'makeNurbCircle415', u'makeNurbCircle416', u'makeNurbCircle417', u'makeNurbCircle418', u'makeNurbCircle419', u'makeNurbCircle420', u'makeNurbCircle421'], 'curve': u'hair_45_CRV', 'tube': [u'hair_45_CRV_TUBE', u'loft103'], 'nulls': [u'hair_45_CRV_0_JNT_CIRCLE_JNT', u'hair_45_CRV_1_JNT_CIRCLE_JNT', u'hair_45_CRV_2_JNT_CIRCLE_JNT', u'hair_45_CRV_3_JNT_CIRCLE_JNT', u'hair_45_CRV_4_JNT_CIRCLE_JNT', u'hair_45_CRV_5_JNT_CIRCLE_JNT', u'hair_45_CRV_6_JNT_CIRCLE_JNT', u'hair_45_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape409', u'curveShape410', u'curveShape411', u'curveShape412', u'curveShape413', u'curveShape414', u'curveShape415', u'curveShape416'], 'shapes': [u'nurbsCircleShape516', u'nurbsCircleShape517', u'nurbsCircleShape518', u'nurbsCircleShape519', u'nurbsCircleShape520', u'nurbsCircleShape521', u'nurbsCircleShape522', u'nurbsCircleShape523'], 'proxy': [u'hair_45_CRV_PXY', u'nurbsTessellate52'], 'influences': [u'bind_hair_45_CRV_7_JNT', u'bind_hair_45_CRV_6_JNT', u'bind_hair_45_CRV_5_JNT', u'bind_hair_45_CRV_4_JNT', u'bind_hair_45_CRV_3_JNT', u'bind_hair_45_CRV_2_JNT', u'bind_hair_45_CRV_1_JNT', u'bind_hair_45_CRV_0_JNT'], 'skin': u'skinCluster403', 'ribbon': [u'hair_45_CRV_RIBBON', u'loft104']}, {'circles': [u'makeNurbCircle422', u'makeNurbCircle423', u'makeNurbCircle424', u'makeNurbCircle425', u'makeNurbCircle426', u'makeNurbCircle427', u'makeNurbCircle428', u'makeNurbCircle429'], 'curve': u'hair_46_CRV', 'tube': [u'hair_46_CRV_TUBE', u'loft105'], 'nulls': [u'hair_46_CRV_0_JNT_CIRCLE_JNT', u'hair_46_CRV_1_JNT_CIRCLE_JNT', u'hair_46_CRV_2_JNT_CIRCLE_JNT', u'hair_46_CRV_3_JNT_CIRCLE_JNT', u'hair_46_CRV_4_JNT_CIRCLE_JNT', u'hair_46_CRV_5_JNT_CIRCLE_JNT', u'hair_46_CRV_6_JNT_CIRCLE_JNT', u'hair_46_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape417', u'curveShape418', u'curveShape419', u'curveShape420', u'curveShape421', u'curveShape422', u'curveShape423', u'curveShape424'], 'shapes': [u'nurbsCircleShape524', u'nurbsCircleShape525', u'nurbsCircleShape526', u'nurbsCircleShape527', u'nurbsCircleShape528', u'nurbsCircleShape529', u'nurbsCircleShape530', u'nurbsCircleShape531'], 'proxy': [u'hair_46_CRV_PXY', u'nurbsTessellate53'], 'influences': [u'bind_hair_46_CRV_7_JNT', u'bind_hair_46_CRV_6_JNT', u'bind_hair_46_CRV_5_JNT', u'bind_hair_46_CRV_4_JNT', u'bind_hair_46_CRV_3_JNT', u'bind_hair_46_CRV_2_JNT', u'bind_hair_46_CRV_1_JNT', u'bind_hair_46_CRV_0_JNT'], 'skin': u'skinCluster404', 'ribbon': [u'hair_46_CRV_RIBBON', u'loft106']}, {'circles': [u'makeNurbCircle430', u'makeNurbCircle431', u'makeNurbCircle432', u'makeNurbCircle433', u'makeNurbCircle434', u'makeNurbCircle435', u'makeNurbCircle436', u'makeNurbCircle437'], 'curve': u'hair_47_CRV', 'tube': [u'hair_47_CRV_TUBE', u'loft107'], 'nulls': [u'hair_47_CRV_0_JNT_CIRCLE_JNT', u'hair_47_CRV_1_JNT_CIRCLE_JNT', u'hair_47_CRV_2_JNT_CIRCLE_JNT', u'hair_47_CRV_3_JNT_CIRCLE_JNT', u'hair_47_CRV_4_JNT_CIRCLE_JNT', u'hair_47_CRV_5_JNT_CIRCLE_JNT', u'hair_47_CRV_6_JNT_CIRCLE_JNT', u'hair_47_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape425', u'curveShape426', u'curveShape427', u'curveShape428', u'curveShape429', u'curveShape430', u'curveShape431', u'curveShape432'], 'shapes': [u'nurbsCircleShape532', u'nurbsCircleShape533', u'nurbsCircleShape534', u'nurbsCircleShape535', u'nurbsCircleShape536', u'nurbsCircleShape537', u'nurbsCircleShape538', u'nurbsCircleShape539'], 'proxy': [u'hair_47_CRV_PXY', u'nurbsTessellate54'], 'influences': [u'bind_hair_47_CRV_7_JNT', u'bind_hair_47_CRV_6_JNT', u'bind_hair_47_CRV_5_JNT', u'bind_hair_47_CRV_4_JNT', u'bind_hair_47_CRV_3_JNT', u'bind_hair_47_CRV_2_JNT', u'bind_hair_47_CRV_1_JNT', u'bind_hair_47_CRV_0_JNT'], 'skin': u'skinCluster405', 'ribbon': [u'hair_47_CRV_RIBBON', u'loft108']}, {'circles': [u'makeNurbCircle438', u'makeNurbCircle439', u'makeNurbCircle440', u'makeNurbCircle441', u'makeNurbCircle442', u'makeNurbCircle443', u'makeNurbCircle444', u'makeNurbCircle445'], 'curve': u'hair_33_CRV', 'tube': [u'hair_33_CRV_TUBE', u'loft109'], 'nulls': [u'hair_33_CRV_0_JNT_CIRCLE_JNT', u'hair_33_CRV_1_JNT_CIRCLE_JNT', u'hair_33_CRV_2_JNT_CIRCLE_JNT', u'hair_33_CRV_3_JNT_CIRCLE_JNT', u'hair_33_CRV_4_JNT_CIRCLE_JNT', u'hair_33_CRV_5_JNT_CIRCLE_JNT', u'hair_33_CRV_6_JNT_CIRCLE_JNT', u'hair_33_CRV_7_JNT_CIRCLE_JNT'], 'lines': [u'curveShape433', u'curveShape434', u'curveShape435', u'curveShape436', u'curveShape437', u'curveShape438', u'curveShape439', u'curveShape440'], 'shapes': [u'nurbsCircleShape540', u'nurbsCircleShape541', u'nurbsCircleShape542', u'nurbsCircleShape543', u'nurbsCircleShape544', u'nurbsCircleShape545', u'nurbsCircleShape546', u'nurbsCircleShape547'], 'proxy': [u'hair_33_CRV_PXY', u'nurbsTessellate55'], 'influences': [u'bind_hair_33_CRV_7_JNT', u'bind_hair_33_CRV_6_JNT', u'bind_hair_33_CRV_5_JNT', u'bind_hair_33_CRV_4_JNT', u'bind_hair_33_CRV_3_JNT', u'bind_hair_33_CRV_2_JNT', u'bind_hair_33_CRV_1_JNT', u'bind_hair_33_CRV_0_JNT'], 'skin': u'skinCluster406', 'ribbon': [u'hair_33_CRV_RIBBON', u'loft110']}]

******************
[{'circles': [u'makeNurbCircle287', u'makeNurbCircle288', u'makeNurbCircle289', u'makeNurbCircle290', u'makeNurbCircle291'], 'curve': u'hair_00_CRV', 'tube': [u'hair_00_CRV_TUBE', u'loft1'], 'nulls': [u'hair_00_CRV_0_JNT_CIRCLE_JNT', u'hair_00_CRV_1_JNT_CIRCLE_JNT', u'hair_00_CRV_2_JNT_CIRCLE_JNT', u'hair_00_CRV_3_JNT_CIRCLE_JNT', u'hair_00_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape1', u'curveShape2', u'curveShape3', u'curveShape4', u'curveShape5'], 'shapes': [u'nurbsCircleShape440', u'nurbsCircleShape441', u'nurbsCircleShape442', u'nurbsCircleShape443', u'nurbsCircleShape444'], 'proxy': [u'hair_00_CRV_PXY', u'nurbsTessellate1'], 'influences': [u'bind_hair_00_CRV_4_JNT', u'bind_hair_00_CRV_3_JNT', u'bind_hair_00_CRV_2_JNT', u'bind_hair_00_CRV_1_JNT', u'bind_hair_00_CRV_0_JNT'], 'skin': u'skinCluster58', 'ribbon': [u'hair_00_CRV_RIBBON', u'loft2']}, {'circles': [u'makeNurbCircle292', u'makeNurbCircle293', u'makeNurbCircle294', u'makeNurbCircle295', u'makeNurbCircle296'], 'curve': u'hair_01_CRV', 'tube': [u'hair_01_CRV_TUBE', u'loft3'], 'nulls': [u'hair_01_CRV_0_JNT_CIRCLE_JNT', u'hair_01_CRV_1_JNT_CIRCLE_JNT', u'hair_01_CRV_2_JNT_CIRCLE_JNT', u'hair_01_CRV_3_JNT_CIRCLE_JNT', u'hair_01_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape6', u'curveShape7', u'curveShape8', u'curveShape9', u'curveShape10'], 'shapes': [u'nurbsCircleShape445', u'nurbsCircleShape446', u'nurbsCircleShape447', u'nurbsCircleShape448', u'nurbsCircleShape449'], 'proxy': [u'hair_01_CRV_PXY', u'nurbsTessellate2'], 'influences': [u'bind_hair_01_CRV_4_JNT', u'bind_hair_01_CRV_3_JNT', u'bind_hair_01_CRV_2_JNT', u'bind_hair_01_CRV_1_JNT', u'bind_hair_01_CRV_0_JNT'], 'skin': u'skinCluster59', 'ribbon': [u'hair_01_CRV_RIBBON', u'loft4']}, {'circles': [u'makeNurbCircle297', u'makeNurbCircle298', u'makeNurbCircle299', u'makeNurbCircle300', u'makeNurbCircle301'], 'curve': u'hair_02_CRV', 'tube': [u'hair_02_CRV_TUBE', u'loft5'], 'nulls': [u'hair_02_CRV_0_JNT_CIRCLE_JNT', u'hair_02_CRV_1_JNT_CIRCLE_JNT', u'hair_02_CRV_2_JNT_CIRCLE_JNT', u'hair_02_CRV_3_JNT_CIRCLE_JNT', u'hair_02_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape11', u'curveShape12', u'curveShape13', u'curveShape14', u'curveShape15'], 'shapes': [u'nurbsCircleShape450', u'nurbsCircleShape451', u'nurbsCircleShape452', u'nurbsCircleShape453', u'nurbsCircleShape454'], 'proxy': [u'hair_02_CRV_PXY', u'nurbsTessellate3'], 'influences': [u'bind_hair_02_CRV_4_JNT', u'bind_hair_02_CRV_3_JNT', u'bind_hair_02_CRV_2_JNT', u'bind_hair_02_CRV_1_JNT', u'bind_hair_02_CRV_0_JNT'], 'skin': u'skinCluster60', 'ribbon': [u'hair_02_CRV_RIBBON', u'loft6']}, {'circles': [u'makeNurbCircle302', u'makeNurbCircle303', u'makeNurbCircle304', u'makeNurbCircle305', u'makeNurbCircle306'], 'curve': u'hair_03_CRV', 'tube': [u'hair_03_CRV_TUBE', u'loft7'], 'nulls': [u'hair_03_CRV_0_JNT_CIRCLE_JNT', u'hair_03_CRV_1_JNT_CIRCLE_JNT', u'hair_03_CRV_2_JNT_CIRCLE_JNT', u'hair_03_CRV_3_JNT_CIRCLE_JNT', u'hair_03_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape16', u'curveShape17', u'curveShape18', u'curveShape19', u'curveShape20'], 'shapes': [u'nurbsCircleShape455', u'nurbsCircleShape456', u'nurbsCircleShape457', u'nurbsCircleShape458', u'nurbsCircleShape459'], 'proxy': [u'hair_03_CRV_PXY', u'nurbsTessellate4'], 'influences': [u'bind_hair_03_CRV_4_JNT', u'bind_hair_03_CRV_3_JNT', u'bind_hair_03_CRV_2_JNT', u'bind_hair_03_CRV_1_JNT', u'bind_hair_03_CRV_0_JNT'], 'skin': u'skinCluster61', 'ribbon': [u'hair_03_CRV_RIBBON', u'loft8']}, {'circles': [u'makeNurbCircle307', u'makeNurbCircle308', u'makeNurbCircle309', u'makeNurbCircle310', u'makeNurbCircle311'], 'curve': u'hair_04_CRV', 'tube': [u'hair_04_CRV_TUBE', u'loft9'], 'nulls': [u'hair_04_CRV_0_JNT_CIRCLE_JNT', u'hair_04_CRV_1_JNT_CIRCLE_JNT', u'hair_04_CRV_2_JNT_CIRCLE_JNT', u'hair_04_CRV_3_JNT_CIRCLE_JNT', u'hair_04_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape21', u'curveShape22', u'curveShape23', u'curveShape24', u'curveShape25'], 'shapes': [u'nurbsCircleShape460', u'nurbsCircleShape461', u'nurbsCircleShape462', u'nurbsCircleShape463', u'nurbsCircleShape464'], 'proxy': [u'hair_04_CRV_PXY', u'nurbsTessellate5'], 'influences': [u'bind_hair_04_CRV_4_JNT', u'bind_hair_04_CRV_3_JNT', u'bind_hair_04_CRV_2_JNT', u'bind_hair_04_CRV_1_JNT', u'bind_hair_04_CRV_0_JNT'], 'skin': u'skinCluster62', 'ribbon': [u'hair_04_CRV_RIBBON', u'loft10']}, {'circles': [u'makeNurbCircle312', u'makeNurbCircle313', u'makeNurbCircle314', u'makeNurbCircle315', u'makeNurbCircle316'], 'curve': u'hair_05_CRV', 'tube': [u'hair_05_CRV_TUBE', u'loft11'], 'nulls': [u'hair_05_CRV_0_JNT_CIRCLE_JNT', u'hair_05_CRV_1_JNT_CIRCLE_JNT', u'hair_05_CRV_2_JNT_CIRCLE_JNT', u'hair_05_CRV_3_JNT_CIRCLE_JNT', u'hair_05_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape26', u'curveShape27', u'curveShape28', u'curveShape29', u'curveShape30'], 'shapes': [u'nurbsCircleShape465', u'nurbsCircleShape466', u'nurbsCircleShape467', u'nurbsCircleShape468', u'nurbsCircleShape469'], 'proxy': [u'hair_05_CRV_PXY', u'nurbsTessellate6'], 'influences': [u'bind_hair_05_CRV_4_JNT', u'bind_hair_05_CRV_3_JNT', u'bind_hair_05_CRV_2_JNT', u'bind_hair_05_CRV_1_JNT', u'bind_hair_05_CRV_0_JNT'], 'skin': u'skinCluster63', 'ribbon': [u'hair_05_CRV_RIBBON', u'loft12']}, {'circles': [u'makeNurbCircle317', u'makeNurbCircle318', u'makeNurbCircle319', u'makeNurbCircle320', u'makeNurbCircle321'], 'curve': u'hair_06_CRV', 'tube': [u'hair_06_CRV_TUBE', u'loft13'], 'nulls': [u'hair_06_CRV_0_JNT_CIRCLE_JNT', u'hair_06_CRV_1_JNT_CIRCLE_JNT', u'hair_06_CRV_2_JNT_CIRCLE_JNT', u'hair_06_CRV_3_JNT_CIRCLE_JNT', u'hair_06_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape31', u'curveShape32', u'curveShape33', u'curveShape34', u'curveShape35'], 'shapes': [u'nurbsCircleShape470', u'nurbsCircleShape471', u'nurbsCircleShape472', u'nurbsCircleShape473', u'nurbsCircleShape474'], 'proxy': [u'hair_06_CRV_PXY', u'nurbsTessellate7'], 'influences': [u'bind_hair_06_CRV_4_JNT', u'bind_hair_06_CRV_3_JNT', u'bind_hair_06_CRV_2_JNT', u'bind_hair_06_CRV_1_JNT', u'bind_hair_06_CRV_0_JNT'], 'skin': u'skinCluster64', 'ribbon': [u'hair_06_CRV_RIBBON', u'loft14']}, {'circles': [u'makeNurbCircle322', u'makeNurbCircle323', u'makeNurbCircle324', u'makeNurbCircle325', u'makeNurbCircle326'], 'curve': u'hair_07_CRV', 'tube': [u'hair_07_CRV_TUBE', u'loft15'], 'nulls': [u'hair_07_CRV_0_JNT_CIRCLE_JNT', u'hair_07_CRV_1_JNT_CIRCLE_JNT', u'hair_07_CRV_2_JNT_CIRCLE_JNT', u'hair_07_CRV_3_JNT_CIRCLE_JNT', u'hair_07_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape36', u'curveShape37', u'curveShape38', u'curveShape39', u'curveShape40'], 'shapes': [u'nurbsCircleShape475', u'nurbsCircleShape476', u'nurbsCircleShape477', u'nurbsCircleShape478', u'nurbsCircleShape479'], 'proxy': [u'hair_07_CRV_PXY', u'nurbsTessellate8'], 'influences': [u'bind_hair_07_CRV_4_JNT', u'bind_hair_07_CRV_3_JNT', u'bind_hair_07_CRV_2_JNT', u'bind_hair_07_CRV_1_JNT', u'bind_hair_07_CRV_0_JNT'], 'skin': u'skinCluster65', 'ribbon': [u'hair_07_CRV_RIBBON', u'loft16']}, {'circles': [u'makeNurbCircle327', u'makeNurbCircle328', u'makeNurbCircle329', u'makeNurbCircle330', u'makeNurbCircle331'], 'curve': u'hair_08_CRV', 'tube': [u'hair_08_CRV_TUBE', u'loft17'], 'nulls': [u'hair_08_CRV_0_JNT_CIRCLE_JNT', u'hair_08_CRV_1_JNT_CIRCLE_JNT', u'hair_08_CRV_2_JNT_CIRCLE_JNT', u'hair_08_CRV_3_JNT_CIRCLE_JNT', u'hair_08_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape41', u'curveShape42', u'curveShape43', u'curveShape44', u'curveShape45'], 'shapes': [u'nurbsCircleShape480', u'nurbsCircleShape481', u'nurbsCircleShape482', u'nurbsCircleShape483', u'nurbsCircleShape484'], 'proxy': [u'hair_08_CRV_PXY', u'nurbsTessellate9'], 'influences': [u'bind_hair_08_CRV_4_JNT', u'bind_hair_08_CRV_3_JNT', u'bind_hair_08_CRV_2_JNT', u'bind_hair_08_CRV_1_JNT', u'bind_hair_08_CRV_0_JNT'], 'skin': u'skinCluster66', 'ribbon': [u'hair_08_CRV_RIBBON', u'loft18']}, {'circles': [u'makeNurbCircle332', u'makeNurbCircle333', u'makeNurbCircle334', u'makeNurbCircle335', u'makeNurbCircle336'], 'curve': u'hair_09_CRV', 'tube': [u'hair_09_CRV_TUBE', u'loft19'], 'nulls': [u'hair_09_CRV_0_JNT_CIRCLE_JNT', u'hair_09_CRV_1_JNT_CIRCLE_JNT', u'hair_09_CRV_2_JNT_CIRCLE_JNT', u'hair_09_CRV_3_JNT_CIRCLE_JNT', u'hair_09_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape46', u'curveShape47', u'curveShape48', u'curveShape49', u'curveShape50'], 'shapes': [u'nurbsCircleShape485', u'nurbsCircleShape486', u'nurbsCircleShape487', u'nurbsCircleShape488', u'nurbsCircleShape489'], 'proxy': [u'hair_09_CRV_PXY', u'nurbsTessellate10'], 'influences': [u'bind_hair_09_CRV_4_JNT', u'bind_hair_09_CRV_3_JNT', u'bind_hair_09_CRV_2_JNT', u'bind_hair_09_CRV_1_JNT', u'bind_hair_09_CRV_0_JNT'], 'skin': u'skinCluster67', 'ribbon': [u'hair_09_CRV_RIBBON', u'loft20']}, {'circles': [u'makeNurbCircle337', u'makeNurbCircle338', u'makeNurbCircle339', u'makeNurbCircle340', u'makeNurbCircle341'], 'curve': u'hair_10_CRV', 'tube': [u'hair_10_CRV_TUBE', u'loft21'], 'nulls': [u'hair_10_CRV_0_JNT_CIRCLE_JNT', u'hair_10_CRV_1_JNT_CIRCLE_JNT', u'hair_10_CRV_2_JNT_CIRCLE_JNT', u'hair_10_CRV_3_JNT_CIRCLE_JNT', u'hair_10_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape51', u'curveShape52', u'curveShape53', u'curveShape54', u'curveShape55'], 'shapes': [u'nurbsCircleShape490', u'nurbsCircleShape491', u'nurbsCircleShape492', u'nurbsCircleShape493', u'nurbsCircleShape494'], 'proxy': [u'hair_10_CRV_PXY', u'nurbsTessellate11'], 'influences': [u'bind_hair_10_CRV_4_JNT', u'bind_hair_10_CRV_3_JNT', u'bind_hair_10_CRV_2_JNT', u'bind_hair_10_CRV_1_JNT', u'bind_hair_10_CRV_0_JNT'], 'skin': u'skinCluster68', 'ribbon': [u'hair_10_CRV_RIBBON', u'loft22']}, {'circles': [u'makeNurbCircle342', u'makeNurbCircle343', u'makeNurbCircle344', u'makeNurbCircle345', u'makeNurbCircle346'], 'curve': u'hair_11_CRV', 'tube': [u'hair_11_CRV_TUBE', u'loft23'], 'nulls': [u'hair_11_CRV_0_JNT_CIRCLE_JNT', u'hair_11_CRV_1_JNT_CIRCLE_JNT', u'hair_11_CRV_2_JNT_CIRCLE_JNT', u'hair_11_CRV_3_JNT_CIRCLE_JNT', u'hair_11_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape56', u'curveShape57', u'curveShape58', u'curveShape59', u'curveShape60'], 'shapes': [u'nurbsCircleShape495', u'nurbsCircleShape496', u'nurbsCircleShape497', u'nurbsCircleShape498', u'nurbsCircleShape499'], 'proxy': [u'hair_11_CRV_PXY', u'nurbsTessellate12'], 'influences': [u'bind_hair_11_CRV_4_JNT', u'bind_hair_11_CRV_3_JNT', u'bind_hair_11_CRV_2_JNT', u'bind_hair_11_CRV_1_JNT', u'bind_hair_11_CRV_0_JNT'], 'skin': u'skinCluster69', 'ribbon': [u'hair_11_CRV_RIBBON', u'loft24']}, {'circles': [u'makeNurbCircle347', u'makeNurbCircle348', u'makeNurbCircle349', u'makeNurbCircle350', u'makeNurbCircle351'], 'curve': u'hair_12_CRV', 'tube': [u'hair_12_CRV_TUBE', u'loft25'], 'nulls': [u'hair_12_CRV_0_JNT_CIRCLE_JNT', u'hair_12_CRV_1_JNT_CIRCLE_JNT', u'hair_12_CRV_2_JNT_CIRCLE_JNT', u'hair_12_CRV_3_JNT_CIRCLE_JNT', u'hair_12_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape61', u'curveShape62', u'curveShape63', u'curveShape64', u'curveShape65'], 'shapes': [u'nurbsCircleShape500', u'nurbsCircleShape501', u'nurbsCircleShape502', u'nurbsCircleShape503', u'nurbsCircleShape504'], 'proxy': [u'hair_12_CRV_PXY', u'nurbsTessellate13'], 'influences': [u'bind_hair_12_CRV_4_JNT', u'bind_hair_12_CRV_3_JNT', u'bind_hair_12_CRV_2_JNT', u'bind_hair_12_CRV_1_JNT', u'bind_hair_12_CRV_0_JNT'], 'skin': u'skinCluster70', 'ribbon': [u'hair_12_CRV_RIBBON', u'loft26']}, {'circles': [u'makeNurbCircle352', u'makeNurbCircle353', u'makeNurbCircle354', u'makeNurbCircle355', u'makeNurbCircle356'], 'curve': u'hair_13_CRV', 'tube': [u'hair_13_CRV_TUBE', u'loft27'], 'nulls': [u'hair_13_CRV_0_JNT_CIRCLE_JNT', u'hair_13_CRV_1_JNT_CIRCLE_JNT', u'hair_13_CRV_2_JNT_CIRCLE_JNT', u'hair_13_CRV_3_JNT_CIRCLE_JNT', u'hair_13_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape66', u'curveShape67', u'curveShape68', u'curveShape69', u'curveShape70'], 'shapes': [u'nurbsCircleShape505', u'nurbsCircleShape506', u'nurbsCircleShape507', u'nurbsCircleShape508', u'nurbsCircleShape509'], 'proxy': [u'hair_13_CRV_PXY', u'nurbsTessellate14'], 'influences': [u'bind_hair_13_CRV_4_JNT', u'bind_hair_13_CRV_3_JNT', u'bind_hair_13_CRV_2_JNT', u'bind_hair_13_CRV_1_JNT', u'bind_hair_13_CRV_0_JNT'], 'skin': u'skinCluster71', 'ribbon': [u'hair_13_CRV_RIBBON', u'loft28']}, {'circles': [u'makeNurbCircle357', u'makeNurbCircle358', u'makeNurbCircle359', u'makeNurbCircle360', u'makeNurbCircle361'], 'curve': u'hair_14_CRV', 'tube': [u'hair_14_CRV_TUBE', u'loft29'], 'nulls': [u'hair_14_CRV_0_JNT_CIRCLE_JNT', u'hair_14_CRV_1_JNT_CIRCLE_JNT', u'hair_14_CRV_2_JNT_CIRCLE_JNT', u'hair_14_CRV_3_JNT_CIRCLE_JNT', u'hair_14_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape71', u'curveShape72', u'curveShape73', u'curveShape74', u'curveShape75'], 'shapes': [u'nurbsCircleShape510', u'nurbsCircleShape511', u'nurbsCircleShape512', u'nurbsCircleShape513', u'nurbsCircleShape514'], 'proxy': [u'hair_14_CRV_PXY', u'nurbsTessellate15'], 'influences': [u'bind_hair_14_CRV_4_JNT', u'bind_hair_14_CRV_3_JNT', u'bind_hair_14_CRV_2_JNT', u'bind_hair_14_CRV_1_JNT', u'bind_hair_14_CRV_0_JNT'], 'skin': u'skinCluster72', 'ribbon': [u'hair_14_CRV_RIBBON', u'loft30']}, {'circles': [u'makeNurbCircle362', u'makeNurbCircle363', u'makeNurbCircle364', u'makeNurbCircle365', u'makeNurbCircle366'], 'curve': u'hair_15_CRV', 'tube': [u'hair_15_CRV_TUBE', u'loft31'], 'nulls': [u'hair_15_CRV_0_JNT_CIRCLE_JNT', u'hair_15_CRV_1_JNT_CIRCLE_JNT', u'hair_15_CRV_2_JNT_CIRCLE_JNT', u'hair_15_CRV_3_JNT_CIRCLE_JNT', u'hair_15_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape76', u'curveShape77', u'curveShape78', u'curveShape79', u'curveShape80'], 'shapes': [u'nurbsCircleShape515', u'nurbsCircleShape516', u'nurbsCircleShape517', u'nurbsCircleShape518', u'nurbsCircleShape519'], 'proxy': [u'hair_15_CRV_PXY', u'nurbsTessellate16'], 'influences': [u'bind_hair_15_CRV_4_JNT', u'bind_hair_15_CRV_3_JNT', u'bind_hair_15_CRV_2_JNT', u'bind_hair_15_CRV_1_JNT', u'bind_hair_15_CRV_0_JNT'], 'skin': u'skinCluster73', 'ribbon': [u'hair_15_CRV_RIBBON', u'loft32']}, {'circles': [u'makeNurbCircle367', u'makeNurbCircle368', u'makeNurbCircle369', u'makeNurbCircle370', u'makeNurbCircle371'], 'curve': u'hair_16_CRV', 'tube': [u'hair_16_CRV_TUBE', u'loft33'], 'nulls': [u'hair_16_CRV_0_JNT_CIRCLE_JNT', u'hair_16_CRV_1_JNT_CIRCLE_JNT', u'hair_16_CRV_2_JNT_CIRCLE_JNT', u'hair_16_CRV_3_JNT_CIRCLE_JNT', u'hair_16_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape81', u'curveShape82', u'curveShape83', u'curveShape84', u'curveShape85'], 'shapes': [u'nurbsCircleShape520', u'nurbsCircleShape521', u'nurbsCircleShape522', u'nurbsCircleShape523', u'nurbsCircleShape524'], 'proxy': [u'hair_16_CRV_PXY', u'nurbsTessellate17'], 'influences': [u'bind_hair_16_CRV_4_JNT', u'bind_hair_16_CRV_3_JNT', u'bind_hair_16_CRV_2_JNT', u'bind_hair_16_CRV_1_JNT', u'bind_hair_16_CRV_0_JNT'], 'skin': u'skinCluster74', 'ribbon': [u'hair_16_CRV_RIBBON', u'loft34']}, {'circles': [u'makeNurbCircle372', u'makeNurbCircle373', u'makeNurbCircle374', u'makeNurbCircle375', u'makeNurbCircle376'], 'curve': u'hair_17_CRV', 'tube': [u'hair_17_CRV_TUBE', u'loft35'], 'nulls': [u'hair_17_CRV_0_JNT_CIRCLE_JNT', u'hair_17_CRV_1_JNT_CIRCLE_JNT', u'hair_17_CRV_2_JNT_CIRCLE_JNT', u'hair_17_CRV_3_JNT_CIRCLE_JNT', u'hair_17_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape86', u'curveShape87', u'curveShape88', u'curveShape89', u'curveShape90'], 'shapes': [u'nurbsCircleShape525', u'nurbsCircleShape526', u'nurbsCircleShape527', u'nurbsCircleShape528', u'nurbsCircleShape529'], 'proxy': [u'hair_17_CRV_PXY', u'nurbsTessellate18'], 'influences': [u'bind_hair_17_CRV_4_JNT', u'bind_hair_17_CRV_3_JNT', u'bind_hair_17_CRV_2_JNT', u'bind_hair_17_CRV_1_JNT', u'bind_hair_17_CRV_0_JNT'], 'skin': u'skinCluster75', 'ribbon': [u'hair_17_CRV_RIBBON', u'loft36']}, {'circles': [u'makeNurbCircle377', u'makeNurbCircle378', u'makeNurbCircle379', u'makeNurbCircle380', u'makeNurbCircle381'], 'curve': u'hair_18_CRV', 'tube': [u'hair_18_CRV_TUBE', u'loft37'], 'nulls': [u'hair_18_CRV_0_JNT_CIRCLE_JNT', u'hair_18_CRV_1_JNT_CIRCLE_JNT', u'hair_18_CRV_2_JNT_CIRCLE_JNT', u'hair_18_CRV_3_JNT_CIRCLE_JNT', u'hair_18_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape91', u'curveShape92', u'curveShape93', u'curveShape94', u'curveShape95'], 'shapes': [u'nurbsCircleShape530', u'nurbsCircleShape531', u'nurbsCircleShape532', u'nurbsCircleShape533', u'nurbsCircleShape534'], 'proxy': [u'hair_18_CRV_PXY', u'nurbsTessellate19'], 'influences': [u'bind_hair_18_CRV_4_JNT', u'bind_hair_18_CRV_3_JNT', u'bind_hair_18_CRV_2_JNT', u'bind_hair_18_CRV_1_JNT', u'bind_hair_18_CRV_0_JNT'], 'skin': u'skinCluster76', 'ribbon': [u'hair_18_CRV_RIBBON', u'loft38']}, {'circles': [u'makeNurbCircle382', u'makeNurbCircle383', u'makeNurbCircle384', u'makeNurbCircle385', u'makeNurbCircle386'], 'curve': u'hair_19_CRV', 'tube': [u'hair_19_CRV_TUBE', u'loft39'], 'nulls': [u'hair_19_CRV_0_JNT_CIRCLE_JNT', u'hair_19_CRV_1_JNT_CIRCLE_JNT', u'hair_19_CRV_2_JNT_CIRCLE_JNT', u'hair_19_CRV_3_JNT_CIRCLE_JNT', u'hair_19_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape96', u'curveShape97', u'curveShape98', u'curveShape99', u'curveShape100'], 'shapes': [u'nurbsCircleShape535', u'nurbsCircleShape536', u'nurbsCircleShape537', u'nurbsCircleShape538', u'nurbsCircleShape539'], 'proxy': [u'hair_19_CRV_PXY', u'nurbsTessellate20'], 'influences': [u'bind_hair_19_CRV_4_JNT', u'bind_hair_19_CRV_3_JNT', u'bind_hair_19_CRV_2_JNT', u'bind_hair_19_CRV_1_JNT', u'bind_hair_19_CRV_0_JNT'], 'skin': u'skinCluster77', 'ribbon': [u'hair_19_CRV_RIBBON', u'loft40']}, {'circles': [u'makeNurbCircle387', u'makeNurbCircle388', u'makeNurbCircle389', u'makeNurbCircle390', u'makeNurbCircle391'], 'curve': u'hair_20_CRV', 'tube': [u'hair_20_CRV_TUBE', u'loft41'], 'nulls': [u'hair_20_CRV_0_JNT_CIRCLE_JNT', u'hair_20_CRV_1_JNT_CIRCLE_JNT', u'hair_20_CRV_2_JNT_CIRCLE_JNT', u'hair_20_CRV_3_JNT_CIRCLE_JNT', u'hair_20_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape101', u'curveShape102', u'curveShape103', u'curveShape104', u'curveShape105'], 'shapes': [u'nurbsCircleShape540', u'nurbsCircleShape541', u'nurbsCircleShape542', u'nurbsCircleShape543', u'nurbsCircleShape544'], 'proxy': [u'hair_20_CRV_PXY', u'nurbsTessellate21'], 'influences': [u'bind_hair_20_CRV_4_JNT', u'bind_hair_20_CRV_3_JNT', u'bind_hair_20_CRV_2_JNT', u'bind_hair_20_CRV_1_JNT', u'bind_hair_20_CRV_0_JNT'], 'skin': u'skinCluster78', 'ribbon': [u'hair_20_CRV_RIBBON', u'loft42']}, {'circles': [u'makeNurbCircle392', u'makeNurbCircle393', u'makeNurbCircle394', u'makeNurbCircle395', u'makeNurbCircle396'], 'curve': u'hair_21_CRV', 'tube': [u'hair_21_CRV_TUBE', u'loft43'], 'nulls': [u'hair_21_CRV_0_JNT_CIRCLE_JNT', u'hair_21_CRV_1_JNT_CIRCLE_JNT', u'hair_21_CRV_2_JNT_CIRCLE_JNT', u'hair_21_CRV_3_JNT_CIRCLE_JNT', u'hair_21_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape106', u'curveShape107', u'curveShape108', u'curveShape109', u'curveShape110'], 'shapes': [u'nurbsCircleShape545', u'nurbsCircleShape546', u'nurbsCircleShape547', u'nurbsCircleShape548', u'nurbsCircleShape549'], 'proxy': [u'hair_21_CRV_PXY', u'nurbsTessellate22'], 'influences': [u'bind_hair_21_CRV_4_JNT', u'bind_hair_21_CRV_3_JNT', u'bind_hair_21_CRV_2_JNT', u'bind_hair_21_CRV_1_JNT', u'bind_hair_21_CRV_0_JNT'], 'skin': u'skinCluster79', 'ribbon': [u'hair_21_CRV_RIBBON', u'loft44']}, {'circles': [u'makeNurbCircle397', u'makeNurbCircle398', u'makeNurbCircle399', u'makeNurbCircle400', u'makeNurbCircle401'], 'curve': u'hair_22_CRV', 'tube': [u'hair_22_CRV_TUBE', u'loft45'], 'nulls': [u'hair_22_CRV_0_JNT_CIRCLE_JNT', u'hair_22_CRV_1_JNT_CIRCLE_JNT', u'hair_22_CRV_2_JNT_CIRCLE_JNT', u'hair_22_CRV_3_JNT_CIRCLE_JNT', u'hair_22_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape111', u'curveShape112', u'curveShape113', u'curveShape114', u'curveShape115'], 'shapes': [u'nurbsCircleShape550', u'nurbsCircleShape551', u'nurbsCircleShape552', u'nurbsCircleShape553', u'nurbsCircleShape554'], 'proxy': [u'hair_22_CRV_PXY', u'nurbsTessellate23'], 'influences': [u'bind_hair_22_CRV_4_JNT', u'bind_hair_22_CRV_3_JNT', u'bind_hair_22_CRV_2_JNT', u'bind_hair_22_CRV_1_JNT', u'bind_hair_22_CRV_0_JNT'], 'skin': u'skinCluster80', 'ribbon': [u'hair_22_CRV_RIBBON', u'loft46']}, {'circles': [u'makeNurbCircle402', u'makeNurbCircle403', u'makeNurbCircle404', u'makeNurbCircle405', u'makeNurbCircle406'], 'curve': u'hair_23_CRV', 'tube': [u'hair_23_CRV_TUBE', u'loft47'], 'nulls': [u'hair_23_CRV_0_JNT_CIRCLE_JNT', u'hair_23_CRV_1_JNT_CIRCLE_JNT', u'hair_23_CRV_2_JNT_CIRCLE_JNT', u'hair_23_CRV_3_JNT_CIRCLE_JNT', u'hair_23_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape116', u'curveShape117', u'curveShape118', u'curveShape119', u'curveShape120'], 'shapes': [u'nurbsCircleShape555', u'nurbsCircleShape556', u'nurbsCircleShape557', u'nurbsCircleShape558', u'nurbsCircleShape559'], 'proxy': [u'hair_23_CRV_PXY', u'nurbsTessellate24'], 'influences': [u'bind_hair_23_CRV_4_JNT', u'bind_hair_23_CRV_3_JNT', u'bind_hair_23_CRV_2_JNT', u'bind_hair_23_CRV_1_JNT', u'bind_hair_23_CRV_0_JNT'], 'skin': u'skinCluster81', 'ribbon': [u'hair_23_CRV_RIBBON', u'loft48']}, {'circles': [u'makeNurbCircle407', u'makeNurbCircle408', u'makeNurbCircle409', u'makeNurbCircle410', u'makeNurbCircle411'], 'curve': u'hair_24_CRV', 'tube': [u'hair_24_CRV_TUBE', u'loft49'], 'nulls': [u'hair_24_CRV_0_JNT_CIRCLE_JNT', u'hair_24_CRV_1_JNT_CIRCLE_JNT', u'hair_24_CRV_2_JNT_CIRCLE_JNT', u'hair_24_CRV_3_JNT_CIRCLE_JNT', u'hair_24_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape121', u'curveShape122', u'curveShape123', u'curveShape124', u'curveShape125'], 'shapes': [u'nurbsCircleShape560', u'nurbsCircleShape561', u'nurbsCircleShape562', u'nurbsCircleShape563', u'nurbsCircleShape564'], 'proxy': [u'hair_24_CRV_PXY', u'nurbsTessellate25'], 'influences': [u'bind_hair_24_CRV_4_JNT', u'bind_hair_24_CRV_3_JNT', u'bind_hair_24_CRV_2_JNT', u'bind_hair_24_CRV_1_JNT', u'bind_hair_24_CRV_0_JNT'], 'skin': u'skinCluster82', 'ribbon': [u'hair_24_CRV_RIBBON', u'loft50']}, {'circles': [u'makeNurbCircle412', u'makeNurbCircle413', u'makeNurbCircle414', u'makeNurbCircle415', u'makeNurbCircle416'], 'curve': u'hair_25_CRV', 'tube': [u'hair_25_CRV_TUBE', u'loft51'], 'nulls': [u'hair_25_CRV_0_JNT_CIRCLE_JNT', u'hair_25_CRV_1_JNT_CIRCLE_JNT', u'hair_25_CRV_2_JNT_CIRCLE_JNT', u'hair_25_CRV_3_JNT_CIRCLE_JNT', u'hair_25_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape126', u'curveShape127', u'curveShape128', u'curveShape129', u'curveShape130'], 'shapes': [u'nurbsCircleShape565', u'nurbsCircleShape566', u'nurbsCircleShape567', u'nurbsCircleShape568', u'nurbsCircleShape569'], 'proxy': [u'hair_25_CRV_PXY', u'nurbsTessellate26'], 'influences': [u'bind_hair_25_CRV_4_JNT', u'bind_hair_25_CRV_3_JNT', u'bind_hair_25_CRV_2_JNT', u'bind_hair_25_CRV_1_JNT', u'bind_hair_25_CRV_0_JNT'], 'skin': u'skinCluster83', 'ribbon': [u'hair_25_CRV_RIBBON', u'loft52']}, {'circles': [u'makeNurbCircle417', u'makeNurbCircle418', u'makeNurbCircle419', u'makeNurbCircle420', u'makeNurbCircle421'], 'curve': u'hair_26_CRV', 'tube': [u'hair_26_CRV_TUBE', u'loft53'], 'nulls': [u'hair_26_CRV_0_JNT_CIRCLE_JNT', u'hair_26_CRV_1_JNT_CIRCLE_JNT', u'hair_26_CRV_2_JNT_CIRCLE_JNT', u'hair_26_CRV_3_JNT_CIRCLE_JNT', u'hair_26_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape131', u'curveShape132', u'curveShape133', u'curveShape134', u'curveShape135'], 'shapes': [u'nurbsCircleShape570', u'nurbsCircleShape571', u'nurbsCircleShape572', u'nurbsCircleShape573', u'nurbsCircleShape574'], 'proxy': [u'hair_26_CRV_PXY', u'nurbsTessellate27'], 'influences': [u'bind_hair_26_CRV_4_JNT', u'bind_hair_26_CRV_3_JNT', u'bind_hair_26_CRV_2_JNT', u'bind_hair_26_CRV_1_JNT', u'bind_hair_26_CRV_0_JNT'], 'skin': u'skinCluster84', 'ribbon': [u'hair_26_CRV_RIBBON', u'loft54']}, {'circles': [u'makeNurbCircle422', u'makeNurbCircle423', u'makeNurbCircle424', u'makeNurbCircle425', u'makeNurbCircle426'], 'curve': u'hair_27_CRV', 'tube': [u'hair_27_CRV_TUBE', u'loft55'], 'nulls': [u'hair_27_CRV_0_JNT_CIRCLE_JNT', u'hair_27_CRV_1_JNT_CIRCLE_JNT', u'hair_27_CRV_2_JNT_CIRCLE_JNT', u'hair_27_CRV_3_JNT_CIRCLE_JNT', u'hair_27_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape136', u'curveShape137', u'curveShape138', u'curveShape139', u'curveShape140'], 'shapes': [u'nurbsCircleShape575', u'nurbsCircleShape576', u'nurbsCircleShape577', u'nurbsCircleShape578', u'nurbsCircleShape579'], 'proxy': [u'hair_27_CRV_PXY', u'nurbsTessellate28'], 'influences': [u'bind_hair_27_CRV_4_JNT', u'bind_hair_27_CRV_3_JNT', u'bind_hair_27_CRV_2_JNT', u'bind_hair_27_CRV_1_JNT', u'bind_hair_27_CRV_0_JNT'], 'skin': u'skinCluster85', 'ribbon': [u'hair_27_CRV_RIBBON', u'loft56']}, {'circles': [u'makeNurbCircle427', u'makeNurbCircle428', u'makeNurbCircle429', u'makeNurbCircle430', u'makeNurbCircle431'], 'curve': u'hair_28_CRV', 'tube': [u'hair_28_CRV_TUBE', u'loft57'], 'nulls': [u'hair_28_CRV_0_JNT_CIRCLE_JNT', u'hair_28_CRV_1_JNT_CIRCLE_JNT', u'hair_28_CRV_2_JNT_CIRCLE_JNT', u'hair_28_CRV_3_JNT_CIRCLE_JNT', u'hair_28_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape141', u'curveShape142', u'curveShape143', u'curveShape144', u'curveShape145'], 'shapes': [u'nurbsCircleShape580', u'nurbsCircleShape581', u'nurbsCircleShape582', u'nurbsCircleShape583', u'nurbsCircleShape584'], 'proxy': [u'hair_28_CRV_PXY', u'nurbsTessellate29'], 'influences': [u'bind_hair_28_CRV_4_JNT', u'bind_hair_28_CRV_3_JNT', u'bind_hair_28_CRV_2_JNT', u'bind_hair_28_CRV_1_JNT', u'bind_hair_28_CRV_0_JNT'], 'skin': u'skinCluster86', 'ribbon': [u'hair_28_CRV_RIBBON', u'loft58']}, {'circles': [u'makeNurbCircle432', u'makeNurbCircle433', u'makeNurbCircle434', u'makeNurbCircle435', u'makeNurbCircle436'], 'curve': u'hair_29_CRV', 'tube': [u'hair_29_CRV_TUBE', u'loft59'], 'nulls': [u'hair_29_CRV_0_JNT_CIRCLE_JNT', u'hair_29_CRV_1_JNT_CIRCLE_JNT', u'hair_29_CRV_2_JNT_CIRCLE_JNT', u'hair_29_CRV_3_JNT_CIRCLE_JNT', u'hair_29_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape146', u'curveShape147', u'curveShape148', u'curveShape149', u'curveShape150'], 'shapes': [u'nurbsCircleShape585', u'nurbsCircleShape586', u'nurbsCircleShape587', u'nurbsCircleShape588', u'nurbsCircleShape589'], 'proxy': [u'hair_29_CRV_PXY', u'nurbsTessellate30'], 'influences': [u'bind_hair_29_CRV_4_JNT', u'bind_hair_29_CRV_3_JNT', u'bind_hair_29_CRV_2_JNT', u'bind_hair_29_CRV_1_JNT', u'bind_hair_29_CRV_0_JNT'], 'skin': u'skinCluster87', 'ribbon': [u'hair_29_CRV_RIBBON', u'loft60']}, {'circles': [u'makeNurbCircle437', u'makeNurbCircle438', u'makeNurbCircle439', u'makeNurbCircle440', u'makeNurbCircle441'], 'curve': u'hair_30_CRV', 'tube': [u'hair_30_CRV_TUBE', u'loft61'], 'nulls': [u'hair_30_CRV_0_JNT_CIRCLE_JNT', u'hair_30_CRV_1_JNT_CIRCLE_JNT', u'hair_30_CRV_2_JNT_CIRCLE_JNT', u'hair_30_CRV_3_JNT_CIRCLE_JNT', u'hair_30_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape151', u'curveShape152', u'curveShape153', u'curveShape154', u'curveShape155'], 'shapes': [u'nurbsCircleShape590', u'nurbsCircleShape591', u'nurbsCircleShape592', u'nurbsCircleShape593', u'nurbsCircleShape594'], 'proxy': [u'hair_30_CRV_PXY', u'nurbsTessellate31'], 'influences': [u'bind_hair_30_CRV_4_JNT', u'bind_hair_30_CRV_3_JNT', u'bind_hair_30_CRV_2_JNT', u'bind_hair_30_CRV_1_JNT', u'bind_hair_30_CRV_0_JNT'], 'skin': u'skinCluster88', 'ribbon': [u'hair_30_CRV_RIBBON', u'loft62']}, {'circles': [u'makeNurbCircle442', u'makeNurbCircle443', u'makeNurbCircle444', u'makeNurbCircle445', u'makeNurbCircle446'], 'curve': u'hair_31_CRV', 'tube': [u'hair_31_CRV_TUBE', u'loft63'], 'nulls': [u'hair_31_CRV_0_JNT_CIRCLE_JNT', u'hair_31_CRV_1_JNT_CIRCLE_JNT', u'hair_31_CRV_2_JNT_CIRCLE_JNT', u'hair_31_CRV_3_JNT_CIRCLE_JNT', u'hair_31_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape156', u'curveShape157', u'curveShape158', u'curveShape159', u'curveShape160'], 'shapes': [u'nurbsCircleShape595', u'nurbsCircleShape596', u'nurbsCircleShape597', u'nurbsCircleShape598', u'nurbsCircleShape599'], 'proxy': [u'hair_31_CRV_PXY', u'nurbsTessellate32'], 'influences': [u'bind_hair_31_CRV_4_JNT', u'bind_hair_31_CRV_3_JNT', u'bind_hair_31_CRV_2_JNT', u'bind_hair_31_CRV_1_JNT', u'bind_hair_31_CRV_0_JNT'], 'skin': u'skinCluster89', 'ribbon': [u'hair_31_CRV_RIBBON', u'loft64']}, {'circles': [u'makeNurbCircle447', u'makeNurbCircle448', u'makeNurbCircle449', u'makeNurbCircle450', u'makeNurbCircle451'], 'curve': u'hair_32_CRV', 'tube': [u'hair_32_CRV_TUBE', u'loft65'], 'nulls': [u'hair_32_CRV_0_JNT_CIRCLE_JNT', u'hair_32_CRV_1_JNT_CIRCLE_JNT', u'hair_32_CRV_2_JNT_CIRCLE_JNT', u'hair_32_CRV_3_JNT_CIRCLE_JNT', u'hair_32_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape161', u'curveShape162', u'curveShape163', u'curveShape164', u'curveShape165'], 'shapes': [u'nurbsCircleShape600', u'nurbsCircleShape601', u'nurbsCircleShape602', u'nurbsCircleShape603', u'nurbsCircleShape604'], 'proxy': [u'hair_32_CRV_PXY', u'nurbsTessellate33'], 'influences': [u'bind_hair_32_CRV_4_JNT', u'bind_hair_32_CRV_3_JNT', u'bind_hair_32_CRV_2_JNT', u'bind_hair_32_CRV_1_JNT', u'bind_hair_32_CRV_0_JNT'], 'skin': u'skinCluster90', 'ribbon': [u'hair_32_CRV_RIBBON', u'loft66']}, {'circles': [u'makeNurbCircle452', u'makeNurbCircle453', u'makeNurbCircle454', u'makeNurbCircle455', u'makeNurbCircle456'], 'curve': u'hair_33_CRV', 'tube': [u'hair_33_CRV_TUBE', u'loft67'], 'nulls': [u'hair_33_CRV_0_JNT_CIRCLE_JNT', u'hair_33_CRV_1_JNT_CIRCLE_JNT', u'hair_33_CRV_2_JNT_CIRCLE_JNT', u'hair_33_CRV_3_JNT_CIRCLE_JNT', u'hair_33_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape166', u'curveShape167', u'curveShape168', u'curveShape169', u'curveShape170'], 'shapes': [u'nurbsCircleShape605', u'nurbsCircleShape606', u'nurbsCircleShape607', u'nurbsCircleShape608', u'nurbsCircleShape609'], 'proxy': [u'hair_33_CRV_PXY', u'nurbsTessellate34'], 'influences': [u'bind_hair_33_CRV_4_JNT', u'bind_hair_33_CRV_3_JNT', u'bind_hair_33_CRV_2_JNT', u'bind_hair_33_CRV_1_JNT', u'bind_hair_33_CRV_0_JNT'], 'skin': u'skinCluster91', 'ribbon': [u'hair_33_CRV_RIBBON', u'loft68']}, {'circles': [u'makeNurbCircle457', u'makeNurbCircle458', u'makeNurbCircle459', u'makeNurbCircle460', u'makeNurbCircle461'], 'curve': u'hair_34_CRV', 'tube': [u'hair_34_CRV_TUBE', u'loft69'], 'nulls': [u'hair_34_CRV_0_JNT_CIRCLE_JNT', u'hair_34_CRV_1_JNT_CIRCLE_JNT', u'hair_34_CRV_2_JNT_CIRCLE_JNT', u'hair_34_CRV_3_JNT_CIRCLE_JNT', u'hair_34_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape171', u'curveShape172', u'curveShape173', u'curveShape174', u'curveShape175'], 'shapes': [u'nurbsCircleShape610', u'nurbsCircleShape611', u'nurbsCircleShape612', u'nurbsCircleShape613', u'nurbsCircleShape614'], 'proxy': [u'hair_34_CRV_PXY', u'nurbsTessellate35'], 'influences': [u'bind_hair_34_CRV_4_JNT', u'bind_hair_34_CRV_3_JNT', u'bind_hair_34_CRV_2_JNT', u'bind_hair_34_CRV_1_JNT', u'bind_hair_34_CRV_0_JNT'], 'skin': u'skinCluster92', 'ribbon': [u'hair_34_CRV_RIBBON', u'loft70']}, {'circles': [u'makeNurbCircle462', u'makeNurbCircle463', u'makeNurbCircle464', u'makeNurbCircle465', u'makeNurbCircle466'], 'curve': u'hair_35_CRV', 'tube': [u'hair_35_CRV_TUBE', u'loft71'], 'nulls': [u'hair_35_CRV_0_JNT_CIRCLE_JNT', u'hair_35_CRV_1_JNT_CIRCLE_JNT', u'hair_35_CRV_2_JNT_CIRCLE_JNT', u'hair_35_CRV_3_JNT_CIRCLE_JNT', u'hair_35_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape176', u'curveShape177', u'curveShape178', u'curveShape179', u'curveShape180'], 'shapes': [u'nurbsCircleShape615', u'nurbsCircleShape616', u'nurbsCircleShape617', u'nurbsCircleShape618', u'nurbsCircleShape619'], 'proxy': [u'hair_35_CRV_PXY', u'nurbsTessellate36'], 'influences': [u'bind_hair_35_CRV_4_JNT', u'bind_hair_35_CRV_3_JNT', u'bind_hair_35_CRV_2_JNT', u'bind_hair_35_CRV_1_JNT', u'bind_hair_35_CRV_0_JNT'], 'skin': u'skinCluster93', 'ribbon': [u'hair_35_CRV_RIBBON', u'loft72']}, {'circles': [u'makeNurbCircle467', u'makeNurbCircle468', u'makeNurbCircle469', u'makeNurbCircle470', u'makeNurbCircle471'], 'curve': u'hair_36_CRV', 'tube': [u'hair_36_CRV_TUBE', u'loft73'], 'nulls': [u'hair_36_CRV_0_JNT_CIRCLE_JNT', u'hair_36_CRV_1_JNT_CIRCLE_JNT', u'hair_36_CRV_2_JNT_CIRCLE_JNT', u'hair_36_CRV_3_JNT_CIRCLE_JNT', u'hair_36_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape181', u'curveShape182', u'curveShape183', u'curveShape184', u'curveShape185'], 'shapes': [u'nurbsCircleShape620', u'nurbsCircleShape621', u'nurbsCircleShape622', u'nurbsCircleShape623', u'nurbsCircleShape624'], 'proxy': [u'hair_36_CRV_PXY', u'nurbsTessellate37'], 'influences': [u'bind_hair_36_CRV_4_JNT', u'bind_hair_36_CRV_3_JNT', u'bind_hair_36_CRV_2_JNT', u'bind_hair_36_CRV_1_JNT', u'bind_hair_36_CRV_0_JNT'], 'skin': u'skinCluster94', 'ribbon': [u'hair_36_CRV_RIBBON', u'loft74']}]
scratch.attach(cs) # perhaps this line?
[{'circles': [u'makeNurbCircle472', u'makeNurbCircle473', u'makeNurbCircle474', u'makeNurbCircle475', u'makeNurbCircle476'], 'curve': u'hair_27_CRV', 'tube': [u'hair_27_CRV_TUBE', u'loft75'], 'nulls': [u'hair_27_CRV_0_JNT_CIRCLE_JNT', u'hair_27_CRV_1_JNT_CIRCLE_JNT', u'hair_27_CRV_2_JNT_CIRCLE_JNT', u'hair_27_CRV_3_JNT_CIRCLE_JNT', u'hair_27_CRV_4_JNT_CIRCLE_JNT'], 'lines': [u'curveShape186', u'curveShape187', u'curveShape188', u'curveShape189', u'curveShape190'], 'shapes': [u'nurbsCircleShape625', u'nurbsCircleShape626', u'nurbsCircleShape627', u'nurbsCircleShape628', u'nurbsCircleShape629'], 'proxy': [u'hair_27_CRV_PXY', u'nurbsTessellate38'], 'influences': [u'bind_hair_27_CRV_4_JNT', u'bind_hair_27_CRV_3_JNT', u'bind_hair_27_CRV_2_JNT', u'bind_hair_27_CRV_1_JNT', u'bind_hair_27_CRV_0_JNT'], 'skin': u'skinCluster95', 'ribbon': [u'hair_27_CRV_RIBBON', u'loft76']}]

******************


'''

for n in mc.ls(sl=1, o=1):
    sn = n+'_skinCluster'
    if mc.objExists(sn):
        print sn
        j1 = n.replace('CRV_RIBBONShape','3_JNT')
        j2 = n.replace('CRV_RIBBONShape','4_JNT')
        pts = n+'.cv[0:3][0:6]'
        print j1, j2, pts
        mc.skinPercent(sn, pts, tv=[(j1, 0.0), (j2, 0.0)])

import maya.cmds as mc
for n in mc.ls(sl=1):
    for i in range(0,44):
        c = mc.cluster(n+'.cv[5]['+str(i)+']',n+'.cv[4]['+str(i)+']',n+'.cv[3]['+str(i)+']',n+'.cv[2]['+str(i)+']',n+'.cv[1]['+str(i)+']',n+'.cv[0]['+str(i)+']',n+'.cv[6:7]['+str(i)+']')
        j = mc.createNode('joint', n='bind'+n+'_'+str(i).zfill(2)+'_JNT')
        mc.delete(mc.pointConstraint(c[1],j))
        mc.delete(c)

for n in mc.ls(sl=1):
    for i in range(0,15):
        #c = mc.cluster(n+'.cv[5]['+str(i)+']',n+'.cv[4]['+str(i)+']',n+'.cv[3]['+str(i)+']',n+'.cv[2]['+str(i)+']',n+'.cv[1]['+str(i)+']',n+'.cv[0]['+str(i)+']',n+'.cv[6:7]['+str(i)+']')
        c = mc.cluster(n+'.cv['+str(i)+'][0:1]')
        j = mc.createNode('joint', n='bind_'+n+'_'+str(i).zfill(2)+'_JNT')
        mc.delete(mc.pointConstraint(c[1],j))
        mc.delete(c)

# CREATE fol AT CLOSEST uv TO u AT 0.5 v THEN PARENT JOINT

import scratch
reload(scratch)
scratch.ribbonCloth()

for n in mc.ls(sl=1):
    mc.rename(n, mc.listRelatives(n, p=1)[0]+'Shape')

import maya.cmds as mc
for n in mc.ls(sl=1):
    a = mc.createNode('transform', n=n+'_A_GRP')
    b = mc.createNode('transform', n=n+'_B_GRP')
    b = mc.parent(b,a)[0]
    mc.delete(mc.parentConstraint(n,a))
    p = mc.listRelatives(n, p=1)
    if p:
        a = mc.parent(a,p)[0]
    mc.parent(n,b)



import maya.cmds as mc
for n in mc.ls(sl=1):
    mc.rename(n, n.split('|')[-1].replace('upper','lower').replace('Upper','Lower'))

import maya.cmds as mc
for n in mc.ls(sl=1):
    mc.rename(n, mc.listRelatives(n, p=1)[0]+'Shape')

import maya.cmds as mc
for n in mc.ls(sl=1):
    j = mc.createNode('joint', n='bind_'+n.replace('CON','JNT'))
    j = mc.parent(j, n, r=1)


mc.select(mc.ls(sl=1, ap=1, dag=1, type='joint'))
bind = []
s = mc.ls(sl=1)
for n in s:
    if 'bind' in n:
        bind.append(n)
        print n
if bind:
    mc.select(n)



import scratch
reload(scratch)
scratch.ribbonCloth()

import skinCluster
reload(skinCluster)
for n in mc.ls(sl=1):
    mc.select(n, n.replace('_TUBE','_PXY'))
    skinCluster.copy_skin_from_selection()
    mc.delete(n.replace('_TUBE','_0_JNT'),n)

import skinCluster
reload(skinCluster)
for n in mc.ls(sl=1):
    rep = n.replace('_CRV_PXY','')
    mc.select(n, rep)
    skinCluster.copy_skin_from_selection()
    mc.delete(rep)

import skinCluster
reload(skinCluster)
for n in mc.ls(sl=1):
    pxy = n.replace('_CRV_RIBBON','_CRV_PXY')
    rep = n.replace('_CRV_RIBBON','')
    mc.select(pxy, rep)
    skinCluster.copy_skin_from_selection()
    mc.delete(pxy)
    hier = mc.ls('bind_'+rep+'CRV_0_JNT', dag=1, ap=1, type='joint')
    ribbonShape = n+'Shape'
    for j in hier:
        f = follicle.follicleFromNode(j, ribbonShape, parent=True)



import scratch
reload(scratch)
for n in mc.ls(sl=1):
    scratch.bindRibbonWithCons(n)







for n in mc.ls(sl=1):
    mc.rename(n, mc.listRelatives(n, p=1)[0]+'Shape')

for n in mc.ls(sl=1):
    mc.rename(n, n.replace('ZERO1','ZERO'))

size




# wait for it, memory fails if not run line at a time, FML, moving on....
scratch.attach(cs)
"""

def build():
    """
    Build hair patches and bind to geom from generated curves
    """

    cs = []
    for crv in maya.cmds.ls(sl=1):

        # build the curve ribbons and proxy
        c = chains.circles(crv)
        c['curve'] = crv
        cs.append(c)

    return cs


def jointAtRibbon(name, ribbon, u, v, group=True):

    ribbonShape = maya.cmds.listRelatives(ribbon, s=True, ni=True, type='nurbsSurface')[0]

    pos = maya.cmds.createNode('pointOnSurfaceInfo')
    maya.cmds.connectAttr( ribbonShape+'.worldSpace[0]', pos+'.inputSurface' )
    x = maya.cmds.createNode('transform')

    maya.cmds.connectAttr( pos+'.position', x+'.t', f=1 )
    maya.cmds.setAttr( pos+'.parameterU', u )
    maya.cmds.setAttr( pos+'.parameterV', v )

    j = maya.cmds.createNode('joint', n=name+'_JNT')
    maya.cmds.delete( maya.cmds.pointConstraint(x, j) )
    maya.cmds.delete( x, pos )

    f = follicle.follicleFromNode(j, ribbonShape, parent=True)
    j = f['null'][0]
    maya.cmds.setAttr(j+'.t', 0,0,0)
    maya.cmds.setAttr(j+'.r', 0,0,0)
    maya.cmds.setAttr(j+'.jo', 0,0,0)

    if group:
        #j = maya.cmds.parent(tj, w=True)[0]
        z1 = maya.cmds.createNode( 'transform', n=name+'_A_ZERO')
        maya.cmds.delete( maya.cmds.pointConstraint( j, z1 ) )
        maya.cmds.delete( maya.cmds.orientConstraint( j, z1 ) )
        z2 = maya.cmds.duplicate( z1, n=name+'_B_ZERO', rr=True )[0]
        z2 = maya.cmds.parent(z2, z1)
        c = maya.cmds.duplicate( j, rr=True, n=name+'_CON')[0]
        c = maya.cmds.parent(c, z2)[0]
        j = maya.cmds.parent(j, c)[0]

        shapeXf = maya.cmds.circle(c=(0,0,0), nr=(0,1,0), sw=360, r=1.5, d=3, ut=0, tol=0.01, s=6, ch=1)
        shapeXf = maya.cmds.parent(shapeXf[0], c, r=1)[0]
        shape = maya.cmds.parent(maya.cmds.listRelatives(shapeXf, s=1, f=1, pa=1, type='nurbsCurve'), c, r=1, s=1)

        maya.cmds.delete(shapeXf, f['transform'])

        return {'joint':j, 'control':c, 'zero':z1}

    else:

        return {'joint':j}



def consFromRibbon(ribbon):

    joints = []
    zeroes = []
    cons = []
    uvs = [[0.5,0.0], [0.5,0.5], [0.5,1.0]]

    name = ribbon.split('_')[0]

    for i in range(len(uvs)):
        r = jointAtRibbon(name+'_'+str(i), ribbon, uvs[i][0], uvs[i][1])
        joints.append(r['joint'])
        zeroes.append(r['zero'])
        cons.append(r['control'])

    maya.cmds.delete( ribbon, ch=True )

    # quick hacks to parent ends to end minus 1 on each end of surface/curve
    zeroes[1] = maya.cmds.parent(zeroes[1], cons[0])[0]
    zeroes[2] = maya.cmds.parent(zeroes[2], cons[0])[0]

    # parent to RIG joints
    head = 'basic_head_01_FOLLOW'

    zeroes[0] = maya.cmds.parent(zeroes[0], head)[0]


    return {'joints':joints, 'zero':zeroes, 'controls':cons}



def bindRibbonWithCons(ribbon, bind=True):

    joints = []
    zeroes = []
    cons = []
    infs = []
    uvs = [[0.5,0.0], [0.5,0.1], [0.5,0.5], [0.5,0.9], [0.5,1.0]]

    name = ribbon.split('_CRV')[0]

    for i in range(len(uvs)):
        r = jointAtRibbon(name+'_'+str(i), ribbon, uvs[i][0], uvs[i][1])
        joints.append(r['joint'])
        zeroes.append(r['zero'])
        cons.append(r['control'])

    maya.cmds.delete( ribbon, ch=True )
    skin = maya.cmds.skinCluster( joints, ribbon, tsb=True, mi=2, obeyMaxInfluences=True)[0]

    # quick hacks to parent ends to end minus 1 on each end of surface/curve
    zeroes[0] = maya.cmds.parent(zeroes[0], cons[1])[0]
    zeroes[4] = maya.cmds.parent(zeroes[4], cons[3])[0]

    # clean ribbon so each line has same weighted verts after copy weights
    cleanRibbonWeights(ribbon)

    # parent to RIG joints
    head = 'basic_head_01_FOLLOW'
    #neckB = 'basic_neck_02_FOLLOW'
    #neckA = 'basic_neck_01_FOLLOW'

    zeroes[1] = maya.cmds.parent(zeroes[1], head)[0]
    zeroes[2] = maya.cmds.parent(zeroes[2], head)[0]
    zeroes[3] = maya.cmds.parent(zeroes[3], head)[0]
    #zeroes[2] = maya.cmds.parent(zeroes[2], neckB)[0]
    #zeroes[3] = maya.cmds.parent(zeroes[3], neckA)[0]

    num = 20
    iter = float(1.0/num)
    value = 0.0
    for i in range(num):
        t = jointAtRibbon('bind_'+name+'_'+str(i), ribbon, 0.5, value, group=False)
        #print t, value
        infs.append(t['joint'])
        maya.cmds.setAttr(t['joint']+'.radius', 0.2)
        value += iter

    if maya.cmds.objExists(name):
        geoskin = maya.cmds.skinCluster( infs, name, tsb=True, mi=3, obeyMaxInfluences=True)[0]

    return {'joints':joints, 'zero':zeroes, 'controls':cons, 'skin':skin, 'influences':infs, 'geomSkin':geoskin}


def attach(cs):
    """
    After manually checking twists on ribbons for any anomolies (twisting) then run this.
    """

    pxy = []
    fols = []

    for c in cs:

        # delete ribbon history
        maya.cmds.delete( c['ribbon'][0], ch=True )

        # # unparent chain or it crashes maya, ugh
        # # build follicles to attach joint chain to
        maya.cmds.select(c['influences'], c['ribbon'][0])
        f = follicle.folliclesFromSel()

        # build ribbon IK cons
        bindRibbonWithCons(c['ribbon'][0])

        # delete proxy history to pass weights to it.
        maya.cmds.delete([c['proxy'][0]], ch=True)

        # bind the proxy mesh with ribbon chain and tube weights
        tubeSkin = maya.cmds.skinCluster(c['influences'], [c['proxy'][0]], tsb=True, mi=1, obeyMaxInfluences=True)[0]
        maya.cmds.copySkinWeights(ss=c['skin'], ds=tubeSkin, noMirror=True, surfaceAssociation='closestPoint', influenceAssociation="closestJoint")

        # get rid of nurbs tube
        maya.cmds.delete(c['tube'])

        # get rid of nurbs generated nulls for loft to tube
        maya.cmds.delete( maya.cmds.listRelatives(c['nulls'], p=1) )

        # copy weights from crv to model geom by assumed naming convention
        mesh = maya.cmds.ls( c['curve'].replace('_CRV','_REN') )
        skinCluster.copy_skin(c['proxy'][0], mesh[0])

        # get rid of pxy
        maya.cmds.delete(c['proxy'][0])



def cleanRibbonWeights(ribbon):

    numv = int(maya.cmds.getAttr(ribbon+'.mxv')+3)
    for i in range(0,numv):
        maya.cmds.select(ribbon+'.cv[0:1]['+str(i)+']')
        glTools.tools.copyPasteWeights.copyWeights()
        glTools.tools.copyPasteWeights.pasteWeights()


def ribbonCloth():

    s = maya.cmds.ls(sl=1)
    for ribbon in s:

        ribbonShape = maya.cmds.listRelatives(ribbon, s=1, ni=1, type='nurbsSurface')
        if ribbonShape:
            ribbonShape = ribbonShape[0]

        name = ribbon.split('_')[0]
        if ribbon[0:2] == 'L_' or ribbon[0:2] == 'R_':
            name = ribbon.split('_')[0]+'_'+ribbon.split('_')[1]

        du = maya.cmds.getAttr(ribbonShape+'.du')
        dv = maya.cmds.getAttr(ribbonShape+'.dv')
        su = maya.cmds.getAttr(ribbonShape+'.su')
        sv = maya.cmds.getAttr(ribbonShape+'.sv')

        uLen = du+su-1
        vLen = dv+sv-1
        div = 1.0/(uLen-1)

        joints = []
        zeroes = []
        for i in range(uLen):
            u = div*i
            v = 0.5
            r = jointAtRibbon(name+'_'+str(i), ribbon, u, v)
            joints.append(r['joint'])
            zeroes.append(r['zero'])

        for j in zeroes:
            f = follicle.follicleFromNode(j, ribbonShape)


def rib(num=3):
    nurbss = mc.ls(sl=1, typ='nurbsSurface', dag=1, ap=1)
    iter = 1.0/(num-1)
    v = 0.0
    ch = []
    for n in nurbss:
        for i in range(num):
            r = follicle.createFollicle(nurbs=n, u=0.5, v=v)
            v += iter
            jt = mc.createNode('joint', n=r['transform']+'_env_tmp')
            mc.delete(mc.parentConstraint(r['transform'], jt))
            mc.select(jt)
            j = mc.joint(n=r['transform']+'_env')
            j = mc.parent(j, w=1)[0]
            mc.delete(jt)
            par = mc.parentConstraint(r['transform'], j, n=r['transform']+'_env_parentConstraint')[0]
            mc.setAttr(par+'.v', 0)
            ch.append(j)
            mc.setAttr(j+'.radius', 0.2)
    for i in range(1, len(ch)):
        print(i)
        print (ch[i], ch[i-1])
        ch[i] = mc.parent(ch[i], ch[i-1])[0]


def flipJo(angle, degree):
    """
    import scratch
    reload(scratch)
    scratch.rib(num=12)
    """
    """
    for n in mc.ls(sl=1):
        mc.select(n)
        j = mc.joint(n=n+'_offset')
        mc.setAttr(j+'.tx', 0.5)
    """
    """
    for n in mc.ls(sl=1):
        mc.setAttr(n+'.tx', (mc.getAttr(n+'.tx')*-1))
    """
    s = mc.ls(sl=1)
    p = mc.listRelatives(s, p=1)
    s = mc.parent(s, w=1)
    for i in range(len(s)):
        print s[i]
        mc.select(s[i])
        j = mc.joint(n=s[i]+'_TMP')
        j = mc.parent(w=1)[0]
        mc.setAttr(j+'.'+angle, degree)
        s[i] = mc.parent(s[i], j)[0]
        mc.setAttr(s[i]+'.jo', 0,0,0)
        mc.setAttr(s[i]+'.r', 0,0,0)
        s[i] = mc.parent(s[i], w=1)[0]
        mc.delete(j)
    for i in range(len(s)):
        s[i] = mc.parent(s[i], p[i])
        mc.reorder(s[i], f=1)

"""
import blendShape as bs
import maya.cmds as mc
reload(bs)
types = ['skinCluster','tweak','blendShape']
for n in mc.ls(sl=1, l=True):
    for type in types:
        deformers = bs.getDeformers(nodeType = type, affectedGeometry=[n], filterTweaks=False)
        if deformers:
            suffix = ''
            if len(deformers) > 1:
                suffix = '_#'
            for deformer in deformers:
                mc.rename(deformer, n.split('|')[-1].split(':')[-1]+'_'+type+suffix)

import scratch
reload(scratch)
s = mc.ls(sl=1)
scratch.flipJo('rz', 90)
mc.select(s)
scratch.flipJo('rx', 90)
mc.select(s)

import scratch
reload(scratch)
s = mc.ls(sl=1)
scratch.flipJo('ry', 180)
mc.select(s)

import scratch
reload(scratch)
s = mc.ls(sl=1)
scratch.flipJo('rx', 180)
mc.select(s)

import scratch
reload(scratch)
s = mc.ls(sl=1)
scratch.flipJo('rx', 90)
mc.select(s)


import scratch
reload(scratch)
s = mc.ls(sl=1)
scratch.flipJo('rx', 0)
mc.select(s)

scratch.rib(num=12)


for n in mc.ls(sl=1):
    mc.rename(n, n.replace('_r','_right'))

for n in mc.ls(sl=1):
    mc.select(n)
    j = mc.joint(n=n+'_offset')
    mc.setAttr(j+'.tx', 0.5)


for n in mc.ls(sl=1):
    mc.setAttr(n+".overrideEnabled", 1)
    mc.setAttr(n+".overrideDisplayType", 1)

new = []
for n in mc.ls(sl=1):
    mc.select(n)
    j=mc.joint(n=n+'_offset')
    mc.reorder(j, b=1)
    v = 0.5
    if 'right' in j:
        v = -0.5
    mc.setAttr(j+'.tx', v)
    mc.setAttr(j+'.radius', 2.0)
    print(j)
    color_index = 10
    mc.setAttr("{0}.overrideEnabled".format(j), True)
    mc.setAttr("{0}.overrideColor".format(j), color_index)
    new.append(j)
mc.select(new)


for n in mc.ls(sl=1):
    mc.select(n)
    j=mc.joint(n=n+'_env')
    j = mc.parent(j, w=1)
    mc.parentConstraint(n,j)



s = mc.ls(sl=1)
for n in mc.ls(sl=1):
    c = mc.cluster(n)
    mc.setAttr(c[1]+'.r', 0,0,90)
    mc.delete(n, ch=1)
mc.select(s)

s = mc.ls(sl=1)
for n in s:
    c = mc.cluster(n)
    mc.setAttr(c[1]+'.s', 1.1,1.1,1.1)
    mc.delete(n, ch=1)
mc.select(s)

from pprint import pprint
import hotkeys
reload(hotkeys)
data = hotkeys.stackTransform(num=2)
pprint(data)


from pprint import pprint
import hotkeys
reload(hotkeys)
data = hotkeys.stackTransform(num=2, world=True)
pprint(data)


from pprint import pprint
reload(hotkeys)
data = hotkeys.stackTransform(num=2, type='joint')
pprint(data)

l=[]
r=[]
c=[]
for n in mc.ls(sl=1):
    if 'zero'  not in n and 'End' not in n:
        if 'left' in n:
            l.append(n)
        elif 'right' in n:
            r.append(n)
        else:
            c.append(n)

mc.select(c)

s = mc.ls(sl=1, l=1)
for n in s:
    mc.setAttr(n+'.jo', 0,0,0)

s = mc.ls(sl=1, l=1)
for n in s:
    new = n.split('|')[-1].replace('_r_','_right_')
    print(new)
    mc.rename(n, new)

import maya.cmds
s = maya.cmds.ls(type='constraint', dag=True, ap=True, sl=True)
s = list(set(s))
for n in s:
    maya.cmds.reorder(n, b=True)
    maya.cmds.setAttr(n+'.v', False)
    maya.cmds.rename(n, maya.cmds.listRelatives(n, p=True, f=True, pa=True)[0].split('|')[-1].split(':')[-1]+'_'+maya.cmds.nodeType(n))

for n in mc.ls(sl=1, ap=1, dag=1, type='nurbsCurve'):
    p = mc.listRelatives(n, p=1)
    color_index = mc.getAttr("{0}.overrideColor".format(n))
    for x in p:
        mc.setAttr("{0}.overrideEnabled".format(x), True)
        mc.setAttr("{0}.overrideColor".format(x), color_index)

for n in mc.ls(sl=1, ap=1, dag=1, type='joint'):
    color_index = 10
    mc.setAttr("{0}.overrideEnabled".format(n), True)
    mc.setAttr("{0}.overrideColor".format(n), color_index)


for n in mc.ls(sl=1):
    mc.setAttr(n+'.tx', (mc.getAttr(n+'.tx')*-1))



s = mc.ls(sl=1)
p = mc.listRelatives(s, p=1)
s = mc.parent(s, w=1)
for i in range(len(s)):
    print s[i]
    mc.select(s[i])
    j = mc.parent(w=1)[0]
    mc.setAttr(j+'.rx', 180)
    s[i] = mc.parent(s[i], j)[0]
    mc.setAttr(s[i]+'.jo', 0,0,0)
    s[i] = mc.parent(s[i], w=1)[0]mc.select(c)
    mc.delete(j)
for i in range(len(s)):
    s[i] = mc.parent(s[i], p[i])


import maya.cmds
s = maya.cmds.ls(sl=1, dag=1, ap=1, type=['nurbsCurve','nurbsSurface','lattice','mesh'])
xfs = maya.cmds.listRelatives(s, p=True, f=True, pa=True)
xfs = list(set(xfs))
for xf in xfs:
    nis = maya.cmds.listRelatives(xf, s=True, ni=True, f=True, pa=True)
    alls = maya.cmds.listRelatives(xf, s=True, ni=False, f=True, pa=True)
    origs = list(set(alls)-set(nis))
    suffix = ''
    if len(nis) > 1:
        suffix = '_#'
    for n in range(len(nis)):
        try:
            nis[n] = maya.cmds.rename(nis[n], xf.split('|')[-1].split(':')[-1]+'Shape'+suffix)
        except:
            pass
    for o in range(len(origs)):
        try:
            origs[o] = maya.cmds.rename(origs[o], xf.split('|')[-1].split(':')[-1]+'OrigShape'+suffix)
        except:
            pass



"""

"""

import maya.mel as mel
s = mc.ls(sl=1)
num = 4
for n in s:
    try:
        mc.select([n+'.vtx[23515:23600]', n+'.vtx[23602]', n+'.vtx[24152:24242]', n+'.vtx[24792:24886]', n+'.vtx[25429:25527]', n+'.vtx[26048:26150]', n+'.vtx[26649:26755]', n+'.vtx[27252:27362]', n+'.vtx[27857:27971]', n+'.vtx[28466:28584]', n+'.vtx[29079:29203]', n+'.vtx[29700:29828]', n+'.vtx[30327:30459]', n+'.vtx[30959:31095]', n+'.vtx[31582:31594]', n+'.vtx[31709]', n+'.vtx[31711:31722]', n+'.vtx[32205:32217]', n+'.vtx[32337:32349]', n+'.vtx[32832:32844]', n+'.vtx[32968:32980]', n+'.vtx[33461:33473]', n+'.vtx[33601:33613]', n+'.vtx[34088:34100]', n+'.vtx[34232:34244]', n+'.vtx[34725:34737]', n+'.vtx[34873:34885]', n+'.vtx[35376:35388]', n+'.vtx[35528:35540]', n+'.vtx[36003:36015]', n+'.vtx[36159:36171]', n+'.vtx[36636:36648]', n+'.vtx[36796:36808]', n+'.vtx[37277:37289]', n+'.vtx[37441:37453]', n+'.vtx[37930:37942]', n+'.vtx[38098:38110]', n+'.vtx[38595:38607]', n+'.vtx[38767:38779]', n+'.vtx[39272:39284]', n+'.vtx[39448:39460]', n+'.vtx[39959:39971]', n+'.vtx[40139:40151]', n+'.vtx[40656:40668]', n+'.vtx[40840:40852]', n+'.vtx[41363:41375]', n+'.vtx[41551:41563]', n+'.vtx[42080:42092]', n+'.vtx[42272:42284]', n+'.vtx[42807:42819]', n+'.vtx[42995:43007]', n+'.vtx[43538:43550]', n+'.vtx[43722:43734]', n+'.vtx[44275:44287]', n+'.vtx[44453:44465]', n+'.vtx[45012:45024]', n+'.vtx[45184:45196]', n+'.vtx[45753:45765]', n+'.vtx[45921:45933]', n+'.vtx[46498:46510]', n+'.vtx[46662:46674]', n+'.vtx[47215:47227]', n+'.vtx[47375:47387]', n+'.vtx[47926:47938]', n+'.vtx[48082:48094]', n+'.vtx[51673:51685]', n+'.vtx[51825:51837]', n+'.vtx[52004:52016]', n+'.vtx[52152:52164]', n+'.vtx[52327:52339]', n+'.vtx[52471:52483]', n+'.vtx[52642:52654]', n+'.vtx[52782:52794]', n+'.vtx[52945:52957]', n+'.vtx[53081:53093]', n+'.vtx[53236:53248]', n+'.vtx[53350:53364]', n+'.vtx[53493:53507]', n+'.vtx[53577:53591]', n+'.vtx[53706:53720]'])
        for i in range(num):
            mel.eval("AverageVertex")
            mel.eval("PolySelectTraverse 1")
    except:
        pass
mc.select(s)


"""



# EOF
